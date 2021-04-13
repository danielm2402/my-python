class Round:
    def __init__(self, perinola):
        self.acumulado = 0
        self.ganador = None
        self.perinola = perinola
        self.turno = 0

    def play(self):
        self.perinola.spin()
        actualValue = self.perinola.get_value()
        return actualValue

    def get_turno(self):
        return self.turno

    def set_turno(self, turno):
        self.turno = turno

    def set_acumulado(self, acumulado):
        self.acumulado = acumulado

    def get_acumulado(self):
        return self.acumulado

    def set_ganador(self, ganador):
        self.ganador=ganador