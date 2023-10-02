import pygame
import random
import graphics_module
import sys
import time
import pathfinder_module
import npc_brain


# Set colors (you can customize these)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (150, 150, 150)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN1 =(25, 71, 14)
BROWN = (54, 27, 1)


class PygameStream:
    def __init__(self, max_lines=5):
        self.max_lines = max_lines
        self.lines = []

    def write(self, text):
        
        if len(self.lines) > self.max_lines:
            self.lines.clear()  # Remove the oldest line
        self.lines.append(text.strip())

    def flush(self):
        pass

    def get_lines(self):
        return self.lines
        

# Initialize Pygame
pygame.init()
print("Welcome to the game! \nwhat is your character name?")
characterName = input ()  # Print a welcome message at the beginning
# Set the dimensions of the screen (adjust as needed)
screen_width = 1120
screen_height = 775
cell_size = 50
grid_size = 14


# Create the screen
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
target_frame_rate = 60

buffer1 = pygame.Surface((screen_width, screen_height))
buffer2 = pygame.Surface((screen_width, screen_height))
current_buffer = buffer1

terminal_barO = pygame.image.load(r"C:\Users\danha\OneDrive\Desktop\programming\rpggame\potential-potato\placeholder graphics\terminal_box.png")
terminal_font = pygame.font.Font(r"C:\Users\danha\OneDrive\Desktop\programming\rpggame\potential-potato\placeholder graphics\PR Viking.ttf", 18)
terminal_font_outer = pygame.font.Font(r"C:\Users\danha\OneDrive\Desktop\programming\rpggame\potential-potato\placeholder graphics\PR Viking.ttf", 18)

# list of all the things so the game mixer can make a random game
all_the_things = []

#abilities dictionary

abilities = []
class Ability:
    def __init__(self, name, reach, type, damage, graphic, splash,frames):
        self.name = name
        self.reach = reach
        self.damage = damage
        self.type = type
        self.graphic = graphic
        self.splash = splash
        self.frames =frames
    
def ability_effect(ability, user, target):
        if ability.name == "sword" or \
            ability.name == "bow" or \
            ability.name == "fireball" or \
            ability.name == "piercing shot" or \
            ability.name == "lightning bolt" or \
            ability.name == "bite":
                calculate_attack_damage(ability, user, target)
        elif ability.name == "teleport":
                i = 0
                for i in range(5):
                    row = random.randint(0, grid_size - 2)
                    col = random.randint(0, grid_size - 1)
                    if open_cell(row,col):
                        if user in enemies:
                            i = pathfinder_module.bruteforce_pathfinding(grid_size,game_board,game_board[row][col],game_board[player.row][player.col])
                            if i == False:
                                i +=1
                                print("\nsomething when wrong \nlet me try again")
                            else:
                                game_board[user.row][user.col].fill = None
                                game_board[row][col].fill = user
                        else:
                            game_board[user.row][user.col].fill = None
                            game_board[row][col].fill = user
                        break
                    else:
                        i +=1
                        print("\nsomething when wrong \nlet me try again")
        elif ability.name == "drain":
                calculate_attack_damage(ability,user,target)
                user.current_hp +=7
                if user.current_hp > user.max_hp:
                    user.current_hp = user.max_hp
        elif ability.name == "fear":
                target.status == "scared"
        elif ability.name == "heal":
                user.current_hp += (random.randint(4,13)+ 2*user.level)
                if user.current_hp > user.max_hp:
                    user.current_hp = user.max_hp
        else:
                 print("\nnot an ability")    
             

