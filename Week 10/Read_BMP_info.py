#This file opens a bitmap image (.bmp) and tries to parse the header.
#The parsed fields are (Width, Height, Bytes offset)
#You should also read the Bits_Per_Pixel
#We are following the bmp file structure from this link: https://upload.wikimedia.org/wikipedia/commons/7/75/BMPfileFormat.svg


#Open the file as binary, then read its contents
f = open('doggy.bmp', 'rb')
file_content = f.read()
print(file_content)

#Extract the width and height fields, which are at offsets 18 and 22 respectively, each one spans 4 bytes
width = int.from_bytes(file_content[18 : 22], byteorder='little')
height = int.from_bytes(file_content[22 : 26], byteorder='little')
#The "byteorder='little'" is to tell python to treat the LSB in the lower address and the MSB at the higher address.
print(width)
print(height)

#Extracting the offset of pixel data, they are the offset of pixels from the beginning of the file.
#This offset is recorded at the 10th byte, spanning 4 bytes
bytes_offset = int.from_bytes(file_content[10 : 14], byteorder='little')

print(f"The image size is {width} x {height} = {width*height}")
print(f"The pixels' offset {bytes_offset}")

#Change the file_content into a list to be able to modify them
file_content = list(file_content)



#Extracting the bits per pixel (note: a single pixel can have 8 bits -greyscale images- or 32 bits -colored images-)
bits_per_pixel = int.from_bytes(file_content[28 : 30], byteorder='little')
bytes_per_pixel = bits_per_pixel // 8


#modify all bytes, make them all Red
NumBytes = bits_per_pixel * width * height // 8
for i in range(0, NumBytes, bytes_per_pixel):
    file_content[bytes_offset + i] = 0  #This is the Blue channel
    file_content[bytes_offset + i + 1] = 0  #Make the green channel as 0
    file_content[bytes_offset + i + 2] = int('11111111', 2) #Make the red channel as much red as possible
    #I left the Alpha channel as it is



#modify the first 1000 pixels, make them blue
for i in range(0, 1000 * bytes_per_pixel, bytes_per_pixel):
    file_content[bytes_offset + i] = int('11111111', 2)  #This is the Blue channel
    file_content[bytes_offset + i + 1] = 0  #Make the green channel as 0
    file_content[bytes_offset + i + 2] = 0 #This is the red channel


#write the new bmp into a new image
f = open('newimg.bmp', 'wb')
f.write(bytes(file_content))