import os

from time import sleep
from Clases import *  # Importa todas las clases y metodos de Clases.py



def cargarPartida():
    """
    Busca en el directorio un archivo .json con el nombre indicado
    y en caso de existir lo abre y crea una instancia de personaje
    con los atributos y objetos guardados.

    En caso de no existir, se lo indica al usuario y le lleva
    a la creacion de personaje.
    :return:
    """
    lArchivos = os.listdir()  # listdir devuelve lista de archivos en una carpeta, si no pones nada muestra la carpeta actual
    nSave = ""
    while nSave not in lArchivos:
        cPersonaje = input("Introduce el nombre de tu personaje: ").capitalize()
        nSave = "Save " + cPersonaje + ".json"
        if nSave in lArchivos:
            with open("Save " + cPersonaje + ".json", "r") as save:
                dPersonaje = json.load(save)  # Datos personaje
                sleep(1)
                personaje = Personaje(dPersonaje["nivel"],
                                      dPersonaje["exp"],
                                      dPersonaje["nombre"],
                                      dPersonaje["clase"],
                                      dPersonaje["ataque"],
                                      dPersonaje["dinero"],
                                      dPersonaje["salud"],
                                      dPersonaje["defensa"],
                                      dPersonaje["saludMaxima"],
                                      dPersonaje["mascotas"],
                                      dPersonaje["pociones"],
                                      dPersonaje["armaduras"])
                print("Se han cargado los datos de " + personaje.nombre)
                return personaje

        else:  # Si no hay save para ese nombre
            print("No existe ningun personaje con ese nombre")
            return None


def muertePersonaje():
    """
    Se llama en caso de que la salud del personaje llegue a 0.

    Permite elegir al usuario si quiere cargar la partida y llama a la funcion cargarPartida(),
    y en caso de que no, para el juego.
    :return:
    """
    cargarMuerte = input("(Si/No) ¿Deseas cargar la partida?: ").capitalize()
    if cargarMuerte == "Si":
        sleep(0.2)
        personaje = cargarPartida()
        return personaje
    else:
        print("Game over, gracias por jugar")
        exit()

def matarMonstruo(personaje):
    """
    Toma como argumento la instancia de personaje y permite pelear
    contra diferentes tipos de monstruos, con stats propios cada uno instanciados dentro de la funcion.

    Permite repetirlo hasta que el usuario indique que quiere parar y da la opcion de parar el juego
    o de ir a la ciudad con la funcion menuCiudad().

    En caso de muerte de el personaje, permite cargar los ultimos datos del personaje con muertePersonaje().

    :param personaje:
    :return:
    """
    orco = Monstruo("Orco", 20, 5, 8, 5)
    vaca = Monstruo("Vaca", 6, 2, 3, 2)
    atacarMonstruo = ""
    totalMonstruo = 0
    sMonstruo = ""
    while atacarMonstruo != "Si" and atacarMonstruo != "No":
        atacarMonstruo = input("(Si/No)¿Quieres atacar a un monstruo?: ").capitalize()
        sleep(0.2)
    if atacarMonstruo == "Si":
        sMonstruo = input("¿A que monstruo quieres atacar?:\n1.Orco\n2.Vaca\n").capitalize()
        sleep(0.2)
    elif atacarMonstruo == "No":
        irCiudad = input("(Si/No)¿Quieres ir a la ciudad?: ").capitalize()
        if irCiudad == "Si":
            sleep(0.5)
            menuCiudad()
        elif irCiudad == "No":
            print("Gracias por jugar")
            exit()


    while sMonstruo != "1" and sMonstruo != "2" and sMonstruo != "Orco" and sMonstruo != "Vaca":
        sMonstruo = input("¿A que monstruo quieres atacar?:\n1.Orco\n2.Vaca\n").capitalize()
        sleep(0.2)
    if sMonstruo == "1" or sMonstruo == "Orco":
        while orco.salud > 0:
            personaje.atacarMonstruo(personaje.ataque, orco)
            if orco.salud > 0:
                orco.atacarPersonaje(orco.ataque, personaje)
            sleep(0.5)
            if personaje.salud <= 0:
                personaje = muertePersonaje()
            if orco.salud <= 0:
                personaje.dinero = personaje.dinero + orco.drop
                print("Nivel: " + str(personaje.nivel)
                      + "\nEXP: " + str(personaje.exp) + "\nDinero: " +
                      str(personaje.dinero))
            sleep(1)


    if sMonstruo == "2" or sMonstruo == "Vaca":
        while vaca.salud > 0:
            personaje.atacarMonstruo(personaje.ataque, vaca)
            if vaca.salud > 0:
                vaca.atacarPersonaje(vaca.ataque, personaje)
            sleep(1)
            if personaje.salud <= 0:
                personaje = muertePersonaje()
            if vaca.salud <= 0:
                personaje.dinero = personaje.dinero + vaca.drop
                print("Nivel: " + str(personaje.nivel) + "\nEXP: "
                      + str(personaje.exp) + "\nDinero: " +
                      str(personaje.dinero))
            sleep(0.5)
    totalMonstruo = totalMonstruo + 1
    seguirMatando = ""

    while seguirMatando != "No" and atacarMonstruo != "No":
        seguirMatando = input("(Si/No) Quieres seguir matando monstruos: ").capitalize()
        if seguirMatando == "Si":
            sMonstruo = input("¿A que monstruo quieres atacar?:\n1.Orco\n2.Vaca\n").capitalize()
            while sMonstruo != "1" and sMonstruo != "2" and sMonstruo != "Orco" and sMonstruo != "Vaca":
                sMonstruo = input("¿A que monstruo quieres atacar?:\n1.Orco\n2.Vaca\n").capitalize()
            if sMonstruo == "1" or sMonstruo == "Orco":
                orco = Monstruo("Orco", 20, 5, 8, 5)
                while orco.salud > 0:
                    personaje.atacarMonstruo(personaje.ataque, orco)
                    if orco.salud > 0:
                        orco.atacarPersonaje(orco.ataque, personaje)
                    sleep(1)
                    if personaje.salud <= 0:
                        personaje = muertePersonaje()
                    if orco.salud <= 0:
                        personaje.dinero = personaje.dinero + orco.drop
                        print("Nivel: " + str(personaje.nivel) +
                              "\nEXP: " + str(personaje.exp)
                              + "\nDinero: " + str(personaje.dinero))
                    sleep(0.5)

            if sMonstruo == "2" or sMonstruo == "Vaca":
                vaca = Monstruo("Vaca", 6, 2, 3, 2)
                while vaca.salud > 0:
                    personaje.atacarMonstruo(personaje.ataque, vaca)
                    if vaca.salud > 0:
                        vaca.atacarPersonaje(vaca.ataque, personaje)
                    sleep(1)
                    if personaje.salud <= 0:
                        personaje = muertePersonaje()
                    if vaca.salud <= 0:
                        personaje.dinero = personaje.dinero + vaca.drop
                        print("Nivel: " + str(personaje.nivel) +
                              "\nEXP: " + str(personaje.exp) + "\nDinero: " +
                              str(personaje.dinero))
                    sleep(0.5)
            totalMonstruo = totalMonstruo + 1
        elif seguirMatando != "No" and seguirMatando != "Si":
            print("Selecciona Si/No")

    irCiudad = input("(Si/No)¿Quieres ir a la ciudad?: ").capitalize()
    if irCiudad == "Si":
        menuCiudad()
    else:
        print("Gracias por jugar")
        exit()


