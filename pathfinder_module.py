





""" end cell start cell path cell pathrevlist path list"""


def open_cell_check(game_board):
    open_cells = []
    for row in range(13):
        for col in range(13):
            if game_board[row][col].fill is None:
                    open_cells.append(game_board[row][col])
            else:
                    continue
    
    return open_cells

def bruteforce_pathfinding(grid_size, game_board, start_cell, end_cell):
    
    i =1
    current_path_cells = [start_cell]
    next_path_cells = []
    open_cells= open_cell_check(game_board)
    open_cells.append(start_cell)
    for i in range(1,30):
        open_cells= open_cell_check(game_board)
        open_cells.append(start_cell)
        next_path_cells.clear()
        for cell in open_cells:
                
                #print (f" current cell {cell.location}")
                neighbor_cells = [game_board[cell.row-1][cell.col], game_board[cell.row][cell.col+1], game_board[cell.row+1][cell.col], game_board[cell.row][cell.col-1]]
                     
                if cell in current_path_cells:
                   # print(f"target cell: {cell.location}")
                    current_path_cells.remove(cell)
                    for neighbor in neighbor_cells:
                        if neighbor is end_cell:
                            end_cell.parent = cell
                            print (f"path found in  {i} steps")
                            return i
                        elif neighbor in open_cells and neighbor != cell.parent:
                            next_path_cells.append(neighbor)
                          #  print (f"neighbor {neighbor.location}")
                            neighbor.parent = cell
                         #  print(f"parent: {neighbor.parent.location}")
                        else:
                            continue 
                else:
                    continue
                
        current_path_cells.extend(next_path_cells)
        open_cells.clear()        
        i +=1
    return False    

def create_true_path(start_cell, end_cell):
  #  print("start create true path")
    cell = end_cell
    path = [end_cell]
    for _ in range(100):  
        if cell.parent != start_cell:
            path.append(cell)
            cell = cell.parent
        else:
            break
    path.reverse
    return path


def reset_cells(grid_size, game_board):
    for row in range(grid_size-1):
            for col in range(grid_size-1):
                current_cell = game_board[row][col]
                current_cell.parent = None
    
    
    
def final_pathfinding(grid_size, game_board, start_cell, end_cell):
    if not bruteforce_pathfinding(grid_size, game_board, start_cell, end_cell):
        print("no path")
        return False
    else:
        path = create_true_path(start_cell, end_cell)
     #   print(f"path {path}")
        reset_cells(grid_size, game_board)
    return path
