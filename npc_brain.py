
"""
i make extensive notes before attempting to write a new part of the code:
my friends told me it would be a good idea to put notes into the code so its easier to follow. 
at some point I will go back through and add smaller notes accross the entirety of the code to lay out extactly whats going on.

heres the notes I wrote before programming this ai model (fun side note: my current job is a dog walker 
so I often type this out on my phone while walking dogs):

turns coutning down 
general:
x-0: movement or (if in range attacks/abilities)
if agg or def not in range get in range (always try to get in range)
if you get in range:
if def use attack once if actions left is 4 or less and twice if greater than 4 then begin evasive manuevers 
if agg attack until turn is over
 

enemy abilities:
1: movement
2: melee attack
3: evasive, defensive or healing
4: long range
5: mid range
6: special 
fighting style (list of weights for logic to choose attack) (add to class)
behavior    (either aggressive or defensive will add switch abilities and low health implications) (add to enemy class)
 I can have them switch from aggro to defensive or rev at a health percent

aggressive: explained above 
defensive: evasive maneuvers: 
Use ability 3 if under full health
Find closest obstacle (lowest hscore)
Check neighbors 
Choose furthest from player (highest h score) 
Create path to cell and go towards it
If cell is reached end turn
if no path attack until turn ends
melee:
  Use aggressive vs defensive
 follow path to player square if len(path) =1 then in-range
If in range 
Face player
If agg then agg
If def then def

long range:
(most in depth)
if not in range:
Make a list of the cells in range 
Make a class for paths with a self. Length
Find paths on all cells in range
Add to class with length
Add to list
Order by smallest .length value path = sorted(paths, key=lambda cell: int(cell.h_score()), reverse=True)
choose lowest length value
return path and append end cell.
follow path 
if cell is reached then in range
face player
agg and def begins here 

if starting in melee range of player:
do the same as if not in range just instead of choosing lowest length value choose the path that has 4 steps 
if one doesnt exist try 3 steps 2 steps else just attack

mid range:
same as long range just with 3 squares
take out the 4 steps and change it to 3 steps

special:
gets in range using in-range algorithm based on reach
use special
for remaining actions use preferred 


functions to make:
tactics function (enemy) -> random weighted choice based on assigned tactics
in range algorithm (pathfinder, player(target), enemy, )
behavior algorithm(actions left, gameboard, enemy, pathfinder, enemy)

items to add to enemy class: tactics, behavior, 

"""
import pygame
import pathfinder_module
import random


def tactics(tactics):
    #chooses what kind of movet the entity will make
    tactics_choices = ["melee", "long range", "midrange", "special"]
    tactic = random.choices(tactics_choices,tactics)
    print(f"tactic {tactic}")
    return tactic

def in_range_check(npc, target, game_board, tactic, grid_size, abilities):
    #check if in range of target with specific tactic
    if tactic == ['melee']:
        attack_name= npc.abilities[1]
    elif tactic == ['long range']:
        attack_name= npc.abilities[3]
    elif tactic ==['midrange']:
        attack_name= npc.abilities[4]
    elif tactic == ['special']:
        attack_name= npc.abilities[5]
    else:
        print("tactic not found")
    print(f"attack {attack_name}")
    for ability in abilities:
        if attack_name == ability.name:
            attack = ability
            print(f"attack reach {attack.reach}")
        else:
            continue
    
    #check cells in range vertical
    col_cells = []
    for row in range(grid_size-1):
        col_cells.append(game_board[row][target.col])
    
    back_inrange = []
    for cell in col_cells[target.row:]:
        if cell.fill == None:
            back_inrange.append(cell)
        else:
            break
    
    col_cellsrev = col_cells[::-1] 
    forward_inrange = []       
    for cell in col_cellsrev[target.row:]:
        if cell.fill == None:
            forward_inrange.append(cell)
        else:
            break
    
    #check cells in range horizontal
    row_cells = []
    for col in range(grid_size-1):
        row_cells.append(game_board[target.row][col])
    right_inrange = []
    for cell in row_cells[target.col:]:
        if cell.fill == None:
            right_inrange.append(cell)
        else:
            break
    row_cellsrev = row_cells[::-1] 
    left_inrange = []       
    for cell in row_cellsrev[target.col:]:
        if cell.fill == None:
            left_inrange.append(cell)
        else:
            break
    
    cells_inrange = []
    possible_cells_inrange = []
    possible_cells_inrange.extend(forward_inrange)
    possible_cells_inrange.extend(back_inrange)
    possible_cells_inrange.extend(right_inrange)
    possible_cells_inrange.extend(left_inrange)
    #alternate method:
    for cell in possible_cells_inrange:
        hscore= h_score(cell, target)
        print(f"hscore {hscore}")
        if hscore <=attack.reach:
            cells_inrange.append(cell)
    npccell = game_board[npc.row][npc.col]
    if npccell in cells_inrange:
        return True
    else:
        return cells_inrange
    """
    if len(forward_inrange)> attack.reach:
        x=0
        for x in range(attack.reach-1):
            cells_inrange.append(forward_inrange[x])
            x+=1
    else:
        cells_inrange.extend(forward_inrange)
    
    if len(back_inrange)> attack.reach:
        x=0
        for x in range(attack.reach-1):
            cells_inrange.append(back_inrange[x])
            x+=1
    else:
        cells_inrange.extend(back_inrange)

    if len(right_inrange)> attack.reach:
        x=0
        for x in range(attack.reach-1):
            cells_inrange.append(right_inrange[x])
            x+=1
    else:
        cells_inrange.extend(right_inrange)
    
        
    if len(left_inrange)> attack.reach:
        x=0
        for x in range(attack.reach-1):
            cells_inrange.append(left_inrange[x])
            x+=1
    else:
        cells_inrange.extend(left_inrange)    

    npccell = game_board[npc.row][npc.col]
    if npccell in cells_inrange:
        return True
    else:
        return cells_inrange
    """
