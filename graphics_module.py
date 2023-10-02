import pygame
import random
import time
#Used for all graphics except the main character for right now
#main character doesn't change as of right now I will incoorporate later
# what will go here is the HUD of abilities and health etc
# a function for determining enemy imagry
#

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (150, 150, 150)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN1 =(25, 71, 14)
BROWN = (54, 27, 1)

# Load custom font (place your font file in the same directory)
pygame.init()
pygame.font.init()
image_size = (50, 50)
grid_size = 14
#fonts
custom_font = pygame.font.Font(r"C:\Users\danha\OneDrive\Desktop\programming\rpggame\potential-potato\placeholder graphics\WELLSLEY.TTF", 20)  # Replace with your font file
custom_font2 = pygame.font.Font(r"C:\Users\danha\OneDrive\Desktop\programming\rpggame\potential-potato\placeholder graphics\WELLSLEY.TTF", 48)  # Replace with your font file
custom_font2_outer = pygame.font.Font(r"C:\Users\danha\OneDrive\Desktop\programming\rpggame\potential-potato\placeholder graphics\WELLSLEY.TTF", 51) 
terminal_font = pygame.font.Font(r"C:\Users\danha\OneDrive\Desktop\programming\rpggame\potential-potato\placeholder graphics\PR Viking.ttf", 14)
#infobars
sealO= pygame.image.load(r"C:\Users\danha\OneDrive\Desktop\programming\rpggame\potential-potato\placeholder graphics\level_seal.png")
seal= pygame.transform.scale(sealO, (85,85))
terminal_barO = pygame.image.load(r"C:\Users\danha\OneDrive\Desktop\programming\rpggame\potential-potato\placeholder graphics\terminal_box.png")
InfobarO = pygame.image.load(r"C:\Users\danha\OneDrive\Desktop\programming\rpggame\potential-potato\placeholder graphics\player_info_box.png")
#player
fpimage = pygame.image.load(r"C:\Users\danha\OneDrive\Desktop\programming\rpggame\potential-potato\placeholder graphics\character_forward.png")
bpimage = pygame.image.load(r"C:\Users\danha\OneDrive\Desktop\programming\rpggame\potential-potato\placeholder graphics\character_back.png")
rpimage = pygame.image.load(r"C:\Users\danha\OneDrive\Desktop\programming\rpggame\potential-potato\placeholder graphics\character_right.png")
lpimage = pygame.image.load(r"C:\Users\danha\OneDrive\Desktop\programming\rpggame\potential-potato\placeholder graphics\character_left.png")
player_graphic =[fpimage,bpimage,rpimage,lpimage]

#enemies
wolves_frontO = pygame.image.load(r"C:\Users\danha\OneDrive\Desktop\programming\rpggame\potential-potato\placeholder graphics\wolf_forward.png")
wolves_backO = pygame.image.load(r"C:\Users\danha\OneDrive\Desktop\programming\rpggame\potential-potato\placeholder graphics\wolf_back.png")
wolves_rightO = pygame.image.load(r"C:\Users\danha\OneDrive\Desktop\programming\rpggame\potential-potato\placeholder graphics\wolf_right.png")
wolves_leftO = pygame.image.load(r"C:\Users\danha\OneDrive\Desktop\programming\rpggame\potential-potato\placeholder graphics\wolf_left.png") 
wolves = [wolves_frontO,wolves_backO,wolves_rightO,wolves_leftO]
#obstacles
customsize3 = (50, 70)
tree1O = pygame.image.load(r"C:\Users\danha\OneDrive\Desktop\programming\rpggame\potential-potato\placeholder graphics\tree.png")
tree1 = pygame.transform.scale(tree1O,image_size)
tree2O = pygame.image.load(r"C:\Users\danha\OneDrive\Desktop\programming\rpggame\potential-potato\placeholder graphics\pine_tree.png")
tree2 = pygame.transform.scale(tree2O,customsize3)
customsize2 = (45,35)
customsize4 = (25,25)
#rock1O = pygame.image.load(r"C:\Users\danha\OneDrive\Desktop\programming\rpggame\potential-potato\placeholder graphics\moss_rock.png")
#rock1 = pygame.transform.scale(rock1O,customsize2)
rock2O = pygame.image.load(r"C:\Users\danha\OneDrive\Desktop\programming\rpggame\potential-potato\placeholder graphics\stone 2.png")
rock2 = pygame.transform.scale(rock2O,customsize2)
logO = pygame.image.load(r"C:\Users\danha\OneDrive\Desktop\programming\rpggame\potential-potato\placeholder graphics\log.png")
log = pygame.transform.scale(logO,customsize4)
stumpO = pygame.image.load(r"C:\Users\danha\OneDrive\Desktop\programming\rpggame\potential-potato\placeholder graphics\stump.png")
stump= pygame.transform.scale(stumpO,customsize2)
mapleO = pygame.image.load(r"C:\Users\danha\OneDrive\Desktop\programming\rpggame\potential-potato\placeholder graphics\maple.png")
maple = pygame.transform.scale(mapleO,customsize3)
forest_obstacles = [tree1,maple,tree2,log,stump,rock2]