def seguirCiudad():
    """
    Despues de cada accion en la ciudad, da la opcion de poder seguir realizando diferentes cosas
    en la ciudad o en caso de no querer, regresar a matar monstruos o terminar la partida.

    :return:
    """
    seguir = input("(Si/No)¿Deseas seguir en la ciudad?: ").capitalize()
    if seguir == "Si":
        sleep(0.5)
        menuCiudad()
    else:
        seguirpartida = input("(Si/No)¿Deseas matar monstruos? ").capitalize()
        if seguirpartida == "Si":
            sleep(0.5)
            matarMonstruo(personaje)
        else:
            print("Gracias por jugar, vuelve pronto")
            exit()



def menuCiudad():
    """
    Le pide al usuario que indique la accion que desea hacer.

    accion == 1: Restaura la salud del personaje actualizando el valor de la misma con su salud
    maxima e indica al usuario la salud recuperada.

    accion == 2: Permite al jugador decidir que desea comprar y le muestra nombre,stats y precio
    de cada articulo a la venta. Cuando lo compra añade el objeto al inventario del personaje
    con la funcion str.append()

    accion == 3: Guarda el progeso realizado hasta el momento junto con todos los objetos
     que contiene el personaje y lo almacena en un archivo .json .

    accion == 4: Devuelve al jugador a la funcion matarMonstruo().

    :return:
    """
    accion = input("Bienvenido a Estivania, ¿Que quieres hacer?:\n1. Descansar\n2. Comprar"
                   "\n3. Guardar\n4. Salir a cazar\n").capitalize()
    if accion == "1" or accion == "Descansar":
        print(personaje.nombre + " ha recuperado " +
              str(personaje.saludMaxima - personaje.salud))
        sleep(0.5)
        personaje.salud = personaje.saludMaxima
        seguirCiudad()

    elif accion == "2" or accion == "Comprar":
        sTienda = input("¿Que deseas comprar?:\n1. Mascota\n2. Pociones\n3. Armadura\n4. Nada\n").capitalize()
        sleep(0.5)
        if sTienda == "1" or sTienda == "Mascota":
            perro = Mascota("Perro", 2, 5, 1, 35)
            gato = Mascota("Gato", 5, 3, 0, 35)
            dragon = Mascota("Dragon", 45, 70, 18, 560)
            cMascota = input("¿Que mascota deseas comprar?:\n1. " + perro.nombre  # c = comprar
                             + "  Precio: " + str(perro.precio) + " Stats perro: " + "Salud: "
                             + str(perro.bsalud) + str(perro.bataque) + " Defensa: " +str(perro.bdefensa)
                             + "\n2. " + gato.nombre + "  Precio: " + str(gato.precio) + " Stats gato:" +
                             " Salud: " + str(gato.bsalud) + " Ataque: " + str(gato.bataque) +
                             " Defensa: " + str(gato.bdefensa) + "\n3. " + dragon.nombre + "  Precio: " +
                             str(dragon.precio) + " Stats dragon: " + "Salud: " + str(dragon.bsalud) +
                             " Ataque: " + str(dragon.bataque) + " Defensa: " + str(dragon.bdefensa) +
                             "\n4. No comprar\n").capitalize()
            sleep(0.5)
            if cMascota == "1" or cMascota == "Perro":
                if personaje.dinero >= perro.precio:
                    personaje.ataque = personaje.ataque + perro.bataque
                    personaje.defensa = personaje.defensa + perro.bdefensa
                    personaje.saludMaxima = personaje.saludMaxima + perro.bsalud
                    print("Has comprado " + perro.nombre)
                    sleep(0.2)
                    personaje.dinero = personaje.dinero - perro.precio
                    personaje.mascotas = personaje.mascotas.append(perro) # Insertar un elemento en una lista (list.append)
                    seguirCiudad()
                elif personaje.dinero < perro.precio:
                    print("Dinero insuficiente")
                    sleep(0.2)
                    seguirCiudad()

            elif cMascota == "2" or cMascota == "Gato":
                if personaje.dinero >= gato.precio:
                    personaje.ataque = personaje.ataque + gato.bataque
                    personaje.defensa = personaje.defensa + gato.bdefensa
                    personaje.saludMaxima = personaje.saludMaxima + gato.bsalud
                    print("Has comprado " + gato.nombre)
                    sleep(0.2)
                    personaje.dinero = personaje.dinero - gato.precio
                    personaje.mascotas = personaje.mascotas.append(gato)
                    seguirCiudad()
                elif personaje.dinero < gato.precio:
                    print("Dinero insuficiente")
                    sleep(0.2)
                    seguirCiudad()

            elif cMascota == "3" or cMascota == "Dragon":
                if personaje.dinero >= dragon.precio:
                    personaje.ataque = personaje.ataque + dragon.bataque
                    personaje.defensa = personaje.defensa + dragon.bdefensa
                    personaje.saludMaxima = personaje.saludMaxima + dragon.bsalud
                    print("Has comprado " + dragon.nombre)
                    sleep(0.2)
                    personaje.dinero = personaje.dinero - dragon.precio
                    personaje.mascotas = personaje.mascotas.append(dragon)
                    seguirCiudad()
                elif personaje.dinero < dragon.precio:
                    print("Dinero insuficiente")
                    sleep(0.2)
                    seguirCiudad()

            else:
                seguirCiudad()

        elif sTienda == "2" or sTienda == "Pociones":
            pocion1 = Pocion("Pocion de salud pequeña", 35, 15)
            pocion2 = Pocion("Pocion de salud mediana", 80, 40)
            pocion3 = Pocion("Pocion de salud grande", 150, 80)
            cPocion = input("¿Que pocion deseas comprar?:\n1. " + pocion1.nombre +
                            "  Precio: " + str(pocion1.precio) + "\n2. " +
                            pocion2.nombre + "  Precio: " + str(pocion2.precio) + "\n3."
                            + pocion3.nombre + "  Precio: " + str(pocion3.precio) + "\n4. No comprar\n")
            sleep(0.5)
            if cPocion == "1":
                if personaje.dinero >= pocion1.precio:
                    print("Has comprado " + pocion1.nombre)
                    sleep(0.2)
                    personaje.dinero = personaje.dinero - pocion1.precio
                    personaje.pociones = personaje.pociones.append(pocion1)
                    seguirCiudad()
                elif personaje.dinero < pocion1.precio:
                    print("Dinero insuficiente")
                    sleep(0.2)
                    seguirCiudad()

            if cPocion == "2":
                if personaje.dinero >= pocion2.precio:
                    print("Has comprado " + pocion2.nombre)
                    sleep(0.2)
                    personaje.dinero = personaje.dinero - pocion2.precio
                    personaje.pociones = personaje.pociones.append(pocion2)
                    seguirCiudad()
                elif personaje.dinero < pocion2.precio:
                    print("Dinero insuficiente")
                    sleep(0.2)
                    seguirCiudad()

            if cPocion == "3":
                if personaje.dinero >= pocion3.precio:
                    print("Has comprado " + pocion3.nombre)
                    sleep(0.2)
                    personaje.dinero = personaje.dinero - pocion3.precio
                    personaje.pociones = personaje.pociones.append(pocion3)
                    seguirCiudad()
                elif personaje.dinero < pocion3.precio:
                    print("Dinero insuficiente")
                    sleep(0.2)
                    seguirCiudad()

            else:
                seguirCiudad()

        elif sTienda == "3":
            cArmadura = input("¿Que deseas comprar?:\n1. Casco" +
                              "\n2. Pechera" + "\n3. Pantalones" +
                              "\n4. Botas\n").capitalize()
            if cArmadura == "1" or cArmadura == "Casco":
                sleep(0.2)
                comprarCasco()
            elif cArmadura == "2" or cArmadura == "Pechera":
                sleep(0.2)
                comprarPechera()
            elif cArmadura == "3" or cArmadura == "Pantalones":
                sleep(0.2)
                comprarPantalon()
            elif cArmadura == "4" or cArmadura == "Botas":
                sleep(0.2)
                comprarBotas()
        else:
            print("Vuelva pronto")
            seguirCiudad()

    if accion == "3":
        gPartida = input("¿Desea guardar la partida?(Si/No): ").capitalize()
        while gPartida != "Si" and gPartida != "No":
            gPartida = input("¿Desea guardar la partida?(Si/No): ").capitalize()
        if gPartida == "Si":
            personaje.guardarPartida()
            print("Progreso guardado, gracias por jugar")
            seguirCiudad()
        while gPartida == "No":
            ngPartida = input("¿Esta seguro de no guardar su partida?(Si/No): ").capitalize()
            if ngPartida == "Si":  # ngPartida = noguardarPartida
                menuCiudad()
            elif ngPartida == "No":
                gPartida = input("¿Desea guardar la partida?(Si/No): ").capitalize()
            if gPartida == "Si":
                personaje.guardarPartida()
                print("Progreso guardado, gracias por jugar")
                seguirCiudad()
    else:
        matarMonstruo(personaje)

