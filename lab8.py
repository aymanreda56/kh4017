class Person:
    def __init__(self, age_chosen=16, height_chosen=180, weight_chosen=100, gender_chosen='Male'):
        self.age = age_chosen
        self.height = height_chosen
        self.weight = weight_chosen
        self.gender = gender_chosen
    
    def eat(self, something):
        print(f"I ate {something}")


class Employee(Person):
    def __init__(self, age=32, height=180,  weight=100, gender="Male", job="Teacher", salary=300000):
        super().__init__(age_chosen = age, height_chosen = height, weight_chosen = weight, gender_chosen = gender)
        self.job = job
        self.salary = salary
    
    def eat(self, something):
        print(f"I eat {something} using a fork")
    


emp1 = Employee(age = 32, job="teacher", salary=100000)
emp1.eat("sandwhich")


person1 = Person()
person1.eat("Burger")