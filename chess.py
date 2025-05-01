from ion import *
from kandinsky import *
from time import *
from draw import *

letter = [i for i in "abcdefgh"]
moves = {"t":[(i,0) for i in range(-7,8) if i!=0]+[(0,i) for i in range(-7,8) if i!=0],
        "c":[(1,2),(1,-2),(2,1),(-2,1),(2,-1),(-1,2),(-1,-2),(-2,-1)],
        "f":[(i,-i) for i in range(-7,8) if i!=0]+[(i,i) for i in range(-7,8) if i!=0],
        "r":[(i,j) for i in range(-1,2) for j in range(-1,2) if (i,j)!=(0,0)]}
moves["d"] = moves["t"] + moves["f"]
piece_color = {"white":["T","C","F","D","R","P"], "black":["t","c","f","d","r","p"]}
designs = {}

castles = {"white":[True,True],
          "black":[True,True]}
game = {"T":[(0,0),(0,7)],
        "C":[(0,1),(0,6)],
        "F":[(0,2),(0,5)],
        "D":[(0,3)],
        "R":[(0,4)],
        "P":[(1,i) for i in range(8)],
        "t":[(7,0),(7,7)],
        "c":[(7,1),(7,6)],
        "f":[(7,2),(7,5)],
        "d":[(7,3)],
        "r":[(7,4)],
        "p":[(6,i) for i in range(8)]}
selected = (1,4)
origin = None
en_passant = None
turn = "white"

def show_piece(piece, i, j) :
  x = 48 + j*25
  y = 190 - i*25
  draw_string(piece, x, y)

def show() :
  global game
  fill_rect(0,0,300,300,color(255,255,255))
  for i in range(9) :
    fill_rect(40,10+i*25,201,1,color(0,0,0))
  for i in range(9) :
    fill_rect(40+i*25,10,1,201,color(0,0,0))
  for piece in game :
    for i, j in game[piece] :
      show_piece(piece ,i, j)
  y,x = selected
  draw_empty_rect(40+25*x,185-25*y,25,25,3,color(255,0,0))
  try :
    j,i = origin
    draw_empty_rect(40+25*i,185-25*j,25,25,3,color(0,255,0))
  except :
    pass
  sleep(0.2)

def select() :
  global selected, origin  
  prev_s = selected
  while not keydown(KEY_OK) :
    if keydown(KEY_DOWN) :
      selected = (max(selected[0]-1,0),selected[1])
    elif keydown(KEY_RIGHT) :
      selected = (selected[0],min(selected[1]+1,7))
    elif keydown(KEY_LEFT) :
      selected = (selected[0],max(selected[1]-1,0))
    elif keydown(KEY_UP) :
      selected = (min(selected[0]+1,7),selected[1])
    
    elif keydown(KEY_BACK) :
      origin = None
      show()
    
    if selected != prev_s :
      prev_s = selected
      show()
  return selected

def move() :
  global game, origin, en_passant, turn, castles
  grid = [["" for _ in range(8)] for _ in range(8)]
  for piece in game :
    for place in game[piece] :
      grid[place[0]][place[1]] = piece
  
  i, j = select()
  while grid[i][j] == "" :
    i, j = select()
  origin = (i, j)
  piece = grid[i][j]
  sleep(0.2)
  ni, nj = select()
  
  if (i, j) == (ni, nj) :
    origin = None
    return False
      
  d = (ni-i, nj-j)
  

