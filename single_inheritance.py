class Animal:

	def speak(self):
	
		print("This is Animal Class")

class Dog(Animal):

	def bark(self):
	
		print("Dog is Barking")
		
d=Dog()
d.speak()
d.bark()
