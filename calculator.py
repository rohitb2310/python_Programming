c='Y'
while c=='y':
 print("\n **********MENU************")
print("\n1.Addition \n2.Substraction \n3.Multiplication \n4.Division")
print("\n Enter value of a:=")
a=input()
print("\n Enter value of b:=")
b=input()
print("\n Enter your Choice:=")
choice=input()

if int(choice)==1:
 print("Addtion:="+str(int(a)+int(b)))
elif int(choice)==2:
 print("Substraction="+str(int(a)+int(b)))
elif int(choice==3:
 print("Multiplication="+str(int(a)*int(b)))
elif int(choice)==4:
 print("Division="+str(int(a)/int(b)))
else:
	print("\n****Please Enter correct choice*****")
print("\n Do you want to repete it again:")
c=input()
