import random as die

class Enemy:
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
    
class Goblin(Enemy):
    def __init__(self, HP = 10, minATK = 2, maxATK = 4):
        super().__init__(HP, minATK, maxATK)

class Skeleton(Enemy):
    def __init__(self, HP = 15, minATK = 3, maxATK = 6):
        super().__init__(HP, minATK, maxATK)

def enemyList():
    return [Goblin, Skeleton]