def comprarCasco():
    """
    Crea una instancia para cada casco y le muestra al usuario todos los atributos de los mismos.
    Lo añade al inventario del personaje en caso de comprarlo y le añade los stats que contiene.

    :return:
    """
    casco1 = Armadura("Gorro de cuero","Canalla",3,15,75)
    casco2 = Armadura("Tiara","Bruja",5,10,150)
    casco3 = Armadura("Casco del inmortal","",45,83,480)
    casco4 = Armadura("Mascara de ladron","Canalla",150,485,2300)
    casco5 = Armadura("Corona encantada","Bruja",200,400,3000)
    cCasco = input("1. " + casco1.nombre + " " + str(casco1.precio)
                       + " clase: Canalla" + "\n2. " + casco2.nombre
                       + " " + str(casco2.precio) + " clase: Bruja" + "\n3. "
                       + casco3.nombre + " " + str(casco3.precio) + " clase: Todas"
                       + "\n4.(Legendario) " + casco4.nombre + " " + str(casco4.precio)
                       + " clase: Canalla" + "\n5.(Legendario) " + casco5.nombre +
                       " " +str(casco5.precio) + " clase: Bruja\n6. No comprar\n")
    if cCasco == "1":
        if personaje.clase != casco1.crequerida:
            print("No cumples con la clase requerida: Canalla")
            sleep(0.2)
            comprarCasco()
        elif personaje.clase == casco1.crequerida and personaje.dinero >= casco1.precio:
            personaje.defensa = personaje.defensa + casco1.defensa
            personaje.saludMaxima = personaje.saludMaxima + casco1.salud
            print("Has comprado " + casco1.nombre)
            sleep(0.2)
            personaje.dinero = personaje.dinero - casco1.precio
            personaje.armaduras = personaje.armaduras.append(casco1)
            seguirCiudad()
        elif personaje.clase == casco1.crequerida and personaje.dinero < casco1.precio:
            print("Dinero insuficiente")
            sleep(0.2)
            comprarCasco()

    elif cCasco == "2":
        if personaje.clase != casco2.crequerida:
            print("No cumples con la clase requerida: Bruja")
            sleep(0.2)
            comprarCasco()
        elif personaje.clase == casco2.crequerida and personaje.dinero >= casco2.precio:
            personaje.defensa = personaje.defensa + casco2.defensa
            personaje.saludMaxima = personaje.saludMaxima + casco2.salud
            print("Has comprado " + casco2.nombre)
            sleep(0.2)
            personaje.dinero = personaje.dinero - casco2.precio
            personaje.armaduras = personaje.armaduras.append(casco2)
            seguirCiudad()
        elif personaje.clase == casco2.crequerida and personaje.dinero < casco2.precio:
            print("Dinero insuficiente")
            sleep(0.2)
            comprarCasco()

    elif cCasco == "3":
        if personaje.dinero >= casco3.precio:
            personaje.defensa = personaje.defensa + casco3.defensa
            personaje.saludMaxima = personaje.saludMaxima + casco3.salud
            print("Has comprado " + casco3.nombre)
            sleep(0.2)
            personaje.dinero = personaje.dinero - casco3.precio
            personaje.armaduras = personaje.armaduras.append(casco3)
            seguirCiudad()
        elif personaje.dinero < casco3.precio:
            print("Dinero insuficiente")
            sleep(0.2)
            comprarCasco()

    elif cCasco == "4":
        if personaje.clase != casco4.crequerida:
            print("No cumples con la clase requerida: Canalla")
            sleep(0.2)
            comprarCasco()
        elif personaje.clase == casco4.crequerida and personaje.dinero >= casco4.precio:
            personaje.defensa = personaje.defensa + casco4.defensa
            personaje.saludMaxima = personaje.saludMaxima + casco4.salud
            print("Has comprado " + casco4.nombre)
            sleep(0.2)
            personaje.dinero = personaje.dinero - casco4.precio
            personaje.armaduras = personaje.armaduras.append(casco4)
            seguirCiudad()
        elif personaje.clase == casco4.crequerida and personaje.dinero < casco4.precio:
            print("Dinero insuficiente")
            sleep(0.2)
            comprarCasco()

    elif cCasco == "5":
        if personaje.clase != casco5.crequerida:
            print("No cumples con la clase requerida: Bruja")
            sleep(0.2)
            comprarCasco()
        elif personaje.clase == casco5.crequerida and personaje.dinero >= casco5.precio:
            personaje.defensa = personaje.defensa + casco5.defensa
            personaje.saludMaxima = personaje.saludMaxima + casco5.salud
            print("Has comprado " + casco5.nombre)
            sleep(0.2)
            personaje.dinero = personaje.dinero - casco5.precio
            personaje.armaduras = personaje.armaduras.append(casco5)
            seguirCiudad()
        elif personaje.clase == casco5.crequerida and personaje.dinero < casco5.precio:
            print("Dinero insuficiente")
            sleep(0.2)
            comprarCasco()
    else:
        sleep(0.2)
        seguirCiudad()

