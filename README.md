# 🎬 Movie Search App

A console application for searching movies in the Sakila database (MySQL)
with search history logging in MongoDB.

## 📌 Project Overview
This project was built as a learning project to practice working with
relational and non-relational databases in Python.

## 🎯 Features
- Search movies by keyword
- Search movies by genre
- Search movies by year or year range
- Filter results by rating
- View database statistics
- Track and display the most popular search queries (via MongoDB)

## 🛠️ Tech Stack
- Python 3.13
- MySQL (via `pymysql`) — main movie database
- MongoDB (via `pymongo`) — search query logging
- python-dotenv — secure configuration management

## 📂 Project Structure
```
movie-search-app/
├── run.py              # entry point
├── main_menu.py         # menu navigation logic
├── search_film.py        # database search functions
├── pagination.py         # paginated results display
├── log_writer.py          # write search logs to MongoDB
├── log_reader.py          # read popular search stats
├── config.py              # database configuration (uses .env)
├── .env.example            # example environment variables
└── requirements.txt
```

## 🚀 How to Run
1. Clone the repository
   ```
   git clone https://github.com/yourusername/movie-search-app.git
   cd movie-search-app
   ```
2. Install dependencies
   ```
   pip install -r requirements.txt
   ```
3. Create a `.env` file based on `.env.example` and add your database credentials
4. Run the app
   ```
   python run.py
   ```

## 💡 What I Learned
- Structuring a multi-file Python console application
- Working with both SQL and NoSQL databases in one project
- Handling user input validation and error cases
- Managing configuration securely with environment variables
