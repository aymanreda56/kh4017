dict_1 = {'a': 1, 'b':2, 'c': 3}

new_dict = dict_1 #they are the same object
data = dict_1.copy() #shallow
new_dict['a'] = 100
print(dict_1)


# def change(x):
#     x[0] = 90
#     x[1][0] = 999

# y = [1, [2, 3], 3]
# change(y) #shallow copy
# print(y)






# # test_list = ['lol', 5, 10]

# # #shallow copy
# # # change(test_list)

# # # print(test_list)


# # #deep copy
# # change(copy.deepcopy(test_list))
# # print(test_list)