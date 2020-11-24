from db.run_sql import run_sql

import repositories.artist_repository as artist_repository

from models.album import Album


# ------ REFER TO ARTIST REPOSITORY COMMENTS FOR CLEARER DESCRIPTION OF EACH FUNCTION ---


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


# ---------------------------------- SELECT ALL and ID -----------------------------

def select_all():  
    albums = [] 
    sql = "SELECT * FROM albums"
    results = run_sql(sql)
    for row in results:
        artist = artist_repository.select(row['artist_id'])
        album = Album(row['title'], row['genre'], artist, row['id'] )
        albums.append(album)
    return albums


def select(id):
    album = None
    sql = "SELECT * FROM albums WHERE id = %s"  
    values = [id] 
    result = run_sql(sql, values)[0]
    if result is not None:
        artist_id = result['artist_id']
        artist = artist_repository.select(artist_id)
        album = Album(result['title'], result['genre'], artist, result['id'] )
    return album



# -------------------------- UPDATE -----------------

def update(album):
    sql = "UPDATE albums SET (title, genre, artist_id) = (%s, %s, %s) WHERE id = %s"
    values = [album.title, album.genre, album.artist.id, album.id]
    run_sql(sql, values) 



# ----------------------- DELETE ALL AND DELETE BY ID --------------------


def delete_all():
    sql = "DELETE  FROM albums" 
    run_sql(sql)


def delete(id):
    sql = "DELETE  FROM albums WHERE id = %s" 
    values = [id]
    run_sql(sql, values)