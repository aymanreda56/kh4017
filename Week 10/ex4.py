# Function to count frequencies of array items
def countFreq(arr, n):
    freq = dict()
    
    # Traverse through array elements and
    # count frequencies
    for i in arr:
        if i not in freq:
            freq[i] = 0
        freq[i]+=1
        
    # Traverse through map and print frequencies
    for x in freq:
        print(x, freq[x])

# Driver Code

# Given array
arr =  [10, 20, 20, 10, 10, 20, 5, 20 ]
n = len(arr)

# Function Call
countFreq(arr, n)