def comprarPechera():
    """
    Crea una instancia para cada pechera/armadura y le muestra al usuario todos los atributos
    de los mismos. Lo añade al inventario del personaje en caso de comprarlo y le añade
    los stats que contiene.

    :return:
    """
    pechera1 = Armadura("Toga de cuero","Canalla",15,35,125)
    pechera2 = Armadura("Armadura oxidada","Bruja",8,25,150)
    pechera3 = Armadura("Malla reluciente","",70,200,670)
    pechera4 = Armadura("Ropaje de desertor","Canalla",350,1000,7500)
    pechera5 = Armadura("Vestimenta abisal","Bruja",285,800,7200)
    cPechera = input("1. " + pechera1.nombre + " " + pechera1.precio
                     + " clase: Canalla" + "\n2. " + pechera2.nombre
                     + pechera2.precio + " clase: Bruja" + "\n3. "
                     + pechera3.nombre + " " + pechera3.precio +
                     " clase: Todas" + "\n4.(Legendario) " + pechera4.nombre
                     + " " + pechera4.precio + " clase: Canalla"
                     + "\n5.(Legendario) " + pechera5.nombre + " "
                     + pechera5.precio + " clase: Bruja\n6. No comprar\n")
    if cPechera == "1":
        if personaje.clase != pechera1.crequerida:
            print("No cumples con la clase requerida: Canalla")
            sleep(0.2)
            comprarPechera()
        elif personaje.clase == pechera1.crequerida and personaje.dinero >= pechera1.precio:
            personaje.defensa = personaje.defensa + pechera1.defensa
            personaje.saludMaxima = personaje.saludMaxima + pechera1.salud
            print("Has comprado " + pechera1.nombre)
            sleep(0.2)
            personaje.dinero = personaje.dinero - pechera1.precio
            personaje.armaduras = personaje.armaduras.append(pechera1)
            seguirCiudad()
        elif personaje.clase == pechera1.crequerida and personaje.dinero < pechera1.precio:
            print("Dinero insuficiente")
            sleep(0.2)
            comprarPechera()

    elif cPechera == "2":
        if personaje.clase != pechera2.crequerida:
            print("No cumples con la clase requerida: Bruja")
            sleep(0.2)
            comprarPechera()
        elif personaje.clase == pechera2.crequerida and personaje.dinero >= pechera2.precio:
            personaje.defensa = personaje.defensa + pechera2.defensa
            personaje.saludMaxima = personaje.saludMaxima + pechera2.salud
            print("Has comprado " + pechera2.nombre)
            sleep(0.2)
            personaje.dinero = personaje.dinero - pechera2.precio
            personaje.armaduras = personaje.armaduras.append(pechera2)
            seguirCiudad()
        elif personaje.clase == pechera2.crequerida and personaje.dinero < pechera2.precio:
            print("Dinero insuficiente")
            sleep(0.2)
            comprarPechera()

    elif cPechera == "3":
        if personaje.dinero >= pechera3.precio:
            personaje.defensa = personaje.defensa + pechera3.defensa
            personaje.saludMaxima = personaje.saludMaxima + pechera3.salud
            print("Has comprado " + pechera3.nombre)
            sleep(0.2)
            personaje.dinero = personaje.dinero - pechera3.precio
            personaje.armaduras = personaje.armaduras.append(pechera3)
            seguirCiudad()
        elif personaje.dinero < pechera3.precio:
            print("Dinero insuficiente")
            sleep(0.2)
            comprarPechera()

    elif cPechera == "4":
        if personaje.clase != pechera4.crequerida:
            print("No cumples la clase requerida: Canalla")
            sleep(0.2)
            comprarPechera()
        elif personaje.clase == pechera4.crequerida and personaje.dinero >= pechera4.precio:
            personaje.defensa = personaje.defensa + pechera4.defensa
            personaje.saludMaxima = personaje.saludMaxima + pechera4.salud
            print("Has comprado " + pechera4.nombre)
            sleep(0.2)
            personaje.dinero = personaje.dinero - pechera4.precio
            personaje.armaduras = personaje.armaduras.append(pechera4)
            seguirCiudad()
        elif personaje.clase == pechera4.crequerida and personaje.dinero < pechera4.precio:
            print("Dinero insuficiente")
            sleep(0.2)
            comprarPechera()
    elif cPechera == "5":
        if personaje.clase != pechera5.crequerida:
            print("No cumples la clase requerida: Bruja")
            sleep(0.2)
            comprarPechera()
        elif personaje.clase == pechera5.crequerida and personaje.dinero >= pechera5.precio:
            personaje.defensa = personaje.defensa + pechera5.defensa
            personaje.saludMaxima = personaje.saludMaxima + pechera5.salud
            print("Has comprado " + pechera5.nombre)
            sleep(0.2)
            personaje.dinero = personaje.dinero - pechera5.precio
            personaje.armaduras = personaje.armaduras.append(pechera5)
            seguirCiudad()
        elif personaje.clase == pechera5.crequerida and personaje.dinero < pechera5.precio:
            print("Dinero insuficiente")
            sleep(0.2)
            comprarPechera()
    else:
        sleep(0.2)
        seguirCiudad()

