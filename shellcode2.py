def get_string(addr):
    out = []
    while True:
        if Byte(addr) == 0xc6:
            if Byte(addr+1) == 0x45:
                out.append(int(Byte(addr+3)))
        else:
            break
        addr += 4
    return out
            

start_addr = 0x402284
dos = "This program cannot be run in DOS mode"

str = get_string(start_addr)

for i in range(len(str)):
    print "{:02x}".format(str[i]),
print ""

flag = ""
for i in range(len(str)):
    flag += chr(str[i] ^ ord(dos[i]))

print flag
