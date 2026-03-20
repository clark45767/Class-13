file = open("Codingal.txt","r")
counter = 0
Content = file.read()
CoList = file.read()
CoList = Content.split("\n")

for i in CoList:
    if i:
        counter +=1

print("This is the number of lines in the file :", counter) 