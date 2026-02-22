import pygame
import random
import math

# --- YOUR CHARACTER CLASS (Unchanged) ---
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


# --- PARTICLE SYSTEM ---
class Particle:
    def __init__(self, x, y, vx, vy, color, lifetime):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.color = color
        self.lifetime = lifetime
        self.max_lifetime = lifetime
        self.size = 5

    def update(self):
        self.x += self.vx
        self.y += self.vy
        self.vy += 0.2  # gravity
        self.lifetime -= 1

    def draw(self, surface):
        alpha = int(255 * (self.lifetime / self.max_lifetime))
        color = tuple(int(c * (self.lifetime / self.max_lifetime)) for c in self.color)
        pygame.draw.circle(surface, color, (int(self.x), int(self.y)), self.size)

    def is_alive(self):
        return self.lifetime > 0

particles = []

def create_particles(x, y, color, count=10):
    for _ in range(count):
        angle = random.uniform(0, 2 * math.pi)
        speed = random.uniform(2, 6)
        vx = math.cos(angle) * speed
        vy = math.sin(angle) * speed - 2
        particles.append(Particle(x, y, vx, vy, color, 30))

def draw_castle_background(surface):
    """Draw a dark castle-themed background"""
    # Dark gradient sky
    for y in range(HEIGHT):
        ratio = y / HEIGHT
        r = int(20 + ratio * 40)
        g = int(15 + ratio * 35)
        b = int(30 + ratio * 50)
        pygame.draw.line(surface, (r, g, b), (0, y), (WIDTH, y))
    
    # Castle towers (left)
    pygame.draw.polygon(surface, (40, 35, 50), [(0, 200), (80, 100), (160, 200)])
    pygame.draw.rect(surface, (50, 45, 60), (20, 200, 120, 400))
    
    # Castle towers (right)
    pygame.draw.polygon(surface, (40, 35, 50), [(WIDTH, 200), (WIDTH-80, 100), (WIDTH-160, 200)])
    pygame.draw.rect(surface, (50, 45, 60), (WIDTH-140, 200, 120, 400))
    
    # Castle walls (middle)
    pygame.draw.rect(surface, (45, 40, 55), (140, 250, WIDTH-280, 350))
    
    # Castle crenellations
    for x in range(150, WIDTH-140, 40):
        pygame.draw.rect(surface, (60, 50, 70), (x, 250, 25, 30))
    
    # Ground
    pygame.draw.rect(surface, (20, 25, 30), (0, HEIGHT-80, WIDTH, 80))
    
    # Trees (dark spooky)
    for x_pos in [100, 300, 700]:
        draw_tree(surface, x_pos, HEIGHT-150)
    
    # Moon glow effect
    pygame.draw.circle(surface, (220, 220, 150), (WIDTH-80, 80), 40)
    pygame.draw.circle(surface, (180, 180, 100), (WIDTH-80, 80), 42, 2)

def draw_tree(surface, x, y):
    """Draw a spooky tree"""
    # Trunk
    pygame.draw.rect(surface, (40, 30, 20), (x-8, y, 16, 100))
    
    # Branches (twisted)
    points = [
        (x, y),
        (x-30, y+20),
        (x-25, y+40),
        (x-40, y+50),
        (x, y+60),
        (x+40, y+50),
        (x+25, y+40),
        (x+30, y+20),
    ]
    pygame.draw.polygon(surface, (30, 60, 20), points)
    
    # Smaller top
    top_points = [
        (x, y-20),
        (x-20, y),
        (x+20, y),
    ]
    pygame.draw.polygon(surface, (25, 50, 15), top_points)

def draw_character_detailed(surface, x, y, is_player):
    """Draw a more detailed character representation"""
    if is_player:
        # Player - Knight with shield
        # Body
        pygame.draw.rect(surface, (100, 100, 150), (x+15, y+40, 70, 80), 0)
        # Head
        pygame.draw.circle(surface, (200, 180, 160), (x+50, y+30), 15)
        # Shield
        pygame.draw.polygon(surface, (200, 100, 0), [(x+10, y+50), (x, y+80), (x+20, y+100), (x+30, y+90)])
        # Sword
        pygame.draw.line(surface, (150, 150, 150), (x+80, y+50), (x+95, y+10), 4)
    else:
        # Enemy - Dark Knight
        # Body
        pygame.draw.rect(surface, (60, 20, 30), (x+15, y+40, 70, 80), 0)
        # Head (skull-like)
        pygame.draw.circle(surface, (80, 60, 70), (x+50, y+30), 15)
        # Eye glow
        pygame.draw.circle(surface, (255, 100, 100), (x+45, y+28), 3)
        pygame.draw.circle(surface, (255, 100, 100), (x+55, y+28), 3)
        # Sword (dark)
        pygame.draw.line(surface, (80, 20, 20), (x+80, y+50), (x+95, y+10), 4)

