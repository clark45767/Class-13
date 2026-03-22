new_file = open('New_file2.txt', 'x')
new_file.close()

import os 
print("Checking if my_file exists or not....")
if os.path.exist("my_file.txt"):
    os.remove("my_file.txt")
else:
    print("the file does not exist")

my_file = open("my_file.txt", "w")
my_file.write("Hi! I am Poulumi and I am a teacher.")
my_file.close()

os.remove("Codingal.txt")
os.rmdir("Folder")
