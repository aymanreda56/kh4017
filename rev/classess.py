class Pen:
    def __init__(self, new_length=10, new_color='red', new_thickness=3):
        self.length = new_length
        self.color = new_color
        self.thickness = new_thickness





class Human:
    def __init__(self, height=180, weight=70):
        self.height = height
        self.weight = weight

    def eat(self):
        print("I am eating now")
    
    def sleep(self):
        print("I am sleeping")



class Teacher(Human):
    def __init__(self, job, salary=20000):
        super().__init__(160, 80) #created a human, and initialized it with the defaults
        self.job = job
        self.salary = salary
        






T1 = Teacher(job='AL')
print(T1.height)
print(T1.job)






var = Pen()
print(var.color)




list_1 = [1, 2, 4, 6, 7, 20]
print(list_1[0]) #list indexing