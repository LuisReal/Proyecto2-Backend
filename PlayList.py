class playlist:

    def __init__(self, id, nombre, artista, album, fecha, imagen, spotify, youtube):

        self.id = id
        self.nombre = nombre
        self.artista = artista
        self.album = album
        self.fecha = fecha
        self.imagen = imagen
        self.spotify = spotify
        self.youtube = youtube

    def getId(self):

        return self.id 

    def getNombre(self):

        return self.nombre
    
    def getArtista(self):

        return self.artista

    def getAlbum(self):

        return self.album

    def getFecha(self):

        return self.fecha

    def getImagen(self):

        return self.imagen

    def getSpotify(self):

        return self.spotify

    def getYoutube(self):

        return self.youtube

    def setId(self, id):
        self.id = id
    
    def setNombre(self, nombre):
        self.nombre = nombre
    
    def setArtista(self, artista):
        self.artista = artista

    def setAlbum(self, album):
        self.album = album
    
    def setFecha(self, fecha):
        self.fecha = fecha
        
    def setImagen(self, imagen):
        self.imagen = imagen
        
    def setSpotify(self, spotify):
        self.spotify = spotify

    def setYoutube(self, youtube):
        self.youtube = youtube