import pymysql
from config import MYSQL_CONFIG

def get_connection():
    return pymysql.connect(**MYSQL_CONFIG)

def search_by_keyword(keyword, limit=10, offset=0):
    query = """
        SELECT title, release_year
        FROM film
        WHERE title LIKE %s
        LIMIT %s OFFSET %s
    """
    with get_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute(query, (f"%{keyword}%", limit, offset))
            return cursor.fetchall()

def get_genres():
    query = "SELECT name FROM category"
    with get_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute(query)
            return [row['name'] for row in cursor.fetchall()]

def search_by_genre_and_year(genre, year_from, year_to, limit=10, offset=0):
    query = """
        SELECT f.title, f.release_year
        FROM film f
        JOIN film_category fc ON f.film_id = fc.film_id
        JOIN category c ON fc.category_id = c.category_id
        WHERE c.name = %s AND f.release_year BETWEEN %s AND %s
        LIMIT %s OFFSET %s
    """
    with get_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute(query, (genre, year_from, year_to, limit, offset))
            return cursor.fetchall()