lines = list(map(lambda x: x.strip(), open("input").readlines()))

def birange(x, y):
    if x > y:
        return range(x, y-1, -1)
    return range(x, y+1)

def put(f, field):
    if f in field:
        field[f] = field[f] + 1
    else:
        field[f] = 1

def solve(part2):
    field = {}
    
    for e in lines:
        x1, y1 = map(int, e.split("->")[0].strip().split(","))
        x2, y2 = map(int, e.split("->")[1].strip().split(","))
        
        if x1 == x2:
            for y_ in birange(y1, y2):
                put((x1, y_), field)
        elif y1 == y2:
            for x_ in birange(x1, x2):
                put((x_, y1), field)
        elif part2:
            for u in list(zip(birange(x1, x2), birange(y1, y2))):
                put(u, field)
    
    cnt = len(list(filter(lambda x: x > 1, field.values())))
    
    return cnt

print(solve(False))
print(solve(True))
