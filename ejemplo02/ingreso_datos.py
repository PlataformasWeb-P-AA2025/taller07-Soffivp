from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# importa las tablas club y jugador
from genera_tablas import Club, Jugador

# traemos las configuraciones de la base de datos
from configuracion import cadena_base_datos
# nos enlazamos a la base de datos 
engine = create_engine(cadena_base_datos)

Session = sessionmaker(bind=engine)
session = Session()


#abro el archivo txt y lo transformo en una lista de listas y los separa por ;
with open("data/datos_clubs.txt") as archivo:
    datoClubs = [linea.split(";") for linea in archivo	]
    #recorro la lista y le asigno a cada dato del objeto un dato de la lista
    for linea in datoClubs:
        club = Club(nombre=linea[0], deporte=linea[1], fundacion=int(linea[2]))
        # Agrega a sesion el objeto de  la tabla club creado 
        session.add(club)

 
#abro el archivo txt y lo transformo en una lista de listas y los separa por ;     
with open("data/datos_jugadores.txt") as archivo:
    datoJugadores = [linea.split(";") for linea in archivo	]

    #separo los datos de cada club deportivo para asignarle el objeto del club correspondiente
    for linea in datoJugadores[0:21]:
    	# obtenemos el objeto de la tabla club con el nombre Barcelona y 
    	# lo asignamos al dato club del jugador
    	datoClub =session.query(Club).filter_by(nombre="Barcelona").one()
    	jugador = Jugador(nombre =linea[3], dorsal=int(linea[2]), posicion=linea[1],club=datoClub)
    	#Agregamos el jugador a la sesion 
    	session.add(jugador)


    for linea in datoJugadores[21:42]:
    	# obtenemos el objeto de la tabla club con el nombre Independiente del Valle y 
    	# lo asignamos al dato club del jugador
    	datoClub =session.query(Club).filter_by(nombre="Independiente del Valle").one()
    	jugador = Jugador(nombre =linea[3], dorsal=int(linea[2]), posicion=linea[1],club=datoClub)
    	session.add(jugador)


    for linea in datoJugadores[42:61]:
    	# obtenemos el objeto de la tabla club con el nombre Mushuc Runa y 
    	# lo asignamos al dato club del jugador
    	datoClub =session.query(Club).filter_by(nombre="Mushuc Runa").one()
    	jugador = Jugador(nombre =linea[3], dorsal=int(linea[2]), posicion=linea[1],club=datoClub)
    	session.add(jugador) 

    for linea in datoJugadores[61:79]:
    	# obtenemos el objeto de la tabla club con el id 4 y 
    	# lo asignamos al dato club del jugador
    	datoClub =session.query(Club).filter_by(id=4).one()
    	jugador = Jugador(nombre =linea[3], dorsal=int(linea[2]), posicion=linea[1],club=datoClub)
    	session.add(jugador) 
   
#guarda la sesion 
session.commit()


