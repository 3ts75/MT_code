plain_file_name = ".\\windows7_sample_photo\\Chrysanthemum.jpg"
crypt_file_name = ".\\EncryptedFiles\\Pictures\\Sample Pictures\\Chrysanthemum.jpg_encrypted"
flag_crypt_file_name = ".\\EncryptedFiles\\Documents\\flag.txt_encrypted"

plain = bytearray(open(plain_file_name, "rb").read(0x20))
crypt = bytearray(open(crypt_file_name, "rb").read(0x20))

key = []

for i in range(len(plain)):
    key.append(plain[i] ^ crypt[i])

for i in range(len(key)):
    print "{:02x}".format(key[i]),
print ""

file_buf = bytearray(open(flag_crypt_file_name, "rb").read())

flag = ""
for i in range(len(file_buf)):
    flag += chr(file_buf[i] ^ key[i % 0x20])

print flag
