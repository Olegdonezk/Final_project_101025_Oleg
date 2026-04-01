from mysql_connector import search_by_keyword, get_genres, search_by_genre_and_year
from log_writer import log_search, log_error
from log_stats import get_top_queries, get_recent_queries
from formatter import print_movies
from datetime import datetime

# ---------------------- Статистика ----------------------
def print_stats(top_queries, recent_queries):

    def format_timestamp(ts):
        return ts.strftime("%Y-%m-%d %H:%M:%S")

    def format_doc_row(doc):
        search_type = doc.get("search_type", "")
        params = doc.get("params", {})
        results_count = doc.get("results_count", "")
        timestamp = format_timestamp(doc.get("timestamp"))
        if search_type == "keyword":
            key_or_genre = params.get("keyword", "")
            year_range = ""
        elif search_type == "genre_year":
            key_or_genre = params.get("genre", "")
            year_range = f"{params.get('from','')}-{params.get('to','')}"
        else:
            key_or_genre = ""
            year_range = ""
        return (search_type, key_or_genre, year_range, results_count, timestamp)

    def print_table(title, docs):
        headers = ["Тип поиска", "Жанр/Ключ", "Годы", "Результаты", "Время"]
        col_widths = [15, 15, 12, 10, 20]
        print("\n" + "=" * (sum(col_widths)+len(col_widths)))
        print(title)
        print("=" * (sum(col_widths)+len(col_widths)))
        print(" ".join(h.ljust(w) for h,w in zip(headers,col_widths)))
        print("-" * (sum(col_widths)+len(col_widths)))

        if not docs:
            print("Нет данных.".ljust(sum(col_widths)))
            return

        for doc in docs:
            row = format_doc_row(doc)
            print(" ".join(str(c).ljust(w) for c,w in zip(row,col_widths)))
        print("=" * (sum(col_widths)+len(col_widths)))

    print_table("🏆 Популярные запросы", top_queries)
    print_table("🕒 Последние запросы", recent_queries)

def show_stats():
    top_queries = get_top_queries()
    recent_queries = get_recent_queries()
    print_stats(top_queries, recent_queries)

# ---------------------- Поиск по ключевому слову ----------------------
def keyword_search():
    keyword = input("Введите ключевое слово: ")
    offset = 0

    while True:
        results = search_by_keyword(keyword, offset=offset)
        print_movies(results)
        log_search("keyword", {"keyword": keyword}, len(results))
        if len(results) < 10:
            break
        cont = input("Показать еще? (y/n): ")
        if cont.lower() != "y":
            break
        offset += 10

# ---------------------- Ввод года ----------------------
def input_year(prompt, genre=None, min_value=None, max_value=None):
    while True:
        value = input(prompt).strip()
        if not value:
            print("Поле не может быть пустым!")
            continue
        try:
            year = int(value)
        except ValueError as e:
            print("Введите корректное число!")
            log_error(f"Некорректный ввод года: {value}", search_type="genre_year", params={"genre": genre})
            continue
        if min_value is not None and year < min_value:
            print(f"Год не может быть меньше {min_value}")
            log_error(f"Год меньше min: {year} < {min_value}", "genre_year", {"genre": genre})
            continue
        if max_value is not None and year > max_value:
            print(f"Год не может быть больше {max_value}")
            log_error(f"Год больше max: {year} > {max_value}", "genre_year", {"genre": genre})
            continue
        return year

# ---------------------- Поиск по жанру и году ----------------------
def genre_search():
    genres = get_genres()
    print("\nДоступные жанры:")
    for i, g in enumerate(genres, 1):
        print(f"{i:2}. {g}")
    print()
    while True:
        user_input = input("Введите жанр (номер или название): ").strip()
        if user_input.isdigit():
            idx = int(user_input)-1
            if 0 <= idx < len(genres):
                genre = genres[idx]
                break
        elif user_input in genres:
            genre = user_input
            break
        print("Некорректный жанр!")
        log_error(f"Некорректный жанр: '{user_input}'", "genre_year", {"genre": user_input})

    year_from = input_year("От года: ", genre, 1990, 2026)
    year_to = input_year("До года: ", genre, 1990, 2026)

    if year_from > year_to:
        print("'От года' не может быть больше 'До года'")
        log_error("Некорректный диапазон", "genre_year", {"genre": genre, "from": year_from, "to": year_to})
        return

    offset = 0
    while True:
        results = search_by_genre_and_year(genre, year_from, year_to, offset=offset)
        if not results:
            print("Нет результатов!")
            log_error(f"Нет результатов: genre={genre}, from={year_from}, to={year_to}", "genre_year", {"genre": genre, "from": year_from, "to": year_to})
            return
        print_movies(results)
        log_search("genre_year", {"genre": genre, "from": year_from, "to": year_to}, len(results))
        if len(results) < 10:
            break
        cont = input("Показать еще? (y/n): ")
        if cont.lower() != "y":
            break
        offset += 10

# ---------------------- Главное меню ----------------------
def main():
    while True:
        print("\n1. Поиск по ключевому слову")
        print("2. Поиск по жанру и году")
        print("3. Статистика")
        print("4. Выход")

        choice = input("Выберите пункт: ")
        if choice == "1":
            keyword_search()
        elif choice == "2":
            genre_search()
        elif choice == "3":
            show_stats()
        elif choice == "4":
            break
        else:
            print("Неверный ввод")

if __name__ == "__main__":
    main()