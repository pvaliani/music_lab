import pdb 
from models.album import Album
from models.artist import Artist
import repositories.album_repository as album_repository
import repositories.artist_repository as artist_repository


metallica = Artist('Metallica')
artist_repository.save(metallica)
black_album = Album('Black Album', 'Heavy Metal', metallica)
album_repository.save(black_album)

pdb.set_trace()