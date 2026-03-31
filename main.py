from enemyList import *
from classList import *

piercer = Piercer()
enemy2 = Goblin()
enemy1 = Skeleton()

print(f'Piercer HP before attack: {piercer.hp}')
print(f'Before HP: {enemy2.hp}')
enemy2.take_damage(piercer.Arrow_Rain())
print(f'Piercer HP after attack: {piercer.hp}')
print(f'After taking damage: {enemy2.hp}')

print(piercer)