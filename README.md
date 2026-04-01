Movie Search CLI Application

📌 Описание проекта



Консольное приложение для поиска фильмов по:



🔍 ключевому слову

🎭 жанру и диапазону годов



Приложение использует:



MySQL — для хранения фильмов (база sakila)

MongoDB — для логирования запросов и ошибок

🎯 Цель проекта

Практика работы с SQL (JOIN, фильтрация, LIMIT/OFFSET)

Работа с NoSQL (MongoDB)

Реализация CLI-интерфейса

Логирование пользовательских действий

Построение простой аналитики (популярные и последние запросы)

⚙️ Технологии

Python 3

pymysql

pymongo

MySQL (sakila database)

MongoDB

🚀 Установка и запуск

1\. Клонировать репозиторий

git clone https://github.com/USERNAME/REPO.git

cd REPO

2\. Установить зависимости

pip install pymysql pymongo python-dotenv

3\. Настроить переменные окружения



Создайте файл .env в корне проекта:



MYSQL\_HOST=your\_host

MYSQL\_USER=your\_user

MYSQL\_PASSWORD=your\_password

MYSQL\_DB=sakila



MONGO\_URI=your\_mongo\_uri

MONGO\_DB=your\_db

MONGO\_COLLECTION=your\_collection



⚠️ Файл .env не должен попадать в Git (используется .gitignore)



4\. Обновить config.py



Если используешь .env, пример:



import os

from dotenv import load\_dotenv



load\_dotenv()



MYSQL\_CONFIG = {

&#x20;   "host": os.getenv("MYSQL\_HOST"),

&#x20;   "user": os.getenv("MYSQL\_USER"),

&#x20;   "password": os.getenv("MYSQL\_PASSWORD"),

&#x20;   "database": os.getenv("MYSQL\_DB"),

}



MONGO\_CONFIG = {

&#x20;   "uri": os.getenv("MONGO\_URI"),

&#x20;   "db\_name": os.getenv("MONGO\_DB"),

&#x20;   "collection": os.getenv("MONGO\_COLLECTION"),

}

5\. Запуск приложения

python main.py

🖥️ Пример использования

Главное меню:

1\. Поиск по ключевому слову

2\. Поиск по жанру и году

3\. Статистика

4\. Выход

🔍 Поиск по ключевому слову

Введите ключевое слово: love



👉 Вывод:



Love Suicides (2000)

Love Affair (1999)

...

🎭 Поиск по жанру

Доступные жанры:

&#x20;1. Action

&#x20;2. Comedy

&#x20;3. Drama

&#x20;...



Введите жанр (номер или название): 2

📅 Введите год (от 1990 до 2026)

От года: 2000

До года: 2010



👉 Вывод:



Funny Movie (2005)

Another Comedy (2008)

...

📊 Статистика

🏆 Популярные запросы

Тип поиска     Жанр/Ключ      Годы        Результаты  Время

\----------------------------------------------------------------

genre\_year     Horror         1990-2005   10          2026-04-01 09:03:17

keyword        love                      10          2026-04-01 09:02:59

📂 Структура проекта

project/

│

├── main.py

├── mysql\_connector.py

├── log\_writer.py

├── log\_stats.py

├── config.py

├── formatter.py

│

├── .env              # ❌ не в репозитории

├── .env.example      # ✅ пример

├── .gitignore

└── README.md

⚠️ Важно

.env файл содержит пароли — никогда не публикуйте его

При утечке — обязательно смените пароли

Логирование происходит в MongoDB

🔮 Возможные улучшения

Добавить GUI (Tkinter / PyQt)

Веб-версия (Flask / FastAPI)

Использование библиотеки rich для красивого CLI

Кэширование запросов

Автодополнение жанров

👨‍💻 Автор



Oleg — Python Developer (Junior)