#background and gameboards tiles
customsize = (80,80)
grass_floor3O = pygame.image.load(r"C:\Users\danha\OneDrive\Desktop\programming\rpggame\potential-potato\placeholder graphics\Grass_1.png")
grass_floor3 = pygame.transform.scale(grass_floor3O,customsize)
grass_floor1O = pygame.image.load(r"C:\Users\danha\OneDrive\Desktop\programming\rpggame\potential-potato\placeholder graphics\Grass_2.png")
grass_floor1= pygame.transform.scale(grass_floor1O,customsize)
grass_floor2O = pygame.image.load(r"C:\Users\danha\OneDrive\Desktop\programming\rpggame\potential-potato\placeholder graphics\grass floor.png")
forest_backgroundO = pygame.image.load(r"C:\Users\danha\OneDrive\Desktop\programming\rpggame\potential-potato\placeholder graphics\Forest_Borders_PNG_Images___Forest__Trees__Rectangle_PNG_Transparent_Background_-_Pngtree-removebg-preview.png")
customsizeback = (830,800)
forest_background = pygame.transform.smoothscale(forest_backgroundO,customsizeback)
grass_floor2 = pygame.transform.scale(grass_floor2O,customsize)
#abilities
sword = pygame.image.load(r"C:\Users\danha\OneDrive\Desktop\programming\rpggame\potential-potato\placeholder graphics\sword.png")
woosh = pygame.image.load(r"C:\Users\danha\OneDrive\Desktop\programming\rpggame\potential-potato\placeholder graphics\woosh.png")
healring = pygame.image.load(r"C:\Users\danha\OneDrive\Desktop\programming\rpggame\potential-potato\placeholder graphics\healing.png")
semetricheart = pygame.image.load(r"C:\Users\danha\OneDrive\Desktop\programming\rpggame\potential-potato\placeholder graphics\symetricheart.png")
growingheart = pygame.image.load(r"C:\Users\danha\OneDrive\Desktop\programming\rpggame\potential-potato\placeholder graphics\growingheart.png")
def draw_player_info(screen, name, level, currenthp, attk, ar, acc, actions, status, ability1, ability2, ability3, ability4, ability5, ability6, ability7, ability8, ability9, ability10): #add abilities later
    size = (275,560)   #screen.get_width())    
    location = (835,5)
    Infobar =  pygame.transform.smoothscale(InfobarO,size)
    screen.blit(Infobar, location)
    size2 = (345,210)
    location2 = (775,565)
    terminal_bar = pygame.transform.smoothscale(terminal_barO,size2)
    screen.blit(terminal_bar, location2)
    screen.blit(seal, (930,65))
    lvl_outer = custom_font2_outer.render(f"{level}" , True, RED)
    lvl = custom_font2.render(f"{level}" , True, BLACK)
    screen.blit(lvl_outer,(965,75))
    screen.blit(lvl, (965, 75))
    
    player_attributes = [name, currenthp, attk, ar, acc, actions, status, ability1, ability3, ability5, ability7, ability9]
    for attribute in player_attributes:
        stat = custom_font.render(attribute, True, BLACK)
        stat2 = custom_font.render(attribute, True, WHITE)
        screen.blit(stat2, (889, 136 + player_attributes.index(attribute)*29))
        screen.blit(stat, (890, 135 + player_attributes.index(attribute)*29))

    abilities_cont = [ability2,ability4,ability6,ability8,ability10]
    for ability in abilities_cont:
        statA = custom_font.render(ability, True, BLACK)
        stat2A = custom_font.render(ability, True, WHITE)
        screen.blit(stat2A, (984, 356 + abilities_cont.index(ability)*29))
        screen.blit(statA, (985, 355 + abilities_cont.index(ability)*29))

    pygame.display.flip()
  
    

   

   
    # Draw other player information text here
