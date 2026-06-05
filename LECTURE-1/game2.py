import json
import random
import os

SAVE_FILE = "rpg_save.json"

# =========================
# ASCII ART
# =========================

TITLE = r"""
=========================================
        TERMINAL RPG QUEST
=========================================
"""

BOSS_ART = r"""
          /\_/\\
         ( o.o )
          > ^ <
      DRAGON KING
"""

# =========================
# PLAYER CLASSES
# =========================

CLASSES = {
    "Warrior": {"hp": 120, "attack": 18},
    "Mage": {"hp": 80, "attack": 25},
    "Assassin": {"hp": 90, "attack": 22}
}

SHOP_ITEMS = {
    "Health Potion": 25,
    "Iron Sword": 75,
    "Magic Scroll": 100
}

# =========================
# PLAYER
# =========================

class Player:
    def __init__(self, name, cls):
        self.name = name
        self.cls = cls
        self.max_hp = CLASSES[cls]["hp"]
        self.hp = self.max_hp
        self.attack = CLASSES[cls]["attack"]

        self.gold = 100
        self.level = 1
        self.xp = 0

        self.inventory = ["Wooden Sword"]

    def level_up(self):
        while self.xp >= self.level * 100:
            self.xp -= self.level * 100
            self.level += 1

            self.max_hp += 20
            self.attack += 5
            self.hp = self.max_hp

            print("\n*** LEVEL UP! ***")
            print(f"Level {self.level}")
            print(f"Attack: {self.attack}")
            print(f"HP: {self.max_hp}")

# =========================
# SAVE / LOAD
# =========================

def save_game(player):
    data = player.__dict__

    with open(SAVE_FILE, "w") as f:
        json.dump(data, f)

    print("Game Saved!")

def load_game():
    if not os.path.exists(SAVE_FILE):
        return None

    with open(SAVE_FILE, "r") as f:
        data = json.load(f)

    player = Player(data["name"], data["cls"])
    player.__dict__.update(data)

    return player

# =========================
# ENEMIES
# =========================

ENEMIES = [
    {"name": "Goblin", "hp": 40, "attack": 8, "gold": 25, "xp": 50},
    {"name": "Skeleton", "hp": 60, "attack": 10, "gold": 40, "xp": 75},
    {"name": "Orc", "hp": 80, "attack": 15, "gold": 60, "xp": 100},
]

BOSS = {
    "name": "Dragon King",
    "hp": 250,
    "attack": 30,
    "gold": 500,
    "xp": 500
}

# =========================
# COMBAT
# =========================

def battle(player, enemy):
    hp = enemy["hp"]

    print(f"\nA wild {enemy['name']} appeared!")

    while hp > 0 and player.hp > 0:

        print("\n----------------")
        print(f"{player.name}: {player.hp}/{player.max_hp}")
        print(f"{enemy['name']}: {hp}")
        print("----------------")

        print("1. Attack")
        print("2. Use Potion")
        print("3. Run")

        choice = input("> ")

        if choice == "1":

            damage = random.randint(
                player.attack - 3,
                player.attack + 3
            )

            hp -= damage

            print(f"You hit for {damage}")

        elif choice == "2":

            if "Health Potion" in player.inventory:
                player.inventory.remove("Health Potion")

                heal = 50
                player.hp = min(
                    player.max_hp,
                    player.hp + heal
                )

                print(f"Healed {heal} HP")

            else:
                print("No potion!")

        elif choice == "3":
            print("Escaped!")
            return

        if hp > 0:

            enemy_damage = random.randint(
                enemy["attack"] - 2,
                enemy["attack"] + 2
            )

            player.hp -= enemy_damage

            print(
                f"{enemy['name']} attacks for "
                f"{enemy_damage}"
            )

    if player.hp <= 0:
        print("\nYOU DIED")
        exit()

    print(f"\n{enemy['name']} defeated!")

    player.gold += enemy["gold"]
    player.xp += enemy["xp"]

    print(f"+{enemy['gold']} Gold")
    print(f"+{enemy['xp']} XP")

    player.level_up()

# =========================
# SHOP
# =========================

def shop(player):

    while True:

        print("\n===== SHOP =====")
        print(f"Gold: {player.gold}")

        items = list(SHOP_ITEMS.items())

        for i, (name, cost) in enumerate(items, start=1):
            print(f"{i}. {name} - {cost} Gold")

        print("0. Exit")

        choice = input("> ")

        if choice == "0":
            break

        try:
            item, cost = items[int(choice)-1]

            if player.gold >= cost:
                player.gold -= cost
                player.inventory.append(item)

                print(f"Bought {item}")

                if item == "Iron Sword":
                    player.attack += 5

                elif item == "Magic Scroll":
                    player.attack += 10

            else:
                print("Not enough gold.")

        except:
            pass

# =========================
# INVENTORY
# =========================

def show_inventory(player):

    print("\n===== INVENTORY =====")

    for item in player.inventory:
        print("-", item)

# =========================
# MAIN GAME
# =========================

def create_character():

    name = input("Hero Name: ")

    print("\nChoose Class")
    print("1. Warrior")
    print("2. Mage")
    print("3. Assassin")

    choice = input("> ")

    cls_map = {
        "1": "Warrior",
        "2": "Mage",
        "3": "Assassin"
    }

    cls = cls_map.get(choice, "Warrior")

    return Player(name, cls)

def main():

    print(TITLE)

    print("1. New Game")
    print("2. Load Game")

    choice = input("> ")

    if choice == "2":
        player = load_game()

        if player is None:
            print("No save found.")
            player = create_character()
    else:
        player = create_character()

    while True:

        print("\n====================")
        print(player.name)
        print(f"Class : {player.cls}")
        print(f"Level : {player.level}")
        print(f"HP    : {player.hp}/{player.max_hp}")
        print(f"ATK   : {player.attack}")
        print(f"Gold  : {player.gold}")
        print("====================")

        print("\n1. Explore")
        print("2. Shop")
        print("3. Inventory")
        print("4. Save")
        print("5. Boss Battle")
        print("6. Quit")

        choice = input("> ")

        if choice == "1":
            battle(
                player,
                random.choice(ENEMIES)
            )

        elif choice == "2":
            shop(player)

        elif choice == "3":
            show_inventory(player)

        elif choice == "4":
            save_game(player)

        elif choice == "5":
            print(BOSS_ART)
            battle(player, BOSS)

        elif choice == "6":
            print("Goodbye Hero!")
            break

if __name__ == "__main__":
    main()