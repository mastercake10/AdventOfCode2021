lines = list(map(lambda x: x.strip(), open("input", "r").readlines()))

pairs = [x.split("-") for x in lines]
pairs2 = []
for pair in pairs:
    pairs2.append(pair[::-1])
    
pairs.extend(pairs2)

def follow(s1, path=[], part1=True):
    global cnt
    path = path.copy()
    path.append(s1)

    if s1 == "end":
        cnt+=1
        return

    for pair in pairs:
        if pair[0] == s1 and pair[1] != "start":
            one_duplicate = len(list(filter(str.islower, path))) - len(set(filter(str.islower, path))) < 2
            if (path.count(pair[1]) < (1 if part1 else 2) and (one_duplicate or part1)) or pair[1].isupper():
                follow(pair[1], path=path, part1=part1)
    return cnt

# part 1
cnt = 0
follow("start")
print(cnt)

#part 2
cnt = 0
follow("start", part1=False)
print(cnt)
