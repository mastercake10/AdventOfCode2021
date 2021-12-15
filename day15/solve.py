arr = list(map(lambda x: [int(y) for y in x.strip()], open("input", "r").readlines()))

def get_neighbors(src):
    neighbors = []
    if src[0] > 0:
        neighbors.append((src[0] - 1, src[1]))
    if src[0] < len(arr[0]) - 1:
        neighbors.append((src[0] + 1, src[1]))
    if src[1] > 0:
        neighbors.append((src[0], src[1] - 1))
    if src[1] < len(arr) - 1:
        neighbors.append((src[0], src[1] + 1))
                           
    return neighbors

def dijkstra(arr, src):
    queue = [src]
    minDistances = {}
    for y in range(len(arr)):
        for x in range(len(arr[0])):
            minDistances[(x, y)] = float("inf")
            
    minDistances[src] = 0

    while queue:
        currentNode = queue.pop(0)
        for neighbor in get_neighbors(currentNode):
            newDist = minDistances[currentNode] + arr[neighbor[1]][neighbor[0]]
            

            if newDist < minDistances[neighbor]:
                minDistances[neighbor] = min(newDist, minDistances[neighbor])
                queue.append(neighbor)

    return minDistances
    

# part 1
minDistances = dijkstra(arr, (0,0))
print(minDistances[len(arr)-1, len(arr)-1])

for y in range(len(arr)):
    original = arr[y]
    new_row = []
    for i in range(5):
        new_row.extend([x+i if x+i < 10 else x+i-9 for x in original.copy()])
    arr[y] = new_row

height = len(arr)
for i in range(1,5):
    for y in range(height):
        original = arr[y]
        new_row = [x+i if x+i < 10 else x+i-9 for x in original.copy()]
        arr.append(new_row)

# part 2
minDistances = dijkstra(arr, (0,0))
print(minDistances[len(arr)-1, len(arr)-1])
