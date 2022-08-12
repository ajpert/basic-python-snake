from random import randrange
from turtle import Screen
import pygame
 
pygame.init()

def init_snake():
    for x in locations:
        pygame.draw.rect(dis,black,[x[0],x[1],size_modifier,size_modifier])
 

size_modifier = 10


screen_width = 500
screen_height = 500

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

food_x = 0
food_y = 0

def place_food():
    x_food = randrange(0,screen_width,size_modifier)
    y_food = randrange(0,screen_height,size_modifier)
    ##for x in locations:
        ##if x_food == x[0] and y_food == x[1]:
            ##place_food()
    pygame.draw.rect(dis,red,[x_food,y_food,size_modifier,size_modifier])
    global food_x
    food_x = x_food
    global food_y
    food_y = y_food
    ##print(x_food,y_food)
 

dis = pygame.display.set_mode((screen_width, screen_height))



game_over = False
 
direction = 0 
x1 = randrange(0,screen_width,size_modifier)
y1 = randrange(0,screen_height,size_modifier)

locations = [(x1,y1)]

x1_change = 0       
y1_change = 0

tick = 15.
clock = pygame.time.Clock()
dis.fill(white)

place_food()
init_snake()

def grid():
    for x in range(0, screen_width, size_modifier):
        for y in range(0, screen_height, size_modifier):
            #rect = pygame.Rect(x,y,size_modifier)
            pygame.draw.rect(dis, black, [x,y,size_modifier,size_modifier], 1)

#grid()
while not game_over:
   
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                if direction == pygame.K_RIGHT:
                    x1_change = size_modifier
                    y1_change = 0
                else:
                    x1_change = -size_modifier
                    y1_change = 0
                    direction = event.key
            elif event.key == pygame.K_RIGHT:
                if direction == pygame.K_LEFT:
                    x1_change = -size_modifier
                    y1_change = 0
                else:
                    x1_change = size_modifier
                    y1_change = 0
                    direction = event.key
            elif event.key == pygame.K_UP:
                if direction == pygame.K_DOWN:
                    y1_change = size_modifier
                    x1_change = 0
                else:
                    y1_change = -size_modifier
                    x1_change = 0
                    direction = event.key    
            elif event.key == pygame.K_DOWN: 
                if direction == pygame.K_UP:
                    y1_change = -size_modifier
                    x1_change = 0
                else:
                    y1_change = size_modifier
                    x1_change = 0
                    direction = event.key
         

        
    x1 += x1_change
    y1 += y1_change
    ##print(x1, y1)
    if x1_change != 0 or y1_change != 0:
        if x1 == food_x and y1 == food_y:
            locations.append((locations[-1][0],locations[-1][1]))
            place_food()
            tick += .1
        for x in range(1,len(locations)):
            if (x1,y1) == locations[x]:
                game_over = True 

        if x1 < 0 or x1 >= screen_width:
            game_over = True
        if y1 < 0 or y1 >= screen_height:
            game_over = True
        
           
        
        pygame.draw.rect(dis, black, [x1, y1, size_modifier, size_modifier])
        temp = locations.pop()
        pygame.draw.rect(dis, white, [temp[0], temp[1], size_modifier, size_modifier])
        locations.insert(0,(x1,y1))
    pygame.display.update()
    clock.tick(tick)
    #tick += .1
 
pygame.quit()
quit()


