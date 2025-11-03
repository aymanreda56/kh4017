class Institute:
	def __init__(self, buildings=1, floors=2):
		self.buildings=buildings
		self.floors=floors


class University(Institute):
	def __init__(self, name, courses, floors=3):
			super().__init__(floors=floors)
			self.courses=courses
			self.name = name
			mrk1 = Marker("red")
			self.markers = [mrk1, Marker("blue", erasable=False)]

	def print_info(self):
		print(f"University {self.name} has {self.courses} courses")


class person:
	def __init__(self, name="ayman", age=21, height=180):
		self.name = name
		self.age = age
		self.height = height


	def eat(self, something):
		print(f"I eat {something}")



class Student(person):
	def __init__(self, major='cmp', id=11):
		super().__init__()
		self.major = major
		self.id = id
	
	def study(self):
		print("I am studying")
	
class Marker:
	def __init__(self, color, erasable=True):
		self.color=color
		self.erasable= erasable

	def write(self, smth):
		print(f"I am writing {smth}")


unv1 = University(name="coventry", courses="prog", floors=2)

unv1.print_info()
