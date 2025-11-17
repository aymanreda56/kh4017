def magic(n):
    if n <=1:
        return n
    
    a = magic(n-1)
    b = magic(n-2)
    return a + b

print(magic(5))