from ion import *
from kandinsky import *
from time import *
moves={"t":[(i,0) for i in range(-7,8) if i!=0]+[(0, i) for i in range(-7, 8) if i!=0],
  "c":[(1,2),(1,-2),(2,1),(-2,1),(2,-1),(-1,2),(-1,-2),(-2,-1)],
  "f":[(i,i) for i in range(-7,8) if i!=0]+[(i,-i) for i in range(-7,8) if i!=0],
  "r":[(i,j) for i in range(-1,2) for j in range(-1,2) if (i,j)!=(0,0)]}
moves["d"]=moves["t"]+moves["f"]
piece_color={"white":["T","C","F","D","R","P"],"black":["t","c","f","d","r","p"]}
pieces={}
pieces["p"]=[[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,2,2,2,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,2,1,1,1,2,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,2,1,1,1,1,1,2,0,0,0,0,0,0,0],
    [0,0,0,0,0,2,1,1,1,1,1,1,1,2,0,0,0,0,0,0],
    [0,0,0,0,0,0,2,1,1,1,1,1,2,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,2,2,1,1,1,2,2,0,0,0,0,0,0,0],
    [0,0,0,0,0,2,1,1,1,1,1,1,1,2,0,0,0,0,0,0],
    [0,0,0,0,0,2,1,1,1,1,1,1,1,2,0,0,0,0,0,0],
    [0,0,0,0,0,0,2,2,1,1,1,2,2,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,2,1,1,1,2,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,2,1,1,1,1,1,2,0,0,0,0,0,0,0],
    [0,0,0,0,0,2,1,1,1,1,1,1,1,2,0,0,0,0,0,0],
    [0,0,0,0,2,1,1,1,1,1,1,1,1,1,2,0,0,0,0,0],
    [0,0,0,2,1,1,1,1,1,1,1,1,1,1,1,2,0,0,0,0],
    [0,0,0,2,1,1,1,1,1,1,1,1,1,1,1,2,0,0,0,0],
    [0,0,0,2,2,2,2,2,2,2,2,2,2,2,2,2,0,0,0,0]
]
pieces["f"] = [
    [0,0,0,0,0,0,0,0,0,0,2,2,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,2,1,1,2,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,2,1,1,2,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,2,1,1,2,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,2,1,1,1,2,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,2,1,1,1,2,0,0,0,2,2,0,0,0,0],
    [0,0,0,0,0,2,1,1,1,1,2,0,0,2,1,1,2,0,0,0],
    [0,0,0,0,2,1,1,1,1,2,0,0,2,1,1,1,2,0,0,0],
    [0,0,0,0,2,1,1,1,1,2,0,0,2,1,1,1,2,0,0,0],
    [0,0,0,0,2,1,1,1,1,2,0,0,2,1,1,1,2,0,0,0],
    [0,0,0,0,2,1,1,1,1,2,2,2,2,1,1,1,2,0,0,0],
    [0,0,0,0,2,1,1,1,1,1,1,1,1,1,1,1,2,0,0,0],
    [0,0,0,0,2,1,1,1,1,1,1,1,1,1,1,1,2,0,0,0],
    [0,0,0,0,2,1,1,1,1,1,1,1,1,1,1,2,0,0,0,0],
    [0,0,0,0,0,2,1,1,1,1,1,1,1,2,0,0,0,0,0,0],
    [0,0,0,0,2,2,2,2,2,2,2,2,2,2,0,0,0,0,0,0],
    [0,0,0,0,2,1,1,1,1,1,1,1,1,1,1,2,0,0,0,0],
    [0,0,0,2,1,1,1,1,1,1,1,1,1,1,1,1,2,0,0,0],
    [0,0,0,2,1,1,1,1,1,1,1,1,1,1,1,1,2,0,0,0],
    [0,0,0,2,2,2,2,2,2,2,2,2,2,2,2,2,2,0,0,0]
]
pieces["t"] = [
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,2,2,0,0,0,2,2,2,2,0,0,0,2,2,0,0,0],
    [0,0,2,1,1,2,0,2,1,1,1,1,2,0,2,1,1,2,0,0],
    [0,0,2,1,1,2,2,2,1,1,1,1,2,2,2,1,1,2,0,0],
    [0,0,0,2,1,1,1,1,1,1,1,1,1,1,1,1,2,0,0,0],
    [0,0,0,2,1,1,1,1,1,1,1,1,1,1,1,1,2,0,0,0],
    [0,0,0,0,2,1,1,1,1,1,1,1,1,1,1,2,0,0,0,0],
    [0,0,0,0,0,2,1,1,1,1,1,1,1,1,2,0,0,0,0,0],
    [0,0,0,0,0,2,1,1,1,1,1,1,1,1,2,0,0,0,0,0],
    [0,0,0,0,0,2,1,1,1,1,1,1,1,1,2,0,0,0,0,0],
    [0,0,0,0,0,2,1,1,1,1,1,1,1,1,2,0,0,0,0,0],
    [0,0,0,0,0,2,1,1,1,1,1,1,1,1,2,0,0,0,0,0],
    [0,0,0,0,0,2,1,1,1,1,1,1,1,1,2,0,0,0,0,0],
    [0,0,0,0,0,2,1,1,1,1,1,1,1,1,2,0,0,0,0,0],
    [0,0,0,0,0,2,2,2,2,2,2,2,2,2,2,0,0,0,0,0],
    [0,0,0,0,2,1,1,1,1,1,1,1,1,1,1,2,0,0,0,0],
    [0,0,0,2,1,1,1,1,1,1,1,1,1,1,1,1,2,0,0,0],
    [0,0,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,0,0],
    [0,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,0,0],
    [0,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,0,0]
]
pieces["c"] = ["00000000000000000000",
"00000000220000000000",
"00000002112200000000",
"00000021111122000000",
"00000211111111200000",
"00002112211111120000",
"00002111111111112000",
"00021111111111111200",
"00211111122111111120",
"02111111202111111120",
"02111120021111111120",
"00222200211111111120",
"00000002111111111200",
"00000021111111111200",
"00000211111111112000",
"00000222222222222000",
"00002111111111111200",
"00021111111111111120",
"00021111111111111120",
"00022222222222222220"]
pieces["d"] = [
    [0,0,0,0,0,0,2,2,0,0,0,0,2,2,0,0,0,0,0,0],
    [0,0,0,0,0,2,1,1,2,0,0,2,1,1,2,0,0,0,0,0],
    [0,0,0,0,0,2,1,1,2,0,0,2,1,1,2,0,0,0,0,0],
    [0,2,2,0,0,0,2,1,2,0,0,2,1,2,0,0,0,2,2,0],
    [2,1,1,2,0,0,2,1,2,0,0,2,1,2,0,0,2,1,1,2],
    [2,1,1,2,0,0,2,1,1,2,2,1,1,2,0,0,2,1,1,2],
    [2,1,1,2,0,0,2,1,1,2,2,1,1,2,0,0,2,1,1,2],
    [0,2,1,1,2,0,2,1,1,1,1,1,1,2,0,2,1,1,2,0],
    [0,0,2,1,1,2,2,1,1,1,1,1,1,2,2,1,1,2,0,0],
    [0,0,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,0,0],
    [0,0,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,0,0],
    [0,0,0,2,1,1,1,1,1,1,1,1,1,1,1,1,2,0,0,0],
    [0,0,0,2,1,1,1,1,1,1,1,1,1,1,1,1,2,0,0,0],
    [0,0,0,0,2,1,1,1,1,1,1,1,1,1,1,2,0,0,0,0],
    [0,0,0,0,2,1,1,1,1,1,1,1,1,1,1,2,0,0,0,0],
    [0,0,0,2,2,2,2,2,2,2,2,2,2,2,2,2,2,0,0,0],
    [0,0,0,2,1,1,1,1,1,1,1,1,1,1,1,1,2,0,0,0],
    [0,0,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,0,0],
    [0,0,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,0,0],
    [0,0,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,0]
]
pieces["r"] = [
    "00000000022000000000",
    "00000002211220000000",
    "00000002111120000000",
    "00000002211220000000",
    "00000000211200000000",
    [0,0,2,2,2,2,2,2,2,1,1,2,2,2,2,2,2,0,0,0],
    [0,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,0],
    [2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2],
    [2,1,1,1,1,2,2,2,1,1,1,1,2,2,2,1,1,1,1,2],
    [2,1,1,1,2,0,0,0,2,1,1,2,0,0,0,2,1,1,1,2],
    [2,1,1,1,1,2,0,0,2,1,1,2,0,0,2,1,1,1,1,2],
    [0,2,1,1,1,1,2,0,2,1,1,2,0,2,1,1,1,1,2,0],
    [0,0,2,1,1,1,1,2,1,1,1,1,2,1,1,1,1,2,0,0],
    [0,0,0,2,1,1,1,1,1,1,1,1,1,1,1,1,2,0,0,0],
    [0,0,0,2,1,1,1,1,1,1,1,1,1,1,1,1,2,0,0,0],
    [0,0,0,0,2,2,2,2,2,2,2,2,2,2,2,2,0,0,0,0],
    [0,0,0,2,1,1,1,1,1,1,1,1,1,1,1,1,2,0,0,0],
    [0,0,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,0,0],
    [0,0,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,0,0],
    [0,0,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,0,0]]
