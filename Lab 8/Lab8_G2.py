class Human:
    def __init__(self, age=21, height=180, weight=100, gender="Male"):
        self.age = age
        self.height = height
        self.weight = weight
        self.gender = gender

    def eat(self, something):
        print(f"I ate {something}")

class Employee(Human):
    def __init__(self, job_chosen, salary_chosen, company_chosen, age_chosen=21, weight_chosen=70, height_chosen=180, gender_chosen="Male"):
        super().__init__(age=age_chosen, weight=weight_chosen, height=height_chosen, gender=gender_chosen)
        self.job = job_chosen
        self.salary = salary_chosen
        self.company = company_chosen
    
    def eat(self, something): #polymorphism
        print(f"I ate {something} with a fork")

emp1 = Employee(age_chosen=31, job_chosen="consultant", salary_chosen=10000, company_chosen="pwc")
emp1.eat("sandwitch")

hum = Human()
hum.eat('burger')

#new comment
