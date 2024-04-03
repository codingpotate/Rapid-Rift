import pygame
import os
import random

pygame.init()
pygame.mixer.init()

pygame.display.set_caption("Rapid Rift")
icon = pygame.image.load(os.path.join("Assets/Other", "icon.ico"))
pygame.display.set_icon(icon)
# Global Constants
SCREEN_HEIGHT = 500
SCREEN_WIDTH = 1100
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
death_sound = pygame.mixer.Sound("Assets/Sounds/death_sound.mp3")
supersonic = pygame.mixer.Sound("Assets/Sounds/supersonic.mp3")
death_sound.set_volume(0.3)
pygame.mixer.music.load("Assets/Sounds/music.mp3")
pygame.mixer.music.play(-1)  # -1 means loop indefinitely
pygame.mixer.music.set_volume(0.3)
pygame.mixer.music.pause()  # Pause music initially
jump_sound = pygame.mixer.Sound("Assets/Sounds/jump_sound.mp3")
jump_sound.set_volume(0.2)
intro_sound = pygame.mixer.Sound("Assets/Sounds/Intro.mp3")
intro_sound.set_volume(0.3)
ring_sound = pygame.mixer.Sound("Assets/Sounds/ring.mp3")
ring_sound.set_volume(0.1)
supersonic.set_volume(0.25)

EMERALD = [pygame.image.load(os.path.join("Assets/Other", "Emerald_0.png")),
           pygame.image.load(os.path.join("Assets/Other", "Emerald_1.png")),
           pygame.image.load(os.path.join("Assets/Other", "Emerald_2.png")),
           pygame.image.load(os.path.join("Assets/Other", "Emerald_3.png"))]
EMERALD = [pygame.transform.scale(pygame.image.load(os.path.join("Assets/Other", f"Emerald_{i}.png")),
                                 (int(1.3 * image.get_width()), int(1.3 * image.get_height())))

           for i, image in enumerate(EMERALD, start=0)]
DEATH = [pygame.image.load(os.path.join("Assets/Sonic", "SonicDead.png")),
         pygame.image.load(os.path.join("Assets/Sonic", "SonicDead.png")),
         pygame.image.load(os.path.join("Assets/Sonic", "SonicDead.png")),]
RING = [pygame.image.load(os.path.join("Assets/Other", "Ring_0.png")),
           pygame.image.load(os.path.join("Assets/Other", "Ring_1.png")),
           pygame.image.load(os.path.join("Assets/Other", "Ring_2.png")),
           pygame.image.load(os.path.join("Assets/Other", "Ring_3.png"))]
RUNNING = [pygame.image.load(os.path.join("Assets/Sonic", "SonicRun1.png")),
           pygame.image.load(os.path.join("Assets/Sonic", "SonicRun2.png")),
           pygame.image.load(os.path.join("Assets/Sonic", "SonicRun3.png")),
           pygame.image.load(os.path.join("Assets/Sonic", "SonicRun4.png"))]
JUMPING = [pygame.image.load(os.path.join("Assets/Sonic", "SonicJump.png")),
           pygame.image.load(os.path.join("Assets/Sonic", "SonicJump2.png")),
           pygame.image.load(os.path.join("Assets/Sonic", "SonicJump3.png"))]

DUCKING = [pygame.image.load(os.path.join("Assets/Sonic", "SonicDuck1.png")),
           pygame.image.load(os.path.join("Assets/Sonic", "SonicDuck2.png"))]

SMALL_Badnik = [pygame.image.load(os.path.join("Assets/Badnik", "SmallBadnik1.png")),
                pygame.image.load(os.path.join("Assets/Badnik", "SmallBadnik2.png")),
                pygame.image.load(os.path.join("Assets/Badnik", "SmallBadnik3.png"))]
LARGE_Badnik = [pygame.image.load(os.path.join("Assets/Badnik", "LargeBadnik1.png")),
                pygame.image.load(os.path.join("Assets/Badnik", "LargeBadnik2.png")),
                pygame.image.load(os.path.join("Assets/Badnik", "LargeBadnik3.png"))]

SuperSonic_Running  = [pygame.image.load(os.path.join("Assets/Sonic", "SuperSonicRun1.png")),
           pygame.image.load(os.path.join("Assets/Sonic", "SuperSonicRun2.png")),
           pygame.image.load(os.path.join("Assets/Sonic", "SuperSonicRun3.png")),
           pygame.image.load(os.path.join("Assets/Sonic", "SuperSonicRun4.png"))]
