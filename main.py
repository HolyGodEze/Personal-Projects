from enemyList import *
from classList import *

piercer = Piercer()
baller  = Baller()
enemy2 = Goblin()
enemy1 = Skeleton()

print(f'Baller HP before attack: {baller.hp}')
print(f'Before HP: {enemy2.hp}')
enemy2.take_damage(baller.Triple_Throw())
print(f'Baller HP after attack: {baller.hp}')
print(f'After taking damage: {enemy2.hp}\n')

print(f"{piercer}\n")
print(f"{baller}\n")