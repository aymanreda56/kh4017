#Make a binary integer
x = 0b1 #1 in binary
x = 0b10 #2 in binary
x = 0b100 #4 in binary


#Bitwise and
x = 0b11111111
y = 0b00001111
result = x & y #this is bitwise and
print(result)

#printing the integer representation of an integer:
print(bin(result)) # <--- THIS RETURNS A STRING, not an integer because '0b1111' != 0b1111



#Bitwise OR
x = 0b11111111
y = 0b00001111
result = x | y #this is bitwise OR
print(result)


#Bitwise NOT
x = 0b11111111
negative_x = ~x #this is bitwise NOT


result = x & negative_x
print(bin(result))


#Bitwise Shift
a = 10  # 0000 1010 (Binary)
b = -10 # 1111 0110 (Binary)
print ("bitwise right shift operator")
print("a >> 1 =", bin(a >> 1))
print("b >> 1 =", bin(b >> 1))      #NOTE that right shifting preserves the sign bit



#left Shifting
a = 5
b = -10
# print bitwise left shift operator
print("a << 1 =", a << 1)
print("b << 1 =", b << 1)          #NOTE Right Shifting puts Zeros on the right


# Forcing a 1 in a specific bit location
# What if we have a binary integer of 0bxxx0xxxx and we want to make the 5th bit (this 0) and turn it into 1 without affecting other bits
# an approach is to OR this integer with 00010000
x = 0b10101010 #This is the binary integer whose 5th bit should be forced to be 1
y = 1 << 4 # This is simply 1, shifting right by 4 positions, so the resulting binary is 10000
result = x | y
print(f"Before forcing 1 in the 5th bit: {bin(x)}")
print(f"After Forcing 1 in the 5th bit: {bin(result)}")


# Forcing a 0 in a specific bit location
# What if we have a binary integer of 0bxxx1xxxx and we want to make the 5th bit (this 1) and turn it into 0 without affecting other bits
# an approach is to AND this integer with 11101111
x = 0b10111011 #This is the binary integer whose 5th bit should be forced to be 1
y = 1 << 4 # This is simply 1, shifting right by 4 positions, so the resulting binary is 10000
y = ~y #Bitwise flipping
result = x & y
print(f"Before forcing 0 in the 5th bit: {bin(x)}")
print(f"After Forcing 0 in the 5th bit: {bin(result)}")





# Create a bytearray from a string
ba = bytearray("Geeks for geeks!", "utf-8")
print(ba)  # Output: bytearray(b'geeks for geeks!')

# Modify the bytearray 
ba[1] = 105  # 'i' in ASCII is 105
print(ba)


#Creating a Byte Array from an integer
ba = bytearray(4)
print(ba)        
print(len(ba))   
ba[0] = 65       
print(ba)



#Creating a Byte array after encoding
#explain the encoding process
ba = bytearray("Hello", "utf-8")
print(ba)         
print(len(ba))    
ba[1] = 105       
print(ba)



#Creating a Byte array from a list of integers
ba = bytearray([72, 101, 108, 108, 111])
print(ba)         
print(len(ba))   
ba[0] = 87       
print(ba)





#Requirement:
# 1- Make a txt file, containiing "Hello World"
# 2- Change the least significant bit of each byte to 0 (Force zero to the LSB)
# 3- Write the file back to the file system
# 4- try to open it again