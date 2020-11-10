from flask import Flask, jsonify, request
from flask_cors import CORS
from Personas import Persona
from Canciones import Cancion
from Comentarios import Comentario
from Solicitud import Solicitar
from PlayList import playlist

app = Flask (__name__)
CORS(app)


Usuarios = []

Canciones = []
contador = 1

Comentarios = []
contador_comentarios = 1

Solicitudes = []
contador_solicitud = 1

PlayList = []
contador_playlist = 1

Usuarios.append(Persona('Usuario','Maestro','admin', 'admin'))
Usuarios.append(Persona('Luis','Gonzalez','Fercho123', '123'))



@app.route('/', methods=['GET'])
def Iniciar():
    
    return("Hello World")

@app.route('/Usuarios/', methods=['GET'])
def getPersonas(): 
    global Usuarios
    Datos = []
    for usuario in Usuarios:
        Dato={'Nombre' : usuario.getNombre(),
              'Apellido': usuario.getApellido(),
              'Usuario': usuario.getUsuario()}  
        Datos.append(Dato)
    respuesta = jsonify(Datos)    
    return(respuesta)

@app.route('/Usuarios/', methods=['POST'])
def addPersonas(): 
    global Usuarios
    nombre = request.json['nombre']
    apellido = request.json['apellido']
    usuario = request.json['usuario']
    contrasena = request.json['contrasena']
    encontrado = False
    
    for i in Usuarios:
        if i.getUsuario() == usuario:
            encontrado = True
            break
    if encontrado:
        return jsonify({'message': "failed",
                        'reason': "El usuario ya existe"})
    else:
        nuevo = Persona(nombre, apellido, usuario, contrasena)
        Usuarios.append(nuevo)
        return jsonify({'message': "successful",
                        'reason': "Se agrego el usuario"})

@app.route('/Usuario', methods=['POST']) # recupera la contrasena
def recuperarContrasena(): 
    global Usuarios
    
    usuario = request.json['usuario']
    
    encontrado = False
    
    for i in Usuarios:
        if i.getUsuario() == usuario:
            Dato={
                'contrasena': i.getContrasena()
            }
            break
    respuesta = jsonify(Dato)
    return(respuesta)

    

@app.route('/Usuarios/<string:usuario>', methods=['GET']) #se obtiene solo 1 persona
def getPersona(usuario): 
    
    global Usuarios
   
    for i in Usuarios:
        if i.getUsuario() == usuario:
            Dato={'Nombre' : i.getNombre(),
                'Apellido': i.getApellido(),
                'Usuario': i.getUsuario(),
                'Contrasena': i.getContrasena()}  
            
            break
    respuesta = jsonify(Dato)    
    return(respuesta)

@app.route('/Usuarios/<string:usuario>', methods=['PUT']) #se modifica usuario 
def modifyPersona(usuario): 
    global Usuarios
    encontrado = False
    for i in range(len(Usuarios)):
        if usuario == Usuarios[i].getUsuario():
            encontrado = True
            break
    if encontrado: 
        Usuarios[i].setNombre(request.json['nombre'])
        Usuarios[i].setApellido(request.json['apellido'])
        Usuarios[i].setUsuario(request.json['usuario'])
        Usuarios[i].setContrasena(request.json['contrasena'])
        return({'message': "Se modifico el Usuario"})
    else:
        return jsonify({'message': "el usuario ya existe"})

@app.route('/ModificarUsuario/<string:usuario>', methods=['PUT']) #se modifica usuario 
def modifyUser(usuario): 
    global Usuarios
    encontrado = False
    for i in range(len(Usuarios)):
        if usuario == Usuarios[i].getUsuario():
            encontrado = True
            break
    if encontrado: 
        return jsonify({'message': "el usuario ya existe"})
    else:
        Usuarios[i].setNombre(request.json['nombre'])
        Usuarios[i].setApellido(request.json['apellido'])
        Usuarios[i].setUsuario(request.json['usuario'])
        Usuarios[i].setContrasena(request.json['contrasena'])
        return({'message': "Se modifico el Usuario"})
        
        
            
@app.route('/Admin', methods=['GET']) #se modifica 1 usuario
def getAdmin(): 
    global Usuarios
    
    admin = Usuarios[0].getUsuario()
       
    return jsonify({'admin': admin})

@app.route('/Admin/<string:admin>', methods=['PUT']) #se modifica el administrador
def modifyAdmin(admin): 
    global Usuarios
    encontrado = False
    for i in range(len(Usuarios)):

        if admin == Usuarios[i].getUsuario():
            encontrado = True
            break
    if encontrado:
        return jsonify({'message': "el usuario ya existe"})
            
    else:
        Usuarios[0].setNombre(request.json['nombre'])
        Usuarios[0].setApellido(request.json['apellido'])
        Usuarios[0].setUsuario(request.json['usuario'])
        Usuarios[0].setContrasena(request.json['contrasena'])
        return({'message': "Se modifico el Usuario"})

