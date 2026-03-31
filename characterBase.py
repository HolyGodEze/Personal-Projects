import random as die
from enemyList import *
class Main_Character():
    def __init__(self, HP: int, DEF: int, minATK: int, maxATK: int):
        self.hp = HP
        self.defense = DEF
        self.minattack = minATK
        self.maxattack= maxATK
        
    def attack(self):
        return die.randint(self.minattack, self.maxattack)
    
    def take_damage(self, enemy):
        self.hp -= max(0, enemy.enemy_attack() - self.defense)
    
    
        