from Food import *
from Weapon import *
from Armor import *

class character():
    def __init__(self, character_name,):
        self.name = character_name
        self.hp = 100
        self.max_hp = 100
        self.weapon_equipped = None
        self.armor_equipped = None
        self.attack = 5
        self.bank = 0
        self.opponents_killed = 0
        self.inventory_weapon = []
        self.inventory_armor = ["Leather Armor"]
        self.inventory_food= ["Bread"]
        

    def infos(self):
        return(self.weapon_equipped, self.attack, self.inventory_weapon, self.armor_equipped, self.inventory_armor)
        
        
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
            print(f'You have sucsessfully equiped {weapon}')
            return
        else: 
            current_weapon = self.weapon_equipped
            self.weapon_equipped = weapon
            self.attack -= weapon_list[current_weapon]
            self.attack += weapon_list[weapon]
            print(f'You have sucsessfully swchtede')
            return
                
                
    def equip_armor(self, armor): 
        
        if armor not in armor_list or armor not in self.inventory_armor:
            raise ValueError("The armor you are trying to equip does not exist or you don't have it")
            return
            
        if self.armor_equipped is None: 
            self.armor_equipped = armor
            print(f'You have sucsessfully equiped {armor}')
            return
        else: 
            self.armor_equipped = armor
            print(f'You have sucsessfully switched')
            return
        
                
        
    def eat_food(self, food):
        assert self.hp < 100
        if food not in food_list or food not in self.inventory_food:
            raise ValueError("The food you are tryin to eat does not exist or you don't have it")
        
        self.hp += food_list[food]
        if self.hp > self.max_hp:
            self.hp = self.max_hp
        print(f"Your hp is now : {self.hp}")


