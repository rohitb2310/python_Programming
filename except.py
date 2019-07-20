"""try:
	a=int(input("Enter the number a:"))
	b=int(input("Enter the number b:"))
	c=a/b
	print("Division=%d"%c)
	
except:
	print("Cant divided by zero")
else:
	print("Hi thid id else")
"""

try:
	age=input("\n Enter the age ")
	if age < 18 :
		raise ValueError
	else :
		print("Age is valid")
		
except ValueError:
		print("Age is  not valid")
