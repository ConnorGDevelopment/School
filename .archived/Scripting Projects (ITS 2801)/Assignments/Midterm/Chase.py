###  "Chase" mini-game - Midterm Project
#
# - At the start of the game, a number of NPCs are placed at the center of the screen,
#   the number of NPCs is controlled by a constant defined at the top of the script.
# - Each NPC moves at a random speed selected from a range set by another constant
# - Each NPC moves diagonally, the direction (up/left, up/right, down/left, or down/right) is
#   selected at random when each NPC is created, it does not change during the game.
# - When an NPC touches the edge of the screen (defined as the center of the NPC 
#   moving past the x or y coordinate defining the screen edge) it becomes invisible
#   and is no longer updated.
#   This is counted as a MISS.

# - The MC (player character) starts at the bottom of the screen, in the center.
# - The MC is moved by WASD key strokes, at a speed that is based on the top NPC speed
#   multiplied by a constant.
# - When the MC overlaps an NPC (using the colliderect function), the NPC becomes invisible
#   and stops being updated, this is counted as a HIT.
#
######
#
# This file contains the basic starting configuration and game loop we have been using, which
# includes closing the game when the window if closed or the Escape key is pressed.
#
######
# NOTE:  You can use the constants as global variables, but all other information
#        must be passed to functions as parameters and returned via the return statment.
#
#        You must use a class to define the NPCs and handle their functions
#        You must use a class to define all MC related data and functions
#
#        This project has 2 "phases" defined below
#
######  Phase I - submitted on the Sunday before Spring Break
#       Phase I can use a lot of your code from the NPCs (Week 7) project
# - Define a class for your NPCs
# -- The __init__ method contains what we have been doing in the "create" function before
#    Load the image (eye64) and retrieve its rectangle
#    Place the NPC (by placing its rectangle)
#    Select the speed and direction for the NPC
# -- Define an "update" method that takes care of:
#    moving the NPC,
#    determining if it hits the screen edge (in that case make it invisible and increment the MISS counter),
#    putting itself on the screen using the "blit" function (if it is visible)
# NOTE: you are going to need an NPC attribute that determines if the NPC is visible.
# - Before the game loop, create and store the required number of NPC objects (you will need to store them in a variable)
# - In the game loop, call the update method for each NPC
#
###### Phase II - submitted a week after we return from Spring Break (Sunday night)
# Phase II (you can "borrow" code from the "pygame-start" (Week 6) project)
# If you submit any Phase II work in Phase I, I will give you feedback w/o any grading impact
#
# - Define an MC class
# -- The __init__ method contains what we used to do in the "create" function
#    Load the MC image (hood64) and retrieve the rectangle for it
#    Place the rectangle at the starting position
#    Set a speed attribute for the MC
# -- Define a "move" method to:
#    move the MC when the w,a,s, and/or d keys are pressed,
#    check whether the MC has collided with any NPC (colliderect function),
#    set any NPC the MC has collided with to be invisible,
#    Extra credit: Increment a HIT counter
# -- Define an "update" method that displays the MC using "blit"
#
# - Before the game loop, define the MC object
# - In the game loop, call the "move" and "update" methods for the MC
#
# - when the game ends, print at least the MISS counter; print the HIT counter for extra credit
#####
# Extra Credit
#
# - Keep track of a HIT counter and print it at the end of the game
# - Keep track of the number of visible NPCs and end the game when no NPCs are left (visible)
#
from typing import List, Literal
import pygame
import random

## Justification for use of techniques not taught in this course:
# Prior to taking this course, I've worked as a web developer for about 4 years
# Aside from making websites for clients, a lot of my work has been making 'functional' websites meaning websites that just provide a tool for multiple people to access
# The best example I have of this is the site I created when I was playing Diablo Immortal
# I became guild leader of LEATHAL LEGENDS (I didn't name it) and we rose to being one of the top guilds
# Eventually I got to become the server's Immortal (The King of the Hill)
# To keep the throne, there were weekly battles where my guild + 2 allied guilds (300 People total) put up 10 pvp teams of 8 people each
# Those teams then battled against 8 person pvp teams from the top 10 Shadow (Guilds not on the Hill) guilds.
# In order to be effective, I created a website with these features:
#   A database of the top players in each enemy guild
#   A login system for my guild members so they could update enemy stats
#   A database of our guild members
#   An algorithm to make balanced pvp teams from our pool of available players
#   An algorithm to match our strongest teams against the weakest enemy guilds (To keep the throne you had to win X of the ten battles)
# Because of that website, doing my best to be kind, and a lot of good friends; I was able to reign for a total of 8 weeks on the server Meshif
# Since then, no one has ever broken my record on that server. Across all servers globally, only maybe 6 guild leaders have ever tied my record and no one has ever beat it.

# Constants
SPEED_RANGE = (50,200) # each NPC moves at a random speed selected from this range - modify as you see fit
NUM_NPC = 10 # the number of NPCs
MCV = 2 # The speed of the MC is set to the top NPC speed range times this factor - modify as you see fit.
MISS_COUNT = 0
HIT_COUNT = 0

