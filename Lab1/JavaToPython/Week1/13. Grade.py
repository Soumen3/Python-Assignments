# Write a program for following grading system. 
# Note: 
#     Percentage>=90% : Grade A 
#     Percentage>=80% : Grade B 
#     Percentage>=70% : Grade C 
#     Percentage>=60% : Grade D 
#     Percentage>=40% : Grade E 
#     Percentage<40% : Grade F

percentage = float(input("Enter your percentage: "))
if percentage >= 90:
    print("Grade A")
elif percentage >= 80:
    print("Grade B")
elif percentage >= 70:
    print("Grade C")
elif percentage >= 60:
    print("Grade D")
elif percentage >= 40:
    print("Grade E")
else:
    print("Grade F")
