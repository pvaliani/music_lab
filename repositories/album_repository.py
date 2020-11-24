from db.run_sql import run_sql

import repositories.artist_repository as artist_repository

from models.album import Album

# CREATE

def save(album):
    sql = "INSERT INTO albums (title, genre, artist_id) VALUES (%s, %s, %s) RETURNING *"
    #  for last item we are referencing the album objects, artist objects id as a reference

    values = [album.title, album.genre, album.artist.id]
    results = run_sql(sql, values)

    # if id was 4 then rhs says its the 0th index of the results list where the key is 'id' and the associated value of that key is 4

    id = results[0]['id']

    # assigns our album with its own id  - i.e if it was 4 on the line above our album.id is now 4

    album.id = id
    return album


# REPLACE


# UPDATE


# DELETE
