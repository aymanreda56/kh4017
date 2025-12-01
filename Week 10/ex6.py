#Analyze the best, average and worst case scenarios


def getSum(arr1):
    n = len(arr1)
    if n % 2 == 0:  # (n) is even
        return 0
    
    sum = 0
    for i in range(n):
        sum += arr1[i]
    return sum  # (n) is odd

print(getSum(range(0, 1000001)))
#best case O(1)
#worst case O(n)
#average case O(n)





if __name__ == '__main__':
    # Declaring two lists, one with an odd length
    # and the other with an even length
    arr1 = [1, 2, 3, 4]
    arr2 = [1, 2, 3, 4, 5]
    print(getSum(arr1))
    print(getSum(arr2))