castles={"white":[True,True],"black":[True,True]}
game={"T":[(0,0),(0,7)],"C":[(0,1),(0,6)],"F":[(0,2),(0,5)],
  "D":[(0,3)],"R":[(0,4)],"P":[(1,i) for i in range(8)],
  "t":[(7,0),(7,7)],"c":[(7,1),(7,6)],"f":[(7,2),(7,5)],
  "d":[(7,3)],"r":[(7,4)],"p":[(6,i) for i in range(8)]}
selected=(1,4)
origin=None
en_passant=None
turn="white"
dirty_cells=set()
temps={"white":int(input("Temps par joueur (min.) : "))*60}
temps["black"]=temps["white"]
bonus=int(input("Bonus par tour (sec.) : "))
h=monotonic()
def draw_empty_rect(x, y, w, h, t, c):
  ha = t//2
  fill_rect(x-ha,y-ha,w+t,t,c)
  fill_rect(x-ha,y+h-ha,w+t,t,c)
  fill_rect(x-ha,y+ha,t,h-1+t%2,c)
  fill_rect(x+w-ha,y+ha,t,h-1+t%2,c)
def show_piece(piece,i,j):
  x=13+j*25
  y=188-i*25
  col = color(220,220,220) if piece == piece.upper() else color(0,0,0)
  bor = color(0,0,0) if piece == piece.upper() else color(100,100,100)
  if piece.lower() in pieces:
    for a in range(len(pieces[piece.lower()])) :
      for b in range(len(pieces[piece.lower()][a])) :
        if int(pieces[piece.lower()][b][a]) == 1:fill_rect(x+a,y+b, 1, 1, col)
        elif int(pieces[piece.lower()][b][a]) == 2:fill_rect(x+a,y+b, 1, 1, bor)
