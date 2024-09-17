from Enemies import *
from Character import *
from random import *
import random
from time import *
import time
class arena():
    def __init__(self):
        self.monsters_list = [
            monster("Slime", 10, 5, 3),     # name, health, attack, gold
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
            print(f"{i}. {monster.name} (Health : {monster.monster_health},  Attack : {monster.attack}, Worth of gold : {monster.gold})")
        print("You can now choose a monster to fight by typing: fight( 'character's name' , 'monster's number')")
        
            
            
    def fight(self, player, opponent):
        assert player.hp > 0 
        assert 1 <= opponent <= len(self.monsters_list), "Choose right opponent"
        opponent = self.monsters_list[opponent - 1]
        
        while player.hp > 0 and opponent.monster_health > 0:
            print(f"\n{player.name} attacks.\n")
            time.sleep(2)
            num1 = randint(1,10)
            num2 = randint(1,10)
            operator = random.choice(["*", "+", "-"])
            problem = f"{num1}{operator}{num2}=?"
            
            start_time = time.time()
            print(problem)
            player_answer = input("Enter your answer: ")
            end_time = time.time()
            
            
            if end_time - start_time > 5:
                print("Time's up!")
                continue
                
            try:
                player_answer = int(player_answer)
                if eval(f"{num1}{operator}{num2}") == player_answer:
                    print("\nCorrect")
                    opponent.monster_health -= player.attack
                    print(f"-{player.attack}hp. {opponent.name} has {opponent.monster_health}hp")
                    time.sleep(3)
                else:
                    print("Incorrect, try next time")
                    time.sleep(3)
            except ValueError:
                print("Invalid, please enter an integer")
                
            if opponent.monster_health > 0:
                print(f"\n{opponent.name} attacks.")
                if player.armor_equipped == None:
                    
                    player.hp -= opponent.attack
                else:
                    if opponent.attack - armor_list[player.armor_equipped] < 0 :
                        print("Your armor is too strong!")
                        
                time.sleep(1)
                print(f"Player's health: {player.hp}")
                
        if player.hp <= 0:
            print(f"{player.name} has been defeated, you can no longer play with him")
        else:
            print(f"You have defeated {opponent.name}, you earn {opponent.gold} gold coins")
            player.bank += opponent.gold
            
# pers =character('Tatata')

# rena = arena()


                      
# rena.fight(pers, 1) 



# popa = character("yeahor")
# popa.equip_armor("Leather Armor")
# print(popa.infos())

# rena = arena()
# rena.display_monsters()  

# rena.fight(popa, 1)
# Fight system idea: 
    # character VS enemy (loop)
    # character attack : rand(int(1,10)) ("/" or "*" or "-" or "+") rand(int(1,10))
    # if answer is correct, character attacks enemy, then enemy strikes
    # enemy attack: basic enemy attack
    # figth untill either enemy's health <= 0 or character's health <= 0 
    # if enemy dies, character recieves gold from the enemy, and moves on
    # if character dies, you cannot use this character 
    
