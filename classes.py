from abc import *

class SchoolMember(metaclass = ABCMeta):
	def __init__(self, name, age):
		self.name = name
		self.age = age
		print(f"SchoolMember: {self.name}")

	@abstractmethod	
	def Tell(self):
		print(f"Name: {self.name}, age: {self.age}", end =' ')

class Teacher(SchoolMember):
	def __init__(self, name, age, salary):
		SchoolMember.__init__(self, name, age)
		self.salary = salary
		print(f"Teacher: {self.name}")

	def Tell(self):
		SchoolMember.Tell(self)
		print(f"Salary: {self.salary}")

class Student(SchoolMember):
	def __init__(self, name, age, marks):
		SchoolMember.__init__(self, name, age)
		self.marks = marks
		print(f"Student {self.name}")

	def Tell(self):
		SchoolMember.Tell(self)
		print(f"Marks: {self.marks}")

t = Teacher('Mrs. Shrividya', 40, 30000)
s = Student('Swaroop', 25, 75)
print() # печатает пустую строку
members = [t, s]
for member in members:
	member.Tell() 