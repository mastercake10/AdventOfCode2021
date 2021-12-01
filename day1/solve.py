import math

lines = open("input", "r").readlines()

def occ(vals):
    prev = 1000000
    cnt = 0
    for i in vals:
            if i > prev:
                cnt += 1
            prev = i
    return cnt

prev = 1000000
s1, s2, s3 = 0, 0, 0
s = []
for line in lines:
    curr = int(line)
    s3 = s2
    s2 = s1
    s1 = curr
    s.append(s1 + s2 +s3)
    

print(occ(map(int,lines)))
print(occ(s[2:]))
