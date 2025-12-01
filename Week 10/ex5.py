#Analyze the best, average and worst case scenarios


# Linearly search target in arr.
# If target is present, return the index;
# otherwise, return -1
def search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

if __name__ == '__main__':
    arr = [1, 10, 30, 15]
    x = 30
    print(search(arr, x))