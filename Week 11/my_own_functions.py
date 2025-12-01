def convert_to_binary(string):
    return bytearray(string, encoding='utf-8')


def modify_bits(bytearray_in):
    new_content = []
    for b in bytearray_in: #for each byte
        x = 1
        b = b | x
        new_content.append(b)
    
    return bytearray(new_content)