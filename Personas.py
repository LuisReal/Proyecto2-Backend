class Persona:

    def __init__(self, nombre, apellido, usuario, contrasena):
        self.nombre = nombre
        self.apellido = apellido
        self.usuario = usuario
        self.contrasena = contrasena

    def getNombre(self):
        return self.nombre

    def getApellido(self):
        return self.apellido

    def getUsuario(self):
        return self.usuario

    def getContrasena(self):
        return self.contrasena

    def setNombre(self, nombre):
        self.nombre=nombre

    def setApellido(self, apellido):
        self.apellido = apellido

    def setUsuario(self, usuario):
        self.usuario = usuario

    def setContrasena(self, contrasena):
        self.contrasena = contrasena