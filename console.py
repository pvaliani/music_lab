import pdb 
from models.album import Album
from models.artist import Artist
import repositories.album_repository as album_repository
import repositories.artist_repository as artist_repository






# metallica = Artist('Metallica')
# artist_repository.save(metallica)
# black_album = Album('Black Album', 'Heavy Metal', metallica)
# album_repository.save(black_album)


# frontierer = Artist('Frontierer')
# artist_repository.save(frontierer)
# orange_mathematics = Album('Orange Mathematics', 'Heavy Metal', frontierer)
# album_repository.save(orange_mathematics)



# album_repository.select_all()

# album_repository.select(2)





# artist_repository.select_all()

# # pdb.set_trace()

# artist_repository.select(2)

# artist_repository.update(frontierer)

# artist_repository.delete(2) - update or delete on table "artists" violates foreign key constraint 


# artist_repository.delete_all() - update or delete on table "artists" violates foreign key constraint 

# artist_repository.get_albums(metallica) --- doesnt print out metallica

# album_repository.delete_all() --- no results to fetch


# adding delete all first so to clear our example for next run
album_repository.delete_all()
artist_repository.delete_all()

# creating and saving an artist
metallica = Artist('Metallica')
artist_repository.save(metallica)
deftones = Artist('Deftones')
artist_repository.save(deftones)

# creating and saving an album
black_album = Album('Black Album', 'Heavy Metal', metallica)
album_repository.save(black_album)

white_pony = Album('White Pony', 'Metal', deftones)
album_repository.save(white_pony)

# updating an album
black_album.genre = "Metal"
album_repository.update(black_album)

# printing results of the above so we can see what's in the db at the end of the changes
for album in album_repository.select_all():
    print(album.__dict__)

pdb.set_trace()