import random

class Character:
    def __init__(self, name, hp, mana):
        self.name = name
        self.hp = hp
        self.mana = mana
        self.max_hp = hp
        self.max_mana = mana

    def is_alive(self):
        return self.hp > 0

    def take_damage(self, damage):
        self.hp = max(0, self.hp - damage)

    def heal(self, amount):
        self.hp = min(self.max_hp, self.hp + amount)

    def use_mana(self, amount):
        self.mana = max(0, self.mana - amount)

    def gain_mana(self, amount):
        self.mana = min(self.max_mana, self.mana + amount)


def enemy_ai(enemy):
    if enemy.hp < 30 and enemy.mana >= 15:
        return "heal"

    actions = ["slash", "fire", "dodge"]

    if enemy.mana < 10:
        actions.remove("fire")

    return random.choice(actions)


def player_menu():
    print("\n1. Slash")
    print("2. Fireball (10 mana)")
    print("3. Heal (15 mana)")
    print("4. Dodge")

    choice = input("Choose: ")

    return {
        "1": "slash",
        "2": "fire",
        "3": "heal",
        "4": "dodge"
    }.get(choice, None)


print("⚔️ SMART DODGE RPG ⚔️")
name = input("Enter hero name: ")

player = Character(name, 120, 50)
enemy = Character("Shadow Knight", 120, 40)

while player.is_alive() and enemy.is_alive():

    print("\n===========================")
    print(f"{player.name} HP: {player.hp} | Mana: {player.mana}")
    print(f"{enemy.name} HP: {enemy.hp} | Mana: {enemy.mana}")
    print("===========================")

    player_action = player_menu()
    enemy_action = enemy_ai(enemy)

    if not player_action:
        print("Invalid choice!")
        continue

    print(f"\nEnemy chose: {enemy_action}")

    # Cancel if same action
    if player_action == enemy_action:
        print("💥 Both used same move! Cancelled!")
        continue

    # ----------------------
    # HANDLE DODGE LOGIC
    # ----------------------

    player_dodged = False
    enemy_dodged = False

    if player_action == "dodge" and enemy_action in ["slash", "fire"]:
        player_dodged = True
        print("😎 You successfully dodged!")
        player.gain_mana(10)
        print("You gained 10 mana!")

    if enemy_action == "dodge" and player_action in ["slash", "fire"]:
        enemy_dodged = True
        print("👻 Enemy dodged your attack!")
        enemy.gain_mana(10)

    # ----------------------
    # PLAYER TURN
    # ----------------------

    if not enemy_dodged:

        if player_action == "slash":
            damage = random.randint(10, 20)
            enemy.take_damage(damage)
            print(f"🗡️ You dealt {damage} damage!")

        elif player_action == "fire" and player.mana >= 10:
            damage = random.randint(20, 30)
            enemy.take_damage(damage)
            player.use_mana(10)
            print(f"🔥 Fireball dealt {damage} damage!")

        elif player_action == "heal" and player.mana >= 15:
            heal_amount = random.randint(15, 25)
            player.heal(heal_amount)
            player.use_mana(15)
            print(f"🧪 You healed {heal_amount} HP!")

    # ----------------------
    # ENEMY TURN
    # ----------------------

    if not player_dodged:

        if enemy_action == "slash":
            damage = random.randint(8, 18)
            player.take_damage(damage)
            print(f"👹 Enemy slashed for {damage} damage!")

        elif enemy_action == "fire" and enemy.mana >= 10:
            damage = random.randint(15, 25)
            player.take_damage(damage)
            enemy.use_mana(10)
            print(f"🔥 Enemy used Dark Flame for {damage} damage!")

        elif enemy_action == "heal" and enemy.mana >= 15:
            heal_amount = random.randint(10, 20)
            enemy.heal(heal_amount)
            enemy.use_mana(15)
            print(f"👹 Enemy healed {heal_amount} HP!")

# Result
if player.is_alive():
    print("\n🏆 YOU WIN!")
else:
    print("\n💀 YOU LOST!")