def draw_cell(piece, i, j, what="piece") :
  if what == "piece" :
    fill_rect(10 + j * 25, 185 - i * 25, 25, 25, color(255, 255, 230) if (i+j)%2 else color(180, 238, 180))
    show_piece(piece, i, j)
  elif what == "legal_move" :
    fill_rect(10 + j * 25, 185 - i * 25, 25, 25, color(255, 255, 230) if (i+j)%2 else color(180, 238, 180))
    show_piece(piece, i, j)
  else:draw_empty_rect(10+25*j,185-25*i,24,24,1,color(255,255,230) if (i+j)%2 else color(180,238,180))
def legal_moves(i, j) :
    liste = []
    grid = [["" for _ in range(8)] for _ in range(8)]
    for piece in game:
      for place in game[piece]:
        grid[place[0]][place[1]] = piece
    if grid[i][j] != "" :
      for ni in range(8) :
        for nj in range(8) :
          if can_move(grid[i][j], grid, i, j, ni, nj, True) :
            if can_move(grid[i][j], grid, i, j, ni, nj) :
              liste.append((ni,nj))
    return liste
def show_legal_moves(i, j) :
    global dirty_cells
    for ni, nj in legal_moves(i, j) :
      fill_rect(19+nj*25,194-ni*25,8,8,color(255,255,0))
      dirty_cells.add(((ni, nj),"legal_move"))
