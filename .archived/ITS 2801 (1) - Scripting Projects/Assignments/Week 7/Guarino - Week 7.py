####  PLEASE NOTE CAREFULLY:
# You will complete this project using an approach that is not very efficient.
# The point is to set the script up in this (inefficient) way once, and next week
#  transition to the better way of solving the problem.
# You are NOT to use class definitions in this submission (we will get there next week), even
#  though Google and your favorite chatbot will tell you to do so.
# One exception: if you have practiced defining custom classes in python in a previous COURSE
#  you are free to go that route (using a class definition).
#  *** YOU MUST PUT A NOTE AT THE TOP OF THE SCRIPT IDENTIFYING THAT COURSE ***
####
#
# Requirements:
# - Display three (3) NPCs using the "eye64.png" image
# - Each NPC starts at y=100 near the top of the screen
# - Each NPC starts at a random x coordinate which must be inside the screen (visible)
# - During each frame, each NPC moves down by a random amount
# ---
# - You must write functions (most likely 3 of them) to create the initial NPCs and
#   call these functions before the game loop starts
# - You must write functions (again most likely 3) to update each NPC by moving is
#   a random amount and displaying it. You must call these functions in the game loop
# ---
# Extra Credit
# When an NPC hits the bottom of the screen, have it "loop around", 
#         i.e. appear at the top of the screen
#
# ***
# Some hints/resources: You will find examples of pretty much everything you need in 
# - the last project (even the starting point)
# - The "Agenda" aka the class notes
# - The files in the Demos folder (especially "blink_squares.py")
######

# I've worked as a programmer since 2018-ish and have a small Web Dev company with two friends
# I've worked extensively with classes, mostly in Typescript but more recently started working on a DND project in C#
# I hope that my experience is a sufficient substitute for taking a Python course, I also found it difficult to unlearn the idea of classes for this assignment.

from enum import Enum
from typing import List
import pygame
import random

# Write your functions here

pygame.init()
screen = pygame.display.set_mode((1600,800))
screen_size = screen.get_size()
pygame.display.set_caption("NPCs")
clock = pygame.time.Clock()

# Call your functions that create the NPCs here

# I did have to google how to write Enums in Python
# I want to restrict the direction parameter of my move_char_manual function
# But Python doesn't let you make Union types like Typescript
# So I'm doing what I would do in C#

# In Typescript, I would normally do
#   type directions = 'Up' | 'Down' | 'Left' | 'Right'
# In C#, I would do
#   enum Directions {Up, Down, Left, Right}

Directions = Enum('Directions', ['Up', 'Down', 'Left', 'Right'])

class NPC:
    # Pulled from past weeks
    def __init__(self, image_path, velocity):
        self.image_path = image_path
        self.image = pygame.image.load(self.image_path)
        self.rect = self.image.get_rect()
        # I had to google what function in random did this, but I kind of assumed it existed
        self.rect.center = (random.randrange(0, screen_size[0]), 100)
        
        self.velocity = velocity
    
    # Pulled from past weeks
    def show_char(self):
        screen.blit(self.image, self.rect)
        
    # Pulled from past weeks
    # Unnecessary, I just used this in dev to make sure I had movement working correctly
    def move_char(self, keys, dt):
        if keys[pygame.K_w]:
            self.rect.y -= dt * self.velocity
        if keys[pygame.K_s]:
            self.rect.y += dt * self.velocity
        if keys[pygame.K_a]:
            self.rect.x -= dt * self.velocity
        if keys[pygame.K_d]:
            self.rect.x += dt * self.velocity
    
    def move_char_manual(self, direction: Directions, distance: int):
        self.move_char_loopcheck(direction, distance)
        
        if direction == "Up":
            self.rect.y -= distance
        if direction == "Down":
            self.rect.y += distance
        if direction == "Left":
            self.rect.x -= distance
        if direction == "Right":
            self.rect.x += distance
            
    # Checks if the amount of distance to move exceeds the edges of the screen
    # I did all four directions because OCD + ADHD
    def move_char_loopcheck(self, direction: Directions, distance: int):
        if (direction == "Up") & (self.rect.top + distance < 0):
            self.rect.y = screen_size[1]
        if (direction == "Down") & (self.rect.bottom + distance > screen_size[1]):
            self.rect.y = 0
        if (direction == "Left") & (self.rect.left + distance < 0):
            self.rect.x = screen_size[0]
        if (direction == "Right") & (self.rect.right + distance > screen_size[0]):
            self.rect.x = 0
    
    
            
IMAGE_FOLDER = "Scripting Projects (ITS 2801)/Assignments/Week 7/Images/"

running = True
dt = 0

# I originally did npc_1, npc_2, npc_3 but that felt gross
npc_count = 3

# I did have to google how to annotate the type here because Python didn't know the type when I was iterating through the loop
npcs: List[NPC] = [] 

for i in range(npc_count):
    npcs.append(NPC(IMAGE_FOLDER + "hood64.png", 300))

# Sets the direction the mob of npcs moves in
designated_direction: Directions = "Down"

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill("silver")
    
    # Only used in fun code
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_ESCAPE]:
        running = False    

    # Call your functions that update the NPCs here

    # If you uncomment this, you can change the direction the mob moves in with WASD
    # if keys[pygame.K_w]:
    #     designated_direction = "Up"
    # if keys[pygame.K_s]:
    #     designated_direction = "Down"
    # if keys[pygame.K_a]:
    #     designated_direction = "Left"
    # if keys[pygame.K_d]:
    #     designated_direction = "Right"

    for npc in npcs:    
        npc.move_char_manual(designated_direction, random.random() * 10)
        npc.show_char()
    
    pygame.display.flip()
    dt = clock.tick(60) / 1000
