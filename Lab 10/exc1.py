#Write a function get_reciprocal that returns the multiplicative inverse of a number
#discuss all side cases
#ex: input:3,  output: 1/3
#ex: input 2, output 1/2


def get_reciprocal(x):
    
    try:
        x = int("str")  # This will cause ValueError
        inv = 1 / x   # Inverse calculation
        
    except ValueError:
        print("Not Valid!")
        
    except ZeroDivisionError:
        print("Zero has no inverse!")
    
    return inv






# Write a program that takes a list.
# Then returns the sum of the first two elements
# Discuss all side cases
def example2():
    a = ["10", "twenty", 30]  # Mixed list of integers and strings
    try:
        total = int(a[0]) + int(a[1])  # 'twenty' cannot be converted to int
        
    except (ValueError, TypeError) as e:
        print("Error", e)
        
    except IndexError:
        print("Index out of range.")



# Write a program that reads a file and prints what is inside it
# Discuss all side cases and handle them
def open_and_read_file(file_name):
    f = open(file_name, 'r')
    content = f.read()
    return content


# Write a program that writes "LMAO" to a file
# Discuss all side cases and handle them