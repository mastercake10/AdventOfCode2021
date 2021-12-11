arr = list(map(lambda x: [int(y) for y in x.strip()], open("input", "r").readlines()))


def flash(x, y):
    if x >= len(arr[0]) or y >= len(arr):
        return
    if x < 0 or y < 0:
        return
    if arr[y][x] == -1:
        return
    
    arr[y][x] += 1
    if arr[y][x] > 9:
        arr[y][x] = -1
        flash(x + 1, y)
        flash(x, y + 1)
        flash(x - 1, y)
        flash(x, y - 1)
        flash(x + 1, y + 1)
        flash(x - 1, y - 1)
        flash(x + 1, y - 1)
        flash(x - 1, y + 1)
        

def step():
    for x in range(len(arr[0])):
        for y in range(len(arr)):
            arr[y][x] +=1
            
    for x in range(len(arr[0])):
        for y in range(len(arr)):
            if arr[y][x] > 9:
                flash(x,y)
                
    flashes = 0
    for x in range(len(arr[0])):
        for y in range(len(arr)):
            if arr[y][x] == -1:
                arr[y][x] = 0
                flashes += 1
    return flashes


total_flahes = sum([step() for i in range(100)])
print(total_flahes)

flahes_per_step = 0
step_cnt = 0
while flahes_per_step != len(arr[0])**2:
    flahes_per_step = step()
    step_cnt += 1
    
print(step_cnt+100)
    
