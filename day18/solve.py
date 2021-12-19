import math

def search(t, nested):
    if isinstance(t, list):
            
        nested.append(t)
        for s in t:
            l = search(s, nested.copy())
            if isinstance(l[-1][0], int) and isinstance(l[-1][1], int):
                if len(l) == 5:
                    return l
            
    return nested

def explode(t):
    nested = search(t, [])

    if len(nested) < 2:
        return
    
    explodingPair = nested[-1]

    for i in range(len(nested)-1, 0, -1):
        if nested[i] in nested[i-1]:
            u = nested[i-1].index(nested[i])
            if u < len(nested[i-1])-1:

                if isinstance(nested[i-1][u+1], int):
                    nested[i-1][u+1] += explodingPair[1]
                else:
                    a = nested[i-1][u+1]
                    while isinstance(a[0], list):
                        a = a[0]
                    a[0] += explodingPair[1]
                break
                
    for i in range(len(nested)-1, 0, -1):
        if nested[i] in nested[i-1]:
            u = nested[i-1].index(nested[i])
            if u > 0:
                if isinstance(nested[i-1][u-1], int):
                    nested[i-1][u-1] += explodingPair[0]
                else:
                    a = nested[i-1][u-1]
                    while isinstance(a[-1], list):
                        a = a[-1]
                    a[-1] += explodingPair[0]
                break
    nested[-2][nested[-2].index(nested[-1])] = 0
        
def split(l):
    for idx, s in enumerate(l):
        if isinstance(s, int):
            if s >= 10:
                l[idx] = [math.floor(s/2), math.ceil(s/2)]
                return True
        if isinstance(s, list):
            if split(s):
                return True
                

def calcMagnitude(l):
    return eval(str(l).replace("[", "(3*").replace(",", "+").replace("]", "*2)"))

def calcSum(t):
     while True:
        t_ = str(t)
        while True:
            t_ = str(t)
            explode(t)
            
            if str(t) == t_:
                break
            
        split(t)
        if str(t) == t_:
            break

lines = list(map(lambda x: eval(x.strip()), open("input", "r").readlines()))


# part 1
t = lines[0]
for line in lines[1:]:
    a = line
    t = [t] + [a]
    calcSum(t)
    
    
print(calcMagnitude(t))


# part 2
sums = []
for line1 in lines:
    for line2 in lines:
        t = [line1] + [line2]
        calcSum(t)
        sums.append(calcMagnitude(t))
        
print(max(sums))
