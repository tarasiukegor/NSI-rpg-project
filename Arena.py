from Enemies import *
from Character import *

class arena():
    def __init__(self):
        self.monsters_list = [
            monster("Slime", 25, 5, 3),
            monster("King Slime", 50, 15, 5),
            monster("Goblin", 35, 10, 4),
            monster("King Goblin", 70, 25, 10),
            monster("Orc", 50, 20, 8),
            monster("King Orc", 100, 30, 15),
            monster("The King of Trolls", 250, 50, 100),
        ]
        
    def display_monsters(self):
        print("Available Monsters: ")
        for i, monster in enumerate(self.monsters_list, 1):
            print(f"{i}. {monster.name} (Health : {monster.health},  Attack : {monster.attack}, Worth of gold : {monster.gold})")
        print("You can now choose a monster to fight by typing: choose_monster(*monster's number*)")
        
    def choose_monster(self, choice):
        if 1 <= choice <= len(self.monsters_list):
            print(f"You have chosen {self.monsters_list[choice]}")
            
