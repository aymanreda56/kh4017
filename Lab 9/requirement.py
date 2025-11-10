# 1) write a python program that sums all numbers till n [using iterative method and recursive]




# 2) write a python program that computes the factorial of a number [using iterative method and recursive]
def factorial_iterative(n):
    cumulative_mul = 1
    while (n >= 1):
        cumulative_mul *= n
        n-=1

    return cumulative_mul

def factorial_recursive(n):
    #base case
    if n == 1:
        return 1
    
    #recurrent case
    return n * factorial_recursive(n-1)


# 3) sum of the harmonic series up to n terms. S = 1 + 1/2 + 1/3 + 1/4 + ...
def harmonic(n):
    #base case
    if n == 1:
        return 1
    
    return 1/n + harmonic(n-1)

print(harmonic(900000000000))


# 4) The following code contains errors, pinpoint and modify them

# sum of nested list elements

# def nested_list_sum(list_in sum):
#     #base case
#     if type(list_in) == int:
#         return list_in
    
#     #recursive case
#     elif type(list_in) = list:
#         for small_elm in list_in:
#             sum = nested_list_sum(list_in, sum)
    
#     return sum
        

# test_list = [1, 2, 3, [4, 5, 6, [7,8], 9], 10, 11]
# print(nested_list_sum(test_list, sum = 0))




#5) try to trace this function and tell what it does
def what_it_does(n):
    if n//10 == 0:
        print(n)
        return n
    
    else:
        print(n%10, end='')
        return n%10 + what_it_does(n//10)

# print(what_it_does(3125998))
