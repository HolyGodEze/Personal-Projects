import random as die
from characterBase import Main_Character

class Piercer(Main_Character):
    def __init__(self, HP = 40, DEF = 0, minATK = 4, maxATK = 6):
        super().__init__(HP, DEF, minATK, maxATK)
        self.critChance = 8
        self.arrow_rain_CD = 3
        self.arrow_rain_start_CD = 0
        self.arrow_explosion_CD = 4
        self.arrow_explosion_start_CD = 0
        self.multiple_glories_CD = 5
      
    def take_damage(self, damage):
        self.hp -= damage
    
    # Piercer has a 1 in 8 chance to deal double damage on an attack and heal for 25% of damage dealt. 
    def shoot_attack(self):
        if die.randint(1, self.critChance) == 1:
            crit_hit = die.randint(self.minattack, self.maxattack) * 2
            print(f"Critical hit! Dealt {crit_hit} damage!")
            healing = crit_hit // 4
            if self.hp + healing >= 40:
                self.hp = 40
                print("Health is maxed out!")
            else:
                self.hp += healing
                print(f"Healed for {healing} HP!")
                
            self.arrow_rain_start_CD -= 1 if self.arrow_rain_start_CD > 0 else 0
            self.arrow_explosion_start_CD -= 1 if self.arrow_explosion_start_CD > 0 else 0
            self.multiple_glories_CD -= 1 if self.multiple_glories_CD > 0 else 0
            return crit_hit
        else:
            print(f"Normal hit.")
            self.arrow_rain_start_CD -= 1 if self.arrow_rain_start_CD > 0 else 0
            self.arrow_explosion_start_CD -= 1 if self.arrow_explosion_start_CD > 0 else 0
            self.multiple_glories_CD -= 1 if self.multiple_glories_CD > 0 else 0
            return die.randint(self.minattack, self.maxattack)
        
    # Activate to send a rain of arrows down on all enemies, dealing 5 damage. Cooldown of 3 turns.
    def Arrow_Rain(self):
        if self.arrow_rain_CD > 0:
            print(f"Arrow Rain is on cooldown for {self.arrow_rain_CD} more turns.")
            return 0
        print("You used Arrow Rain! Dealt 5 damage to all enemies!")
        self.arrow_rain_start_CD = self.arrow_rain_CD
        return 5
    
    # Activate to shoot an infused arrow with explosive power to a single enemy, dealing 24 damage. Cooldown of 4 turns.
    def Arrow_Explosion(self):
        if self.arrow_explosion_start_CD > 0:
            print(f"Blaster Explosion is on cooldown for {self.arrow_explosion_start_CD} more turns.")
            return 0
        print("You used Blaster Explosion! Dealt 24 damage!")
        self.arrow_explosion_start_CD = self.arrow_explosion_CD
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
        
    # Returns a skillset and stats for the Piercer class
    def piercer_stats_and_abilities(self):
        return {
            "name": "Piercer",
            "HP": self.hp,
            "DEF": self.defense,
            "min_ATK": self.minattack,
            "max_ATK": self.maxattack,
            "crit_chance": f"{round(1 / self.critChance * 100, 1)}%",
            "color": "#8f29bb",
            "skills": [
                {
                    "skill_name": "Shoot",
                    "description": "Shoots an arrow at the enemy, with a 12.5% "  + "chance of landing a critical hit. A critical hit deals double damage and heals 25% "  + "of the damage dealt."
                },
                {
                    "skill_name": "Arrow Rain",
                    "skill_CD": self.arrow_rain_CD,
                    "description": f"Sends a rain of arrows down on all enemies, dealing 5 damage."
                },
                {
                    "skill_name": "Arrow Explosion",
                    "skill_CD": self.arrow_explosion_CD,
                    "description": "Shoots an infused arrow with explosive power to a single enemy, dealing 24 damage."
                },
                {
                    "skill_name": "One Shot, Multiple Glories",
                    "skill_CD": self.multiple_glories_CD,
                    "description": "Summons a massive arrow to the sky, striking all enemies for 25 damage. If this skill kills at least 1 enemy, cooldown is reduced by 2 turns. Heals 6 HP for every enemy killed. Starts with a cooldown of 5 turns."
                }
            ]
        }
    
    

