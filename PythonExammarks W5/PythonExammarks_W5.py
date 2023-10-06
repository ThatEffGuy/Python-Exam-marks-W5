"""
You will be prompted to your name and exam mark.
The exam has two parts
    examMark     - max  of 100 marks
    praticalMark - max of 50 marks
"""

name          = ""
examMark      = 0   
practicalMark = 0
totalMark     = 0
courseworkMark = 0
percentage    = 0
grade         = ""

name =input    ("Please enter your name ")
while name =="":
    print      ("You must enter your name !")
    name =input("Please enter your name ")

examMark = int(input("enter exam mark (0-100) :"))
while examMark <0 or examMark>100:
        print("Invalid mark. Must between 1 and 100")
        examMark = int(input("enter exam mark (0-100) :"))

practicalMark = int(input("Enter Practical Mark (0 - 50) :"))
while practicalMark < 0 or practicalMark>50:
 print("Invalid mark. Must between 0 and 50")
 practicalMark = int(input("Enter Practical Mark (0 - 50) :"))


courseWorkMark = int(input("Enter Course Work Mark (0 - 50) :"))
while courseWorkMark < 0 or courseWorkMark>50:
 print("Invalid mark. Must between 0 and 50")
 courseWorkMark = int(input("Enter Course Work Mark (0 - 50) :"))

totalMark = examMark+ practicalMark

percentage = round(totalMark/150*100,0)

if percentage < 40:
    grade = "E"
elif percentage < 49:
    grade = "D"
elif percentage < 60:
    grade = "C"
elif percentage < 70:
    grade = "B"
elif percentage < 90:
    grade = "A"
else:
    grade = "A*"

print(name, "Scored", percentage,"%. That's Grade",grade)