def in_range_path(game_board, npc, target, grid_size):
    # if not in range determines best end cell in attack range for tactic and sets path to that cell
    cells_inrange = in_range_check(npc, target, game_board)
    possible_paths = []
    for cell in cells_inrange:
        possible_path = pathfinder_module.final_pathfinding(grid_size,game_board,game_board[npc.row][npc.col],cell )
        possible_paths.append(possible_path)
    possible_paths_sorted= sorted(possible_paths, key=lambda x: len(x))
    move_path = possible_paths_sorted[0]

    return move_path

def h_score(self, target):
        row_score = abs(target.row - self.row)
        col_score = abs(target.col - self.col)
        h_score = abs(row_score + col_score)
        return h_score   
def ranger_move(enemy, target, game_board): #foreward back left right
    neighbors = [game_board[target.row-1][target.col],game_board[target.row+1][target.col],game_board[target.row][target.col-1],game_board[target.row][target.col+1]]
    enemycell = game_board[enemy.row][enemy.col]
    
    if game_board[enemy.row][enemy.col] in neighbors:
        if enemycell == neighbors[0]:
            movement = "forward"
        elif enemycell == neighbors[1]:
            movement = "back"
        elif enemycell == neighbors[2]:
            movement = "left"
        elif enemycell == neighbors[3]:
            movement = "right"
        moves = [movement, movement, movement]
        return moves
    else:
        return False
def behavior(tactic, npc):
    #first things first determine the tactic being used:
    # determine if the npc is aggressive or defensive by .behavior
    

    ability_actions = []
    
    evasive_ability = npc.abilities[2]
    if tactic == "melee":
        attack= npc.abilities[1]
    elif tactic == "long range":
        attack= npc.abilities[3]
    elif tactic == " midrange":
        attack= npc.abilities[4]
    elif tactic == "special":
        attack= npc.abilities[5]
    if npc.behavior == "aggresive":
        ability_actions.append(attack)
        #if npc.boss == True:
        #    ability_actions.append("spawner") #add a npc.minion to enemy class
        if tactic == "special":
            if npc.abilities[5].reach == 1:
                for _ in range(npc.actions_left):
                    ability_actions.append(npc.abilities[1])    
            elif npc.abilities[5].reach == 3:
                for _ in range(npc.actions_left):
                    ability_actions.append(npc.abilities[4])    
            elif npc.abilities[5].reach > 3:
                for _ in range(npc.actions_left):
                    ability_actions.append(npc.abilities[3]) 
            else:
                return ability_actions
    else:
        ability_actions.append(attack)
        if npc.actions_left>4:
            
            if tactic == "special":
                if npc.abilities[5].reach == 1:
                
                    ability_actions.append(npc.abilities[1])    
                elif npc.abilities[5].reach == 3:
               
                    ability_actions.append(npc.abilities[4])    
                elif npc.abilities[5].reach > 3:
                
                    ability_actions.append(npc.abilities[3]) 
                
            else:
                ability_actions.append(attack)
            if npc.current_hp < (npc.max_hp *.6) and evasive_ability != "locked" :
                ability_actions.append(evasive_ability)
            
    return ability_actions
       


def evasive(grid_size, npc, player, game_board, obstacles):
    # for defensive actions finds nearest obstacle by hscore to npc (search board for all obstacles and sort by hscore choose lowest)
    # search neighbors for opening and find one with highest hscore from player
    # now we have the closest "hiding spot" cell 
    #create path to that cell
    obstacle_cells =[]
    for row in range(grid_size-1):
        for col in range(grid_size-1):
            cell = game_board[row][col]
            if cell.fill in obstacles:
                obstacle_cells.append(cell)
                cell.h_score = h_score(cell,npc)
   
    closest_cells = sorted(obstacle_cells)
    closest_obstacle = closest_cells[0]
    obstacle_neighbors = [game_board[closest_obstacle.row-1][closest_obstacle.col],game_board[closest_obstacle.row+1][closest_obstacle.col],game_board[closest_obstacle.row][closest_obstacle.col+1],game_board[closest_obstacle.row][closest_obstacle.col+1]]
    furthest_cell_unsorted = []
    for neighbors in obstacle_neighbors:
        if neighbors.fill == None:
            neighbors.h_score = h_score(neighbors,player)
            furthest_cell_unsorted.append(neighbors)
    furthest_cell = sorted(furthest_cell_unsorted,reverse=True)       
    hiding_spot = furthest_cell[0] 
    path = pathfinder_module.final_pathfinding(grid_size,game_board,game_board[npc.row][npc.col],hiding_spot)
    if path != False:
        return path
    else:
        return False
    

    