from functools import reduce
import operator

expr = [operator.add, operator.mul, min, max, None, operator.gt, operator.lt, operator.eq]

version_sum = 0
def parse(bits):
    global version_sum
    
    version = int(bits[0:3], 2)
    type_id = int(bits[3:6], 2)
    
    version_sum += version
    
    if type_id == 4: #literal
        idx = 6
        res = ""
        while True:
            group = bits[idx+1:idx+5]
            res += group
                
            if not int(bits[idx]):
                # end of packet reached
                return idx + 5, int(res, 2)
            
            idx += 5
        
    else: #operator
        idx = 6
        lenght_type_id = int(bits[idx], 2)
        
        sub_values = []
        
        if lenght_type_id == 0:
            idx += 1
            sub_packet_length = int(bits[idx:idx+15], 2)
            idx += 15
            
            total_bits = 0
            while total_bits < sub_packet_length:
                offset, val = parse(bits[idx:])
                sub_values.append(val)
                
                idx += offset
                total_bits += offset
        else:
            idx += 1
            sub_packet_length = int(bits[idx:idx+11], 2)
            idx += 11
            
            for _ in range(sub_packet_length):
                offset, val = parse(bits[idx:])
                sub_values.append(val)
                
                idx += offset
        
        res = int(reduce(expr[type_id], sub_values))
        
        return idx, res
                        

line = open("input", "r").readline()

bits = bin(int('1'+line, 16))[3:]
res = parse(bits)

# part 1
print(version_sum)

# part 2
print(res[1])
