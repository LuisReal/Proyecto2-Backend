class Comentario:

    def __init__(self, id, comentario, nombre, usuario, imagen):

        self.id = id
        self.comentario = comentario
        self.nombre = nombre
        self.usuario = usuario
        self.imagen = imagen
        
        
        
    def getId(self):

        return self.id 

    def getComentario(self):

        return self.comentario
    
    def getNombre(self):
        return self.nombre 
    
    def getUsuario(self):
        return self.usuario 
    
    def getImagen(self):
        return self.imagen 
    
    def setId(self, id):
        self.id = id
    
    def setComentario(self, comentario):
        self.comentario = comentario

    def setNombre(self, nombre):
        self.nombre = nombre
    
    def setUsuario(self, usuario):
        self.usuario = usuario

    def setImagen(self, imagen):
        self.imagen = imagen
    