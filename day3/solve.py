lines_ = list(map(lambda x: x.strip(), open("input").readlines()))

def mostFreq(list, idx):
    entries = []
    for line in list:
        entries.append(line[idx])
    
    if entries.count("1") >= entries.count("0"):
        return "1"
    
    return "0"

# part1

gamma = ""
epsilon = ""
for i in range(len(lines_[0])):
    gamma += mostFreq(lines_, i)
    epsilon += "0" if int(mostFreq(lines_, i)) else "1"

gamma = int(gamma, 2)
epsilon = int(epsilon, 2)

print(gamma * epsilon)

# part2

def calc(s1, s2):
    lines = lines_
    for i in range(len(lines_[0])):
        c = s1 if int(mostFreq(lines, i)) else s2

        lines = list(filter(lambda x: x[i] == c, lines))
        if len(lines) == 1:
            break
    return int(lines[0], 2)

oxygen = calc("1", "0")
co2 = calc("0", "1")

print(oxygen * co2)
