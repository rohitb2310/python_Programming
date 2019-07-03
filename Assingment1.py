f=open("File.txt","r")  ## opening the file
content = f.read()		## reading the data in a variable
print(content)			##printing all the content

##s="I am Rohit I am Rohit"
l=content.split()		##Splitting the content
dictonary={ }			##creatin the blank dictonary
for word in l:			
	if word in dictonary:				## if word is present increse the value of the word otherwise leave it
	 dictonary[word]=dictonary[word] + 1
	else:
	 dictonary[word]=1					## if not present increament it by 1

print(dictonary)

