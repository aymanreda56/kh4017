from my_own_functions import *
message = input("please enter a message")
image_path = input("please enter the path of the image")
f = open(image_path, 'rb')
content = f.read()
print(content)
result = modify_bits(content)
f = open('result.bmp', 'wb')
f.write(result)