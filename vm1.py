reg = 0

def get_code(addr, size):
    out = []
    for i in range(size):
        out.append(int(Byte(addr + i)))
    return out
    
start_addr = 0x404040
code_size = 0x1fb

dst = get_code(start_addr, code_size)
    
for i in range(len(dst)):
    print "{:02x}".format(dst[i]),
print "\n"

i = 0
while True:
    op1 = dst[i + 255]
    op2 = dst[i + 256]
    op3 = dst[i + 257]
    if op1 == 1:
        dst[op2] = op3
    elif op1 == 2:
        reg = dst[op2]
    elif op1 == 3:
        dst[op2] ^= reg
    else:
        break
    i += 3

flag = ""
for i in range(len(dst)):
    flag += chr(dst[i])
print flag
