from Food import *
from Weapon import *

class character():
    def __init__(self, nom,):
        self.nom = nom
        self.hp = 100
        self.weapon = None
        self.armor = None
        self.attack = 5
        self.bank = 100
        self.opponents_killed = 0 
        
        
    def attack_deal(self, opponent):
        assert self.hp > 0
        print("yihaaa")
        opponent.recieve_damage(self.attack)
        
    def recieve_damage(self, damage):
        self.hp -= damage 
        if self.hp < 0: 
            self.death()
            
            
    def equip_weapon(self, weapon):
        self.weapon = weapon 
        self.attack += sword[weapon]
        if self.weapon != None:
            print('aaa')
            print("oooo")
            print("eeeee")