def draw_damage_numbers(surface, x, y, damage, is_critical=False):
    """Display floating damage numbers"""
    font_dmg = pygame.font.SysFont("Arial", 32, bold=True)
    color = (255, 50, 50) if not is_critical else (255, 200, 0)
    text = font_dmg.render(str(damage), True, color)
    surface.blit(text, (x, y))


# --- PYGAME SETUP ---
pygame.init()

# Screen dimensions and colors
WIDTH, HEIGHT = 1000, 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("⚔️ DARK CASTLE RPG ⚔️")

# Dark theme colors
BG_DARK = (15, 15, 25)
CASTLE_STONE = (50, 45, 60)
GOLD = (220, 180, 80)
DARK_RED = (150, 30, 50)
SHADOW_BLUE = (100, 120, 180)
TEXT_LIGHT = (220, 220, 220)

font = pygame.font.SysFont("Georgia", 20)
large_font = pygame.font.SysFont("Georgia", 40, bold=True)

# Create Characters
player = Character("Knight", 120, 50)
enemy = Character("Shadow Knight", 120, 40)

# Game Variables
game_log = ["⚔️ Battle Start! Press 1 (Slash), 2 (Fire), 3 (Heal), 4 (Dodge)"]
game_over = False
frame_count = 0

def draw_bar(surface, x, y, width, height, current, maximum, color, label):
    # Draw background bar (dark)
    pygame.draw.rect(surface, (40, 40, 50), (x, y, width, height))
    # Draw current stat bar
    ratio = max(0, current / maximum)
    pygame.draw.rect(surface, color, (x, y, width * ratio, height))
    # Draw outline (gold)
    pygame.draw.rect(surface, GOLD, (x, y, width, height), 2)
    # Label
    label_text = font.render(f"{label}: {int(current)}/{int(maximum)}", True, TEXT_LIGHT)
    surface.blit(label_text, (x - 10, y - 25))

