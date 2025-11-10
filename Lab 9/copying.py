#shallow copy
def change(x):
    x[0] = 90


test_list = ['lol', 5, 10]

change(test_list)

print(test_list)