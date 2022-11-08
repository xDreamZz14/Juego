import os

from time import sleep

class Personaje:
    def __init__(self,nivel,exp,nombre,clase,ataque):
        self.nivel = nivel
        self.exp = exp
        self.nombre = nombre
        self.clase = clase
        self.ataque = ataque

    def ganarExp(self,cantidad):
        self.exp = self.exp + cantidad
        while self.exp >= 20:
           self.nivel = self.nivel + 1
           self.exp = self.exp - 20   # Aumentar ataque de cada clase
           if self.clase == "Bruja":
               self.ataque = self.ataque + 5
           if self.clase == "Canalla":
               self.ataque = self.ataque + 3


    def atacarMonstruo(self,daño,monstruo):
        monstruo.salud = monstruo.salud - daño
        if monstruo.salud <= 0:
            print(monstruo.nombre + " Ha muerto")
            self.ganarExp(monstruo.exp)
        else:
            print("La salud de " + monstruo.nombre + " es " + str(monstruo.salud))


    def guardarPartida(self):
        with open("Save " + personaje.nombre + ".txt", "w") as text_file:
            text_file.write(str(personaje.nivel) + "," +
                            str(personaje.exp) + "," +
                            personaje.nombre + "," +
                            personaje.clase + "," +
                            str(personaje.ataque))

class Monstruo:
    def __init__(self,nombre,salud,drop,exp): # drop = oro
        self.nombre = nombre
        self.salud = salud
        self.drop = drop
        self.exp = exp


# l = Lista
lArchivos = os.listdir()  # listdir devuelve lista de archivos en una carpeta, si no pones nada muestra la carpeta actual
nSave = ""
dPersonaje = ""
while nSave not in lArchivos:
    cPartida = input("(Si/No)Quieres cargar una partida: ")
    if cPartida == "Si":  # c = Cargar
        cPersonaje = input("Introduce el nombre de tu personaje: ")
        nSave = "Save " + cPersonaje + ".txt"
        if nSave in lArchivos:
            with open("Save " + cPersonaje + ".txt", "r") as save:
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
            ataque = 2
        elif eclase == 2:
            clase = "Bruja"
            ataque = 6
        else:
            print("No es una clase valida")

    personaje = Personaje(1, 0, nombre, clase, ataque)
    print("Se ha creado un personaje llamado " + personaje.nombre + " de clase " + personaje.clase)
else: # Existen dPersonaje
    dPersonaje = dPersonaje.split(",") # ['1', '3', 'Dream', 'Canalla', '2'] split convierte string a lista, separado por un caracter. En este caso ,
    personaje = Personaje(int(dPersonaje[0]),int(dPersonaje[1]),dPersonaje[2],
                          dPersonaje[3],int(dPersonaje[4]))
    print("Se han cargado los datos de " + personaje.nombre)

orco = Monstruo("Orco",25,2,15)
vaca = Monstruo("Vaca",3,2,3)
atacarMonstruo = ""
totalMonstruo = 0
while atacarMonstruo != "Si" and atacarMonstruo != "No":
    atacarMonstruo = input("(Si/No)¿Quieres atacar a un monstruo?: ")
if atacarMonstruo == "Si":
   sMonstruo = input("¿A que monstruo quieres atacar?:\n1.Orco\n2.Vaca\n")
elif atacarMonstruo == "No":
    print("A descansar")
if sMonstruo == "1":
    while orco.salud > 0:
        personaje.atacarMonstruo(personaje.ataque,orco)
        sleep(1)
        if orco.salud <= 0:
            print("Nivel: " + str(personaje.nivel) + "\nEXP: " + str(personaje.exp))
if sMonstruo == "2":
    while vaca.salud > 0:
        personaje.atacarMonstruo(personaje.ataque,vaca)
        sleep(1)
        if vaca.salud <= 0:
            print("Nivel: " + str(personaje.nivel) + "\nEXP: " + str(personaje.exp))
totalMonstruo = totalMonstruo + 1
seguirMatando = ""

while seguirMatando != "No":
    seguirMatando = input("(Si/No) Quieres seguir matando monstruos: ")
    if seguirMatando == "Si":
       sMonstruo = input("¿A que monstruo quieres atacar?:\n1.Orco\n2.Vaca\n")

       if sMonstruo == "1":
          orco = Monstruo("Orco",25,2,15)
          while orco.salud > 0:
            personaje.atacarMonstruo(personaje.ataque,orco)
            sleep(1)
            if orco.salud <= 0:
                print("Nivel: " + str(personaje.nivel) + "\nEXP: " + str(personaje.exp))

       if sMonstruo == "2":
          vaca = Monstruo("Vaca",3,2,3)
          while vaca.salud > 0:
            personaje.atacarMonstruo(personaje.ataque,vaca)
            sleep(1)
            if vaca.salud <= 0:
                print("Nivel: " + str(personaje.nivel) + "\nEXP: " + str(personaje.exp))
       totalMonstruo = totalMonstruo + 1
    elif seguirMatando != "No":
        print("Selecciona Si/No")

irCiudad = input("(Si/No)¿Quieres ir a la ciudad?: ")
if irCiudad == "Si":
    accion = input("Bienvenido a Estivania, ¿Que quieres hacer?:\n1.Descansar\n2.Comprar\n3.Guardar ")
    if accion == "1":
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




# Dar la opcion de seguir matando sMonstruo
# Hacer una clase Ciudad y dar opciones

"""
class Ciudad:
    def __init__(self,nombre,nivelr,medico,mercader,posada,arena)
        self.nombre = nombre
        self.nivelr = nivelr   #nivelr = nivelrequerido
        self.medico = medico
        self.mercader = mercader
        self.posada = posada
        self.arena = arena

c1 = Ciudad("Estivania",1,"Medico","Mercader","Posada")
c2 = Ciudad("Zanarkand",8,"Medico","Mercader","Posada","Arena")
    
    
        
        
"""

"""
dream = Personaje(1,0)
print(dream.nivel,dream.exp)
dream.ganarExp(20)
print(dream.nivel,dream.exp)
orco = Monstruo("Orco",200,"",43)
dream.atacarMonstruo(180,orco)
dream.atacarMonstruo(40,orco)
print("Nivel: " + str(dream.nivel) + "\nEXP: " + str(dream.exp))
"""