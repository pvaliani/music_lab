import pdb 
from models.album import Album
from models.artist import Artist
import repositories.album_repository as album_repository
import repositories.artist_repository as artist_repository


metallica = Artist('Metallica')
black_album = Album('Black Album', 'Heavy Metal', 'Metallica')
album_repository.save(black_album)
