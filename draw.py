from kandinsky import *

def draw_line(x1, y1, x2, y2, color, thickness=1):
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    sx = 1 if x1 < x2 else -1
    sy = 1 if y1 < y2 else -1
    err = dx - dy
    
    for t in range(thickness):
        offset = t - thickness//2
        x = x1
        y = y1
        while True:
            if dx > dy:
                set_pixel(x, y + offset, color)
            else:
                set_pixel(x + offset, y, color)
            if x == x2 and y == y2:
                break
            e2 = 2 * err
            if e2 > -dy:
                err -= dy
                x += sx
            if e2 < dx:
                err += dx
                y += sy
                
def draw_circle(xc, yc, radius, thickness, color):
    for t in range(thickness):
        r = radius + t - thickness//2
        x = r
        y = 0
        err = 0
        while x >= y:
            set_pixel(xc + x, yc + y, color)
            set_pixel(xc + y, yc + x, color)
            set_pixel(xc - y, yc + x, color)
            set_pixel(xc - x, yc + y, color)
            set_pixel(xc - x, yc - y, color)
            set_pixel(xc - y, yc - x, color)
            set_pixel(xc + y, yc - x, color)
            set_pixel(xc + x, yc - y, color)
            if err <= 0:
                y += 1
                err += 2*y + 1
            if err > 0:
                x -= 1
                err -= 2*x + 1

def draw_empty_rect(x, y, width, height, thickness, color):
    draw_line(x-thickness, y-thickness, x + width + thickness, y + thcikness, color)
    draw_line(x-thickness, y-thickness, x + thickness, y + thickness + height, color)
    draw_line(x-thickness + width, y-thickness, x + thickness + width, y + thickness + height, color)
    draw_line(x-thickness, y-thickness + height, x + thickness + width, y + thickness + height, color)