def can_move(piece, grid, i, j, ni, nj, for_check = False) :

  d = (ni-i, nj-j)
  ok = False
  
  if piece == "p" :
    if d[0] in [-1,-2] and d[1] in [-1,0,1] :
      if (d == (-1,0) and grid[ni][nj] == "") or (d == (-2,0) and i == 6 and grid[ni][nj] == "") :
        ok = True
      elif d in [(-1,-1),(-1,1)] and grid[ni][nj] != "" :
        ok = True
      elif d in [(-1,-1),(-1,1)] and en_passant :
        if (ni, nj) == (en_passant[1], en_passant[2]) :
          game["P"].remove((en_passant[0],en_passant[2]))
          ok = True
  elif piece == "P" :
    if d[0] in [1,2] and d[1] in [-1,0,1] :
      if (d == (1,0) and grid[ni][nj] == "") or (d == (2,0) and i == 1 and grid[ni][nj] == "") :
        ok = True
      elif d in [(1,-1),(1,1)] and grid[ni][nj] != "" :
        ok = True
      elif d in [(1,-1),(1,1)] and en_passant :
        if (ni, nj) == (en_passant[1], en_passant[2]) :
          game["p"].remove((en_passant[0],en_passant[2]))
          ok = True
  elif piece.lower() == "c" :
    if d in moves[piece.lower()] :
      ok = True
  elif d in moves[piece.lower()] :
    ok = True
    if d[0] == 0 :
      if any(grid[i][j+x]!="" for x in range(1,d[1])) or any(grid[i][j+x]!="" for x in range(d[1]+1,0)) :
        ok = False
    elif d[1] == 0 :
      if any(grid[i+y][j]!="" for y in range(1,d[0])) or any(grid[i+y][j]!="" for y in range(d[0]+1,0)) :
        ok = False
    elif any(grid[i+int(d[0]/abs(d[0]))*n][j+int(d[1]/abs(d[1]))*n]!="" for n in range(1,d[0],1)) :
      ok = False
    
  if piece.lower() == "r" and not ok :
    if piece == "R" :
      if d == (0,-2) and castles["white"][0] and all(grid[0][i]=="" for i in range(1,4)) :
        ok = True
        game["T"].remove((0,0))
        game["T"].append((0,3))
      if d == (0,2) and castles["white"][1] and all(grid[0][i]=="" for i in range(5,7)) :
        ok = True
        game["T"].remove((0,7))
        game["T"].append((0,5))
    if piece == "r" :
      if d == (0,-2) and castles["black"][0] and all(grid[7][i]=="" for i in range(1,4)) :
        ok = True
        game["t"].remove((7,0))
        game["t"].append((7,3))      
      if d == (0,2) and castles["black"][1] and all(grid[7][i]=="" for i in range(5,7)) :
        ok = True
        game["t"].remove((7,7))
        game["t"].append((7,5))
    
  if (piece in piece_color["white"] and grid[ni][nj] in piece_color["white"]) or (piece in piece_color["black"] and grid[ni][nj] in piece_color["black"]) :
    ok = False
  
  if not for_check and piece not in piece_color[turn] :
    ok = False
  
  return ok
  
def double_check(team) :
  
  grid = [["" for _ in range(8)] for _ in range(8)]
  for piece in game :
    for place in game[piece] :
      grid[place[0]][place[1]] = piece
  ni, nj = game["R"][0] if team == "white" else game["r"][0]
  for piece in game :
    if piece in piece_color[team]:
        for (i, j) in game[piece]:
            if can_move(grid[i][j], grid, i, j, ni, nj, True):
                return True
  return False

def move() :
  global game, origin, en_passant, turn, castles
  grid = [["" for _ in range(8)] for _ in range(8)]
  for piece in game :
    for place in game[piece] :
      grid[place[0]][place[1]] = piece
  
  i, j = select()
  while grid[i][j] == "" :
    i, j = select()
  origin = (i, j)
  piece = grid[i][j]
  sleep(0.2)
  ni, nj = select()
  
  if (i, j) == (ni, nj) :
    origin = None
    return False
      

  if not can_move(piece, grid, i, j, ni, nj) :
    origin = None
    return False
      
  d = (ni-i, nj-j)
  if (i,j) == (0,0) or (i,j) == (0,4) :
    castles["white"][0] = False
  if (i,j) == (0,7) or (i,j) == (0,4) :
    castles["white"][1] = False
  if (i,j) == (7,0) or (i,j) == (7,4) :
    castles["black"][0] = False
  if (i,j) == (7,7) or (i,j) == (7,4) :
    castles["black"][1] = False    
  
  if piece.lower() == "p" and abs(d[0]) == 2 :
    en_passant = (ni,int((ni+i)/2),nj)
  else :
    en_passant = None
    
  if turn == "white" :
    turn = "black"
  else :
    turn = "white"
  
  if grid[ni][nj] != "" :
    game[grid[ni][nj]].remove((ni,nj))  
  game[piece].remove((i,j))
  if (piece == "P" and ni == 7) or (piece == "p" and ni == 0) :
    prom = True
  else :
    prom = False
    game[piece].append((ni,nj))
  
  if prom :
    show_piece(" ", i, j)
    sleep(0.2)
    low = True if piece == piece.lower() else False
    prom_pieces = ["D","T","F","C"]
    piece = "D"
    if low :
      piece = piece.lower()
    while not keydown(KEY_OK) :
      if keydown(KEY_LEFT) :
        piece = prom_pieces[(prom_pieces.index(piece.upper())-1)%4]
      elif keydown(KEY_RIGHT) :
        piece = prom_pieces[(prom_pieces.index(piece.upper())+1)%4]
      if low :
        piece = piece.lower()
      show_piece(piece, ni, nj)
      sleep(0.2)
    game[piece].append((ni,nj))
  
  
  if double_check(turn) :
    draw_string(piece,ni,nj)
  
  origin = None
  return True

show()
while True :
  move()
  show()