SuperSonic_Running = [pygame.transform.scale(pygame.image.load(os.path.join("Assets/Sonic", f"SuperSonicRun{i}.png")),
                                 (int(1.3 * image.get_width()), int(1.3 * image.get_height())))
           for i, image in enumerate(JUMPING, start=1)]

SuperSonic_Ducking = [pygame.image.load(os.path.join("Assets/Sonic", "SuperSonicDuck1.png")),
           pygame.image.load(os.path.join("Assets/Sonic", "SuperSonicDuck2.png"))]


SuperSonic_Jumping = [pygame.image.load(os.path.join("Assets/Sonic", "SuperSonicJump1.png")),
           pygame.image.load(os.path.join("Assets/Sonic", "SuperSonicJump2.png")),
           pygame.image.load(os.path.join("Assets/Sonic", "SuperSonicJump3.png")),
           pygame.image.load(os.path.join("Assets/Sonic", "SuperSonicJump4.png"))]

SuperSonic_Jumping = [pygame.transform.scale(pygame.image.load(os.path.join("Assets/Sonic", f"SuperSonicJump{i}.png")),
                                 (int(1.8 * image.get_width()), int(1.8 * image.get_height())))
           for i, image in enumerate(JUMPING, start=1)]

EGGMAN = [pygame.image.load(os.path.join("Assets/Eggman", "Eggman1.png")),
          pygame.image.load(os.path.join("Assets/Eggman", "Eggman2.png"))]
EGGMAN = [pygame.transform.scale(pygame.image.load(os.path.join("Assets/Eggman", f"Eggman{i}.png")),
                                 (int(1.4 * image.get_width()), int(1.4 * image.get_height())))
          for i, image in enumerate(EGGMAN, start=1)]

CLOUD = pygame.image.load(os.path.join("Assets/Other", "Cloud.png"))
           
title = pygame.image.load(os.path.join("Assets/Other", "Title.png"))
title = pygame.transform.scale(title, (SCREEN_WIDTH, SCREEN_HEIGHT))

BG = pygame.image.load(os.path.join("Assets/Other", "Track.png"))
WP = pygame.image.load("Assets/Other/your_background.png")

JUMPING = [pygame.transform.scale(pygame.image.load(os.path.join("Assets/Sonic", f"SonicJump{i}.png")),
                                 (int(0.75 * image.get_width()), int(0.75 * image.get_height())))
           for i, image in enumerate(JUMPING, start=1)]

invincibility_timer = 0
invincibility_spawn_time = 20 * 60 

class AnimatedBackground:
    def __init__(self):
        self.frames = [pygame.image.load(os.path.join("Assets/Other", f"Background_{i}.png")) for i in range(3)]
        self.current_frame = 0
        self.image = self.frames[self.current_frame]
        self.image = pygame.transform.scale(self.image, (SCREEN_WIDTH, SCREEN_HEIGHT))
        self.rect = self.image.get_rect()
        self.animation_speed = 5
        self.frame_counter = 0

    def update(self):
        if self.frame_counter % self.animation_speed == 0:
            self.current_frame = (self.current_frame + 1) % len(self.frames)
            self.image = pygame.transform.scale(self.frames[self.current_frame], (SCREEN_WIDTH, SCREEN_HEIGHT))
        self.frame_counter += 1

    def draw(self, screen):
        screen.blit(self.image, self.rect)

background_sprite = AnimatedBackground()

class InvincibilityItem:
    def __init__(self):
        self.x = SCREEN_WIDTH + random.randint(800, 1000)
        self.y = random.randint(200, 200)
        self.frames = EMERALD
        self.current_frame = 0
        self.image = self.frames[self.current_frame]
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.collected = False
        self.rect = self.image.get_rect(topleft=(self.x, self.y))
        self.animation_speed = 5
        self.frame_counter = 0

    def update(self):
        self.x -= game_speed
        self.rect.topleft = (self.x, self.y)
        if self.x < -self.rect.width:
            self.reset_item()

        if self.frame_counter % self.animation_speed == 0:
            self.current_frame = (self.current_frame + 1) % len(self.frames)
            self.image = pygame.transform.scale(self.frames[self.current_frame], (100, 100))
        self.frame_counter += 1

    def reset_item(self):
        self.x = SCREEN_WIDTH + random.randint(9000, 10000)
        self.y = random.randint(200, 200)
        self.collected = False
        self.frame_counter = 0
        
        
    def draw(self, SCREEN):
        if not self.collected:
            SCREEN.blit(self.image, (self.x, self.y))

    def on_collected(self, player):
        self.collected = True
        supersonic.play()
        player.on_invincibility_collected()