sword = Ability("sword",1,"plain",10,"graphic",False, 2)
abilities.append(sword)  
bite = Ability("bite",1,"plain",10,"graphic",False, 1)
abilities.append(bite)     
teleport = Ability("teleport",0,0,"none","graphic",False,1)
abilities.append(teleport)         
bow = Ability("bow",grid_size,"plain",7,"graphic",False,13)
abilities.append(bow)
fireball = Ability("fireball",grid_size,"fire",7,"graphic",False,13)
abilities.append(fireball)
piercing_shot = Ability("piercing shot", grid_size, "plain", 12, "graphic",True,13)
abilities.append(piercing_shot)
lightning_bolt = Ability("lightning bolt", grid_size, "lightning", 12, "graphic",True,13)
abilities.append(lightning_bolt)
drain = Ability("drain", 4,"necrotic",12,"graphic",False,2)
abilities.append(drain)
fear = Ability("fear", 2, "pychic", 0, "graphic", False, 1)
abilities.append(fear)
heal = Ability("heal",0,0,"none","graphic",False,1)
abilities.append(heal)

#enemy dictionary
 
wolf_dict = {
    "name": "wolf",
    "level": 1,
    "graphic": graphics_module.graphic_dictionary("wolf"),
    "found": "forest",
    "resistance": "none",
    "weakness": "none",
    "max_hp": 30,
    "attack_points": 1,
    "armor_rating": 5,
    "attack_skill_modifier": 2,
    "total_actions": 10,
    "actions_left": 10,
    "abilities": ["movement", "bite", "locked", "locked", "locked", "locked"],
    "tactics": [1,0,0,0],
    "behavior": "aggressive"
    

    
}

enemies = []
class Enemy:
    def __init__(self, name, level, graphic, found, resistance, weakness, max_hp, attack_points, armor_rating, attack_skill_modifier, total_actions, actions_left, abilities,tactics, behavior):
        self.name = name
        self.level = level
        self.graphic = graphic
        self.found = [found]
        self.resistance = resistance
        self.weakness = weakness
        self.max_hp = max_hp
        self.current_hp = max_hp
        self.attack_points = attack_points
        self.armor_rating = armor_rating
        self.attack_skill_modifier = attack_skill_modifier
        self.status = "none"
        self.disabled = []
        self.position = "back"
        self.row = random.randint(0, grid_size - 3)
        self.col = random.randint(0, grid_size - 2)
        self.total_actions = total_actions
        self.actions_left = actions_left
        self.abilities = abilities
        self.tactics = tactics
        self.behavior = behavior



# Create instances of Enemy class for different enemies
wolf = Enemy(**wolf_dict)
#vampire = Enemy("Vampire", 2,"dungeon","necrotic",["radiant","fire"], 70, 20, 17, 3, 4, ["movement", "drain"])
#ghost = Enemy("Ghost", 3, ["graveyard","dungeon"],["necrotic","psychic"], ["radiant","fire"], 30, 10, 13, 1, 6, ["movement", "fear"])
#create randomizer spawn  
for _ in range(3):
    enemy_instance = Enemy(**wolf_dict)
    enemies.append(enemy_instance)

#obstacle creation

obstacles = []
class Obstacle:
    def __init__(self,name,found):
        self.name = name
        self.found = found
        self.graphic = graphics_module.graphic_dictionary(self.name)
forest_obstacle = {
     "name":"forest" ,
      "found": "forest"
        }

obnum = random.randint(30,45) # can add differ
for _ in range(obnum):
    # here is the game mixer randomizer from location chooses a random choice obstacle and returns it as a string might work
    obstacle_instance = Obstacle(**forest_obstacle) 
    obstacles.append(obstacle_instance)

def spawner(obstacles):
   for obstacle in obstacles:
        free_cells = []
        for row in range(grid_size-3):
            for col in range(grid_size-1):
                if game_board[row][col].fill is None and game_board[row][col].location !=(0,0):
                    free_cells.append(game_board[row][col].location)
        obobj = random.choice(free_cells)
        obrow = obobj[0]
        obcol = obobj[1]
        game_board[obrow][obcol].fill = obstacle
        free_cells.clear()
        continue