def comprarPantalon():
    """
    Crea una instancia para cada pantalon y le muestra al usuario todos los atributos de los mismos.
    Lo añade al inventario del personaje en caso de comprarlo y le añade los stats que contiene.

    :return:
    """
    pantalon1 = Armadura("Pantalones de asesino","Canalla",8,23,90)
    pantalon2 = Armadura("Grebas de amazona","Bruja",5,17,85)
    pantalon3 = Armadura("Pantalones de la orden",60,170,585)
    pantalon4 = Armadura("Grebas fantasma","Canalla",300,875,6315)
    pantalon5 = Armadura("Pantalones de asesino de dragones","Bruja",238,690,6100)
    cPantalon = input("1. " + pantalon1.nombre + " " + pantalon1.precio
                      + " clase: Canalla" + "\n2. " + pantalon2.nombre
                      + " " + pantalon2.precio + " clase: Bruja" + "\n3. "
                      + pantalon3.nombre + " " + pantalon3.precio +
                      " clase: Todas" + "\n4.(Legendario) " + pantalon4.nombre +
                      " " + pantalon4.precio + " clase: Canalla" +
                      "\n5.(Legendario) " + pantalon5.nombre + " " +
                      pantalon5.precio + " clase: Bruja\n6. No comprar\n")
    if cPantalon == "1":
        if personaje.clase != pantalon1.crequerida:
            print("No cumples la clase requerida: Canalla")
            sleep(0.2)
            comprarPantalon()
        elif personaje.clase == pantalon1.crequerida and personaje.dinero >= pantalon1.precio:
            personaje.defensa = personaje.defensa + pantalon1.defensa
            personaje.saludMaxima = personaje.saludMaxima + pantalon1.salud
            print("Has comprado " + pantalon1.nombre)
            sleep(0.2)
            personaje.dinero = personaje.dinero - pantalon1.precio
            personaje.armaduras = personaje.armaduras.append(pantalon1)
            seguirCiudad()
        elif personaje.clase == pantalon1.crequerida and personaje.dinero < pantalon1.precio:
            print("Dinero insuficiente")
            sleep(0.2)
            comprarPantalon()

    elif cPantalon == "2":
        if personaje.clase != pantalon2.crequerida:
            print("No cumples la clase requerida: Bruja")
            sleep(0.2)
            comprarPantalon()
        elif personaje.clase == pantalon2.crequerida and personaje.dinero >= pantalon2.precio:
            personaje.defensa = personaje.defensa + pantalon2.defensa
            personaje.saludMaxima = personaje.saludMaxima + pantalon2.salud
            print("Has comprado " + pantalon2.nombre)
            sleep(0.2)
            personaje.dinero = personaje.dinero - pantalon2.precio
            personaje.armaduras = personaje.armaduras.append(pantalon2)
            seguirCiudad()
        elif personaje.clase == pantalon2.crequerida and personaje.dinero < pantalon2.precio:
            print("Dinero insuficiente")
            sleep(0.2)
            comprarPantalon()

    elif cPantalon == "3":
        if personaje.dinero >= pantalon3.precio:
            personaje.defensa = personaje.defensa + pantalon3.defensa
            personaje.saludMaxima = personaje.saludMaxima + pantalon3.salud
            print("Has comprado " + pantalon3.nombre)
            sleep(0.2)
            personaje.dinero = personaje.dinero - pantalon3.precio
            personaje.armaduras = personaje.armaduras.append(pantalon3)
            seguirCiudad()
        elif personaje.dinero < pantalon3.precio:
            print("Dinero insuficiente")
            sleep(0.2)
            comprarPantalon()
    elif cPantalon == "4":
        if personaje.clase != pantalon4.crequerida:
            print("No cumples con la clase requerida: Canalla")
            sleep(0.2)
            comprarPantalon()
        elif personaje.clase == pantalon4.crequerida and personaje.dinero >= pantalon4.precio:
            personaje.defensa = personaje.defensa + pantalon4.defensa
            personaje.saludMaxima = personaje.saludMaxima + pantalon4.salud
            print("Has comprado " + pantalon4.nombre)
            sleep(0.2)
            personaje.dinero = personaje.dinero - pantalon4.precio
            personaje.armaduras = personaje.armaduras.append(pantalon4)
            seguirCiudad()
        elif personaje.clase != pantalon4.crequerida and personaje.dinero < pantalon4.precio:
            print("Dinero insuficiente")
            sleep(0.2)
            comprarPantalon()
    elif cPantalon == "5":
        if personaje.clase != pantalon5.crequerida:
            print("No cumples con la clase requerida: Bruja")
            sleep(0.2)
            comprarPantalon()
        elif personaje.clase == pantalon5.crequerida and personaje.dinero >= pantalon5.precio:
            personaje.defensa = personaje.defensa + pantalon5.defensa
            personaje.saludMaxima = personaje.saludMaxima + pantalon5.salud
            print("Has comprado " + pantalon5.nombre)
            sleep(0.2)
            personaje.dinero = personaje.dinero - pantalon5.precio
            personaje.armaduras = personaje.armaduras.append(pantalon5)
            seguirCiudad()
        elif personaje.clase == pantalon5.crequerida and personaje.dinero < pantalon5.precio:
            print("Dinero insuficiente")
            sleep(0.2)
            comprarPantalon()
    else:
        sleep(0.2)
        seguirCiudad()

