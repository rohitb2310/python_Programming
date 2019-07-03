## File operations....

f=open("File.txt","r")
print (f.read())  ## print all the lines in file
print("\n Reading Line by Line.....")
f.close()
f=open("File.txt","r")
print(f.readline())	## reads only single line
print(f.readline())
f.close() 	
