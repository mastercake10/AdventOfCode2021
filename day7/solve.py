line = open("input", "r").readlines()[0]

values = list(map(int, line.split(",")))

def solve(fn):
    heights = {}
    for i in range(min(values), max(values)):
        costs = 0
        for val in values:
            n = abs(val - i)
            costs += fn(n)
            
        heights[i] = costs
        
    return min(heights.values())

# part 1
print(solve(lambda n: n))

# part 2
print(solve(lambda n: n*(n+1)//2))