def graphic_dictionary(name):
      if name == "player":
           return player_graphic
      if name == "wolf":
            return wolves
      if name == "forest": #add random choice piece for dirrent trees 
            #forest_obstacles = ["tree1", "maple", "tree2", "log", "stump", "rock2"]    
            weights = [0.30, 0.25, 0.25, 0.05, 0.05, 0.10]
            forest = random.choices(forest_obstacles, weights, k=1)[0]
            return forest
      
      
def determine_graphic(screen, graphic, position, location):
                       #front back right left
                image_size = (40, 50)
                image_reset = (0,0)
                if position == "back":
                    fpimageS = pygame.transform.scale(graphic[0],image_reset)
                    bpimageS = pygame.transform.scale(graphic[1],image_size)
                    rpimageS = pygame.transform.scale(graphic[2],image_reset)
                    lpimageS = pygame.transform.scale(graphic[3],image_reset)
                    screen.blit(bpimageS, location) 
                    pygame.display.flip()
                elif position == "forward":
                    fpimageS = pygame.transform.scale(graphic[0],image_size)
                    bpimageS = pygame.transform.scale(graphic[1],image_reset)
                    rpimageS = pygame.transform.scale(graphic[2],image_reset)
                    lpimageS = pygame.transform.scale(graphic[3],image_reset)
                    screen.blit(fpimageS, location)
                    pygame.display.flip()
                elif position == "left":
                    fpimageS = pygame.transform.scale(graphic[0],image_reset)
                    bpimageS = pygame.transform.scale(graphic[1],image_reset)
                    rpimageS = pygame.transform.scale(graphic[2],image_reset)
                    lpimageS = pygame.transform.scale(graphic[3],image_size)
                    screen.blit(lpimageS, location)
                    pygame.display.flip()
                elif position == "right":
                    fpimageS = pygame.transform.scale(graphic[0],image_reset)
                    bpimageS = pygame.transform.scale(graphic[1],image_reset)
                    rpimageS = pygame.transform.scale(graphic[2],image_size)
                    lpimageS = pygame.transform.scale(graphic[3],image_reset)
                    screen.blit(rpimageS, location)
                    pygame.display.flip()
             
                    
def obstacle_graphic(screen, graphic, location): 
      screen.blit(graphic, location)

def game_board_graphic(type):
      if  type == "forest":
            floor_tile = []
            square2 = grass_floor2
            floor_tile.append(square2)
            square1 = grass_floor3
            floor_tile.append(square1)
            square3 = grass_floor1
            floor_tile.append(square3)
            background = forest_background
            floor_tile.append(background)
            return floor_tile
#rows 1-9 col 14

def draw_board(buffer, player, type):
    
    tiles = game_board_graphic(type)
    for row in range(0,grid_size):
        for col in range(0,grid_size-1):
            location = (col*50+75,row*50+75)
            if (row + col) % 2 == 0:
                buffer.blit(tiles[1], location) 
            else:
                buffer.blit(tiles[0], location)
    buffer.blit(tiles[3],(0,0))
    level = str(player.level)
    actions = str(f"Actions. {player.actions_left}") 
    current_hp = str(f"Health: {player.current_hp} / {player.max_hp}") 
    attack_points = str(f"Attack Points. {player.attack_points}") 
    armor_rating = str(f"Armor Rating. {player.armor_rating}") 
    attack_skill_modifier = str(f"Accuracy. {player.attack_skill_modifier}")
    player_status = str(f"Status. {player.status}")
    ability1 = str(f"1. {player.abilities[1]}")
    ability2 = str(f"2. {player.abilities[2]}")
    ability3 = str(f"3. {player.abilities[3]}")
    ability4 = str(f"4. {player.abilities[4]}")
    ability5 = str(f"5. {player.abilities[5]}")
    ability6 = str(f"6. {player.abilities[6]}")
    ability7 = str(f"7. {player.abilities[7]}")
    ability8 = str(f"8. {player.abilities[8]}")
    ability9 = str(f"9. {player.abilities[9]}")
    ability10 = str(f"10. {player.abilities[10]}")
    draw_player_info(
    buffer, 
    player.name, 
    level, 
    current_hp, 
    attack_points, 
    armor_rating, 
    attack_skill_modifier,
    actions, 
    player_status,
    ability1,
    ability2,
    ability3,
    ability4,
    ability5,
    ability6,
    ability7,
    ability8,
    ability9,
    ability10
    
    )

