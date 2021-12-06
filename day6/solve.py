line = open("input", "r").readlines()[0]


def solve(cycles):
    states = [0]*10
    for num in list(map(int, line.split(","))):
        states[num] += 1
    
    for _ in range(cycles):
        
        prev = states[0]
        for state in range(0, 9):
            states[state-1] = states[state]
            
        states[6] += prev
        states[8] = prev
        states[9] = 0
        
    return sum(states)

# part 1
print(solve(80))
# part 2
print(solve(256))
