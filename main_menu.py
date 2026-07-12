# main_menu.py

from search_film import *
from pagination import *
from log_writer import *
from log_reader import *


def handle_keyword_search():
    # Handle search by keyword
    keyword = input("\nEnter a keyword to search: ").strip()
    if not keyword:
        print("The keyword cannot be empty.")
        return

    # Search movies
    films = search_films_by_keyword(keyword)

    # Filter by rating
    ratings = get_available_ratings()
    if ratings and films:
        print("\nFilter by rating:")
        for i, rating in enumerate(ratings, 1):
            print(f"{i}. {rating}")
        print("0. All ratings")

        choice = input("Choose a rating: ").strip()
        if choice and choice != '0' and choice.isdigit():
            index = int(choice) - 1
            if 0 <= index < len(ratings):
                selected_rating = ratings[index]
                films = [f for f in films if f['rating'] == selected_rating]
                print(f"Filter applied: {selected_rating}")

    # Log and display results
    log_keyword_search(keyword, len(films))
    show_films_paginated(films, f"Found {len(films)} movies for '{keyword}'")


def handle_genre_search():
    # Handle search by genre
    genres = get_all_genres()
    if not genres:
        print("No genres found.")
        return

    print("\nAvailable genres:")
    for i, genre in enumerate(genres, 1):
        print(f"{i}. {genre['name']}")

    choice = input("Choose a genre number: ").strip()
    if not choice.isdigit():
        print("Please enter a number.")
        return

    index = int(choice) - 1
    if index < 0 or index >= len(genres):
        print("Invalid genre number.")
        return

    selected_genre = genres[index]
    films = search_films_by_genre(selected_genre['category_id'])

    # Filter by rating
    ratings = get_available_ratings()
    if ratings and films:
        print("\nFilter by rating:")
        for i, rating in enumerate(ratings, 1):
            print(f"{i}. {rating}")
        print("0. All ratings")

        choice = input("Choose a rating: ").strip()
        if choice and choice != '0' and choice.isdigit():
            index = int(choice) - 1
            if 0 <= index < len(ratings):
                selected_rating = ratings[index]
                films = [f for f in films if f['rating'] == selected_rating]
                print(f"Filter applied: {selected_rating}")

    # Log and display results
    log_genre_search(selected_genre['name'], len(films))
    show_films_paginated(films, f"Found {len(films)} movies in the '{selected_genre['name']}' genre")


def handle_year_search():
    # Handle search by year
    year_range = get_min_max_years()
    print(f"\nAvailable year range: {year_range['min_year']} - {year_range['max_year']}")

    print("\n1. Search by a specific year")
    print("2. Search by a year range")
    choice = input("Choose a search type: ").strip()

    if choice == "1":
        year = input("Enter a year: ").strip()
        if not year.isdigit():
            print("Year must be a number.")
            return

        films = search_films_by_year(int(year))

        # Log and display results
        log_year_search(year, len(films))
        show_films_paginated(films, f"Found {len(films)} movies from {year}")

    elif choice == "2":
        year_from = input("Enter the start year: ").strip()
        year_to = input("Enter the end year: ").strip()
        if not year_from.isdigit() or not year_to.isdigit():
            print("Years must be numbers.")
            return

        films = search_films_by_year(int(year_from), int(year_to))

        # Log and display results
        log_year_range_search(year_from, year_to, len(films))
        show_films_paginated(films, f"Found {len(films)} movies from {year_from}-{year_to}")

    else:
        print("Invalid choice.")


def show_info():
    # Show database information
    year_range = get_min_max_years()
    genres = get_all_genres()
    ratings = get_available_ratings()

    print(f"\nDatabase information:")
    print(f"Year range: {year_range['min_year']} - {year_range['max_year']}")
    print(f"Number of genres: {len(genres)}")
    print(f"Available ratings: {', '.join(ratings)}")


def main_menu():
    # Application main menu
    menu_options = [
        "Search by keyword",
        "Search by genre",
        "Search by year",
        "Database information",
        "Popular searches",
        "Exit"
    ]

    print("=" * 50)
    print("MOVIE SEARCH")
    print("=" * 50)

    while True:
        print("\nMain menu:")
        for i, option in enumerate(menu_options, 1):
            print(f"{i}. {option}")

        choice = input("\nChoose an option: ").strip()

        if choice == "1":
            handle_keyword_search()
        elif choice == "2":
            handle_genre_search()
        elif choice == "3":
            handle_year_search()
        elif choice == "4":
            show_info()
        elif choice == "5":
            show_popular_searches()
        elif choice == "6":
            print("Thank you for using our service. See you again soon!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 6.")
