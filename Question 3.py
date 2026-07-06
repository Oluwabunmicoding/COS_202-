# COS202 Personal Pocket CGPA Calculator

print("=================================")
print("   PERSONAL POCKET CGPA")
print("=================================")

while True:
    total_points = 0
    total_units = 0

    courses = int(input("Enter number of courses: "))

    for i in range(courses):
        print("\nCourse", i + 1)

        unit = int(input("Course Unit: "))
        score = int(input("Score: "))

        if score >= 70:
            gp = 5
        elif score >= 60:
            gp = 4
        elif score >= 50:
            gp = 3
        elif score >= 45:
            gp = 2
        elif score >= 40:
            gp = 1
        else:
            gp = 0

        total_points += gp * unit
        total_units += unit

    cgpa = total_points / total_units

    print("\nYour CGPA is:", round(cgpa, 2))

    option = input("\nDo you want to calculate again? (yes/no): ")

    if option.lower() != "yes":
        print("Thank you for using Personal Pocket CGPA Calculator.")
        break