def comprarBotas():
    """
    Crea una instancia para cada bota y le muestra al usuario todos los atributos de los mismos.
    Lo añade al inventario del personaje en caso de comprarlo y le añade los stats que contiene.

    :return:
    """
    botas1 = Armadura("Botas de cuero","Canalla",2,10,50)
    botas2 = Armadura("Zapatos de caballeria","Bruja",3,7,55)
    botas3 = Armadura("Zapatillas de runner","",30,70,400)
    botas4 = Armadura("Botas sigilosas","Canalla",125,420,2000)
    botas5 = Armadura("Botas de la ruina","Bruja",100,325,2700)
    cBotas = input("1. " + botas1.nombre + " " + botas1.precio +
                   " clase: Canalla" + "\n2. " + botas2.nombre + " "
                   + botas2.precio + " clase: Bruja" + "\n3. " +
                   botas3.nombre + " " + botas3.precio + " clase: Todas"
                   + "\n4. " + botas4.nombre + " " + botas4.precio +
                   " clase: Canalla" + "\n5. " + botas5.nombre + " " +
                   botas5.precio + " clase: Bruja\n6. No comprar\n")
    if cBotas == "1":
        if personaje.clase != botas1.crequerida:
            print("No cumples con la clase requerida: Canalla")
            sleep(0.2)
            comprarBotas()
        elif personaje.clase == botas1.crequerida and personaje.dinero >= botas1.precio:
            personaje.defensa = personaje.defensa + botas1.defensa
            personaje.saludMaxima = personaje.saludMaxima + botas1.salud
            print("Has comprado " + botas1.nombre)
            sleep(0.2)
            personaje.dinero = personaje.dinero - botas1.precio
            personaje.armaduras = personaje.armaduras.append(botas1)
            seguirCiudad()
        elif personaje.clase == botas1.crequerida and personaje.dinero < botas1.precio:
            print("Dinero insuficiente")
            sleep(0.2)
            comprarBotas()

    elif cBotas == "2":
        if personaje.clase != botas2.crequerida:
            print("No cumples con la clase requerida: Bruja")
            sleep(0.2)
            comprarBotas()
        elif personaje.clase == botas2.crequerida and personaje.dinero >= botas2.precio:
            personaje.defensa = personaje.defensa + botas2.defensa
            personaje.saludMaxima = personaje.saludMaxima + botas2.salud
            print("Has comprado " + botas2.nombre)
            sleep(0.2)
            personaje.dinero = personaje.dinero - botas2.precio
            personaje.armaduras = personaje.armaduras.append(botas2)
            seguirCiudad()
        elif personaje.clase == botas2.crequerida and personaje.dinero < botas2.precio:
            print("Dinero insuficiente")
            sleep(0.2)
            comprarBotas()

    elif cBotas == "3":
        if personaje.dinero >= botas3.precio:
            personaje.defensa = personaje.defensa + botas3.defensa
            personaje.saludMaxima = personaje.saludMaxima + botas3.salud
            print("Has comprado " + botas3.nombre)
            sleep(0.2)
            personaje.dinero = personaje.dinero - botas3.precio
            personaje.armaduras = personaje.armaduras.append(botas3)
            seguirCiudad()
        elif personaje.dinero < botas3.precio:
            print("Dinero insuficiente")
            sleep(0.2)
            comprarBotas()

    elif cBotas == "4":
        if personaje.clase != botas4.crequerida:
            print("No cumples con la clase requerida: Canalla")
            sleep(0.2)
            comprarBotas()
        elif personaje.clase == botas4.crequerida and personaje.dinero >= botas4.precio:
            personaje.defensa = personaje.defensa + botas4.defensa
            personaje.saludMaxima = personaje.saludMaxima + botas4.salud
            print("Has comprado " + botas4.nombre)
            sleep(0.2)
            personaje.dinero = personaje.dinero - botas4.precio
            personaje.armaduras = personaje.armaduras.append(botas4)
            seguirCiudad()
        elif personaje.clase == botas4.crequerida and personaje.dinero < botas4.precio:
            print("Dinero insuficiente")
            sleep(0.2)
            comprarBotas()

    elif cBotas == "5":
        if personaje.clase != botas5.crequerida:
            print("No cumples con la clase requerida: Bruja")
            sleep(0.2)
            comprarBotas()
        elif personaje.clase == botas5.crequerida and personaje.dinero >= botas5.precio:
            personaje.defensa = personaje.defensa + botas5.defensa
            personaje.saludMaxima = personaje.saludMaxima + botas5.salud
            print("Has comprado " + botas5.nombre)
            sleep(0.2)
            personaje.dinero = personaje.dinero - botas5.precio
            personaje.armaduras = personaje.armaduras.append(botas5)
            seguirCiudad()
        elif personaje.clase == botas5.crequerida and personaje.dinero < botas5.precio:
            print("Dinero insuficiente")
            sleep(0.2)
            comprarBotas()
    else:
        sleep(0.2)
        seguirCiudad()

