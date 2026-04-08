import random as die
from abc import abstractmethod, ABC
class Main_Character(ABC):
    def __init__(self, HP: int, minATK: int, maxATK: int):
        self.hp = HP
        self.minattack = minATK
        self.maxattack= maxATK
        
    
    @abstractmethod
    def take_damage(self, enemy):
        pass
        
class Enemy():
    def __init__(self, HP, minATK, maxATK):
       self.hp = HP
       self.minATK = minATK
       self.maxATK = maxATK
        
    def enemy_attack(self):
        return die.randint(self.minATK, self.maxATK)
    
    def take_damage(self, damage):
        if damage > self.hp:
            self.hp = 0
        else:
            self.hp -= damage
    
    
        