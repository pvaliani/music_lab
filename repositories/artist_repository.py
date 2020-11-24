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

# --------------------------------------------- SELECT ALL --------------------

# loop over each dictionary in the list and append to the users list which is empty

# - Select all creates an empty list of artists which will be used to store all artists we select
# - We then input the SQL query and our results are when run_sql runs our query in python
# - Once we have results we loop through each row in the table of rsults and state that our empty artists list is appended by each artist in the table.  artist = Artist(...) defines what an artist is so that we can return the object and append it to our empty artists list
# - Why can't we just hold our select in results?

def select_all(): 
    artists = [] 

    sql = "SELECT * FROM artists"
    results = run_sql(sql)

    for row in results:
        artist = Artist(row['name'], row['id'] )
        artists.append(artist)
    return artists


# --------------------------------------------- SELECT ONE --------------------------


# - Select one sets artist to None. Then we define the SQL query as normal to locate our artist with its ID reference.
# - Values is then set to the value of id
# - The variable result stores the output of the run_sql query at list index 0
# - If the result is not None i.e if theres a value then our artist to be returned is the key/value dictionary pair for name and id.
# - Artist is set to None as it is just an empty variable - ????

# add result [id] at the end of artist

def select(id):
    artist = None
    sql = "SELECT * FROM artists WHERE id = %s"  
    values = [id] 
    result = run_sql(sql, values)[0]
    
    if result is not None:
        artist = Artist(result['name'], result['id'] )
    return artist



# ---------------------------- UPDATE -----------------------------------



# - The update method first requires a SQL statement to retrieve the data.
# - Values is then created as a variable to store the artist objects name and id parameters
# - We then run the run_sql method which is a "standard" method we have created for the course. It will convert our SQL query into python code along with the values we pass it in Values


def update(artist):
    sql = "UPDATE artists SET (name) = (%s) WHERE id = %s"
    values = [artist.name, artist.id]
    run_sql(sql, values) 


# --------------------------- DELETE ----------------------------------------------------------


# - The delete method first requires a SQL statement to retrieve the data.
# - Values is then created as a variable to store the value of id passed to it as an input
# - We then run the run_sql method which is a "standard" method we have created for the course. It will convert our SQL query into python code along with the values we pass it in values


def delete(id):
    sql = "DELETE  FROM artists WHERE id = %s" 
    values = [id]
    run_sql(sql, values)



# -------------------- DELETE ALL ----------------------------------------

# - The delete all method doesn't require any inputs as run_sql is literally converting our sql query from a string to usable python code which will act on the database


def delete_all():
    sql = "DELETE  FROM artists" 
    run_sql(sql)


# -------------------- GET ARTISTS ----------------------------

# - Get albums takes an artist object. First we create our SQL query to retrieve the albums. 
# - We basically loop through each row of our results again and our album object is created from a class instance of Album. We are passing in the full artist object on line 124 because we require artist as an input to our get_albums function. We are retrieving albums based on an artist when we call the function so thats why we pass the full object. We then append our results to the empty list of artists_albums and return the result


def get_albums(artist):
  sql = "SELECT * FROM albums WHERE artist_id = %s"
  values = [artist.id]
  results = run_sql(sql, values)
  artists_albums = []
  for row_data in results:

    album = Album(
      row_data["title"], 
      row_data['genre'], 
      artist,
      row_data["id"]
    )

    artists_albums.append(album)
  return artists_albums