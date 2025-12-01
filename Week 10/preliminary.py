c=10 #c doesn't change, it is a fixed constant
n=100000 #n is our input, its size changes as needed


##########################################################################
# Here c is a constant
for i in range(1, c+1):
    # some O(1) expressions
    pass
#Time cost = C*1 = 10
#O(1)
##########################################################################

##########################################################################
# Here c is a positive integer constant
for i in range(1, n+1, c):
    # some O(1) expressions
    pass
#Time cost = n/10 * 1
#O(n)

for i in range(n, 0, -c):
    # some O(1) expressions
    pass
#Time cost = n/c *1
#O(n)
##########################################################################


##########################################################################
for i in range(1, n+1, c):
    for j in range(1, n+1, c):
        # some O(1) expressions
        pass
#O(n^2)

for i in range(n, 0, -c):
    for j in range(i+1, n+1, c):
        # some O(1) expressions
        pass
#outer loop iterates n/c iteration
#inner loop iterate i/c
#first iteration: inner loop executes 1 time
#second iteration: inner loop executes 2 times
#3rd iteration: innter loop exectues 3 times
#1 + 2 + 3 +4 + 5 +... +n
#n(n+1/2) --> n^2/2 + n/2
#O(n^2)
##########################################################################


##########################################################################
i = 1
while(i <= n):
    # some O(1) expressions
    i = i*c
#Cost = root(N) * 1
#O(root(n))



i = n
while(i > 0):
    # some O(1) expressions
    i = i//c

#O(root(n))
##########################################################################



##########################################################################
# Recursive function
def recurse(n):
    if(n <= 0):
        return
    else:
        # some O(1) expressions
        pass
    recurse(n//c)
# Here c is positive integer constant greater than 1
##########################################################################




##########################################################################
# Here c is a constant greater than 1
i = 2
while(i <= n):
    # some O(1) expressions
    i = i**c


i = n
while(i > 1):
    # some O(1) expressions
    i = pow(i, 0.5) #square root
##########################################################################