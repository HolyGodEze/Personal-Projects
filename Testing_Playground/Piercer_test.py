import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from classList import Piercer
from enemyList import Skeleton, Goblin

piercer = Piercer()
goblin = Goblin()
skeleton = Skeleton()

class Test_Piercer(unittest.TestCase):

    def test_init(self):
        piercer = Piercer()
        self.assertEqual(piercer.hp, 40)
        self.assertEqual(piercer.minattack, 4)
        self.assertEqual(piercer.maxattack, 6)
        self.assertEqual(piercer.defense, 0)

    # Critical hit check on enemies
    def test_CriticalAttackOnEnemies(self):
        piercer = Piercer()
        goblin = Goblin()
        skeleton = Skeleton()
        piercer.critChance = 1
        goblin.take_damage(piercer.shoot_attack())
        self.assertTrue(0 <= goblin.hp <= 2)
        
        skeleton.take_damage(piercer.shoot_attack())
        self.assertTrue(3 <= skeleton.hp <= 7)
        
    # Check if healing is correctly implemented on a critical hit.
    def test_CritHeal(self):
        piercer = Piercer()
        goblin = Goblin()
        skeleton = Skeleton()
        piercer.critChance = 1
        piercer.hp = 10
        
        # Character is not at full health
        goblin.take_damage(piercer.shoot_attack())
        print(piercer.hp)
        self.assertTrue(12 <= piercer.hp <= 13)
        
        # Character is at full health
        piercer.hp = 40
        skeleton.take_damage(piercer.shoot_attack())
        self.assertEqual(piercer.hp, 40)
    
        
if __name__ == '__main__':
    unittest.main()