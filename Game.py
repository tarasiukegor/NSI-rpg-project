from Arena import * 
from Armor import * 
from Character import *
from Enemies import * 
from Food import *
from Store import *
from Weapon import *


popa = character("yeahor") # on cree un perso 
print(popa.infos()) # on regarde ses stats
popa.eat_food("Bread") # on mange pour montrer que la max PV est 100 
rena = arena() # on cree l'arena
rena.display_monsters() # avec cette fonction on peut voir la liste des monsters
rena.fight(popa, 1) # on choisie la premiere (index 0(1-1))

popa.eat_food("Bread") # on mange nyam nyam

popa.equip_weapon("Common Bow") # on essaie un arme
popa.equip_armor("Leather Armor") # et l'armure
print(popa.infos()) #des infos

popa.equip_weapon("Legendary Super Puper Katana") #nous n'aimions pas l'arme 
popa.equip_armor("Legenday Super Puper Armor")  #et l'armure, alors nous l'avons changée pour une autre

rena.fight(popa, 7) # on combat le monstre le plus difficile 

print(popa.infos()) # on voir notre stats

popa.eat_food("Standart Dish") # et mange nyam nyam