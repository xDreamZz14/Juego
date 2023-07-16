import json
from time import sleep

class Personaje:
    """
    Representa al personaje.

    Atributos:
    nivel (int): Nivel del personaje, por defecto 1
    exp (int): Cuando llega a cierto valor permite aumentar el nivel
    nombre (str): Valor indicado por el usuario al instanciar un personaje
    clase (str): Instanciado por el usuario en la creacion de personaje
    ataque (int): Definido por defecto al crear un personaje (Diferente para cada clase)
    dinero (int): Dinero del personaje con el que puede comprar diferentes objetos.
    salud (int): Salud del personaje, cada clase tiene un valor por defecto. Si llega a 0, muere
    defensa (int): Valor por defecto en cada clase, reduce el daño hasta el minimo posible: 1
    saludMaxima (int): Maximo valor al que puede llegar la salud
    mascotas (str): Lista que contiene el personaje, por defecto esta vacia. Aumentan los parametros del personaje
    pociones (str): Lista del personaje, pueden comprarse y recuperar salud. Por defecto esta vacia
    armaduras (str): Lista del personaje, pueden equiparse cambiando los parametros del personaje. Por defecto esta vacia

    """
    def __init__(self, nivel, exp, nombre, clase, ataque, dinero, salud, defensa, saludMaxima, mascotas, pociones, armaduras):
        """
        Inicializa un objeto de tipo Personaje.

        Argumentos:
        :param nivel:
        :param exp:
        :param nombre:
        :param clase:
        :param ataque:
        :param dinero:
        :param salud:
        :param defensa:
        :param saludMaxima:
        :param mascotas:
        :param pociones:
        :param armaduras:
        """
        self.nivel = nivel
        self.exp = exp
        self.nombre = nombre
        self.clase = clase
        self.ataque = ataque
        self.dinero = dinero
        self.salud = salud
        self.defensa = defensa
        self.saludMaxima = saludMaxima
        self.mascotas = mascotas
        self.pociones = pociones
        self.armaduras = armaduras

    def ganarExp(self, cantidad):
        """
        Metodo creado para aumentar la experiencia de el personaje y subir de nivel.
        Cuando llega al maximo, se actualiza y suma los atributos correspondientes a su clase.

        Argumentos:
        :param cantidad:
        :return:
        """
        self.exp = self.exp + cantidad
        while self.exp >= 20:
            self.nivel = self.nivel + 1
            self.exp = self.exp - 20
            if self.clase == "Bruja":
                self.ataque = self.ataque + 2
                self.salud = self.salud + 8
                self.defensa = self.defensa + 6
                self.saludMaxima = self.saludMaxima + 8

            if self.clase == "Canalla":
                self.ataque = self.ataque + 3
                self.salud = self.salud + 5
                self.defensa = self.defensa + 5
                self.saludMaxima = self.saludMaxima + 5

    def atacarMonstruo(self, daño, monstruo):
        """
        Permite atacar a un monstruo hasta que su salud llega a 0 y suma la experiencia del mismo
        a el personaje.
        Mientras monstruo.salud no sea <= 0 lo actualiza restando el daño recibido
        y lo muestra al usuario.

        Argumentos:
        :param daño:
        :param monstruo:
        :return:
        """
        monstruo.salud = monstruo.salud - daño
        if monstruo.salud <= 0:
            print(monstruo.nombre + " Ha muerto")
            self.ganarExp(monstruo.exp)
        else:
            print("La salud de " + monstruo.nombre + " es " + str(monstruo.salud))

    def guardarPartida(self):
        """
        Metodo creado para guardar el progreso realizado en la partida.
        Almacena todos los datos de la instancia Personaje en un diccionario
        usando un .json

        :return:
        """
        savePersonaje = {
            "nombre":self.nombre,
            "nivel":self.nivel,
            "exp":self.exp,
            "clase":self.clase,
            "ataque":self.ataque,
            "dinero":self.dinero,
            "salud":self.salud,
            "defensa":self.defensa,
            "saludMaxima":self.saludMaxima,
            "mascotas":self.mascotas,
            "pociones":self.pociones,
            "armaduras":self.armaduras
        }
        with open("Save " + self.nombre + ".json", "w") as json_file:
            json.dump(savePersonaje,json_file,indent=4)

    def guardarPartidaTxt(self):
        """
        Igual que guardarPartida() pero en este caso usamos el formato .txt
        (A la hora de querer ver cada atributo es menos intuitivo, por lo tanto no es recomendado usarlo)

        :return:
        """
        with open("Save " + self.nombre + ".txt", "w") as save_file:
            save_file.write(str(self.nivel) + "," +
                            str(self.exp) + "," +
                            self.nombre + "," +
                            self.clase + "," +
                            str(self.ataque) + "," +
                                str(self.dinero) + "," +
                                str(self.salud) + "," +
                                str(self.defensa) + "," +
                                str(self.saludMaxima) + "," + str(self.mascotas) +
                             "," + str(self.pociones) + "," + str(self.armaduras))

    def usarPocion(self):
        """
        Metodo del personaje. Sirve para recuperar salud usando pociones almacenadas self.pociones.
        En caso de no tener ninguna se lo indica al usuario.
        Si la salud recuperada supera a la saludMaxima, actualiza self.salud para tener el valor maximo (self.saludMaxima)

        :return:
        """
        if not self.pociones:
            print("No hay pociones en el inventario")
            sleep(0.5)
        else:
            pocion = input(f"¿Que pocion deseas usar?: {self.pociones}").capitalize()
            if pocion not in self.pociones:
                print(f"No tienes ninguna {pocion} ")
                sleep(1)
                self.usarPocion()
            else:
                for pot in self.pociones:
                    if pocion == pot.nombre: #pot.content.capitalize()
                        self.salud += pot.crecuperacion
                        self.pociones.remove(pot)
                        print(f"Has recuperado {pot.crecuperacion} de salud")
                if self.salud > self.saludMaxima:
                    self.salud = self.saludMaxima



