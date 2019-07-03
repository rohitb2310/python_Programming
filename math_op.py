import math_module
print("\n 1.Addition \n2.substraction \n 3.MUltiplication \n 4.Division")
a=input("Enter first number::")
b=input("Enter second number::")
ch=input("Enter your choice ")
if(ch==1):
 math_module.add(a,b)
elif(ch==2):
  math_module.sub(a,b)
elif(ch==3):
  math_module.mul(a,b)
elif(ch==4):
  math_module.div(a,b)
else:
	print("Enter correct choice:::")
	
 
