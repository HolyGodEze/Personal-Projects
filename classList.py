import random as die
from characterBase import Main_Character

class Piercer(Main_Character):
    def __init__(self, HP = 40, DEF = 0, minATK = 4, maxATK = 6, critChance = 8):
        super().__init__(HP, DEF, minATK, maxATK)
        self.critChance = critChance
        self.arrow_rain_CD = 0
        self.arrow_explosion_CD = 0
        self.multiple_glories_CD = 5
    
    # Piercer has a 1 in 8 chance to deal double damage on an attack and heal for 25% of damage dealt. 
    def shoot_attack(self):
        if die.randint(1, self.critChance) == 1:
            crit_hit = super().attack() * 2
            print(f"Critical hit! Dealt {crit_hit} damage!")
            healing = crit_hit // 4
            if self.hp + healing >= 40:
                self.hp = 40
                print("Health is maxed out!")
            else:
                self.hp += healing
                print(f"Healed for {healing} HP!")
                
            self.arrow_rain_CD -= 1 if self.arrow_rain_CD > 0 else 0
            self.arrow_explosion_CD -= 1 if self.arrow_explosion_CD > 0 else 0
            self.multiple_glories_CD -= 1 if self.multiple_glories_CD > 0 else 0
            return crit_hit
        else:
            print(f"Normal hit.")
            self.arrow_rain_CD -= 1 if self.arrow_rain_CD > 0 else 0
            self.arrow_explosion_CD -= 1 if self.arrow_explosion_CD > 0 else 0
            self.multiple_glories_CD -= 1 if self.multiple_glories_CD > 0 else 0
            return super().attack()
        
    # Activate to send a rain of arrows down on all enemies, dealing 5 damage. Cooldown of 3 turns.
    def Arrow_Rain(self):
        if self.arrow_rain_CD > 0:
            print(f"Arrow Rain is on cooldown for {self.arrow_rain_CD} more turns.")
            return 0
        print("You used Arrow Rain! Dealt 5 damage to all enemies!")
        self.arrow_rain_CD = 3
        return 5
    
    # Activate to shoot an infused arrow with explosive power to a single enemy, dealing 24 damage. Cooldown of 4 turns.
    def Arrow_Explosion(self):
        if self.arrow_explosion_CD > 0:
            print(f"Blaster Explosion is on cooldown for {self.arrow_explosion_CD} more turns.")
            return 0
        print("You used Blaster Explosion! Dealt 24 damage!")
        self.arrow_explosion_CD = 4
        return 24
    
    # Activate to summon a massive arrow to the sky, striking all enemies for 25 damage. If this skill kills at least 1 enemy, cooldown is reduced by 2 turns. Heals 6 HP for every enemy killed. Starts with a cooldown of 5 turns.
    def One_Shot_Multiple_Glories(self):
        if self.multiple_glories_CD > 0:
            print(f"One Shot Multiple Glories is on cooldown for {self.multiple_glories_CD} more turns.")
            return 0
        print("You used One Shot Multiple Glories! Dealt 25 damage to all enemies!")
        self.multiple_glories_CD = 5
        self.hp += 6
        return 25
        

    def __str__(self):
        return f"Piercer\nHP: {self.hp}\nDEF: {self.defense}\nATK: {self.minattack}-{self.maxattack}\nCrit Chance: 1 in {self.critChance}\nArrow Rain (3 turn CD): Activate to send a rain of arrows, dealing 5 damage to all enemies.\nArrow Explosion (4 turn CD): Activate to shoot an infused arrow with explosive power to a single enemy, dealing 24 damage. Cooldown of 4 turns.\nOne Shot, Multiple Glories (5 turn CD): Activate to summon a massive arrow to the sky, striking all enemies for 25 damage. If this skill kills at least 1 enemy, cooldown is reduced by 2 turns. Heals 6 HP for every enemy killed. Starts with a cooldown of 5 turns."
    
    
#TODO: Add class Baller
class Baller(Main_Character):
    def __init__(self, HP = 35, DEF = 0, minATK = 8, maxATK = 10):
        super().__init__(HP, DEF, minATK, maxATK)
        self.extradamage = 5
        self.extradamagechance = 6
        self.triple_throw = 0
    
    # Activate to throw a ball at the enemy, with a chance to deal extra damage.
    def ball_attack(self):
        if die.randint(1, self.extradamagechance) == 1:
            print(f"Dealt {self.extradamage} extra damage!")
            return super().attack() + self.extradamage
        else:
            dmg = die.randint(self.minattack, self.maxattack)
            print(f"Dealt {dmg} damage!")
            return dmg
    
    # Activate to throw three balls consecutively, dealing three hits of damage to the enemy. 2 turn CD.
    def Triple_Throw(self):
        total_dmg = 0
        for _ in range(3):
            total_dmg += die.randint(self.minattack, self.maxattack)
        print(total_dmg)
        return total_dmg
    
    def __str__(self):
        return f"Baller\nHP: {self.hp}\nDEF: {self.defense}\nATK: {self.minattack}-{self.maxattack}\n"
    

#TODO: Add class Slicer


#TODO: Add class Crusher


