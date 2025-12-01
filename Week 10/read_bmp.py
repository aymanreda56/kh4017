f = open('doggy.bmp', 'rb')
file_contents = f.read()

# print(file_contents)

# print(file_contents[0]) #first byte

width = int.from_bytes(file_contents[18: 22], byteorder='little')
height = int.from_bytes(file_contents[22: 26], byteorder='little')
bits_per_pixel = int.from_bytes(file_contents[28: 30], byteorder='little')
bytes_per_pixel = bits_per_pixel // 8
pixels_offset = int.from_bytes(file_contents[10: 14], byteorder='little')

print(width)
print(height)
print(bits_per_pixel)



print(file_contents[pixels_offset : pixels_offset + bits_per_pixel])

file_contents = list(file_contents) #casting to a list
for i in range(0, width * height * bytes_per_pixel //2, 4):
    file_contents[pixels_offset + i] = 0
    file_contents[pixels_offset + i + 1] = 0
    file_contents[pixels_offset + i + 2] = 255
    file_contents[pixels_offset + i + 3] = 255

for i in range(width * height * bytes_per_pixel //2, width * height * bytes_per_pixel, 4):
    file_contents[pixels_offset + i] = 255
    file_contents[pixels_offset + i + 1] = 0
    file_contents[pixels_offset + i + 2] = 0
    file_contents[pixels_offset + i + 3] = 255


f = open('result.bmp', 'wb')
f.write(bytes(file_contents))