try:
    f = open('lol.txt', 'rb')
except:
    print('file open error')


content = f.read()

print(type(content))
content = bytearray(content)

new_content = []
for b in content: #for each byte
    #forcing zero in the LSB
    # x = 0b00000001
    # x = ~x #0b11111110
    # b = b & x
    # new_content.append(b)

    #forcing 1 in the LSB
    x = 1
    b = b | x
    new_content.append(b)


f = open('result.txt', 'wb')
f.write(bytearray(new_content))
