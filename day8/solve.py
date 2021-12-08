lines = [line.strip() for line in open("input", "r").readlines()]


digits = {"abcefg": 0, "cf": 1, "acdeg": 2, "acdfg": 3, "bcdf": 4, "abdfg": 5, "abdefg": 6, "acf": 7, "abcdefg": 8, "abcdfg": 9}

total_sum = 0
unique_digit_count = 0

for line in lines:

    signals = list(map(set, sorted(line.split(" | ")[0].split(" "), key=lambda x: len(x))))
    wire_map = {}
    
    # substract 1 from 7 to get a
    seg_a = list(signals[1].difference(signals[0]))[0]
    wire_map[seg_a] = "a"
    
    # find 6 and subtract 1 to get c and f
    digit_6 = list(filter(lambda x: len(x) == 6 and not signals[0].issubset(x), signals))[0]
    seg_f = list(digit_6.intersection(signals[0]))[0]
    wire_map[seg_f] = "f"
    
    seg_c = list(signals[0].difference(seg_f))[0]
    wire_map[seg_c] = "c"
    #wire_map[list(signals[0])[0]] = "c"
    
    # get b and e from 5 digit numbers
    digit_2 = list(filter(lambda x: len(x) == 5 and not set(seg_f).issubset(x), signals))[0]
    digit_5 = list(filter(lambda x: len(x) == 5 and not set(seg_c).issubset(x), signals))[0]
    digit_3 = list(filter(lambda x: len(x) == 5 and set([seg_c, seg_f]).issubset(x), signals))[0]
    seg_e = list(digit_2.difference(digit_3))[0]
    seg_b = list(digit_5.difference(digit_3))[0]
    wire_map[seg_e] = "e"
    wire_map[seg_b] = "b"
    
    # find 4, subtract 1 and intersect with 3 to get d
    digit_4 = list(filter(lambda x: len(x) == 4, signals))[0]
    seg_d = list(digit_4.difference(signals[0]).intersection(digit_3))[0]
    wire_map[seg_d] = "d"
    
    # subtract digit 4 and seg a from digit 3 to get g
    seg_g = list(digit_3.difference(digit_4).difference(seg_a))[0]
    wire_map[seg_g] = "g"
    
    output = ""
    for num in line.split(" | ")[1].split(" "):
        translated = ""
        for c in num:
            digit = wire_map[c]
            translated += digit
            
        digit_num = digits["".join(sorted(translated))]
        if digit_num in [1, 4, 7, 8]:
            unique_digit_count += 1
        output += str(digit_num)
            
    total_sum += int(output)
    
# part 1
print(unique_digit_count)

# part 2
print(total_sum)
