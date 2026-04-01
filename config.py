import pymysql
import os
from dotenv import load_dotenv
import pymysql.cursors

load_dotenv()

MYSQL_CONFIG = {
    "host": os.getenv("MYSQL_HOST"),
    "port": int(os.getenv("MYSQL_PORT", 3306)),
    "user": os.getenv("MYSQL_USER"),
    "password": os.getenv("MYSQL_PASSWORD"),
    "database": os.getenv("MYSQL_DB"),
    "cursorclass": pymysql.cursors.DictCursor,
}

MONGO_CONFIG = {
    "uri": os.getenv("MONGO_URI"),
    "db_name": os.getenv("MONGO_DB"),
    "collection": os.getenv("MONGO_COLLECTION")
}