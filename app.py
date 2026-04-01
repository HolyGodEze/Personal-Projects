from flask import Flask, render_template

app = Flask(__name__)

# --- Game Data ---

classes = [
    {
        "name": "Piercer",
        "hp": 40,
        "defense": 0,
        "atk_min": 4,
        "atk_max": 6,
        "crit_chance": "12.5%",
        "description": "A ranged specialist who fires arrows with deadly precision. Critical hits deal double damage and restore health.",
        "tag": "Ranged • Critical • Sustain",
        "color": "#c8a84b",
        "abilities": [
            {
                "name": "Shoot Attack",
                "description": "Basic ranged attack. Has a 1-in-8 chance to critically strike for double damage, healing for 25% of damage dealt."
            },
            {
                "name": "Arrow Rain",
                "description": "Sends a rain of arrows down on all enemies, dealing 5 damage to each. Cooldown: 3 turns.",
                "cooldown": 3
            },
            {
                "name": "Arrow Explosion",
                "description": "Fires an infused explosive arrow at a single enemy, dealing 24 damage. Cooldown: 4 turns.",
                "cooldown": 4
            },
            {
                "name": "One Shot Multiple Glories",
                "description": "Summons a massive arrow that strikes all enemies for 25 damage. Killing an enemy reduces cooldown by 2 turns and heals 6 HP per kill. Starts on cooldown.",
                "cooldown": 5
            }
        ]
    },
    {
        "name": "Baller",
        "hp": 35,
        "defense": 0,
        "atk_min": 8,
        "atk_max": 10,
        "crit_chance": "1 in 6 (bonus damage)",
        "description": "A high-risk, high-reward fighter who hurls balls at enemies with explosive force. Excels at burst damage.",
        "tag": "Melee • Burst • High Damage",
        "color": "#5b8dd9",
        "abilities": [
            {
                "name": "Ball Attack",
                "description": "Throws a ball at the enemy. Has a 1-in-6 chance to deal an extra 5 bonus damage on top of the normal hit."
            },
            {
                "name": "Triple Throw",
                "description": "Throws three balls consecutively, dealing three separate hits of damage to the enemy."
            }
        ]
    }
]

enemies = [
    {
        "name": "Goblin",
        "hp": 10,
        "atk_min": 2,
        "atk_max": 4,
        "description": "A small but sneaky creature. Low health makes it easy to dispatch, but don't underestimate its bite.",
        "tag": "Common • Weak",
        "color": "#6abf69"
    },
    {
        "name": "Skeleton",
        "hp": 15,
        "atk_min": 3,
        "atk_max": 6,
        "description": "An undead warrior with rattling bones and a relentless will to fight. Hits harder than it looks.",
        "tag": "Common • Moderate",
        "color": "#b0b0b0"
    }
]

# --- Routes ---

@app.route("/")
def home():
    return render_template("index.html", classes=classes, enemies=enemies)

@app.route("/classes")
def classes_page():
    return render_template("classes.html", classes=classes)

@app.route("/enemies")
def enemies_page():
    return render_template("enemies.html", enemies=enemies)

if __name__ == "__main__":
    app.run(debug=True)
