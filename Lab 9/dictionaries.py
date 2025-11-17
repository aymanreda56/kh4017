a_list = [2, 1, 2, 3, 5]

#dictionary
#key-value pairs
Y = "aslo"#input("enter something as a key")
dict_1 = {2:'lol', 'ayman': 10, 3: 10, 2: 20, 10:Y }


#insertion
dict_1['new_key'] = 'new_value'


#modification
dict_1['ayman'] = 90000

#deletion
del dict_1['ayman']


#concatenation (appending)
new_dict = {bin(10): 'lmao', 2.5: True, 2:'pythoon'}

dict_1.update(new_dict)

print(dict_1)