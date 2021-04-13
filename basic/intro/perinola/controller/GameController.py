from dominio import Game, Perinola, Player, Round

class GamerController:
    def __init__(self):
        p1 = Player.Player(1, 'Daniel', 700)
        p2 = Player.Player(2, 'Luis', 700)
        p3 = Player.Player(3, 'Wilmer', 700)
        self.game = Game.Game([p1, p2, p3])
        self.game.new_round()

    def play(self):
        return self.game.play()
    def get_players(self):
        return self.game.get_actual_players()