#grading system.
marks = int(input("Enter your marks: "))

if marks < 0 or marks > 100:
    print ("Invalid marks entered")
elif marks >= 90:
    print("Grade A")
elif marks >= 80:
     print("Grade B")
elif marks >= 70:
    print("Grade C")
elif marks >= 60:
    print("Grade D")
else:
    print("Grade F")

    print("Your grade is: ")
