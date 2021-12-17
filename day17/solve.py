line = open("input", "r").readline()


x1, x2 = map(int, line.split(" ")[-2][2:-1].split(".."))
y1, y2 = map(int, line.split(" ")[-1][2:-1].split(".."))

def launch(vel_x, vel_y):

    pos_x = 0
    pos_y = 0

    max_height = pos_y
    
    for _ in range(1000):
        if pos_y > max_height:
            max_height = pos_y
            
        pos_x += vel_x
        pos_y += vel_y
        
        if vel_x > 0:
            vel_x -= 1
        
        vel_y -= 1
        
        if x1 <= pos_x <= x2 and y1 <= pos_y <= y2:
            return max_height, True
        
        if pos_x > x2 and pos_y > y2:
            break

    return 0, False

max_height = 0
velocities = set()
for x in range(1000):
    for y in range(-1000, 1000):
        height, reached = launch(x,y)
        if height > max_height:
            max_height = height
        if reached:
            velocities.add((x, y))

# part 1
print(max_height)

# part 2
print(len(velocities))
