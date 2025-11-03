class Institute:
	def __init__(self, name='tkh', floors=2, buildings=2):
		self.name = name
		self.floors = floors
		self.buildings=buildings

	def print_info(self):
		print(f"the {self.name} has {self.floors} floors")	

class University(Institute):
	def __init__(self, courses, devices, floors=2, buildings=2, name='bla'):
		super().__init__(floors=floors, buildings=buildings, name=name)
		self.courses = courses
		self.devices = devices

	def print_info(self):
		print(f"{self.name} has courses {self.courses}")

class Course:
	def __init__(self, name, hours):
		self.name = name
		self.hours = hours

	def __repr__(self):
		return f"course: {self.name} with hours {self.hours}"


class Human:
	def __init__(self, age=21, name='aym', gender='Male'):	
		self.age=age
		self.name=name
		self.gender=gender

	def eat(self, smth):
		print(f"I am eating {smth}")

class Teacher(Human):
	def __init__(self, workhours, salary, name='aym', age=21, gender="Male"):
		super().__init__(age, name, gender)
		self.workhours = workhours
		self.salary = salary

	def eat(self, smth):
		print(f"I am currently eating a {smth}")
		


		
c1 = Course('prog', 20)
unv = University(courses=[c1, Course('ctf', 10)], devices='lp', buildings=10, name='coventry')
unv.print_info()


t1 = Teacher(workhours=20, salary=200000)
t1.eat("sandwitch")