cPartida = input("(Si/No)¿Deseas cargar una partida?: ").capitalize()
personaje = None
if cPartida == "Si":
    personaje = cargarPartida()
    menuCiudad()

if not personaje:  # == None
    sleep(0.2)
    nombre = input("Introduce tu nombre: ").capitalize()
    eclase = 0
    while eclase != 1 and eclase != 2:
        eclase = int(input("(Indica con un numero) Que clase quieres escoger: \n1.Canalla\n2.Bruja\n"))
        if eclase == 1:
            clase = "Canalla"
            ataque = 4
            salud = 40
            defensa = 7
            saludMaxima = 40
        elif eclase == 2:
            clase = "Bruja"
            ataque = 6
            salud = 50
            defensa = 10
            saludMaxima = 50
        else:
            print("No es una clase valida")

    personaje = Personaje(1, 0, nombre, clase, ataque, 0, salud, defensa, saludMaxima, [], [], [])
    print("Se ha creado un personaje llamado " + personaje.nombre + " de clase " + personaje.clase)
    sleep(1)

matarMonstruo(personaje)

"""
else:
    print("Gracias por jugar!!!\n" + personaje.nombre +
          " ha matado a " + str(totalMonstruo) +
          " monstruos\n" + "Nivel: " + str(personaje.nivel)
          + "EXP: " + str(personaje.exp))
"""
# TODO Crear continentes y dentro de cada continente añadir ciudades con diferentes funcionalidades
# TODO Separar las clases y funciones en diferentes .py con nombres identificativos
"""
class Ciudad:
    def __init__(self,nombre,nivelr)
        self.nombre = nombre
        self.nivelr = nivelr   #nivelr = nivelrequerido

estivania = Ciudad("Estivania",1)
zanarkand = Ciudad("Zanarkand",8)
meowyork = Ciudad("MeowYork",20)
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