# Player and enemy attributes
class Player:
    def __init__(self,characterName):

        self.name =characterName
        self.type = "player"
        self.level = 1
        self.max_hp = 300
        self.current_hp = 300
        self.attack_points = 20
        self.armor_rating = 17
        self.attack_skill_modifier = 3
        self.abilities = ["movement","sword","locked","heal","locked","locked","locked","locked","locked","locked","locked"]
        self.resistance = "none"
        self.weakness = "none"
        self.status = "none"
        self.disabled = []
        self.total_actions = 6
        self.actions_left = 6
        self.position = "forward"
        self.graphic = graphics_module.graphic_dictionary("player")
        self.row = grid_size - 2
        self.col = (grid_size -2) // 2
player = Player(characterName)

class Cell:
    def __init__(self, row, col):
        self.location = (row, col)
        self.row = row
        self.col = col
        self.fill = None  # You can set this to an entity object if the cell is occupied
        self.parent = None
        self.h_score = None
        



# Define the game board as a 2D array
# Define the game board as a grid of Cell objects
game_board = [[Cell(row, col) for col in range(grid_size)] for row in range(grid_size)]


#pygame_stream = PygameStream()
#sys.stdout =  pygame_stream

def buffer_screen(cbuffer, player):
    
    
    cbuffer.fill(BROWN)
    graphics_module.draw_board(cbuffer,player, "forest")
    graphics_module.draw_units(cbuffer, player, enemies, obstacles,game_board)
    """
    terminal_textstr = pygame_stream.get_lines()
    for termtxt in terminal_textstr:
        terminal_texto = terminal_font_outer.render(f"\n {termtxt}", True, BLACK)
        terminal_text = terminal_font.render(f"\n {termtxt}", True, GRAY)
        cbuffer.blit(terminal_texto, (798, 627 +10*terminal_textstr.index(termtxt)))
        cbuffer.blit(terminal_text, (800, 625 +10*terminal_textstr.index(termtxt)))
        pygame.display.flip()
   """
    pygame.display.flip()


    if cbuffer == buffer1:
            cbuffer = buffer2
            screen.blit(buffer1, (0, 0))
    else:
            cbuffer = buffer1
            screen.blit(buffer2, (0, 0))

    pygame.display.flip()
    clock.tick(target_frame_rate)

# Function to draw the game board added to graphic mod

    

            
    


def handle_events():
    check_status(player)
    if player.status != "dead":
            for event in pygame.event.get(): 
                if event.type == pygame.KEYDOWN and player.actions_left > 0:
                    handle_key_event(event.key)
                if player.actions_left <= 0:
                    return             
        
    
            
    
def handle_key_event(key):
    if player.actions_left <= 0:
        print ("\nno move left this turn")
        return    
    if key == pygame.K_UP:
            move_direction(player, "forward")
    elif key == pygame.K_LEFT:
            move_direction(player, "left")
    elif key == pygame.K_DOWN:
            move_direction(player, "back")
    elif key == pygame.K_RIGHT:
            move_direction(player, "right")
    elif key == pygame.K_w:
            player.position = "forward"
            buffer_screen(current_buffer, player)         
    elif key == pygame.K_a:
            player.position = "left"
            buffer_screen(current_buffer, player)
            
    elif key == pygame.K_s:
            player.position = "back"
            buffer_screen(current_buffer, player)
            
    elif key == pygame.K_d:
            player.position = "right"
            buffer_screen(current_buffer, player)
            
    elif key == pygame.K_1:
            use_ability(current_buffer, player, player.abilities[1])
    elif key == pygame.K_2:
            use_ability( current_buffer, player, player.abilities[2])
    elif key == pygame.K_3:
            use_ability( current_buffer, player, player.abilities[3])
    elif key == pygame.K_4:
            use_ability( current_buffer, player, player.abilities[4])    
    elif key == pygame.K_5:
            use_ability( current_buffer, player, player.abilities[5])
    elif key == pygame.K_6:
            use_ability( current_buffer, player, player.abilities[6])
    elif key == pygame.K_7:
            use_ability( current_buffer, player, player.abilities[7])
    elif key == pygame.K_8:
            use_ability( current_buffer, player, player.abilities[8])
    elif key == pygame.K_9:
            use_ability( current_buffer, player, player.abilities[9])                        
    elif key == pygame.K_q:
            print(player.abilities)
    elif key == pygame.K_ESCAPE:
            pygame.quit()
            quit()
    
    
    
    

