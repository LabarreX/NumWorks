from time import *
from kandinsky import *
from ion import *
from draw import *

grid = [[" " for _ in range(6)] for _ in range(7)]
selected = 4
player = "X"
dispo = {i:0 for i in range(7)}

def show () :
  global grid, selected
  fill_rect(0,0,300,300,color(255,255,255))
  for i in range(7) :
    fill_rect(40,20+i*30,211,1,color(0,0,0))
  for i in range(8) :
    fill_rect(40+i*30,20,1,181,color(0,0,0))
  for i in range(6) :
    for j in range(7) :
      draw_string(grid[j][i],50+30*j,177-30*i)
  x, y = selected, dispo[selected]
  if y < 6 :
    draw_empty_rect(40+30*x,170-30*y,30,30,3,color(255,0,0))
  sleep(0.1)

def select() :
  global selected
  prev_s = selected
  while not dispo[selected] < 6 or not keydown(KEY_OK) :
    if keydown(KEY_RIGHT) :
      selected = min(selected+1,6)
      while dispo[selected] == 6 :
        selected = min(selected+1,6)
    elif keydown(KEY_LEFT) :
      selected = max(selected-1,0)
      while dispo[selected] == 6 :
        selected = max(selected-1,0)

    if selected != prev_s :
      prev_s = selected
      show()
  return selected     

def win(x,y) :
  global grid
  DIRS = [(1,0),(1,1),(0,1),(-1,1)]
  for dir in DIRS :
    i, j = dir
    l = 0
    while grid[i*l+x][j*l+y] == player :
      l += 1
      if not ( 0 <= i*l+x < 7 and 0 <= j*l+y < 6 ) :
        break
    start = (55 + 30*(i*(l-1)+x), 185 - 30*(j*(l-1)+y))
    ll = 0
    while grid[-i*ll+x][-j*ll+y] == player :
      ll += 1
      if not ( 0 <= -i*ll+x < 7 and 0 <= -j*ll+y < 6 ) :
        break
    end = (55 + 30*(-i*(ll-1)+x), 185 - 30*(-j*(ll-1)+y))
    if l+ll >= 5 :
      draw_line(start[0],start[1],end[0],end[1],4,color(255,0,0))
      return True
  return False

while True :
  show()
  select()
  grid[selected][dispo[selected]] = player
  draw_string(grid[selected][dispo[selected]],50+30*selected,177-30*dispo[selected])
  if win(selected,dispo[selected]) :
    break
  dispo[selected] += 1
  player = "X" if player == "O" else "O"
  sleep(0.1)
  

draw_string(player,270,100)
draw_string("won !",265,115)
print(player, "won")
