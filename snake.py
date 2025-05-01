from kandinsky import *
from time import *
from random import *
from ion import *

t = (21,31)
#0:droite, 1:bas
d = 0
s= [(2,2)]
p = []

def add_p():
    global s, p, t
    if len(s+p) == t[0]*t[1] :
        return False
    new = (randint(0,t[0]-1) , randint(0,t[1]-1))
    while new in s+p :
        new = (randint(0,t[0]-1) ,randint(0,t[1]-1))
    p.append(new)
    return True

def move(dir) :
    global s, p, t
    l_dir = [(0,1), (1,0),(0,-1),(-1,0)]
    i,j = s[-1][0]+l_dir[dir][0], s[-1][1]+l_dir[dir][1]
    if 0 <= i < t[0] and 0 <= j < t[1] and (i,j) not in s[1:] :
        if (i,j) in p :
            p.remove((i,j))
            add_p()
        else :
            s.pop(0)
        s. append((i,j))
        return True
    else :
        return False

def find_dir() :
    if keydown(KEY_RIGHT) :
        return 0
    elif keydown(KEY_DOWN) :
        return 1
    elif keydown(KEY_LEFT) :
        return 2
    elif keydown(KEY_UP) :
        return 3
    return False

def screen() :
    global s, p, t
    fill_rect(5,5,t[1]*10,t[0]*10,color(0,0,0))
    for (i,j) in s[:-1] :
        fill_rect(j*10+5,i*10+5,10,10,color(0,255,0))
    fill_rect(s[-1][1]*10+5,s[-1][0]*10+5,10,10,color(0,200,0))
    for (i,j) in p :
        fill_rect(j*10+5,i*10+5,10,10,color(255,0,0))
    draw_string("Score : "+str(len(s)-1),100,205)

add_p()
add_p()
add_p()

while True :
    screen()
    sleep(0.2)
    if type(find_dir ()) == int and abs(find_dir()-d) != 2 :
        d = find_dir ()
    ok = move (d)
    if not ok :
        break
draw_string("PERDU",100,115)
print ("Fin")
print ("Score :", len(s)-1)
