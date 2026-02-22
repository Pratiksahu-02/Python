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
    elif enemy.hp<30 and enemy.mana < 15:
        return "dodge"

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
enemy = Character("Shadow Knight", 120, 50)

while player.is_alive() and enemy.is_alive():

    print("\n===========================")
    print(f"{player.name} HP: {player.hp} | Mana: {player.mana}")
    print(f"{enemy.name} HP: {enemy.hp} | Mana: {enemy.mana}")
    print("===========================")

    # Get player and enemy actions (only call once)
    player_action = player_menu()
    enemy_action = enemy_ai(enemy)
    
    # Initialize all action variables
    player_action_attack = None
    player_action_heal = None
    player_action_dodge = None
    enemy_action_attack = None
    enemy_action_heal = None
    enemy_action_dodge = None
    player_dodged = False
    enemy_dodged = False

    # Validate player input
    if player_action is None:
        print("Invalid choice!")
        continue

    # Categorize player action
    if player_action in ["slash", "fire"]:
        player_action_attack = player_action
    elif player_action == "heal":
        player_action_heal = player_action
    elif player_action == "dodge":
        player_action_dodge = player_action

    # Categorize enemy action
    if enemy_action in ["slash", "fire"]:
        enemy_action_attack = enemy_action
    elif enemy_action == "heal":
        enemy_action_heal = enemy_action
    elif enemy_action == "dodge":
        enemy_action_dodge = enemy_action

    print(f"\n Enemy chose: {enemy_action}")

    # Cancel if same action
    if player_action_attack and enemy_action_attack and player_action_attack == enemy_action_attack:
        print("🤝 Both chose the same attack! No damage dealt.")
        continue

    list=["dodge","critical srtike","dodge"]

    if player_action_dodge and enemy_action_attack:
        outcome=random.shuffle(list)
        if outcome=="dodge":
            player_dodged = True
            print("🛡️ You dodged the enemy's attack!")
            mana=random.randrange(5,10)
            player.gain_mana(mana)
        elif outcome=="critical srtike" :
            damage = random.randint(15, 30)
            player.take_damage(damage)
            print(f"💥 You took {damage} damage from the critical strike!")

    if enemy_action_dodge and player_action_attack:
        outcome=random.shuffle(list)
        if outcome=="dodge":
            enemy_dodged = True
            print("👹 Enemy dodged your attack!")
            mana=random.randrange(5,10)
            enemy.gain_mana(mana)
        elif outcome=="critical srtike":
            damage = random.randint(15, 30)
            enemy.take_damage(damage)
            print(f"💥 Enemy took {damage} damage from the critical strike!")


    # ----------------------
    # PLAYER TURN
    # ----------------------

    if not enemy_dodged:

        if player_action_attack == "slash":
            damage = random.randint(10, 20)
            enemy.take_damage(damage)
            print(f"🗡️ You dealt {damage} damage!")

        elif player_action_attack == "fire" and player.mana >= 10:
            damage = random.randint(20, 30)
            enemy.take_damage(damage)
            player.use_mana(10)
            print(f"🔥 Fireball dealt {damage} damage!")

        elif player_action_heal == "heal" and player.mana >= 15:
            heal_amount = random.randint(15, 25)
            player.heal(heal_amount)
            player.use_mana(15)
            print(f"🧪 You healed {heal_amount} HP!")

    # ----------------------
    # ENEMY TURN
    # ----------------------

    if not player_dodged:

        if enemy_action_attack == "slash":
            damage = random.randint(8, 18)
            player.take_damage(damage)
            print(f"👹 Enemy slashed for {damage} damage!")

        elif enemy_action_attack == "fire" and enemy.mana >= 10:
            damage = random.randint(15, 25)
            player.take_damage(damage)
            enemy.use_mana(10)
            print(f"🔥 Enemy used Dark Flame for {damage} damage!")

        elif enemy_action_heal == "heal" and enemy.mana >= 15:
            heal_amount = random.randint(10, 20)
            enemy.heal(heal_amount)
            enemy.use_mana(15)
            print(f"👹 Enemy healed {heal_amount} HP!")

# Result
if player.is_alive():
    print("\n🏆 YOU WIN!")
else:
    print("\n💀 YOU LOST!")