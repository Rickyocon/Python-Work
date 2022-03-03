iScore = int(input("Enter the score: "));
if iScore>90:
    sGrade = "A";
elif iScore>80:
    sGrade = "B";
elif iScore>70:
    sGrade = "c";
elif iScore>60:
    sGrade = "d";
else:
    sGrade = "F";

print("your grade: " + sGrade);
