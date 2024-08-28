class Personaje:

    def __init__(self, nombre): #constructor
        self.nombre = nombre
        self.nivel = 1
        self.experiencia = (
            0 #experiencia 0 al crear
        )

    @property #getter de estado
    def estado(self):
        return f"NOMBRE: {self.nombre} NIVEL: {self.nivel} EXP: {self.experiencia}" #llamada a variable exp

    @estado.setter #setter de estado
    def estado(self, exp: int): #agregue tipo int de variable exp
        tmp_exp = self.experiencia + exp

        while tmp_exp >= 100:
            self.nivel += (
                1 #suma solo 1 nivel por 100 de exp
            )
            tmp_exp -= 100 #resta 100 a la experiencia por nivel subido

        while tmp_exp < 0:
            if self.nivel > 1:
                tmp_exp += 100  #suma 100 de exp por nivel reducido
                self.nivel -= (
                    1 #baja 1 nivel por cada -100 de experiencia recibida
                )
            elif self.nivel == 1: #si el personaje esta en nivel 1 y la exp es negativa
                tmp_exp = (
                    0
                )

        self.experiencia = tmp_exp #se asigna a la experiencia actual el valor de suma temporal actualizado

    def __lt__(self, other): #sobrecarga menor que
        return (
            self.experiencia < other
        )

    def __gt__(self, other): #sobrecarga menor que
        return (
            self.experiencia > other
        )

    def __eq__(self, other): #sobrecarga igual que
        return (
            self.experiencia == other
        )

    def get_probabilidad_ganar(self, other): #metodo de instancia que retorna la probabilidad de la instancia de ganar respecto a la otra
        if self < other:
            return (
                0.33 #probabilidad de ganar al ser menor que el orco
            )
        elif self > other:
            return (
                0.66 #probabilidad de ganar al ser mayor que el orco
            )
        else:
            return 0.50 #probabilidad de ganar al ser igual al orco

    @staticmethod #dialogo de enfrentamiento al orco
    def mostrar_dialogo_opcion(probabilidad_ganar):
        return int(
            input(
                f"\nCon tu nivel actual, tienes {probabilidad_ganar * 100}% "
                "de probabilidades de ganar contra el Orco.\n" #perder
                "\nSi ganas, ganarás 50 puntos de experiencia y el orco perderá 30. \n" #faltaba comillas y datos cambiados de exp
                "Si pierdes, perderás 30 puntos de experiencia y el orco ganará 50.\n" #datos cambiados de exp
                "\n¿Qué deseas hacer?\n"
                "1. Atacar\n" #opciones cambiadas
                "2. Huir\n"
            )
        )