class Monstruo:
    """
    Representa los monstruos instanciados.

    Atributos:
    nombre (str): Nombre del monstruo instanciado en el programa
    salud (int): Salud de Monstruo, indica si sigue vivo o en caso de llegar a 0, muere.
    drop (str,int): Objetos o dinero que contiene el Monstruo. Cuando muere puede soltar un objeto
    aleatorio o dinero al personaje.
    exp (int): Experiencia que otorga al personaje cuando la salud de Monstruo llega a 0.
    ataque (int): Ataque que contiene Monstruo. Sirve para quitar puntos de salud al Personaje.
    """
    def __init__(self, nombre, salud, drop, exp, ataque):  # drop = oro
        """
        Argumentos:
        :param nombre: 
        :param salud: 
        :param drop: 
        :param exp: 
        :param ataque: 
        """
        self.nombre = nombre
        self.salud = salud
        self.drop = drop
        self.exp = exp
        self.ataque = ataque

    def atacarPersonaje(self, daño, personaje):
        """
        Metodo que sirve para realizar daño a Personaje. Indica la salud restante al usuario.
        En caso de que Personaje tenga cierta cantidad de defensa, reduce el daño realizado
        por Monstruo hasta un minimo de 1.

        Argumentos:
        :param daño: 
        :param personaje: 
        :return: 
        """
        if personaje.defensa >= 15:
            daño = daño - 3
        elif personaje.defensa >= 10:
            daño = daño - 2
        elif personaje.defensa >= 5:
            daño = daño - 1
        if daño < 1:
            daño = 1
        personaje.salud = personaje.salud - daño
        if personaje.salud <= 0:
            print(personaje.nombre + " Ha muerto")
        else:
            print("La salud de " + personaje.nombre + " es "
                  + str(personaje.salud))


class Mascota:
    """
    Representa a las Mascotas instanciadas.

    Atributos:
    nombre (str): Nombre de Mascota instanciado en el programa
    bataaque (int): Bufo de ataque. Cuando el usuario compra la Mascota, suma su ataque a la de Personaje
    bsalud (int): Bufo de salud. Cuando el usuario compra la Mascota, suma su salud a la de Personaje
    bdefensa (int): Bufo de defensa. Cuando el usuario compra la Mascota, suma su defensa a la de Personaje
    precio (int): Costo de Mascota que se indica al usuario en el programa
    """
    def __init__(self, nombre, bataque, bsalud, bdefensa, precio):  # b = buff
        """
        Argumentos:
        :param nombre:
        :param bataque:
        :param bsalud:
        :param bdefensa:
        :param precio:
        """
        self.nombre = nombre
        self.bataque = bataque
        self.bsalud = bsalud
        self.bdefensa = bdefensa
        self.precio = precio


class Pocion:
    """
    Representa a las Pociones instanciadas

    Atributos:
    nombre (str): Nombre de Pocion instanciado en el programa
    crecuperacion (int): Cantidad que recupera la Pocion usada
    precio (int): Precio requerido para comprar Pocion, indicado al usuario en el programa

    """
    def __init__(self, nombre, crecuperacion, precio):  # c = cantidad
        """
        Argumentos:
        :param nombre:
        :param crecuperacion:
        :param precio:
        """
        self.nombre = nombre
        self.crecuperacion = crecuperacion
        self.precio = precio



class Armadura:
    """
    Representa a las Armaduras instanciadas

    Atributos:
    nombre (str): Nombre de Armadura instanciado en el programa
    crequerida (str): Clase requerida para poder comprar la Armadura
    defensa (int): Defensa que contiene Armadura, añadida al usuario al comprar
    salud (int): Salud que contiene Armadura, añadida al usuario al comprar
    precio (int): Precio requerido para comprar Armadura
    """
    def __init__(self,nombre,crequerida,defensa,salud,precio): # c = clase
        self.nombre = nombre
        self.crequerida = crequerida
        self.defensa = defensa
        self.salud = salud
        self.precio = precio

"""
class Ciudad:
    def __init__(self,nombre,nivelr)
        self.nombre = nombre
        self.nivelr = nivelr   #nivelr = nivelrequerido

estivania = Ciudad("Estivania",1)
zanarkand = Ciudad("Zanarkand",8)
meowyork = Ciudad("MeowYork",20)
"""