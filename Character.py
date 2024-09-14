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
        self.inventory_weapon = ["Common Sword", "Common Bow"]
        self.inventory_armor = []
        self.inventory_food= []
        

    def infos(self):
        return(self.weapon, self.attack, self.inventory_weapon)
        
        
    def attack_deal(self, opponent):
        assert self.hp > 0
        print("yihaaa")
        opponent.recieve_damage(self.attack)
        
    def recieve_damage(self, damage):
        self.hp -= damage 
        if self.hp < 0: 
            self.death()
            
            
    def equip_weapon(self, weapon): 
        
        if weapon not in [weapon for weapon in weapons] and weapon not in self.inventory_weapon:
            print('loser')
            return False
        for w in weapons:
            if self.weapon is None: 
                self.weapon = weapon
                self.attack += w[weapon]
                print(f'u have sucsessfully equiped {weapon}')
                return
            else: 
                current_weapon = self.weapon
                self.weapon = weapon
                self.attack -= w[current_weapon]
                self.attack += w[weapon]
                print(f'u have sucsessfully swchtede')
                return
                
        
        
        # for w in weapons:
        #     if weapon in w and weapon in self.inventory_weapon: 
        #         self.weapon = weapon 
        #         self.attack += w[weapon]
        #         print(f"You have sucsessfully equipped {weapon}")
            
            
        # raise ValueError(f"The weapon {weapon} you are trying to equip is not avalibble")
                
                
popa = character("yeahor")
popa.equip_weapon("Common Sword")
print(popa.infos())

popa.equip_weapon("Common Bow")
