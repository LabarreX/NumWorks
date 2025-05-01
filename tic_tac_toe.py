from time import *
from kandinsky import *
from ion import *
from draw import *


grid = [[" " for _ in range(3)] for _ in range(3)]
selected = (1,1)
player = "X"

def show () :
  global grid, selected
  fill_rect(0,0,300,300,color(255,255,255))
  for i in range(4) :
    fill_rect(40,20+i*60,181,1,color(0,0,0))
  for i in range(4) :
    fill_rect(40+i*60,20,1,181,color(0,0,0))
  for i in range(3) :
    for j in range(3) :
      draw_string(grid[i][j],65+j*60,160-i*60)
  y,x = selected
  draw_empty_rect(40+60*x,140-60*y,60,60,4,color(255,0,0))
  sleep(0.1)

def select() :
  global selected
  prev_s = selected
  while not keydown(KEY_OK) :
    if keydown(KEY_DOWN) :
      selected = (max(selected[0]-1,0),selected[1])
    elif keydown(KEY_RIGHT) :
      selected = (selected[0],min(selected[1]+1,2))
    elif keydown(KEY_LEFT) :
      selected = (selected[0],max(selected[1]-1,0))
    elif keydown(KEY_UP) :
      selected = (min(selected[0]+1,2),selected[1])

    if selected != prev_s :
      prev_s = selected
      show()
  return selected
    
def win() :
  for i in range(3) :
    if all(grid[i][j] == player for j in range(3)) :
      draw_line(68,168-i*60,193,168-i*60,3,color(255,0,0))
      return True
  for j in range(3) :
    if all(grid[i][j] == player for i in range(3)) :
      draw_line(190-j*60,168,190-j*60,48,3,color(255,0,0))
      return True
  if all(grid[i][i] == player for i in range(3)) :
    draw_line(70,168,190,48,3,color(255,0,0))
    return True
  if all(grid[i][2-i] == player for i in range(3)) :
    draw_line(70,48,190,168,3,color(255,0,0))
    return True
  return False
      
      
while True :
  show()
  i, j = select()
  if grid[i][j] == " " :
    grid[i][j] = player
    draw_string(grid[i][j],65+j*60,160-i*60)
    if win() :
      break
    player = "X" if player == "O" else "O"
  sleep(0.1)


draw_string(player+" won !",240,100)
print(player, "won")