def show_hour() :
  global temps
  fill_rect(250,50, 150, 150, color(255,255,255))
  t = [int(temps["white"]//60), int(temps["black"]//60)]
  t.append(int(temps["white"]-t[0]*60))
  t.append(int(temps["black"]-t[1]*60))
  t[0], t[1] = str(t[0]), str(t[1])
  t[2] = ("0" if t[2]<10 else "") + str(t[2])
  t[3] = ("0" if t[3]<10 else "") + str(t[3])
  draw_string(t[0]+":"+t[2],230,180)
  draw_string(t[1]+":"+t[3],230,30)
def show(total = False):
  global game, dirty_cells
  if total :
    fill_rect(0,0,300,300,color(255,255,255))
    for i in range(8):
      for j in range(8):
        draw_cell("", i, j)
    for piece in game:
      for i, j in game[piece]:
        show_piece(piece, i, j)
    draw_empty_rect(9,9,201,201,1,color(0,0,0))
  else :
    if str(total) == "0" :
      show_hour()
      return True
    grid = [["" for _ in range(8)] for _ in range(8)]
    for piece in game:
      for place in game[piece]:
        grid[place[0]][place[1]] = piece
    for ((i, j),s) in dirty_cells :
      draw_cell(grid[i][j], i, j, s)
    dirty_cells = set()
  y, x = selected
  draw_empty_rect(10 + 25 * x, 185 - 25 * y, 24, 24, 1, color(255, 0, 0))
  dirty_cells.add(((y, x), "bord"))
  if origin:
    i, j = origin
    draw_empty_rect(10 + 25 * j, 185 - 25 * i, 24, 24, 1, color(100, 0, 150))
    dirty_cells.add(((i, j),"bord"))
    show_legal_moves(i, j)
  else :
    i, j = selected
    show_legal_moves(i, j)
  show_hour()
  sleep(0.2)
def select():
  global selected, origin, h
  prev = selected
  temps[turn] -= monotonic() - h
  h = monotonic()
  while not keydown(KEY_OK):
    if monotonic()-1>h :
      temps[turn] -= monotonic()-h
      h = monotonic()
      if temps[turn] <= 0 :
        return "temps"
      show(0)
    if keydown(KEY_DOWN): selected = (max(selected[0] - 1, 0), selected[1])
    elif keydown(KEY_RIGHT): selected = (selected[0], min(selected[1] + 1, 7))
    elif keydown(KEY_LEFT): selected = (selected[0], max(selected[1] - 1, 0))
    elif keydown(KEY_UP): selected = (min(selected[0] + 1, 7), selected[1])
    elif keydown(KEY_BACK): origin = None; show()
    if selected != prev:
      prev = selected
      show(False)
  return selected
def can_move(piece, grid, i, j, ni, nj, check_only=False):
  global game, en_passant, castles
  d = (ni - i, nj - j)
  if not check_only and piece not in piece_color[turn]:
    return False
  if grid[ni][nj] in piece_color["white" if piece != piece.lower() else "black"] :
    return False
  if not check_only :
    grid_copy = [[a for a in b] for b in grid]
    grid_copy[i][j] = ""
    grid_copy[ni][nj] = piece
    if any("r" in l for l in grid_copy) and any("R" in l for l in grid_copy)  :
      if double_check(turn, grid_copy) :
        return False
    else :
      return False
  if piece.lower() == "p":
    direction = 1 if piece == "P" else -1
    start_row = 1 if piece == "P" else 6
    enemy = piece_color["black"] if piece == "P" else piece_color["white"]
    if d == (direction, 0) and grid[ni][nj] == "":
      return True
    elif d == (2 * direction, 0) and i == start_row and grid[ni][nj] == "" and grid[i + direction][j] == "":
      return True
    elif d in [(direction, -1), (direction, 1)] and (grid[ni][nj] in enemy or (en_passant and (ni, nj) == (en_passant[1], en_passant[2]))):
      if check_only:
        return True
      if en_passant and (ni, nj) == (en_passant[1], en_passant[2]):
        return "en passant"
      return True
  elif piece.lower() == "c":
    if d in moves["c"]:
      return True
  else:
    if d in moves[piece.lower()]:
      step = (int(d[0] / max(1, abs(d[0]))) if d[0] != 0 else 0,
              int(d[1] / max(1, abs(d[1]))) if d[1] != 0 else 0)
      pos = (i + step[0], j + step[1])
      while pos != (ni, nj):
        if grid[pos[0]][pos[1]] != "":
          return False
        pos = (pos[0] + step[0], pos[1] + step[1])
      return True
  if piece.lower() == "r":
    team = "white" if piece.isupper() else "black"
    row = 0 if team == "white" else 7
    if d == (0, -2) and castles[team][0] and all(grid[row][k] == "" for k in range(1, 4)):
      return True if check_only else "roque"
    elif d == (0, 2) and castles[team][1] and all(grid[row][k] == "" for k in range(5, 7)):
      return True if check_only else "roque"
  if (piece in piece_color["white"] and grid[ni][nj] in piece_color["white"]) or \
     (piece in piece_color["black"] and grid[ni][nj] in piece_color["black"]):
    return False
  return False
def double_check(team, grid = False):
  if not grid :
    grid = [["" for _ in range(8)] for _ in range(8)]
    for piece in game:
      for place in game[piece]:
        grid[place[0]][place[1]] = piece
    game_used = game
  else :
    game_used = {}
    for i in range(len(grid)) :
      for j in range(len(grid)) :
        if grid[i][j] != "" :
          if grid[i][j] not in game_used :
            game_used[grid[i][j]] = []
          game_used[grid[i][j]].append((i, j))
  king_pos = game_used["R" if team == "white" else "r"][0]
  for piece in game_used:
    if piece in piece_color["black" if team == "white" else "white"]:
      for i, j in game_used[piece]:
        if can_move(piece, grid, i, j, king_pos[0], king_pos[1], True):
          return True
  return False
def move():
  global game, origin, en_passant, turn, castles, h, dirty_cells
  grid = [["" for _ in range(8)] for _ in range(8)]
  for piece in game:
    for place in game[piece]:
      grid[place[0]][place[1]] = piece
  temps[turn] += bonus
  h = monotonic()
  try : i, j = select()
  except : return False
  while not (grid[i][j] in piece_color[turn] and len(legal_moves(i,j))) :
    try : i, j = select()
    except : return False
  origin = (i, j)
  show(False)
  piece = grid[i][j]
  sleep(0.2)
  try : ni, nj = select()
  except : return False
  while True :
    result = can_move(piece, grid, i, j, ni, nj)
    if result == False:
        if (ni,nj) == origin :
          origin = None
        elif grid[ni][nj] in piece_color[turn] :
            origin = (ni, nj)
            i, j = origin
        show(False)
        try : ni, nj = select()
        except : return False
    else : break
  temps[turn] -= (monotonic()-h)
  if piece == "T":
    if (i, j) == (0, 0): castles["white"][0] = False
    elif (i, j) == (0, 7): castles["white"][1] = False
  elif piece == "t":
    if (i, j) == (7, 0): castles["black"][0] = False
    elif (i, j) == (7, 7): castles["black"][1] = False
  if result == "en passant":
    game["P" if piece == "p" else "p"].remove((i, nj))
    dirty_cells.add(((i, nj),"piece"))
  elif result == "roque":
    row = 0 if turn == "white" else 7
    if nj == 2:
      game["T" if turn == "white" else "t"].remove((row, 0))
      game["T" if turn == "white" else "t"].append((row, 3))
      for c in range(5) :
        dirty_cells.add(((row, c),"piece"))
    elif nj == 6:
      game["T" if turn == "white" else "t"].remove((row, 7))
      game["T" if turn == "white" else "t"].append((row, 5))
      for c in range(4,8) :
        dirty_cells.add(((row, c),"piece"))
  if piece.lower() == "p" and abs(ni - i) == 2:
    en_passant = (ni, int((ni + i) / 2), nj)
  else:
    en_passant = None
  if grid[ni][nj] != "":
    game[grid[ni][nj]].remove((ni, nj))
    dirty_cells.add(((ni, nj),"piece"))
  game[piece].remove((i, j))
  dirty_cells.add(((i, j),"piece"))
  if (piece == "P" and ni == 7) or (piece == "p" and ni == 0):
    prom = True
  else:
    prom = False
    game[piece].append((ni, nj))
  if prom:
    draw_cell(" ", i, j)
    sleep(0.2)
    low = piece.islower()
    prom_pieces = ["D", "T", "F", "C"]
    idx = 0
    while not keydown(KEY_OK):
      if keydown(KEY_LEFT): idx = (idx - 1) % 4
      elif keydown(KEY_RIGHT): idx = (idx + 1) % 4
      p = prom_pieces[idx].lower() if low else prom_pieces[idx]
      draw_cell(p, ni, nj)
      sleep(0.2)
    game[p].append((ni, nj))
  turn = "black" if turn == "white" else "white"
  origin = None
  return True
def check_end() :
    ok=False
    for piece in piece_color[turn] :
        for i,j in game[piece] :
            if len(legal_moves(i,j))>0 :
                ok = True
    if not ok :
        fill_rect(0,0,350,300,color(255,255,255))
        if double_check(turn) :
            draw_string("Victoire des "+("blancs" if turn == "black" else "noirs") + " par mat",20,100)
        else:draw_string("Pat",100,100)
        return True
    w = [piece for _ in game[piece] for piece in piece_color["white"] if piece != "R"]
    b = [piece for _ in game[piece] for piece in piece_color["black"] if piece != "r"]
    if all(x not in w for x in ("d","t","p")) :
      if all(x not in b for x in ("d","t","p")) :
        if len(w)<=1 and len(b)<=1:
          if any(w==x[0] and b==x[1] for x in [([],[]), (["C"],[]), (["F"],[]), ([],["f"]), ([],["c"])]) or (w == ["F"] and b == ["f"] and (game["F"][0][0]+game["F"][0][1])%2 != (game["f"][0][0]+game["f"][0][1])%2) :
            fill_rect(0,0,350,300,color(255,255,255))
            draw_string("Nulle par manque de matériel", 20, 100)
def main():
  show(True)
  while True:
    if move():show(False)
    else:
      fill_rect(0,0,350,300,color(255,255,255))
      draw_string("Victoire des "+("blancs" if turn=="black" else "noirs")+" au temps.",20,100)
      break
    if check_end() :
      break
main()
