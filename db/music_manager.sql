DROP TABLE IF EXISTS albums;
DROP TABLE IF EXISTS artists;


CREATE TABLE artists (

    id SERIAL PRIMARY KEY,
    name VARCHAR(255)

);


CREATE TABLE albums (
    id SERIAL PRIMARY KEY,
    artist_id INT REFERENCES artists(id), -- Foreign Key to artists table
    title VARCHAR(255),
    genre VARCHAR(255)
    
);
