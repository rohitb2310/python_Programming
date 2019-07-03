f=open("File.txt","w")
f.write("File has more conrent to add in a file")
f=open("File.txt","r")
print( f.read())
f.close()

import os
if os.path.exists("File.txt"):
 os.remove("File.txt")
else:
 print("File does not exist") 
