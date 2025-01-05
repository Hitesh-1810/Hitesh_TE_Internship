print("STUDENT RESULT EVALUATION")

name=input("Enter student name :")
maths = int(input("enter marks of maths :"))
science = int(input("enter marks of science :"))
social_science = int(input("enter the marks of social science :"))
art = int(input("enter the marks of art :"))
marathi = int(input("enter the marks of marathi :"))
if maths < 35 or science < 35 or social_science < 35 or art < 35 or marathi <35:
    print("Student is Fail in Exam")
    exit()
Total_Marks = maths + science + social_science + art + marathi
print("Total Marks:",Total_Marks)

Average_marks = Total_Marks / 5
print("Average marks :", Average_marks )
    
Total_percentage=Total_Marks*0.2
print("Total percentage:", Total_percentage)    

if Total_percentage >= 85:
    print("Grade A")
    
elif Total_percentage >= 75:
    print("Grade B")
    
elif Total_percentage >= 55:
    print("Grade C")
    
elif Total_percentage >= 35:
    print("Grade D")

else:
    print("Needs Improvement!")
    

    
