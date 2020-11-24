from models.artist import Artist
from models.album import Album
from db.run_sql import run_sql




def save(artist):
    sql = "INSERT INTO artists (name) VALUES (%s) RETURNING id"
    #  for last item we are referencing the album objects, artist objects id as a reference

    values = [artist.name]
    results = run_sql(sql, values)

    # if id was 4 then rhs says its the 0th index of the results list where the key is 'id' and the associated value of that key is 4

    id = results[0]['id']

    # assigns our album with its own id  - i.e if it was 4 on the line above our album.id is now 4

    artist.id = id
    return artist