def check_status(entity):
    if entity.status == "none":
        return
    if entity.status == "dead":
         game_board[entity.row][entity.col].fill = None
         entity.total_actions == 0
         entity.actions_left == 0
         if entity == player:
            print("\ndead")
            pygame.quit()
              
    elif entity.status == "scared":
        entity.disabled = entity.abilities[1:]
        
    else:
         return
    
#movement function
def open_cell(row,col): 
      # Check if the destination cell is empty (not occupied by an enemy or object)
     if game_board[row][col].fill == None and row in range(grid_size-1) and col in range(grid_size-1): 
          return True
     else:
          return False
     
def move_direction(entity, direction):
    row = entity.row
    col = entity.col
    if "movement" in entity.abilities:
        if direction == "forward":
            if open_cell(row - 1, col):
                
                game_board[row][col].fill = None
                entity.row -= 1
                game_board[entity.row][entity.col].fill = entity
                entity.actions_left -= 1 
                        
            else:
                print("\nCannot move there.")    
        elif direction == "left":
            if open_cell(row, col- 1):
                
                game_board[row][col].fill = None
                entity.col -= 1
                game_board[entity.row][entity.col].fill = entity
                entity.actions_left -= 1
                           
            else:
                print("\nCannot move there.")
            
        elif direction == "back":
            if open_cell(row + 1, col):
                game_board[row][col].fill = None
                entity.row += 1
                game_board[entity.row][entity.col].fill = entity
                entity.actions_left -= 1
                
            else:
                print("\nCannot move there.")
            
        elif direction == "right":
            if open_cell(row, col+1):
                game_board[row][col].fill = None
                entity.col += 1
                game_board[entity.row][entity.col].fill = entity
                entity.actions_left -= 1
                
                         
            else:
                print("\nCannot move there.")     
    else:
         print("\n" + entity.name + " can't move")   
    buffer_screen(current_buffer, player)
    return

def in_range(attacker, ability): 
    enemies_in_range = []
    if attacker is player:
        if attacker.position == "back":
            for row in range(attacker.row, attacker.row + ability.reach +1):
                target = game_board[row][attacker.col].fill
                if target is None:
                     continue
                elif target in enemies:
                     enemies_in_range.append(target)
                
                else:
                    continue
        elif attacker.position == "forward":
            for row in range(attacker.row - ability.reach, attacker.row):
                target = game_board[row][attacker.col].fill
                if target is None:
                 continue
                elif target in enemies:
                     enemies_in_range.append(target)   
                else:
                     continue
                    
        elif attacker.position == "right":
            for col in range(attacker.col, attacker.col + ability.reach +1):
                target = game_board[attacker.row][col].fill
                if target is None:
                    continue
                elif target in enemies:
                    enemies_in_range.append(target)     
                else:
                    continue
        elif attacker.position == "left":
            for col in range(attacker.col - ability.reach, attacker.col):
                target = game_board[attacker.row][col].fill
                if target is None:
                    continue
                elif target in enemies:
                    enemies_in_range.append(target)
                else:
                    continue       
    else:
        if attacker.position == "back":
            for row in range(attacker.row, attacker.row + ability.reach +1):
                target = game_board[row][attacker.col].fill
                if target is None:
                    continue
                elif target is player:
                    enemies_in_range.append(target)
                else:
                    continue
        elif attacker.position == "forward":
            for row in range(attacker.row - ability.reach, attacker.row):
                target = game_board[row][attacker.col].fill
                if target is None:
                    continue
                elif target is player:
                    enemies_in_range.append(target)   
                else:
                    continue
                    
        elif attacker.position == "right":
            for col in range(attacker.col, attacker.col + ability.reach +1):
                target = game_board[attacker.row][col].fill
                if target is None:
                    continue
                elif target is player:
                    enemies_in_range.append(target)     
                else:
                    continue
        elif attacker.position == "left":
            for col in range(attacker.col - ability.reach, attacker.col):
                target = game_board[attacker.row][col].fill
                if target is None:
                    continue
                elif target is player:
                    enemies_in_range.append(target)
                else:
                    continue 
    if not enemies_in_range:
         return None
    else:    
        return enemies_in_range

