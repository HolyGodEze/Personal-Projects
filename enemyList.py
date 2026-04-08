from characterBase import Enemy

class Goblin(Enemy):
    def __init__(self, HP = 10, minATK = 2, maxATK = 4):
        super().__init__(HP, minATK, maxATK)

class Skeleton(Enemy):
    def __init__(self, HP = 15, minATK = 3, maxATK = 6):
        super().__init__(HP, minATK, maxATK)

def enemyList():
    return [Goblin, Skeleton]
