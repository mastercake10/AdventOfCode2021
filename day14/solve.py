lines = list(map(lambda x: x.strip(), open("input", "r").readlines()))

template = lines[0]
translation = {}
for line in lines[2:]:
    line = line.split(" ")
    translation[line[0]] = line[2]

def solve(n=40):
    
    pairs = {}
    for i in range(len(template)-1):
        p = template[i] + template[i+1]
        if p not in pairs:
            pairs[p] = 1
        else:
            pairs[p] += 1
        
    for i in range(n):
        pairs2 = {}
        for p in pairs:

            p2 = p[0] + translation[p]
            if p2 not in pairs2:
                pairs2[p2] = pairs[p]
            else:
                pairs2[p2] += pairs[p]
                
            p2 = translation[p] + p[1]
            if p2 not in pairs2:
                pairs2[p2] = pairs[p]
            else:
                pairs2[p2] += pairs[p]
        pairs = pairs2
    
    counted = {template[0]: 1}

    for p in pairs:
        if p[1] in counted:
            counted[p[1]] += pairs[p]
        else:
            counted[p[1]] = pairs[p]

    print(max(counted.values()) - min(counted.values()))

# part 1
solve(10)

# part 2
solve(40)
