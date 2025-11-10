#dictionary
#key-value pairs

#define a dict
y = 'lol'
test_dict = {3: 'ayman', 1: "emad", y: 10}

#insertion
test_dict['new_key'] = 'new_value'

#modification
test_dict[y] = 'ayman_mohamed'


#delete an entry
del test_dict[3]


list_keys = test_dict.keys()
list_values = test_dict.values()


# print(list_keys)
# print(list_values)



second_dict = {2.4: 'pen', bin(2): False, 1: 'zaki'}

test_dict.update(second_dict)
# print(test_dict)


copy_dict = test_dict.copy() #shallow copy
copy_dict[1] = 'kamal'
print(copy_dict)