import json

class Personaje:
    def __init__(self, nivel, exp, nombre, clase, ataque, dinero, salud, defensa, saludMaxima, mascotas, pociones, armaduras):
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
        self.exp = self.exp + cantidad
        while self.exp >= 20:
            self.nivel = self.nivel + 1
            self.exp = self.exp - 20  # Aumentar ataque de cada clase
            if self.clase == "Bruja":
                self.ataque = self.ataque + 5
                self.salud = self.salud + 8
                self.defensa = self.defensa + 6
                self.saludMaxima = self.saludMaxima + 8

            if self.clase == "Canalla":
                self.ataque = self.ataque + 3
                self.salud = self.salud + 5
                self.defensa = self.defensa + 5
                self.saludMaxima = self.saludMaxima + 5

    def atacarMonstruo(self, daño, monstruo):
        monstruo.salud = monstruo.salud - daño
        if monstruo.salud <= 0:
            print(monstruo.nombre + " Ha muerto")
            self.ganarExp(monstruo.exp)
        else:
            print("La salud de " + monstruo.nombre + " es " + str(monstruo.salud))

    def guardarPartida(self):
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



class Monstruo:
    def __init__(self, nombre, salud, drop, exp, ataque):  # drop = oro
        self.nombre = nombre
        self.salud = salud
        self.drop = drop
        self.exp = exp
        self.ataque = ataque

    def atacarPersonaje(self, daño, personaje):
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
    def __init__(self, nombre, bataque, bsalud, bdefensa, precio):  # b = buff
        self.nombre = nombre
        self.bataque = bataque
        self.bsalud = bsalud
        self.bdefensa = bdefensa
        self.precio = precio


class Pocion:
    def __init__(self, nombre, crecuperacion, precio):  # c = cantidad
        self.nombre = nombre
        self.crecuperacion = crecuperacion
        self.precio = precio



class Armadura:
    def __init__(self,nombre,crequerida,defensa,salud,precio): # c = clase
        self.nombre = nombre
        self.crequerida = crequerida
        self.defensa = defensa
        self.salud = salud
        self.precio = precio