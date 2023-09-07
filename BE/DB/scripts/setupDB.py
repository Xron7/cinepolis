import sqlite3
import csv

DB_PATH   = 'BE/DB/'
DATA_PATH = 'BE/DB/data/100k/'

sql_movies  = 'INSERT INTO tmovie  (id, title, genres) VALUES (?, ?, ?)'
sql_links   = 'INSERT INTO tlink   (movie_id, imdb_id, tmdb_id) VALUES (?, ?, ?)'
sql_ratings = 'INSERT INTO trating (user_id, movie_id, rating, timestamp) VALUES (?, ?, ?, ?)'
sql_tags    = 'INSERT INTO ttags   (user_id, movie_id, tag, timestamp) VALUES (?, ?, ?, ?)'

conn   = sqlite3.connect(DB_PATH + 'ratings.db')
cursor = conn.cursor()

def insert_from_csv(csv_file,sql_statement):
    
    with open(csv_file, 'r',  encoding='utf-8') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  # Skip the header
        for row in csv_reader:
            cursor.execute(sql_statement, row)
    return None

# Create the tables
with open(DB_PATH + 'scripts/setupDB.sql', 'r') as script_file:
    script = script_file.read()

cursor.executescript(script)

# Insert the movies
movies_csv = DATA_PATH + 'movies.csv'
insert_from_csv(movies_csv, sql_movies)

# Insert the links
links_csv = DATA_PATH + 'links.csv'
insert_from_csv(links_csv, sql_links)

# Insert the ratings
links_csv = DATA_PATH + 'ratings.csv'
insert_from_csv(links_csv, sql_ratings)

# Insert the ratings
links_csv = DATA_PATH + 'tags.csv'
insert_from_csv(links_csv, sql_tags)

conn.commit()
conn.close()