# New Ring class definition
class Ring:
    def __init__(self):
        self.x = SCREEN_WIDTH + random.randint(800, 1000)
        self.y = random.randint(300, 300)
        self.frames = RING
        self.current_frame = 0
        self.image = self.frames[self.current_frame]
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.collected = False
        self.rect = self.image.get_rect(topleft=(self.x, self.y))
        self.animation_speed = 5
        self.frame_counter = 0

    def update(self):
        self.x -= game_speed
        self.rect.topleft = (self.x, self.y)
        if self.x < -self.rect.width:
            self.reset_ring()

        if self.frame_counter % self.animation_speed == 0:
            self.current_frame = (self.current_frame + 1) % len(self.frames)
            self.image = pygame.transform.scale(self.frames[self.current_frame], (50, 50))
        self.frame_counter += 1

    def reset_ring(self):
        self.x = SCREEN_WIDTH + random.randint(2500, 3000)
        self.y = random.randint(300, 350)
        self.collected = False
        self.frame_counter = 0

    def draw(self, SCREEN):
        if not self.collected:
            SCREEN.blit(self.image, (self.x, self.y))

    def on_collected(self):
        global points
        if not self.collected:
            self.collected = True
            ring_sound.play()
            points += 100

RING = [pygame.transform.scale(pygame.image.load(os.path.join("Assets/Other", f"Ring_{i}.png")),
                                 (int(0.75 * image.get_width()), int(0.75 * image.get_height())))
           for i, image in enumerate(RING, start=0)]
