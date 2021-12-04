lines = list(map(lambda x: x.strip(), open("input").readlines()))

lines.append(" ")

nums = list(map(int, lines[0].split(",")))

boards = []
rows = []
for line in lines[2:]:
    if not line.strip():
        boards.append(rows)
        rows = []
    else:
        rows.append(list(map(lambda x: int(x.strip()), filter(lambda y: y,line.split(" ")))))


winning = list()

def calcScore(board):
    s = 0
    for row in board:
        s+=sum(filter(lambda x: x != -1, row))
        
    return s


n_first = 0
for n in nums:
    for num, board in enumerate(boards):
        if num in winning:
            continue
        
        for row in board:
            for i, x in enumerate(row):
                if x == n:
                    row[i] = -1
                   
        for board in [board, zip(*board)]:
            for row in board:
                if all(map(lambda x: x == -1, row)):
                    if not winning:
                        n_first = n
                    winning.append(num)

    if len(set(winning)) == len(boards):
        # part 1
        print(calcScore(boards[winning[0]]) * n_first)
        # part 2
        print(calcScore(boards[winning[-1]]) * n)
        break
