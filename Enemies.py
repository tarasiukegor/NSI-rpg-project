class slime():
    def __init__(self):
        self.name = "Normal Slime"
        self.hp = 50
        self.attack = 10
        

class boss_slime(slime):
    def __init__(self):
        self.name = "Boss Slime"
        self.hp = 100
        self.attack = 20