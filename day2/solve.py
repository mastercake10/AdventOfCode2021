lines = list(map(lambda x: x.strip(), open("input").readlines()))

# part 1
hp, dp = 0, 0
for line in lines:
    d, i = line.split()
    i = int(i)
    
    if d == "forward":
        hp += i
    if d == "down":
        dp += i
    if d == "up":
        dp -= i
        
print(hp*dp)


# part 2
hp, dp, aim = 0, 0, 0
for line in lines:
    d, i = line.split()
    i = int(i)
    
    if d == "forward":
        hp += i
        dp += aim*i
    if d == "down":
        aim += i
    if d == "up":
        aim -= i
        
print(hp*dp)
