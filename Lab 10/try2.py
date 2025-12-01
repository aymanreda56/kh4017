class Human:
    def __init__(self, height=170, weight=70):
        self.height = height
        self.weight = weight

    def sleep(self):
        print("i am sleeping")

class Teacher(Human):
    def __init__(self, job):
        self.job = job
        self.height = 200
        super().__init__() #initialize the parent class
    
    def sleep(self):
        print("I am a teacher, i am sleeping")

T1 = Teacher(job="AL")
print(T1.height)
print(T1.sleep())





string = 'aymoioooon'
def func(string):
    new_str = ""
    for i in range(len(string)):
        new_str += string[-i]
    
    return new_str

print(func(string))
print(string[-9])
# A) Synt error
# B) Runtime error
# C) aymoioooon
# D) nooooiomya