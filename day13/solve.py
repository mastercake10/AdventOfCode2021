lines = list(map(lambda x: x.strip(), open("input", "r").readlines()))

pairs = [list(map(int, x.split(","))) for x in lines[:lines.index("")]]
instructions = lines[lines.index("")+1:]

for idx, ins in enumerate(instructions):    
    axis, at = ins.split(" ")[-1].split("=")
    axis = axis == "y"
    for pair in filter(lambda p: p[axis] >= int(at), pairs):
        pair[axis] = int(at)*2 - pair[axis]

    if idx == 0:
        # part 1
        pairs2 = set(tuple(x) for x in pairs)
        print(len(pairs2))


# part 2
pairs2 = set(tuple(x) for x in pairs)
for y in range(max(pairs)[1] + 1):
    s = ""
    for x in range(max(pairs)[0] + 1):
        if (x,y) in pairs2:
            s+="█"
        else:
            s+=" "
    print(s)
