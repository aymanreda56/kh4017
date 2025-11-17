#add 2 numbers, return the result
def add (x, y, w, g, a, n, d=20, u=10 ): #arguments
    result = x + y
    print(result)
    #return result



def split_and_swap (string):
    first_half = string[0: len(string) // 2]
    second_half = string[len(string) // 2 : ]

    new_string = second_half + first_half
    return new_string


sum_num = add(2, 5, 3, 6, 8, 3, 900)
print(sum_num)


string = "hello world"
print(split_and_swap(string))

string = "aymanmohamed"
print(split_and_swap(string))


var = 3
varr = [2, 1] #list
varrr = 0.4 #float