def use_ability(current_buffer, user, ability_name):
    
    for ability in abilities:
        if ability.name == ability_name: 
            frame = 0
            for frame in range(ability.frames+1):
                graphics_module.ability_graphic(screen, ability, user, game_board, player,frame)
                buffer_screen(current_buffer,player)
                frame += 1
            pygame.display.flip()
            if ability.reach > 0:
                enemies_in_range = in_range(user, ability)
                if not in_range(user, ability):
                        print("\nNo enemies in range")
                        return
                else:
                    user.actions_left -= 1
                    if ability.splash:
                        for target in enemies_in_range:
                            if ability_success(user, target):
                                print(f"{ability_name} attack Hit!")
                                ability_effect(ability, user, target)
                            else:
                                print(f"{ability_name} attack Miss!")    
                    else:
                            if ability_success(user, enemies_in_range[0]):
                                print(f"{ability_name} attack Hit!")
                                ability_effect(ability,user,enemies_in_range[0])            
                            else:
                                print(f"{ability_name} attack Miss!")
                
            elif ability.reach <= 0:
                 ability_effect(ability,user,user)
            graphics_module.ability_graphic(screen, ability, user, game_board, player, ability.frames+1)
            buffer_screen(current_buffer,player)
            
            
      
    return 
        
def ability_success(attacker, target):
        attack_roll = random.randint(1, 20)  # Rolling a d20 for luck (truly random)
        attack_total = attack_roll + attacker.attack_skill_modifier
        defense_total = target.armor_rating
        if attack_total > defense_total:
             return True
        else:
             return False

def calculate_attack_damage(ability, attacker, target):
  
        # The attack hits
        if ability.type == target.weakness:
            damage = attacker.attack_points + (ability.damage *1.5) 
            target.current_hp -= damage
            print(f"{attacker.name} dealt {damage} damage to {target.name}. \n Seemed extremely effective! \n")
             
        elif ability.type == target.resistance:
            damage = attacker.attack_points + (ability.damage*0.5)
            target.current_hp -= damage
            print(f"{attacker.name} dealt {damage} damage to {target.name}. \n Seemed to have very little effect! \n")
            
        else:
            damage = (attacker.attack_points) + ability.damage
            target.current_hp -= damage
            print(f"{attacker.name} dealt {damage} damage to {target.name}.\n")
               
    
        if target.current_hp <= 0:
            print(f" \n{target.name} was defeated.\n")
            target.status == "dead"
            game_board[target.row][target.col].fill = None
            if target in enemies:
                enemies.remove(target)
            buffer_screen(current_buffer, player)
            
            
             
        return