@app.route('/Usuarios/<string:nombre>', methods=['DELETE']) #se elimina 1 usuario
def deletePersona(nombre): 
    global Usuarios
    for i in range(len(Usuarios)):

        if nombre == Usuarios[i].getNombre():
            del Usuarios[i]
            break
       
    return({'message': "Se Elimino el Usuario"})

@app.route('/Login', methods=['POST'])
def Login():
    global Usuarios
    
    username = request.json['username']
    password = request.json['password']

    for usuario in Usuarios:
        if usuario.getUsuario() == username and usuario.getContrasena() == password:
            Dato={'message': 'Bienvenido',
                  'usuario': usuario.getUsuario(),
                  'contrasena': usuario.getContrasena()
                 }
            break
        else:
            Dato={
                 'message': 'Usuario o contrasena no existen',
                 'usuario': ''   

            }
    respuesta = jsonify(Dato)
    return(respuesta)
    

@app.route('/Canciones', methods = ['POST'])
def crearCanciones():
    global Canciones, contador
    id = contador
    nombre = request.json['nombre']
    artista = request.json['artista']
    album = request.json['album']
    fecha = request.json['fecha']
    imagen = request.json['imagen']
    spotify = request.json['spotify']
    youtube = request.json['youtube']

    new = Cancion(id,nombre,artista,album,fecha,imagen,spotify,youtube)
    Canciones.append(new)
    contador += 1
    return jsonify({'message': "success",
                    'reason': "Se agrega la cancion"})


@app.route('/Canciones/<int:id>', methods=['GET']) #se obtiene solo 1 persona
def getCanciones(id): 
    
    global Canciones
   
    for i in Canciones:
        if i.getId() == id:
            Dato={'nombre' : i.getNombre(),
                'artista': i.getArtista(),
                'album': i.getAlbum(),
                'fecha': i.getFecha(),
                'imagen': i.getImagen(),
                'spotify': i.getSpotify(),
                'youtube': i.getYoutube()}  
            
            break
    respuesta = jsonify(Dato)    
    return(respuesta)

@app.route('/Canciones/<int:id>', methods=['PUT']) #se modifica 1 usuario
def modifyCancion(id): 
    global Canciones
    for i in range(len(Canciones)):

        if id == Canciones[i].getId():
            Canciones[i].setNombre(request.json['nombre'])
            Canciones[i].setArtista(request.json['artista'])
            Canciones[i].setAlbum(request.json['album'])
            Canciones[i].setFecha(request.json['fecha'])
            Canciones[i].setImagen(request.json['imagen'])
            Canciones[i].setSpotify(request.json['spotify'])
            Canciones[i].setYoutube(request.json['youtube'])
            break
       
    return({'message': "Se modifico la Cancion"})

@app.route('/Canciones', methods=['GET'])
def getCancion():
    global Canciones
    Datos = []

    for i in Canciones:
        Dato={
            'id': i.getId(),
            'nombre': i.getNombre(),
            'artista': i.getArtista(),
            'album': i.getAlbum(),
            'fecha': i.getFecha(),
            'imagen': i.getImagen(),
            'spotify': i.getSpotify(),
            'youtube': i.getYoutube()
        }
        Datos.append(Dato)
    respuesta = jsonify(Datos)
    return(respuesta)

@app.route('/Canciones/<string:nombre>', methods=['DELETE'])
def eliminarCancion(nombre):
    global Canciones
    
    for i in range(len(Canciones)):
        if nombre == Canciones[i].getNombre():
            del Canciones[i]
            break
       
    return({'message': "Se Elimino la Cancion"})

@app.route('/Comentarios/<int:id>', methods=['POST']) #se modifica 1 comentario
def crearComentario(id): 
    global Comentarios, Canciones, Usuarios, contador_comentarios 
    
    
    comentario = request.json['comentario']
    usuario = request.json['usuario']

    for i in range(len(Canciones)):
        if id == Canciones[i].getId():      
            nombre = Canciones[i].getNombre()
            imagen = Canciones[i].getImagen()
            new = Comentario(id,comentario, nombre, usuario, imagen)
            Comentarios.append(new)
            
            break

    return jsonify({'message': "success",
                    'reason': "se agrego el comentario"})

@app.route('/Comentarios/<int:id>', methods=['GET']) #se modifica 1 comentario
def getComentario(id): 
    global Comentarios 
    
    Datos = []

    for i in range(len(Comentarios)):
        if id == Comentarios[i].getId():
            Dato={
                'id': Comentarios[i].getId(),
                'comentario': Comentarios[i].getComentario(),
                'nombre': Comentarios[i].getNombre(),
                'usuario': Comentarios[i].getUsuario(),
                'imagen': Comentarios[i].getImagen()
                
            }
        Datos.append(Dato)
    respuesta = jsonify(Datos)
    return(respuesta)

