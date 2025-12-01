def fun(a, b):
    while (a != b):
        if (a > b):
            a = a - b
        else:
            b = b - a
    
    print(fun(5,7))
            
#best case O(1)
#worst case O(n)