# Functions to handle enemy's turn
#path finder old
"""
def calculate_path(enemy): #enemy, player
        current_cell = game_board[enemy.row][enemy.col]
        neighborF = game_board[enemy.row-1][enemy.col] 
        neighborB = game_board[enemy.row+1][enemy.col]
        neighborR = game_board[enemy.row][enemy.col+1]
        neighborL = game_board[enemy.row][enemy.col-1]
        potential_neighbors = [neighborF,neighborB,neighborR,neighborL]  # Generate neighboring nodes here what goes in here? (maybe list the possible neighbors)
        
        neighbors=[]
        blocked = []
        paths =[]
        path = []
        for potential_neighbor in potential_neighbors:
            if potential_neighbor.fill is player:
                return potential_neighbor
            elif open_cell(potential_neighbor.row,potential_neighbor.col) and potential_neighbor != current_cell.parent:
                neighbors.append(potential_neighbor)
            else:
                blocked.append(potential_neighbor)
                continue
        print(f"neighbors {neighbors}") 
        
        
        for neighbor in neighbors:
            
            neighbor_h_score = neighbor.h_score(player)
            current_cell_h_score = current_cell.h_score(player)
            if neighbor_h_score <= current_cell_h_score:
                 paths.append(neighbor)
            else:
                 continue
        if not paths:
            for neighbor in neighbors:
                if neighbor_h_score <= current_cell_h_score+2:
                    print (f"flanking? {paths}")
                    paths.append(neighbor)
             
        if not paths:        
            print ("no open cells")
            return None
        else:
            path = sorted(paths, key=lambda cell: int(cell.h_score()), reverse=True)
            print(f" path {path}")         
            next_cell = path[0]
            next_cell.parent = current_cell
            return next_cell
            
"""
def determine_direction(target_row, target_col, enemy_row, enemy_col):
     if target_row>enemy_row and target_col == enemy_col:
          position = "back"
     elif target_row<enemy_row and target_col == enemy_col:
          position = "forward"
     elif target_col>enemy_col and target_row == enemy_row:
          position = "right"
     elif target_col<enemy_col and target_row == enemy_row:
          position = "left"
     
     return position
"""
def handle_enemy_turn(enemy):
    x=0 
    for x in range(enemy.total_actions+1):
        path = calculate_path(enemy)
        if path:
            print(f"next move {path.location}")
            path_h_score = int(path.h_score(player))
            print (f"next move score {path_h_score}")
            # Check if the enemy is within 1 node of the player
            if path.fill == player:
             # Attack the player using the use_ability function      
                position = determine_direction(player.row, player.col, enemy.row, enemy.col)
                enemy.position = position
                print(f"attack {position}")
                use_ability( current_buffer, enemy, enemy.abilities[1])
                buffer_screen(current_buffer,player)
                x +=1
                if enemy.actions_left <=0:
                    break
            else:
                direction = determine_direction(path.row,path.col,enemy.row,enemy.col)
                enemy.position = direction
                buffer_screen(current_buffer,player)
                print(f"direction of movement {direction}")
            
                move_direction(enemy,direction)
                buffer_screen(current_buffer,player)
                x += 1
                if enemy.actions_left <=0:
                    break      
        elif not path:
            print("no open spaces")
            x += 1
        
    for row in range(grid_size):
         for col in range(grid_size):
              game_board[row][col].parent is None

    print(f"{enemy.name}'s turn over")
"""
def handle_enemy_turn(enemy):
    actionsleft = enemy.actions_left
    tactic = npc_brain.tactics(enemy.tactics)
    in_range_bool = npc_brain.in_range_check(enemy, player, game_board, tactic, grid_size, abilities)
    if not in_range_bool:
        path = npc_brain.in_range_path(game_board, enemy, player, grid_size)
        for cell in path: 
            if enemy.actions_left <=0:
                return print("turn over")
            else:
                nextrow = cell.row
                nextcol = cell.col
                move = determine_direction(nextrow, nextcol, enemy.row, enemy.col)
                enemy.position = move
                buffer_screen(current_buffer,player)
                move_direction(enemy,move)
                buffer_screen(current_buffer,player)
    if tactic == "midrange" or tactic == "long range": # only occurs when the enemy is in a neighboring cell
        movesR= npc_brain.ranger_move(enemy, player, game_board)
        if movesR != False:
            for moveR in movesR: 
                enemy.position = moveR
                buffer_screen(current_buffer,player)
                move_direction(enemy,moveR)
                buffer_screen(current_buffer,player)
        
    # check h score of npc to player if 
        #h_score()
    #finish back up manveuvor
      # game_board will use this as "next cell info" and run through the list for positioning and movement removing an action each time
    # so run both tactics and in_range_path before the turn loop
    if enemy.behavior == "aggressive":
        for actionsleft in range(enemy.total_actions):
            actions= npc_brain.behavior(tactic, enemy)
            position = determine_direction(player.row, player.col, enemy.row, enemy.col)
            enemy.position = position
            buffer_screen(current_buffer,player)
            for action in actions:
                if actionsleft <=0:
                    return print("turn over")
                use_ability(current_buffer,enemy,action)
                buffer_screen(current_buffer,player)
        return print("turn over")
    else:
            actions = npc_brain.behavior(tactic, enemy)
            position = determine_direction(player.row, player.col, enemy.row, enemy.col)
            enemy.position = position
            buffer_screen(current_buffer,player)
            for action in actions:
                if actionsleft <=0:
                    return print("turn over")
                use_ability(current_buffer,enemy,action)
                buffer_screen(current_buffer,player)
                
            evasive_manuevers = npc_brain.evasive(grid_size, enemy, player, game_board, obstacles)
            if evasive_manuevers != False:
                for move in evasive_manuevers:
                    if actionsleft <=0:
                        return print("turn over")
                    nextrow = move.row
                    nextcol = move.col
                    position = determine_direction(nextrow, nextcol, enemy.row, enemy.col)
                    enemy.position = position
                    buffer_screen(current_buffer,player)
                    move_direction(enemy,position)
                    buffer_screen(current_buffer,player)
                return print("turn over")
            else: 
                for actionsleft in range(enemy.total_actions):
                    actions= npc_brain.behavior(tactic, enemy)
                    position = determine_direction(player.row, player.col, enemy.row, enemy.col)
                    enemy.position = position
                    buffer_screen(current_buffer,player)
                    for action in actions:
                        if actionsleft <=0:
                            return print("turn over")
                        use_ability(current_buffer,enemy,action)
                        buffer_screen(current_buffer,player)
                    return print("turn over")
                 
