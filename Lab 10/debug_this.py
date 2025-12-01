# This long piece of code contains errors
# Pinpoint them via debuggging and by the use of breakpoints

def replace_numbers_in_string (string:str):
    all_numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    new_string = ""
    for i in range(len(string)):
        if string[i] in all_numbers:
            new_string += "NUM"
        else:
            new_string += string[i]
    return new_string

res = replace_numbers_in_string('aymoo12n')
# A) 'aymoon'
# B) '12'
# c) 'NUMNUM'
# D) 'aymooNUMNUMn'        





def replace_all_numbers_in_file (filename):
    try:
        f = open(filename, 'r')
    except Exception as e:
        print(e)
        return False
    
    content = f.read()
    new_content = replace_numbers_in_string(content)

    try:
        f = open(filename, 'w')
        f.write(new_content)
    except Exception as e:
        print(e)
        return False

replace_all_numbers_in_file('lol.txt')
#if lol.txt contains "hello world"