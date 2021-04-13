from .Round import Round
from .Perinola import Perinola

class Game:
    def __init__(self, players):
        self.rounds = []
        self.startingPlayer = players
        self.actualPlayers = players
        self.winner = None
        self.perinola = Perinola()

    def get_playes(self):
        return self.startingPlayer
    def get_actual_players(self):
        return self.actualPlayers
    def new_round(self):
        round = Round(self.perinola)
        self.rounds.append(round)

    def play(self):
        actualRound=self.rounds[-1]
        playRound= actualRound.play()
        if playRound == 'Toma1':
            if actualRound.get_acumulado() >= 100:
                actualRound.set_acumulado(actualRound.get_acumulado()-100)
                self.actualPlayers[actualRound.get_turno()].set_money( self.actualPlayers[actualRound.get_turno()].get_money()+100)
        if playRound == 'Toma2':
            if actualRound.get_acumulado() >= 200:
                actualRound.set_acumulado(actualRound.get_acumulado()-200)
                self.actualPlayers[actualRound.get_turno()].set_money( self.actualPlayers[actualRound.get_turno()].get_money()+200)
        if playRound == 'Pon1':
            if self.actualPlayers[actualRound.get_turno()].get_money() > 100:
                actualRound.set_acumulado(actualRound.get_acumulado()+100)
                self.actualPlayers[actualRound.get_turno()].set_money( self.actualPlayers[actualRound.get_turno()].get_money()-100)
            else:
                if self.actualPlayers[actualRound.get_turno()].get_money() == 100:
                    actualRound.set_acumulado(actualRound.get_acumulado() + 100)
                    self.actualPlayers[actualRound.get_turno()].set_money(
                        self.actualPlayers[actualRound.get_turno()].get_money() - 100)
                self.actualPlayers.pop(actualRound.get_turno())
        if playRound == 'Pon2':
            if self.actualPlayers[actualRound.get_turno()].get_money() > 200:
                self.actualPlayers[actualRound.get_turno()].set_money( self.actualPlayers[actualRound.get_turno()].get_money()-200)
                actualRound.set_acumulado(actualRound.get_acumulado()+200)
            else:
                if self.actualPlayers[actualRound.get_turno()].get_money() == 200:
                    actualRound.set_acumulado(actualRound.get_acumulado() + 200)
                    self.actualPlayers[actualRound.get_turno()].set_money(
                        self.actualPlayers[actualRound.get_turno()].get_money() - 200)
                self.actualPlayers.pop(actualRound.get_turno())
        if playRound == 'TodosPonen':
            tempList = self.actualPlayers
            for i, e in enumerate(self.actualPlayers):
                if e.get_money() > 100:
                    actualRound.set_acumulado(actualRound.get_acumulado() + 100)
                    e.set_money(e.get_money()-100)
                else:
                    if e.get_money() == 100:
                        actualRound.set_acumulado(actualRound.get_acumulado() + 100)
                        e.set_money(e.get_money() - 100)
                    tempList.pop(i)
            self.actualPlayers=tempList
        if playRound == 'TomaTodo':
            self.actualPlayers[actualRound.get_turno()].set_money(self.actualPlayers[actualRound.get_turno()].get_money() + actualRound.get_acumulado())
            actualRound.set_ganador(self.actualPlayers[actualRound.get_turno()])
            actualRound.set_acumulado(0)
            round = Round(self.perinola)
            self.rounds.append(round)

        print('----------')
        print(actualRound.get_turno())
        print(playRound)
        for i in self.actualPlayers:
            print(i.get_name(), i.get_money())
        print(actualRound.get_acumulado())

        turno = actualRound.get_turno()+1 if actualRound.get_turno()+1 < len(self.actualPlayers) else 0
        actualRound.set_turno(turno)
        return {'money':actualRound.get_acumulado(), 'pos':playRound, 'turn':actualRound.get_turno(), 'ronda':len(self.rounds)}