def enemies_on_board():
    buffer_screen(current_buffer,player)
    
    for row in range(grid_size):
        for col in range(grid_size):
            
            if game_board[row][col].fill in enemies:
                return True
    
    return False        

def spawner_issue_checker(enemies):
    for enemy in enemies:
        path = pathfinder_module.final_pathfinding(grid_size,game_board,game_board[enemy.row][enemy.col], game_board[player.row][player.col])
        #path = pathfinder_module.bruteforce_pathfinding(grid_size,game_board,game_board[enemy.row][enemy.col], game_board[player.row][player.col])
        if path != False:
                print("path found")
                path.clear()
        else:
                for row in range(grid_size-1):
                    for col in range(grid_size-1):
                        current_cell = game_board[row][col]
                        current_cell.parent = None
                        if current_cell.fill in obstacles:
                            current_cell.fill = None
                        else: 
                            continue 
                return False
    return True

    


# Main loop
def main_loop():
    running = True
    
    # start screen
    # Set the player's initial position at the bottom row middle column
    game_board[player.row][player.col].fill = player
    #place obstacles

    # Place the enemy on the game board
    for enemy in enemies:
        game_board[enemy.row][enemy.col].fill = enemy  

    spawner(obstacles)
    
    p = 0
    for p in range(3):
        clear = spawner_issue_checker(enemies)
    
        if clear:
            break
        else:        
            spawner(obstacles)
            
    
    buffer_screen(current_buffer, player)
    

    while running:     
       
            
            if player.status == "dead":
                        print("You're dead x_x")
                        print("Goodbye")
                        running = False
            elif enemies_on_board(): 
                
                check_status(player)
                handle_events()
                if player.actions_left == 0:
                    player.actions_left = player.total_actions
                    if player.status != "dead":
                        player.status = "none"
                        player.disabled = None
                    for enemy in enemies:
                        if enemy.status != "dead":    
                            handle_enemy_turn(enemy)
                            enemy.actions_left = enemy.total_actions
                            continue
                        else:
                            continue  
                    print("your turn")    
                running = True
            
            else:
                        print("Congratulations! You defeated all enemies.")
                        print("press esc to exit")
                        running = False
                
                    
            
         
                   
                
                
                
                        
            

            

            
        
        
    

#start screen function 
main_loop()
    




#Quit Pygame
pygame.quit()