class Baller(Main_Character):
    def __init__(self, HP = 35, DEF = 0, minATK = 8, maxATK = 10):
        super().__init__(HP, DEF, minATK, maxATK)
        self.extradamage = 5
        self.extradamagechance = 6
        self.triple_throw_CD = 2
        self.triple_throw_start_CD = 0
        self.gigantic_throw_CD = 4
        self.gigantic_throw_start_CD = 0
        
    def take_damage(self, damage):
        self.hp -= damage
    
    # Activate to throw a ball at the enemy, with a chance to deal extra damage.
    def ball_attack(self):
        if die.randint(1, self.extradamagechance) == 1:
            print(f"Dealt {self.extradamage} extra damage!")
            self.triple_throw_start_CD -= 1 if self.triple_throw_start_CD > 0 else 0
            self.gigantic_throw_start_CD -= 1 if self.gigantic_throw_start_CD > 0 else 0
            return die.randint(self.minattack, self.maxattack) + self.extradamage
        else:
            dmg = die.randint(self.minattack, self.maxattack)
            print(f"Dealt {dmg} damage!")
            self.triple_throw_start_CD -= 1 if self.triple_throw_start_CD > 0 else 0
            self.gigantic_throw_start_CD -= 1 if self.gigantic_throw_start_CD > 0 else 0
            return dmg
    
    # Activate to throw three balls consecutively, dealing three hits of damage to the enemy. 2 turn CD.
    def Triple_Throw(self):
        total_dmg = 0
        for _ in range(3):
            total_dmg += die.randint(self.minattack, self.maxattack)
        print(total_dmg)
        return total_dmg
    
    # Activate to increase the size of the ball, before throwing it at the enemy, dealing 30 damage. 4 turn CD.
    def Gigantic_Throw(self):
        return 30
    
    # Returns a skillset and stats for the Baller class
    def baller_stats_and_abilities(self):
        return {
            "name": "Baller",
            "HP": self.hp,
            "DEF": self.defense,
            "min_ATK": self.minattack,
            "max_ATK": self.maxattack,
            "extra_dmg": self.extradamage,
            "extra_chance": round((1/self.extradamagechance) * 100, 1),
            "color": "#e61111",
            "skills": [
                {
                   "skill_name": "Throw",
                   "description": "Throws a ball a the enemy, with a 16.7% " + "chance to deal 5 extra damage."
                },
                {
                    "skill_name": "Triple Throw",
                    "skill_CD": self.triple_throw_CD,
                    "description": "Throw three balls consecutively at the enemy, dealing three hits of damage to the enemy."
                },
                {
                    "skill_name": "Gigantic Throw",
                    "skill_CD": self.gigantic_throw_CD,
                    "description": "Increases the size of the ball before throwing it at the enemy, dealing 30 damage."
                }
            ]
        }
    

#TODO: Add class Slicer
class Slicer(Main_Character):
    def __init__(self, HP = 50, DEF = 2, minATK = 6, maxATK = 10):
        super().__init__(HP, DEF, minATK, maxATK)
        self.pierce_dmg = 4
        self.pierce_chance = 3
        self.sword_thrust_CD = 2
        self.sword_thrust_start_CD = 0
        self.sword_spin_CD = 3
        self.sword_spin_start_CD = 0
        self.flurry_rush_CD = 5
        self.flurry_rush_start_CD = 0
    
    def take_damage(self, damage):
        self.hp -= damage
           
    # Slices the enemy with a sword, with a 33.3% chance of dealing piercing damage.
    def sword_attack(self):
        if die.randint(1, self.pierce_chance) == 1:
            piercing_dmg = super().attack() + self.pierce_dmg
            self.sword_thrust_start_CD -= 1 if self.sword_thrust_start_CD > 0 else 0
            self.sword_spin_start_CD -= 1 if self.sword_spin_start_CD > 0 else 0
            self.flurry_rush_start_CD -= 1 if self.flurry_rush_start_CD > 0 else 0
            print(f"Dealt {piercing_dmg} piercing damage!")
            return piercing_dmg
        else:
            dmg = die.randint(self.minattack, self.maxattack)
            print(f"Dealt {dmg} damage!")
            return dmg
    
    # Dashes into the enemy with the sword, dealing 10 damage. 2 turn cooldown.
    def Sword_Thrust(self):
        self.sword_thrust_start_CD = self.sword_thrust_CD
        return 10

    # Attacks the enemy by doing a sword spin, dealing 2 consecutive hits of damage. 3 turn cooldown.
    def Sword_Spin(self):
        self.sword_spin_start_CD = self.sword_spin_CD
        return die.randint(self.minattack, self.maxattack) + die.randint(self.minattack, self.maxattack)
    
    # Rushes the enemy with a flurry of 6 sword strikes, each having a chance to pierce the enemy. Damage is cut in half when using this skill. 5 turn cooldown.
    def Flurry_Rush(self):
        total_dmg = 0
        for _ in range(6):
            total_dmg += die.randint(self.minattack, self.maxattack) // 2
            if die.randint(1, self.pierce_chance) == 1:
                total_dmg += self.pierce_dmg
        self.flurry_rush_start_CD = self.flurry_rush_CD
        # minimum damage dealt (no pierce chance) would be 3 * 6 = 18, maximum damage dealt (with pierce chance) is (5 + 4) * 6 = 54
        print(f"{total_dmg} damage dealt!")
        return total_dmg
    
    # Returns a skillset and stats for the Slicer class
    def slicer_stats_and_abilities(self):
        return {
            "name": "Slicer",
            "HP": self.hp,
            "DEF": self.defense,
            "min_ATK": self.minattack,
            "max_ATK": self.maxattack,
            "pierce_dmg": self.pierce_dmg,
            "pierce_chance": round((1/self.pierce_chance) * 100, 1),
            "color": "#1809ebf6",
            "skills": [
                {
                    "skill_name": "Slice",
                    "description": "Slices the enemy with a sword, with a 33.3% " + "chance of dealing piercing damage."
                },
                {
                    "skill_name": "Sword Thrust",
                    "skill_CD": self.sword_thrust_CD,
                    "description": f"Dashes into the enemy with the sword, dealing 10 damage."
                },
                {
                    "skill_name": "Sword Spin",
                    "skill_CD": self.sword_spin_CD,
                    "description": "Attacks the enemy by doing a sword spin, dealing 2 consecutive hits of damage."
                },
                {
                    "skill_name": "Flurry Rush",
                    "skill_CD": self.flurry_rush_CD,
                    "description": "Rushes the enemy with a flurry of 6 sword strikes, each strike having a chance to pierce the enemy. Damage is cut in half when using this skill."
                }
            ]
        }
