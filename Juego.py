import os

from time import sleep

def menuCiudad(): # pegar todo lo de la ciudad

class Personaje:
    def __init__(self,nivel,exp,nombre,clase,ataque,dinero,salud,defensa): # saludMaxima
        self.nivel = nivel
        self.exp = exp
        self.nombre = nombre
        self.clase = clase
        self.ataque = ataque
        self.dinero = dinero
        self.salud = salud
        self.defensa = defensa

    def ganarExp(self,cantidad):
        self.exp = self.exp + cantidad
        while self.exp >= 20:
           self.nivel = self.nivel + 1
           self.exp = self.exp - 20   # Aumentar ataque de cada clase
           if self.clase == "Bruja":
               self.ataque = self.ataque + 5
               self.salud = self.salud + 8
               self.defensa = self.defensa + 6
           if self.clase == "Canalla":
               self.ataque = self.ataque + 3
               self.salud = self.salud + 5
               self.defensa = self.defensa + 5

    def atacarMonstruo(self,daño,monstruo):
        monstruo.salud = monstruo.salud - daño
        if monstruo.salud <= 0:
            print(monstruo.nombre + " Ha muerto")
            self.ganarExp(monstruo.exp)
        else:
            print("La salud de " + monstruo.nombre + " es " + str(monstruo.salud))

    def guardarPartida(self):
        with open("Test " + personaje.nombre + ".txt", "w") as text_file:
            text_file.write(str(personaje.nivel) + "," +
                            str(personaje.exp) + "," +
                            personaje.nombre + "," +
                            personaje.clase + "," +
                            str(personaje.ataque + "," +
                                personaje.dinero + "," +
                                personaje.salud))


class Monstruo:
    def __init__(self,nombre,salud,drop,exp,ataque): # drop = oro
        self.nombre = nombre
        self.salud = salud
        self.drop = drop
        self.exp = exp
        self.ataque = ataque

    def atacarPersonaje(self,daño,personaje):
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

# l = Lista
lArchivos = os.listdir()  # listdir devuelve lista de archivos en una carpeta, si no pones nada muestra la carpeta actual
nSave = ""
dPersonaje = ""
while nSave not in lArchivos:
    cPartida = input("(Si/No)Quieres cargar una partida: ")
    if cPartida == "Si":  # c = Cargar
        cPersonaje = input("Introduce el nombre de tu personaje: ")
        nSave = "Test " + cPersonaje + ".txt"
        if nSave in lArchivos:
            with open("Test " + cPersonaje + ".txt", "r") as save:
                dPersonaje = save.read()        # Datos personaje
        else: # Si no hay save para ese nombre
            print("No existe ningun personaje con ese nombre")
    else:
        break # Rompe el bucle while


if dPersonaje == "":
    nombre = input("Introduce tu nombre: ")
    eclase = 0
    while eclase != 1 and eclase != 2:
        eclase = int(input("(Indica con un numero) Que clase quieres escoger: \n1.Canalla\n2.Bruja\n"))
        if eclase == 1:
            clase = "Canalla"
            ataque = 4
            salud = 40
            defensa = 7
        elif eclase == 2:
            clase = "Bruja"
            ataque = 6
            salud = 50
            defensa = 10
        else:
            print("No es una clase valida")

    personaje = Personaje(1,0,nombre,clase,ataque,0,salud,defensa)
    print("Se ha creado un personaje llamado " + personaje.nombre + " de clase " + personaje.clase)
else: # Existen dPersonaje
    dPersonaje = dPersonaje.split(",") # ['1', '3', 'Dream', 'Canalla', '2'] split convierte string a lista, separado por un caracter. En este caso ,
    personaje = Personaje(int(dPersonaje[0]),int(dPersonaje[1]),dPersonaje[2],
                          dPersonaje[3],int(dPersonaje[4]),int(dPersonaje[5])
                          ,int(dPersonaje[6]),int(dPersonaje[7]))
    print("Se han cargado los datos de " + personaje.nombre)

orco = Monstruo("Orco",20,5,8,5)
vaca = Monstruo("Vaca",6,2,3,2)
atacarMonstruo = ""
totalMonstruo = 0
sMonstruo = ""
while atacarMonstruo != "Si" and atacarMonstruo != "No":
    atacarMonstruo = input("(Si/No)¿Quieres atacar a un monstruo?: ")
if atacarMonstruo == "Si":
   sMonstruo = input("¿A que monstruo quieres atacar?:\n1.Orco\n2.Vaca\n")
elif atacarMonstruo == "No":
    print("A descansar")