def handle_combat(player_action):
    global game_log, game_over
    
    enemy_action = enemy_ai(enemy)
    game_log.append(f"👹 Enemy: {enemy_action.upper()}")

    if player_action == enemy_action:
        game_log.append("💥 Both used same move!")
        create_particles(WIDTH//2, HEIGHT//2, (255, 150, 0), 20)
        return

    player_dodged = False
    enemy_dodged = False

    # Dodge Logic
    if player_action == "dodge" and enemy_action in ["slash", "fire"]:
        player_dodged = True
        player.gain_mana(10)
        game_log.append("😎 You dodged perfectly!")
        create_particles(200, 300, (100, 200, 255), 15)

    if enemy_action == "dodge" and player_action in ["slash", "fire"]:
        enemy_dodged = True
        enemy.gain_mana(10)
        game_log.append("👻 Enemy dodged!")

    # Player Turn
    if not enemy_dodged:
        if player_action == "slash":
            damage = random.randint(10, 20)
            enemy.take_damage(damage)
            game_log.append(f"🗡️ Slash: -{damage} HP!")
            create_particles(750, 300, (200, 50, 50), 12)
        elif player_action == "fire" and player.mana >= 10:
            damage = random.randint(20, 30)
            enemy.take_damage(damage)
            player.use_mana(10)
            game_log.append(f"🔥 Fireball: -{damage} HP!")
            create_particles(750, 300, (255, 100, 0), 20)
        elif player_action == "heal" and player.mana >= 15:
            heal_amount = random.randint(15, 25)
            player.heal(heal_amount)
            player.use_mana(15)
            game_log.append(f"🧪 Healed +{heal_amount} HP!")
            create_particles(200, 300, (100, 255, 100), 15)
        elif player_action in ["fire", "heal"]:
            game_log.append("❌ Not enough mana!")

    # Enemy Turn
    if not player_dodged and enemy.is_alive():
        if enemy_action == "slash":
            damage = random.randint(8, 18)
            player.take_damage(damage)
            game_log.append(f"⚔️ Enemy Slash: -{damage} HP!")
            create_particles(200, 300, (255, 50, 50), 12)
        elif enemy_action == "fire":
            damage = random.randint(15, 25)
            player.take_damage(damage)
            enemy.use_mana(10)
            game_log.append(f"🔥 Dark Flame: -{damage} HP!")
            create_particles(200, 300, (255, 100, 0), 20)
        elif enemy_action == "heal":
            heal_amount = random.randint(10, 20)
            enemy.heal(heal_amount)
            enemy.use_mana(15)
            game_log.append(f"👹 Enemy healed +{heal_amount} HP!")
            create_particles(750, 300, (100, 100, 255), 15)

    # Keep log short
    if len(game_log) > 7:
        game_log = game_log[-7:]

    # Check Game Over
    if not player.is_alive() or not enemy.is_alive():
        game_over = True

# --- MAIN GAME LOOP ---
running = True
clock = pygame.time.Clock()

while running:
    clock.tick(60)  # 60 FPS
    frame_count += 1

    # 1. Event Handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN and not game_over:
            if event.key == pygame.K_1:
                handle_combat("slash")
            elif event.key == pygame.K_2:
                handle_combat("fire")
            elif event.key == pygame.K_3:
                handle_combat("heal")
            elif event.key == pygame.K_4:
                handle_combat("dodge")

    # Update particles
    particles[:] = [p for p in particles if p.is_alive()]
    for p in particles:
        p.update()

    # 2. Draw Background
    draw_castle_background(screen)

    # 3. Draw Characters (Enhanced)
    draw_character_detailed(screen, 100, 150, True)
    draw_character_detailed(screen, 750, 150, False)

    # 4. Draw Particles
    for p in particles:
        p.draw(screen)

    # 5. Draw Character Names & HP/Mana
    screen.blit(large_font.render("⚔️ " + player.name, True, SHADOW_BLUE), (100, 80))
    screen.blit(large_font.render(enemy.name + " 👹", True, DARK_RED), (700, 80))

    # 6. Draw Health & Mana Bars
    draw_bar(screen, 100, 120, 180, 20, player.hp, player.max_hp, (50, 255, 50), "HP")
    draw_bar(screen, 100, 160, 180, 20, player.mana, player.max_mana, SHADOW_BLUE, "Mana")
    
    draw_bar(screen, 720, 120, 180, 20, enemy.hp, enemy.max_hp, (50, 255, 50), "HP")
    draw_bar(screen, 720, 160, 180, 20, enemy.mana, enemy.max_mana, SHADOW_BLUE, "Mana")

    # 7. Draw Combat Log (with dark background panel)
    log_panel = pygame.Surface((WIDTH - 40, 180))
    log_panel.set_alpha(200)
    log_panel.fill((20, 20, 35))
    screen.blit(log_panel, (20, HEIGHT - 220))
    pygame.draw.rect(screen, GOLD, (20, HEIGHT - 220, WIDTH - 40, 180), 2)

    for i, message in enumerate(game_log):
        text = font.render(message, True, TEXT_LIGHT)
        screen.blit(text, (40, HEIGHT - 200 + (i * 25)))

    # 8. Draw Menu
    menu_panel = pygame.Surface((WIDTH - 40, 50))
    menu_panel.set_alpha(200)
    menu_panel.fill((20, 20, 35))
    screen.blit(menu_panel, (20, HEIGHT - 60))
    pygame.draw.rect(screen, GOLD, (20, HEIGHT - 60, WIDTH - 40, 50), 2)

    menu_text = "🗡️ [1] Slash  |  🔥 [2] Fire (10m)  |  🧪 [3] Heal (15m)  |  🛡️ [4] Dodge"
    menu_render = font.render(menu_text, True, TEXT_LIGHT)
    screen.blit(menu_render, (40, HEIGHT - 48))

    # 9. Draw Win/Loss Message
    if game_over:
        # Semi-transparent overlay
        overlay = pygame.Surface((WIDTH, HEIGHT))
        overlay.set_alpha(150)
        overlay.fill((0, 0, 0))
        screen.blit(overlay, (0, 0))
        
        if player.is_alive():
            end_text = large_font.render("🏆 VICTORY! 🏆", True, GOLD)
            screen.blit(end_text, (WIDTH//2 - 200, HEIGHT//2 - 50))
        else:
            end_text = large_font.render("💀 DEFEATED 💀", True, DARK_RED)
            screen.blit(end_text, (WIDTH//2 - 220, HEIGHT//2 - 50))

    # Update the display
    pygame.display.flip()

pygame.quit()