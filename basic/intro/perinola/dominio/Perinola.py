from random import randint

class Perinola:
    def __init__(self):
        self.values = ('Toma1', 'Toma2', 'Pon1', 'Pon2', 'TodosPonen', 'TomaTodo')
        self.value = None

    def spin(self):
        option = randint(0, 5)
        self.value=self.values[option]
        return self.values[option]

    def get_value(self):
        return self.value