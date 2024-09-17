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
        self.inventory_weapon = ["Common Sword", "Common Bow", "Twohanded Sword", "Dad's Sword", "Legendary Super Puper Katana"]    #Pour ajouter un élément à ces listes, 
        self.inventory_armor = ["Leather Armor", "Iron Armor", "Dad's Armor","Legenday Super Puper Armor"]                          #il faut appeler la fonction store() et acheter un élément,
        self.inventory_food= ["Bread","Apple","Golden Apple","Standart Dish"]                                                       #mais je n'ai pas eu le temps de le faire, alors faisons comme si nous avons tout !
        

    def infos(self): #cette fonction montre preaque tout les infos de pesonnage
        assert self.hp > 0 , "u dead ll"
        return(f"Hello {self.name}!\nYou are currently at: {self.hp}Hp.\nYour weapon is: {self.weapon_equipped}, and your armor is: {self.armor_equipped}.\nThere is {self.bank} golden coins in your pocket\nYou already defeated {self.opponents_killed} opponnents\n")
        
        

            
    def equip_weapon(self, weapon): 
        assert self.hp > 0 , "u dead ll" #si le pesonnage est mort le fonction renvoie un erreur
        
        if weapon not in weapon_list or weapon not in self.inventory_weapon:
            raise ValueError("The weapon you are trying to equip does not exist or you don't have it") #donc ce ca
            
        if self.weapon_equipped is None: 
            self.weapon_equipped = weapon 
            self.attack += weapon_list[weapon]
            print(f'You have sucsessfully equiped {weapon}')
            return
        else:                                       #cette fonction permet de changer d'arme
            current_weapon = self.weapon_equipped   #nous créons une variable temporaire 
            self.weapon_equipped = weapon
            self.attack -= weapon_list[current_weapon]  #pour soustraire le nombre de points de dégâts de l'attaque du personnage
            self.attack += weapon_list[weapon]          #puis ajouter des points de dégâts de l'arme choisie par l'utilisateur
            print(f'You have sucsessfully switched to {weapon}')
            return
                
                
    def equip_armor(self, armor): 
        assert self.hp > 0 , "u dead ll"
        
        if armor not in armor_list or armor not in self.inventory_armor:
            raise ValueError("The armor you are trying to equip does not exist or you don't have it") # ce ca
            return
            
        if self.armor_equipped is None: 
            self.armor_equipped = armor
            print(f'You have sucsessfully equiped {armor}')
            return
        else: 
            self.armor_equipped = armor
            print(f'You have sucsessfully switched to {armor}')
            return
        
                
        
    def eat_food(self, food):
        assert self.hp > 0 , "u dead ll"
        if food not in food_list or food not in self.inventory_food:
            raise ValueError("The food you are tryin to eat does not exist or you don't have it")
        
        self.hp += food_list[food]
        if self.hp > self.max_hp:
            self.hp = self.max_hp
        print(f"Your hp is now : {self.hp}")


# popa = character("yeahor")
# print(popa.infos())
# popa.eat_food("Bread")