lines = list(map(lambda x: x.strip(), open("input", "r").readlines()))

d = ["()", "{}", "<>", "[]"]

scores_1 = [3, 1197, 25137, 57]
scores_2 = [1, 3, 4, 2]

total_score_1 = 0
total_score_2 = []

for s in lines:

    while any([a in s for a in d]):
        for a in d:
            s = s.replace(a, "")
            
    line_score = 0
    for i in range(len(s)-1):
        if s[i] in map(lambda x: x[0], d) and s[i + 1] in map(lambda x: x[1], d):

            line_score = scores_1[list(map(lambda x: x[1], d)).index(s[i + 1])]
    
    line_score_2 = 0
    if line_score == 0:
        for c in reversed(s):
            line_score_2 = line_score_2 * 5 + scores_2[list(map(lambda x: x[0], d)).index(c)]
            
        total_score_2.append(line_score_2)
    
    total_score_1 += line_score
    
# part 1
print(total_score_1)

# part 2
print(sorted(total_score_2)[len(total_score_2) // 2])
