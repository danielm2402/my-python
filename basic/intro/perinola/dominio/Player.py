class Player:
    def __init__(self,id, name, money):
        self.id = id
        self.name = name
        self.money= money

    def get_name(self):
        return self.name

    def get_money(self):
        return self.money

    def get_id(self):
        return self.id

    def set_money(self, money):
        self.money=money