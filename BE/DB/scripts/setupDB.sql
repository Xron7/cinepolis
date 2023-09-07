-- MOVIES TABLE
DROP TABLE IF EXISTS tmovie;
CREATE TABLE tmovie (
    id INTEGER PRIMARY KEY,
    title TEXT,
    genres TEXT
);

-- LINKS TABLE
DROP TABLE IF EXISTS tlink;
CREATE TABLE tlink (
    id INTEGER PRIMARY KEY,
    movie_id INTEGER,
    imdb_id INTEGER,
    tmdb_id INTEGER,
    FOREIGN KEY (movie_id) REFERENCES tmovie(id)
);

-- RATINGS TABLE
DROP TABLE IF EXISTS trating;
CREATE TABLE trating (
    id INTEGER PRIMARY KEY,
    user_id INTEGER,
    movie_id INTEGER,
    rating DECIMAL(3, 1),
    timestamp TIMESTAMP,
    FOREIGN KEY (movie_id) REFERENCES tmovie(id)
);

-- TAGS TABLE
DROP TABLE IF EXISTS ttags;
CREATE TABLE ttags (
    user_id INTEGER,
    movie_id INTEGER,
    tag TEXT,
    timestamp TIMESTAMP,
    FOREIGN KEY (movie_id) REFERENCES tmovie(id)
);
