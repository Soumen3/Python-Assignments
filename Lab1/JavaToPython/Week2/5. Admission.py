# Admission to a professional course is subject to the following conditions:
# (a) marks in Mathematics >= 60 (b) marks in Physics >=50
# (c) marks in Chemistry >=40 (d) Total in all 3 subjects >=200
# (Or)
# Total in Maths & Physics>=150

math = int(input("Enter marks in Mathematics: "))
phy = int(input("Enter marks in Physics: "))
chem = int(input("Enter marks in Chemistry: "))

if (math >= 60 and phy >= 50 and chem >= 40 and ((math + phy + chem) >= 200 or (math + phy) >= 150)) :
    print("You are eligible for admission.")
else:
    print("You are not eligible for admission.")