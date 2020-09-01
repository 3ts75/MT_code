def get_string(addr):
    out = []
    while True:
        if Byte(addr) != 0:
            out.append(int(Byte(addr)))
        else:
            break
        addr += 1
    return out

shell_addr = 0x404068
str_addr = 0x404040

shell = get_string(shell_addr)
str = get_string(str_addr)

print "shellcode:",
for i in range(len(shell)):
    print "{:02x}".format(shell[i]),
print ""

flag = ""
print "strings:",
for i in range(len(str)):
    print "{:02x}".format(str[i]),
    hoge = str[i] << 5
    fuga = str[i] >> 3
    piyo = 0xff & (hoge | fuga)
    flag += chr(piyo)
print ""

print flag
