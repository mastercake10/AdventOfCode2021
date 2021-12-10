from functools import reduce

arr = list(map(lambda x: [int(y) for y in x.strip()], open("input", "r").readlines()))

total_lows = 0

found = []
def find(x, y):
    if x > len(arr[0])-1 or x < 0:
        return
    if y > len(arr)-1 or y < 0:
        return
    
    if [x,y] in found:
        return
    
    if arr[y][x] != 9:
        found.append([x,y])

        find(x+1, y)
        find(x-1, y)
        find(x, y+1)
        find(x, y-1)

basins = []

for y in range(len(arr)):
    for x in range(len(arr[0])):
        if (x == len(arr[0]) - 1 or arr[y][x] < arr[y][x + 1]) and (x == 0 or arr[y][x] < arr[y][x - 1]):
            if (y == len(arr) - 1 or arr[y][x] < arr[y + 1][x]) and (y == 0 or arr[y][x] < arr[y - 1][x]):
                total_lows += arr[y][x] + 1
                
                found = []
                find(x, y)
                basins.append(len(found))


# part 1
print(total_lows)

# part 2
print(reduce((lambda x, y: x * y), sorted(basins)[-3:]))
