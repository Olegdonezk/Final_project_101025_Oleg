def print_movies(movies):
    if not movies:
        print("Нет результатов.")
        return

    print("\nРезультаты:")
    print("-" * 30)

    for movie in movies:
        print(f"{movie['title']} ({movie['release_year']})")

    print("-" * 30)