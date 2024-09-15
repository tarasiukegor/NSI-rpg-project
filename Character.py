from Food import *
from Weapon import *

class character():
    def __init__(self, character_name,):
        self.name = character_name
        self.hp = 100
        self.weapon_equipped = None
        self.armor_equipped = None
        self.attack = 5
        self.bank = 0
        self.opponents_killed = 0
        self.inventory_weapon = []
        self.inventory_armor = []
        self.inventory_food= []
        

    def infos(self):
        return(self.weapon_equipped, self.attack, self.inventory_weapon)
        
        
    def attack_deal(self, opponent):
        assert self.hp > 0
        print("yihaaa")
        opponent.recieve_damage(self.attack)
        
    def recieve_damage(self, damage):
        self.hp -= damage 
        if self.hp < 0: 
            self.death()
            
            
    def equip_weapon(self, weapon): 
        
        if weapon not in weapon_list or weapon not in self.inventory_weapon:
            raise ValueError("The weapon you are trying to equip does not exist or you don't have it")
            
            
        
        
        if self.weapon_equipped is None: 
            self.weapon_equipped = weapon
            self.attack += weapon_list[weapon]
            print(f'u have sucsessfully equiped {weapon}')
            return
        else: 
            current_weapon = self.weapon_equipped
            self.weapon_equipped = weapon
            self.attack -= weapon_list[current_weapon]
            self.attack += weapon_list[weapon]
            print(f'u have sucsessfully swchtede')
            return
                
                
    def equip_armor(self, armor): 
        
        if armor not in weapon_list or weapon not in self.inventory_weapon:
            raise ValueError("The weapon you are trying to equip does not exist or you don't have it")
            return
            
        
        
        if self.weapon is None: 
            self.weapon = weapon
            self.attack += weapon_list[weapon]
            print(f'u have sucsessfully equiped {weapon}')
            return
        else: 
            current_weapon = self.weapon
            self.weapon = weapon
            self.attack -= weapon_list[current_weapon]
            self.attack += weapon_list[weapon]
            print(f'u have sucsessfully swchtede')
            return
        
                
