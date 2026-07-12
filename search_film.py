# search_film.py
import pymysql
from config import MYSQL_CONFIG


def search_films_by_keyword(keyword):
    # Connect to the MySQL server
    with pymysql.connect(**MYSQL_CONFIG) as connection:
        with connection.cursor() as cursor:
            # SQL query to search movies by keyword
            query = """
                SELECT f.title, f.description, f.release_year, l.name as language, f.rating
                FROM film f
                JOIN language l ON f.language_id = l.language_id
                WHERE f.title LIKE %s OR f.description LIKE %s
                ORDER BY f.title
            """
            cursor.execute(query, ('%' + keyword + '%', '%' + keyword + '%'))

            # Collect results
            films = []
            for row in cursor:
                films.append({
                    'title': row[0],
                    'description': row[1],
                    'release_year': row[2],
                    'language': row[3],
                    'rating': row[4]
                })
            return films


def search_films_by_genre(genre_id):
    # Connect to the MySQL server
    with pymysql.connect(**MYSQL_CONFIG) as connection:
        with connection.cursor() as cursor:
            # SQL query to search movies by genre
            query = """
                SELECT f.title, f.description, f.release_year, l.name as language, f.rating
                FROM film f
                JOIN film_category fc ON f.film_id = fc.film_id
                JOIN category c ON fc.category_id = c.category_id
                JOIN language l ON f.language_id = l.language_id
                WHERE c.category_id = %s
                ORDER BY f.title
            """
            cursor.execute(query, (genre_id,))

            # Collect results
            films = []
            for row in cursor:
                films.append({
                    'title': row[0],
                    'description': row[1],
                    'release_year': row[2],
                    'language': row[3],
                    'rating': row[4]
                })
            return films


def search_films_by_year(year_from, year_to=None):
    # Connect to the MySQL server
    with pymysql.connect(**MYSQL_CONFIG) as connection:
        with connection.cursor() as cursor:
            if year_to is None:
                # SQL query to search by a specific year
                query = """
                    SELECT f.title, f.description, f.release_year, l.name as language, f.rating
                    FROM film f
                    JOIN language l ON f.language_id = l.language_id
                    WHERE f.release_year = %s
                    ORDER BY f.title
                """
                cursor.execute(query, (year_from,))
            else:
                # SQL query to search by a year range
                query = """
                    SELECT f.title, f.description, f.release_year, l.name as language, f.rating
                    FROM film f
                    JOIN language l ON f.language_id = l.language_id
                    WHERE f.release_year BETWEEN %s AND %s
                    ORDER BY f.release_year, f.title
                """
                cursor.execute(query, (year_from, year_to))

            # Collect results
            films = []
            for row in cursor:
                films.append({
                    'title': row[0],
                    'description': row[1],
                    'release_year': row[2],
                    'language': row[3],
                    'rating': row[4]
                })
            return films


def get_min_max_years():
    # Connect to the MySQL server
    with pymysql.connect(**MYSQL_CONFIG) as connection:
        with connection.cursor() as cursor:
            # SQL query to get the minimum and maximum release year
            query = "SELECT MIN(release_year), MAX(release_year) FROM film"
            cursor.execute(query)

            result = cursor.fetchone()
            return {'min_year': result[0], 'max_year': result[1]}


def get_all_genres():
    # Connect to the MySQL server
    with pymysql.connect(**MYSQL_CONFIG) as connection:
        with connection.cursor() as cursor:
            # SQL query to get all genres
            query = "SELECT name, category_id FROM category ORDER BY name"
            cursor.execute(query)

            # Collect results
            genres = []
            for row in cursor:
                genres.append({'name': row[0], 'category_id': row[1]})
            return genres


def get_available_ratings():
    # Connect to the MySQL server
    with pymysql.connect(**MYSQL_CONFIG) as connection:
        with connection.cursor() as cursor:
            # SQL query to get available ratings
            query = "SELECT DISTINCT rating FROM film WHERE rating IS NOT NULL ORDER BY rating"
            cursor.execute(query)

            # Collect results
            ratings = []
            for row in cursor:
                ratings.append(row[0])
            return ratings
