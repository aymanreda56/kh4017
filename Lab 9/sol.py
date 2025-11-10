# 1) write a python program that sums all numbers till n [using iterative method and recursive]
def sum_till_n(n):
    if n <= 1:
        return n
    
    return n + sum_till_n(n-1)


print(sum_till_n(5))



# 2) write a python program that computes the factorial of a number [using iterative method and recursive]
def fact(n):
    if n == 1:
        return n
    
    return n * fact(n-1)


print(fact(5))


# 3) sum of the harmonic series up to n terms. S = 1 + 1/2 + 1/3 + 1/4 + ...
def harmonic_sum(n):
    if n <= 1:
        return 1
    
    return (1/n) + harmonic_sum(n-1)


print(harmonic_sum(5))


# 4) sum of nested list elements
def nested_sum(list_in, sum):
    #base case
    if type(list_in) == int:
        return list_in
    
    #recursive case
    elif type(list_in) == list:
        for small_elm in list_in:
            sum += nested_sum(list_in=small_elm, sum=sum)
    
    return sum
        

test_list = [1, 2, 3, [4, 5, 6, [7,8], 9], 10, 11]
print(nested_sum(test_list, sum = 0))





def what_it_does(n):
    #sums all digits in a number (ex: 321) and prints the number reversed
    if n//10 == 0:
        print(n)
        return n
    
    else:
        print(n%10, end='')
        return n%10 + what_it_does(n//10)



print(what_it_does(3125998))