# New instantiation of Ring in the main function
ring = Ring()
invincibility_item = InvincibilityItem()
class Sonic:
    X_POS = 80
    Y_POS = 310
    Y_POS_DUCK = 340
    JUMP_VEL = 6.9

    def __init__(self):
        self.duck_img = DUCKING
        self.run_img = RUNNING
        self.jump_img = JUMPING
        self.invincible = False
        self.invincibility_duration = 5 * 60  # 5 seconds at 60 frames per second
        self.invincibility_timer = 0

        self.Sonic_duck = False
        self.Sonic_run = True
        self.Sonic_jump = False

        self.step_index = 0
        self.jump_vel = self.JUMP_VEL
        self.image = self.run_img[0]
        self.rect = self.image.get_rect()
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS
        self.jump_frame_index = 0
        self.Sonic_death = False
        self.death_img = DEATH
        self.death_frame_index = 0

    def update(self, userInput):
        if self.Sonic_death:
            self.death()
            return 
        
    def update(self, userInput):
        if self.Sonic_duck:
            self.duck()
        if self.Sonic_run:
            self.run()
        if self.Sonic_jump:
            self.jump()

        if self.step_index >= 10:
            self.step_index = 0

        if pygame.sprite.collide_rect(self, invincibility_item) and not invincibility_item.collected:
            global points
            points += 100
            invincibility_item.collected = True
            ring_sound.play()
            self.on_invincibility_collected()

        self.handle_invincibility()
        pygame.mixer.music.set_volume(0.1)
        if userInput[pygame.K_UP] and not self.Sonic_jump:            
            jump_sound.play()
            self.Sonic_duck = False
            self.Sonic_run = False
            self.Sonic_jump = True
        elif userInput[pygame.K_DOWN] and not self.Sonic_jump:
            self.Sonic_duck = True
            self.Sonic_run = False
            self.Sonic_jump = False
        elif not (self.Sonic_jump or userInput[pygame.K_DOWN]):
            self.Sonic_duck = False
            self.Sonic_run = True
            self.Sonic_jump = False

        # Check for collision with the ring and update score
        if pygame.sprite.collide_rect(self, ring) and not ring.collected:
            
            points += 100
            ring.collected = True
            ring_sound.play()


    def on_invincibility_collected(self):
        self.invincible = True
        self.invincibility_timer = self.invincibility_duration
        self.run_img = SuperSonic_Running
        self.jump_img = SuperSonic_Jumping
        self.duck_img = SuperSonic_Ducking
        

    def handle_invincibility(self):
        if self.invincible:
            self.invincibility_timer -= 1
            if self.invincibility_timer <= 0:
                self.invincible = False
                self.run_img = RUNNING
                self.jump_img = JUMPING
                self.duck_img = DUCKING
                self.image = self.run_img[0]

    def duck(self):
        self.image = self.duck_img[self.step_index // 5]
        self.rect = self.image.get_rect()
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS_DUCK
        self.step_index += 1

    def run(self):
        self.step_index = (self.step_index + 1) % (len(self.run_img) * 5)
        self.image = self.run_img[self.step_index // 4]
        self.rect = self.image.get_rect()
        self.rect.x = self.X_POS
        self.rect.y = self.Y_POS

    def jump(self):
        self.image = self.jump_img[self.jump_frame_index]
        if self.Sonic_jump:
            self.rect.y -= self.jump_vel * 4
            self.jump_vel -= 0.8
            self.jump_frame_index = (self.jump_frame_index + 1) % len(JUMPING)
        if self.jump_vel < -self.JUMP_VEL:
            self.Sonic_jump = False
            self.jump_frame_index = 0
            self.jump_vel = self.JUMP_VEL
            
            

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (self.rect.x, self.rect.y))

    def get_mask(self):
        return pygame.mask.from_surface(self.image)

intro_sound.play()
ring = Ring()

class Cloud:
    def __init__(self):
        self.x = SCREEN_WIDTH + random.randint(800, 1000)
        self.y = random.randint(100, 100)
        self.image = pygame.transform.scale(CLOUD, (50, 30))  # Adjust initial size
        self.width = self.image.get_width()
        self.scale_factor = 4.0  # Set the initial scale factor
        

    def update(self):
        self.x -= game_speed
        if self.x < -self.width:
            self.x = SCREEN_WIDTH + random.randint(2500, 3000)
            self.y = random.randint(50, 100)

    def draw(self, SCREEN):
        # Scale the image before drawing
        scaled_image = pygame.transform.scale(self.image, (int(self.image.get_width() * self.scale_factor),
                                                           int(self.image.get_height() * self.scale_factor)))
        SCREEN.blit(scaled_image, (self.x, self.y))

class Obstacle:
    def __init__(self, image, type):
        self.image = image
        self.type = type
        self.rect = self.image[self.type].get_rect()
        self.rect.x = SCREEN_WIDTH
        self.mask = pygame.mask.from_surface(self.image[self.type])

    def update(self):
        self.rect.x -= game_speed
        if self.rect.x < -self.rect.width:
            obstacles.pop()

    def draw(self, SCREEN):
        SCREEN.blit(self.image[self.type], self.rect)

class SmallBadnik(Obstacle):
    def __init__(self, image):
        self.type = random.randint(0, 2)
        super().__init__(image, self.type)
        self.rect.y = 325

class LargeBadnik(Obstacle):
    def __init__(self, image):
        self.type = random.randint(0, 2)
        super().__init__(image, self.type)
        self.rect.y = 300

class Eggman(Obstacle):
    def __init__(self, image):
        self.type = 0
        super().__init__(image, self.type)
        self.rect.y = 250
        self.index = 0

    def draw(self, SCREEN):
        if self.index >= 9:
            self.index = 0
        SCREEN.blit(self.image[self.index // 5], self.rect)
        self.index += 1

def main():
    global game_speed, x_pos_bg, y_pos_bg, points, obstacles, ring, background_sprite, invincibility_item, invincibility_timer
    run = True
    clock = pygame.time.Clock()
    player = Sonic()
    cloud = Cloud()
    game_speed = 20
    x_pos_bg = 0
    y_pos_bg = 380
    points = 0
    font = pygame.font.Font('freesansbold.ttf', 20)
    obstacles = []
    death_count = 0
    invincibility_timer = 0
    invincibility_spawn_interval = 20 * 60  # 20 seconds * 60 frames per second
    last_invincibility_time = pygame.time.get_ticks()

    ring = Ring()  # Create a new Ring instance
    invincibility_item = InvincibilityItem() 

    def set_scale_factor(self, scale_factor):
        self.scale_factor = scale_factor

    def score():
        global points, game_speed
        points += 1
        if points % 100 == 0:
            game_speed += 1
        if points % 1000 == 0:
            invincibility_item.reset_item()

        text = font.render("Points: " + str(points), True, (0, 0, 0))
        textRect = text.get_rect()
        textRect.center = (1000, 40)
        SCREEN.blit(text, textRect)

    def background():
        global x_pos_bg, y_pos_bg
        image_width = BG.get_width()
        SCREEN.blit(BG, (x_pos_bg, y_pos_bg))
        SCREEN.blit(BG, (image_width + x_pos_bg, y_pos_bg))
        x_pos_bg -= game_speed
        if x_pos_bg <= -image_width:
            x_pos_bg = 0

    while run:
        current_time = pygame.time.get_ticks()
        elapsed_time = current_time - last_invincibility_time

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        pygame.mixer.music.unpause()
        SCREEN.blit(WP, (0, 0))
        userInput = pygame.key.get_pressed()

        background_sprite.update()
        background_sprite.draw(SCREEN)
        player.handle_invincibility()

        player.draw(SCREEN)
        player.update(userInput)

        ring.update()
        ring.draw(SCREEN)
        
        invincibility_timer += 1
        if invincibility_timer >= invincibility_spawn_interval:
            invincibility_item.reset_item()
            invincibility_timer = 0
            last_invincibility_time = current_time  # Update the last invincibility time

        invincibility_item.update()
        invincibility_item.draw(SCREEN)

        if len(obstacles) == 0:
            if random.randint(0, 2) == 0:
                obstacles.append(SmallBadnik(SMALL_Badnik))
            elif random.randint(0, 2) == 1:
                obstacles.append(LargeBadnik(LARGE_Badnik))
            elif random.randint(0, 2) == 2:
                obstacles.append(Eggman(EGGMAN))

        for obstacle in obstacles:
            obstacle.draw(SCREEN)
            obstacle.update()
            if player.invincible:
                continue
            # Check for pixel-perfect collision
            if pygame.sprite.collide_mask(player, obstacle):
                death_sound.play()
                pygame.time.delay(500)
                death_count += 1
                menu(death_count)

        background()
        cloud.draw(SCREEN)
        cloud.update()

        score()

        clock.tick(30)
        pygame.display.update()

        # Check for collision with the ring and update score
        if pygame.sprite.collide_rect(player, ring) and not ring.collected:
            ring.on_collected()

        # Check for collision with invincibility item and update player state
        if pygame.sprite.collide_rect(player, invincibility_item) and not invincibility_item.collected:
            invincibility_item.on_collected(player)

    pygame.quit()

# Define button images and rects
button_width = 100  # Width of the buttons
button_height = 100  # Height of the buttons

restart_button = pygame.image.load("Assets/Other/restart_button.png")
close_button = pygame.image.load("Assets/Other/close_button.png")

restart_button = pygame.transform.scale(restart_button, (button_width, button_height))
close_button = pygame.transform.scale(close_button, (button_width, button_height))

button_spacing = 30  # Space between the buttons

restart_button_rect = restart_button.get_rect()
restart_button_rect.center = (SCREEN_WIDTH // 10, SCREEN_HEIGHT // 5 - button_spacing)

close_button_rect = close_button.get_rect()
close_button_rect.center = (SCREEN_WIDTH // 10, SCREEN_HEIGHT // 2 + button_height + button_spacing)

def menu(death_count):
    global points
    run = True
    while run:
        SCREEN.fill((255, 255, 255))
        SCREEN.blit(title, (0,0))
        font = pygame.font.Font('freesansbold.ttf', 30)

        if death_count == 0:
            text = font.render("     ", True, (0, 0, 0))
        elif death_count > 0:
            pygame.mixer.music.pause()
            text = font.render("Thank you for Playing!", True, (255, 165, 0))
            score = font.render("Your Score: " + str(points), True, (255, 0, 0))
            scoreRect = score.get_rect()
            scoreRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 2 + button_spacing)
            SCREEN.blit(score, scoreRect)

        # Draw buttons
        SCREEN.blit(restart_button, restart_button_rect)
        SCREEN.blit(close_button, close_button_rect)

        textRect = text.get_rect()
        textRect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        SCREEN.blit(text, textRect)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        # Check for mouse click
        if pygame.mouse.get_pressed()[0]:
            mouse_pos = pygame.mouse.get_pos()
            if restart_button_rect.collidepoint(mouse_pos):
                main()  # Restart the game
            elif close_button_rect.collidepoint(mouse_pos):
                pygame.quit()  # Close the game

menu(death_count=0)