# Function to draw units on the board
def draw_units(buffer, player, enemies,obstacles, game_board):

    
    for row in range(grid_size):
        for col in range(grid_size):
            draw_cell = game_board[row][col]
            location = (col*50+75,row*50+75)
            if draw_cell.fill == player and player.status != "dead":   #front back right left
                determine_graphic(buffer,draw_cell.fill.graphic,draw_cell.fill.position,location)
                pygame.display.flip()                        
            elif draw_cell.fill in enemies:
                determine_graphic(buffer,draw_cell.fill.graphic,draw_cell.fill.position,location)
                pygame.display.flip()
            elif draw_cell.fill in obstacles:
                obstacle_graphic(buffer,draw_cell.fill.graphic,location)
            elif draw_cell.fill == None:
                continue
            else:
                 continue

def ability_graphic(screen, ability, entity, game_board, player, frame):
    col = entity.col
    row = entity.row
    #topleft topright bottomright bottomleft
    animation_frames = []
    #topleft topright bottomright bottomleft
    if ability.name == "sword":
        graphic0 = sword
        animation_frames.append(graphic0)

        graphic1 = woosh
        animation_frames.append(graphic1)

        graphic2 = pygame.transform.rotate(sword,270)
        animation_frames.append(graphic2)

        graphic3 = pygame.transform.rotate(woosh,270)
        animation_frames.append(graphic3)

        graphic4 = pygame.transform.rotate(sword,180)
        animation_frames.append(graphic4)

        graphic5 = pygame.transform.rotate(woosh,180)
        animation_frames.append(graphic5)

        graphic6 = pygame.transform.rotate(sword,90)
        animation_frames.append(graphic6)

        graphic7 = pygame.transform.rotate(woosh,90)
        animation_frames.append(graphic7)
    elif ability.name == "heal":
            animation_frames.append(healring)
            graphic0 = pygame.transform.scale_by(growingheart,0.25)      
            animation_frames.append(graphic0)
            graphic1 = pygame.transform.scale_by(growingheart,0.5)
            animation_frames.append(graphic1)
            animation_frames.append(growingheart)
    else:
        return
    if ability.reach >= 1:  
        locations = [(col*50+65,row*50+50), (col*50+80, row*50+60), (col*50+100, row*50+50), (col*50+120, row*50+80), (col*50+95, row*50+95), (col*50+80, row*50+130), (col*50+40, row*50+110), (col*50+50, row*50+80), (col*50+40,row*50+50)]
 
        if entity.position == "forward":
            if frame == 0:
                screen.blit(animation_frames[0],locations[0])
                pygame.display.flip()
                time.sleep(.06)
            elif frame == 1:       
                screen.blit(animation_frames[1],locations[1] )
                pygame.display.flip()
                time.sleep(.05)
            elif frame == 2:
                screen.blit(animation_frames[2],locations[2])
                pygame.display.flip()
                time.sleep(.05)

        if entity.position == "right":
            if frame == 0:
                screen.blit(animation_frames[2],locations[2])
                pygame.display.flip()
                time.sleep(.06)
            elif frame == 1:       
                screen.blit(animation_frames[3],locations[3] )
                pygame.display.flip()
                time.sleep(.05)
            elif frame == 2:
                screen.blit(animation_frames[4],locations[4])
                pygame.display.flip()
                time.sleep(.05)

        if entity.position == "back":
            if frame == 0:
                screen.blit(animation_frames[4],locations[4])
                pygame.display.flip()
                time.sleep(.06)
            elif frame == 1:       
                screen.blit(animation_frames[5],locations[5] )
                pygame.display.flip()
                time.sleep(.05)
            elif frame == 2:
                screen.blit(animation_frames[6],locations[6])
                pygame.display.flip()
                time.sleep(.05)

        if entity.position == "left":
            if frame == 0:
                screen.blit(animation_frames[0],locations[8])
                pygame.display.flip()
                time.sleep(.06)
            elif frame == 1:       
                screen.blit(animation_frames[7],locations[7] )
                pygame.display.flip()
                time.sleep(.05)
            elif frame == 2:
                screen.blit(animation_frames[6],locations[6])
                pygame.display.flip()
                time.sleep(.05)
        animation_frames.clear()  
    elif ability.reach < 1:
        locations = [(col*50+50,row*50+50), (col*50+75,row*50+70), (col*50+60, row*50+40), (col*50+50,row*50+25)]
        if frame == 0:
                screen.blit(animation_frames[0],locations[0])
                pygame.display.flip()
                time.sleep(.08)
        elif frame == 1:       
                screen.blit(animation_frames[1],locations[1] )
                pygame.display.flip()
                time.sleep(.08)
        elif frame == 2:
                screen.blit(animation_frames[2],locations[2])
                pygame.display.flip()
                time.sleep(.08)
        elif frame == 3:
                screen.blit(animation_frames[3],locations[3])
                pygame.display.flip()
                time.sleep(.08)
    return

#def ability_graphic2