
class Human():
    def __init__(self, height=160):
        self.height = height


class Teacher(Human):
    def __init__(self, job):
        super().__init__()
        self.job = job
        self.height = 200
        

T1 = Teacher(job="AL")
print(T1.height)






def func1():
    list_1 = [9, 5, '1', 'ayman', 2]
    for i in list_1: #element wise iteration
        print(i)
    
    for i in range(len(list_1)): #return a list starting from 0 till before what's inside
        print(list_1[i]) #index iteration


    print(list_1)
    return (list_1)

x = func1() # x = None
print(x[2]) #None [2]
# A) syntax error
# B) Index Error
# C) 9
# D) 2











# for i in list_1: #element-wise iteration
#     print(i)

# for i in range(0, len(list_1)):
#     print(list_1[i])




# len(list_1)

# inp = int(input("enter a number"))

# def func (x, y=5):
#     pass

# func(y=2, x=3)