#Write a function get_reciprocal that returns the multiplicative inverse of a number
#discuss all side cases
#ex: input:3,  output: 1/3
#ex: input 2, output 1/2
def recip(num):
    try:
        raise OSError
        return 1/num
        
    except ArithmeticError:
        print('please enter a non-zero number')
    except TypeError:
        print('please enter an integer not a string')

    # except Exception: #very general case
    #     print('erroneous use')
    #     return 0

try:
    x = recip(10)
except:
    print("I handled the OS error")











# class Pen:
#     pass


# def reciprocal (num):
#     try:
#         print(1/num)
#         return 1/num
    
#     except ZeroDivisionError:
#         print("dont divide by zero")

#     except ArithmeticError:
#         print("math error")
    
#     except TypeError:
#         print("please enter the correct type")

#     except:
#         print("error")
#         return 0

# reciprocal(3)






# def get_reciprocal(x):
    
#     try:
#         x = int("str")  # This will cause ValueError
#         inv = 1 / x   # Inverse calculation
        
#     except ValueError:
#         print("Not Valid!")
        
#     except ZeroDivisionError:
#         print("Zero has no inverse!")
    
#     return inv






# # Write a program that takes a list.
# # Then returns the sum of the first two elements
# # Discuss all side cases
def sum_list(list_input):
    try:
        sum = list_input[0] + list_input[1]
    except TypeError:
        print('mismatch type')
    except IndexError:
        print('out of range')
    except:
        print('general error')
    return sum

x = sum_list([1, 4, 8])















# # def sum_first_2_list(list_input):
# #     try:
# #         sum = list_input[0] + list_input[1]
# #         return sum
    
# #     except TypeError:
# #         print('Type error')
# #         return 0
    
# #     except:
# #         print('error')
# #         return 0
    
    

# sum_first_2_list()





# def example2():
#     a = ["10", "twenty", 30]  # Mixed list of integers and strings
#     try:
#         total = int(a[0]) + int(a[1])  # 'twenty' cannot be converted to int
        
#     except (ValueError, TypeError) as e:
#         print("Error", e)
        
#     except IndexError:
#         print("Index out of range.")



# # Write a program that reads a file and prints what is inside it
# # Discuss all side cases and handle them
# def open_and_read_file(file_name):
#     f = open(file_name, 'r')
#     content = f.read()
#     return content


# # Write a program that writes "LMAO" to a file
# # Discuss all side cases and handle them