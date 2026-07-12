# pagination.py

def show_films_paginated(films, title="Search results"):
    if not films:
        print("No movies found.")
        return

    print(f"\n{title}")
    print("=" * 80)

    page_size = 10
    current_page = 0
    total_films = len(films)

    while current_page * page_size < total_films:
        start_idx = current_page * page_size
        end_idx = min((current_page + 1) * page_size, total_films)

        print(f"\nShowing movies {start_idx + 1}-{end_idx} of {total_films}:")
        print("-" * 80)

        for i in range(start_idx, end_idx):
            film = films[i]
            print(f"{i + 1}. {film['title']} ({film['release_year']})")
            print(f"   Language: {film['language']}, Rating: {film['rating']}")
            desc = film['description'] or "No description"
            print(f"   Description: {desc[:100]}{'...' if len(desc) > 100 else ''}")
            print()

        if end_idx < total_films:
            show_more = input("Show the next 10 movies? (y/n): ").strip().lower()
            if show_more not in ['y', 'yes']:
                break
            current_page += 1
        else:
            print("All movies have been shown.")
            break