if sMonstruo == "1":
    while orco.salud > 0:
        personaje.atacarMonstruo(personaje.ataque, orco)
        if orco.salud > 0:
            orco.atacarPersonaje(orco.ataque, personaje)
        sleep(1)
        if orco.salud <= 0:
            personaje.dinero = personaje.dinero + orco.drop
            print("Nivel: " + str(personaje.nivel)
                  + "\nEXP: " + str(personaje.exp) + "\nDinero: " +
                  str(personaje.dinero))

if sMonstruo == "2":
    while vaca.salud > 0:
        personaje.atacarMonstruo(personaje.ataque, vaca)
        if vaca.salud > 0:
            vaca.atacarPersonaje(vaca.ataque,personaje)
        sleep(1)
        if vaca.salud <= 0:
            personaje.dinero = personaje.dinero + vaca.drop
            print("Nivel: " + str(personaje.nivel) + "\nEXP: " + str(personaje.exp))
totalMonstruo = totalMonstruo + 1
seguirMatando = ""

while seguirMatando != "No" and atacarMonstruo != "No":
    seguirMatando = input("(Si/No) Quieres seguir matando monstruos: ")
    if seguirMatando == "Si":
       sMonstruo = input("¿A que monstruo quieres atacar?:\n1.Orco\n2.Vaca\n")

       if sMonstruo == "1":
           orco = Monstruo("Orco",20,2,8,4)
           while orco.salud > 0:
               personaje.atacarMonstruo(personaje.ataque, orco)
               if orco.salud > 0:
                  orco.atacarPersonaje(orco.ataque, personaje)
               sleep(1)
               if orco.salud <= 0:
                   personaje.dinero = personaje.dinero + orco.drop
                   print("Nivel: " + str(personaje.nivel) + "\nEXP: " + str(personaje.exp))

       if sMonstruo == "2":
          vaca = Monstruo("Vaca",6,2,3,2)
          while vaca.salud > 0:
            personaje.atacarMonstruo(personaje.ataque, vaca)
            if vaca.salud > 0:
               vaca.atacarPersonaje(vaca.ataque, personaje)
            sleep(1)
            if vaca.salud <= 0:
                personaje.dinero = personaje.dinero + vaca.drop
                print("Nivel: " + str(personaje.nivel) + "\nEXP: " + str(personaje.exp))
       totalMonstruo = totalMonstruo + 1
    elif seguirMatando != "No":
        print("Selecciona Si/No")

irCiudad = input("(Si/No)¿Quieres ir a la ciudad?: ")
if irCiudad == "Si":
    accion = input("Bienvenido a Estivania, ¿Que quieres hacer?:\n1.Descansar\n2.Comprar\n3.Guardar ")
    if accion == "1":
        # personaje.salud = personaje.saludMaxima
        # Hacer que se cure
        print(personaje.nombre + " ha recuperado su salud ")# + personaje.salud)
        # [!]Dar la opcion de volver a matar monstruos o seguir en la ciudad

    elif accion == "2":
        sTienda = input("¿Que deseas comprar?:\n1.Mascota\n2.Pocion\n3.Armadura ")
        if sTienda == "1":
            print("Has comprado una Mascota")
            # if personaje.dinero < objeto.precio:
                # print("Dinero insuficiente")
            print("Gracias por comprar en la tienda")
        elif sTienda == "2":
            print("Has comprado una Pocion")
            print("Gracias por comprar en la tienda")
        elif sTienda == "3":
            print("Has comprado una Armadura")
            print("Gracias por comprar en la tienda")
        else:
            print("Vuelva pronto")
        # Dar la opcion de seguir en la ciudad o volver a matar monstruos

    if accion == "3":
        gPartida = input("¿Desea guardar la partida?(Si/No): ")
        while gPartida != "Si" and gPartida != "No":
            gPartida = input("¿Desea guardar la partida?(Si/No): ")
        if gPartida == "Si":
            personaje.guardarPartida()
            print("Progreso guardado, gracias por jugar")
        while gPartida == "No":
            ngPartida = input("¿Esta seguro de no guardar su partida?(Si/No): ")
            if ngPartida == "Si":  # ngPartida = noguardarPartida
               accion = input("¿Que quieres hacer?:\n1.Descansar\n2.Comprar\n3.Guardar ") # Crear funcion menu ciudad
            elif ngPartida == "No":
                 gPartida = input("¿Desea guardar la partida?(Si/No): ")
                 if gPartida == "Si":
                    personaje.guardarPartida()
                    print("Progreso guardado, gracias por jugar")

else:
    print("Gracias por jugar!!!\n" + personaje.nombre +
          " ha matado a " + str(totalMonstruo) +
          " monstruos\n" + "Nivel: " + str(personaje.nivel)
          + "EXP: " + str(personaje.exp))