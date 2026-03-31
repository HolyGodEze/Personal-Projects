from enemyList import *
from classList import *

piercer = Piercer()
baller  = Baller()
enemy2 = Goblin()
enemy1 = Skeleton()

print(f'Baller HP before attack: {piercer.hp}')
print(f'Before HP: {enemy2.hp}')
enemy2.take_damage(baller.Triple_Throw())
print(f'Piercer HP after attack: {piercer.hp}')
print(f'After taking damage: {enemy2.hp}')

print(piercer)