@app.route('/Comentarios', methods=['GET']) #se obtiene los comentarios
def getComentario1(): 
    global Comentarios 
    
    Datos = []

    for i in range(len(Comentarios)):
        Dato={
                'id': Comentarios[i].getId(),
                'comentario': Comentarios[i].getComentario(),
                'nombre': Comentarios[i].getNombre(),
                'usuario': Comentarios[i].getUsuario(),
                'imagen': Comentarios[i].getImagen()
                
            }
        Datos.append(Dato)
    respuesta = jsonify(Datos)
    return(respuesta)

@app.route('/Solicitud', methods=['GET'])
def getSolicitud():
    global Solicitudes
    Datos = []

    for i in Solicitudes:
        Dato={
            'id': i.getId(),
            'nombre': i.getNombre(),
            'artista': i.getArtista(),
            'album': i.getAlbum(),
            'fecha': i.getFecha(),
            'imagen': i.getImagen(),
            'spotify': i.getSpotify(),
            'youtube': i.getYoutube()
        }
        Datos.append(Dato)
    respuesta = jsonify(Datos)
    return(respuesta)

@app.route('/Solicitud/<int:id>', methods=['DELETE']) # ay que pasar parametro para que funcione
def eliminarSolicitud(id):
    global Solicitudes
    
    for i in range(len(Solicitudes)):
        if id == Solicitudes[i].getId():
            del Solicitudes[i]
            break
       
    return({'message': "Se Elimino la Solicitud"})

@app.route('/Solicitud', methods = ['POST'])
def crearSolicitud():
    global Solicitudes, contador_solicitud
    id = contador_solicitud

    nombre = request.json['nombre']
    artista = request.json['artista']
    album = request.json['album']
    fecha = request.json['fecha']
    imagen = request.json['imagen']
    spotify = request.json['spotify']
    youtube = request.json['youtube']

    new = Solicitar(id,nombre,artista,album,fecha,imagen,spotify,youtube)
    Solicitudes.append(new)
    contador_solicitud += 1
    return jsonify({'message': "success",
                    'reason': "Se agrego la Solicitud"})

@app.route('/AgregarSolicitud/<int:id>', methods = ['POST']) #ay que pasar parametro para que funcione
def crearSolicitud1(id):
    global Solicitudes, contador, Canciones, contador_solicitud

    id_cancion = contador
    
    for i in range(len(Solicitudes)):
        if id==Solicitudes[i].getId():
            nombre = Solicitudes[i].getNombre()
            artista = Solicitudes[i].getArtista()
            album = Solicitudes[i].getAlbum()
            fecha = Solicitudes[i].getFecha()
            imagen = Solicitudes[i].getImagen()
            spotify = Solicitudes[i].getSpotify()
            youtube = Solicitudes[i].getYoutube()
            new = Cancion(id_cancion,nombre,artista,album,fecha,imagen,spotify,youtube)
            Canciones.append(new)
            Solicitudes.append(new)
            contador_solicitud +=1
            contador += 1
            break
            
    return jsonify({'message': "success",
                    'reason': "Se agrego la Solicitud"})

@app.route('/CrearPlayList/<int:id>', methods = ['POST']) #ay que pasar parametro para que funcione
def crearPlayList(id):
    global PlayList, Canciones

    for i in range(len(Canciones)):
        if id == Canciones[i].getId():
            nombre = Canciones[i].getNombre()
            artista = Canciones[i].getArtista()
            album = Canciones[i].getAlbum()
            fecha = Canciones[i].getFecha()
            imagen = Canciones[i].getImagen()
            spotify = Canciones[i].getSpotify()
            youtube = Canciones[i].getYoutube()
            new = playlist(id,nombre,artista,album,fecha,imagen,spotify,youtube)
            PlayList.append(new) 
            break
            
    return jsonify({'message': "success",
                    'reason': "Se agrego la cancion a la PlayList"})
    
@app.route('/getPlayList', methods=['GET'])
def getPlayList():
    global PlayList
    Datos = []

    for i in PlayList:
        Dato={
            'id': i.getId(),
            'nombre': i.getNombre(),
            'artista': i.getArtista(),
            'album': i.getAlbum(),
            'fecha': i.getFecha(),
            'imagen': i.getImagen(),
            'spotify': i.getSpotify(),
            'youtube': i.getYoutube()
        }
        Datos.append(Dato)
    respuesta = jsonify(Datos)
    return(respuesta)           
if __name__ == "__main__":
    app.run(threaded=True, host="0.0.0.0", port = 5000, debug=True)