#TODO: Add class Crusher
class Crusher(Main_Character):
    def __init__(self, HP = 80, DEF = 3, minATK = 9, maxATK = 12):
        super().__init__(HP, DEF, minATK, maxATK)
        self.cooldown_turn = 1
        self.cooldown_chance = 4
        self.cyclone_cd = 3
        self.cyclone_start_cd = 0
        self.heavy_slam_cd = 4
        self.heavy_slam_start_cd = 0
        self.shake_the_world_cd = 9
        
    # If the character takes 6 or more damage, cooldown of Shake The World is decreased by 1.
    def take_damage(self, damage):
        if damage >= 6:
            self.shake_the_world_cd -= 1
            print("Cooldown decreased by 1!")
        self.hp -= damage
    
    # Attacks the enemy with a sledgehammer, with a 25% chance to decrease the skill cooldown of Shake The World by 1 turn.
    def sledgehammer_attack(self):
        if die.randint(1, self.cooldown_chance) == 1:
            self.shake_the_world_cd -= 1
        self.cyclone_start_cd -= 1 if self.cyclone_start_cd > 0 else 0
        self.heavy_slam_start_cd -= 1 if self.heavy_slam_start_cd > 0 else 0
        self.shake_the_world_cd -= 1 if self.shake_the_world_cd > 0 else 0
        return die.randint(self.minattack, self.maxattack)
    
    
    # Spins around with a sledgehammer, dealing 12 damage to a single enemy. Cooldown of 3 turns.
    def Cyclone(self):
        self.cyclone_start_cd = self.cyclone_cd
        return 12
    
    # Slams the sledgehammer to a single enemy, dealing 25 damage. Cooldown of 4 turns.
    def Heavy_Slam(self):
        self.heavy_slam_start_cd = self.heavy_slam_cd
        return 25
    
    # Slams the ground to cause a massive earthquake to all enemies, dealing 30 damage. Starts with a cooldown of 9 turns.
    def Shake_The_World(self):
        self.shake_the_world_cd = 9
        return 30
    
    # Stats and skills for Crusher
    def crusher_stats_and_abilities(self):
        return {
            "name": "Crusher",
            "HP": self.hp,
            "DEF": self.defense,
            "min_ATK": self.minattack,
            "max_ATK": self.maxattack,
            "cd_turn": self.cooldown_turn,
            "cd_chance": round((1/self.cooldown_chance) * 100, 1),
            "color": "#09eb23fb",
            "skills": [
                {
                    "skill_name": "Smash",
                    "description": "Attacks the enemy with a sledgehammer, with a 25% chance to decrease the skill cooldown of Shake The World by 1 turn."
                },
                {
                    "skill_name": "Cyclone",
                    "skill_CD": self.cyclone_cd,
                    "description": "Spins around with a sledgehammer, dealing 12 damage to a single enemy."
                },
                {
                    "skill_name": "Heavy Slam",
                    "skill_CD": self.heavy_slam_cd,
                    "description": "Slams the sledgehammer to a single enemy, dealing 25 damage."
                },
                {
                    "skill_name": "Flurry Rush",
                    "skill_CD": self.shake_the_world_cd,
                    "description": "Slams the ground to cause a massive earthquake to all enemies, dealing 30 damage. Starts with a cooldown of 9 turns."
                }
            ]
        }