# Initialization
pygame.init()
screen = pygame.display.set_mode((1600,800))
screen_size = screen.get_size()
pygame.display.set_caption(" My Game")  # Replace this with a proper window title
clock = pygame.time.Clock()

class Character:
    def __init__(self, image_path: str, starting: tuple[int, int], velocity: int):
        self.image_path = image_path
        self.image = pygame.image.load(self.image_path)
        
        self.rect = self.image.get_rect()
        self.rect.center = starting
        
        self.velocity = velocity
        
    def show_char(self):
        screen.blit(self.image, self.rect)

    def move_char(self, horizontal: Literal[-1, 0, 1], vertical: Literal[-1, 0, 1], dt):
        self.rect.x = self.rect.x + (dt * self.velocity * horizontal)
        self.rect.y = self.rect.y + (dt * self.velocity * vertical)
        


class NPC(Character):
    def get_random_direction(self, include_zero: bool)-> tuple[int ,int]:
        direction_ints = [-1, 1, 0]
        
        index_max = (len(direction_ints) -1) if include_zero else (len(direction_ints) - 2)
        
        return [
            direction_ints[random.randint(0, index_max)],
            direction_ints[random.randint(0, index_max)]
        ]        
    
    def __init__(self):
        super().__init__("Scripting Projects (ITS 2801)/Assignments/Midterm/Images/eye64.png", [screen_size[0] / 2,screen_size[1] / 2], random.randrange(SPEED_RANGE[0], SPEED_RANGE[1]))
        self.static_direction = self.get_random_direction(False)
        self.is_visible = True
        self.is_hit = False
    
    def is_offscreen(self) -> bool:    
        if(self.rect.center[0] >= screen_size[0]):
            return True
        if(self.rect.center[0] <= 0):
            return True
        if(self.rect.center[1] >= screen_size[1]):
            return True
        if(self.rect.center[1] <= 0):
            return True
        else:
            return False
        
    def check_visible(self) -> bool:
        if(self.is_hit):
            return False
        elif(self.is_offscreen()):
            return False
        else:
            return True
        
    def move_char(self, dt):
        return super().move_char(self.static_direction[0], self.static_direction[1], dt)
    
    def update(self, dt):
        self.move_char(dt)
        if(self.check_visible()):
            return self.show_char()
        else:
            if(self.is_visible & (self.is_hit == False) & self.is_offscreen()):
                self.is_visible = False
                global MISS_COUNT
                MISS_COUNT = MISS_COUNT + 1
            if(self.is_visible & self.is_hit):
                self.is_visible = False
                global HIT_COUNT
                HIT_COUNT = HIT_COUNT + 1
          
class MC(Character):
    def __init__(self):
        # 32 is added to the starting position to make sure the char starts fully on screen
        super().__init__("Scripting Projects (ITS 2801)/Assignments/Midterm/Images/hood64.png", [screen_size[0]/2, screen_size[1] - 32], SPEED_RANGE[1]*1.5)
     
    def move_char(self, keys, dt):
        horizontal = 0
        vertical = 0
        
        if keys[pygame.K_a]:
            horizontal = -1
        if keys[pygame.K_d]:
            horizontal = 1
        if keys[pygame.K_s]:
            vertical = 1
        if keys[pygame.K_w]:
            vertical = -1
            
        super().move_char(horizontal, vertical, dt)
    
    def is_collided(self, npcs: List[NPC]):
        for npc in npcs:
            if self.rect.colliderect(npc.rect):
                npc.is_hit = True
    
    def loopcheck(self):
        if (self.rect.x < 0):
            self.rect.x = screen_size[0]
        if (self.rect.x > screen_size[0]):
            self.rect.x = 0
        if (self.rect.y < 0):
            self.rect.y = screen_size[1]
        if (self.rect.y > screen_size[1]):
            self.rect.y = 0

    def update(self, keys, npcs: List[NPC], dt):
        self.move_char(keys, dt)
        self.loopcheck()
        self.is_collided(npcs)
        self.show_char()
        
            
npcs: List[NPC] = []

for i in range(NUM_NPC):
    npcs.append(NPC())

mc = MC()

running = True
dt = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill("silver")  # Replace this with a more appropriate color (your choice)
    
    def exit_game():
        print(f"Missed: {MISS_COUNT}")
        print(f"Hit: {HIT_COUNT}")
        global running
        running = False
    
    keys = pygame.key.get_pressed() # dictionary of all keys, True = pressed
    
    if keys[pygame.K_ESCAPE]:
        exit_game()
    
    if ((HIT_COUNT + MISS_COUNT) == NUM_NPC):
        exit_game()

    mc.update(keys, npcs, dt)

    for npc in npcs:
        npc.update(dt)

    pygame.display.flip()
    dt = clock.tick(60) / 1000
