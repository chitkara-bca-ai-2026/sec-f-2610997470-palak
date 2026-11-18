print("=" * 50)
print("          SCHOOL RESULT PROCESSING")
print("=" * 50)
name = input("Enter Student Name : ")
roll_no = input("Enter Roll Number : ")

print()
print("--- Enter Marks for 5 Subjects (0-100) ---")
total = 0
failed = False

for i in range(1, 6):
    mark = float(input("Enter marks for Subject " + str(i) + ": "))
    if mark < 0 or mark > 100:
        print("Invalid marks! Please enter marks between 0 and 100.")
        exit()

    total = total + mark

    if mark < 40:
        failed = True

percentage = (total / 500) * 100

if failed == True:
    result = "FAIL"
    grade = "F"
    remark = "Failed in one or more subjects"

elif percentage >= 90:
    result = "PASS"
    grade = "A+"
    remark = "Outstanding"

elif percentage >= 80:
    result = "PASS"
    grade = "A"
    remark = "Excellent"

elif percentage >= 70:
    result = "PASS"
    grade = "B"
    remark = "Very Good"

elif percentage >= 60:
    result = "PASS"
    grade = "C"
    remark = "Good"

elif percentage >= 50:
    result = "PASS"
    grade = "D"
    remark = "Satisfactory"

else:
    result = "PASS"
    grade = "F"
    remark = "Pass"

print()
print("=" * 50)
print("              STUDENT REPORT CARD")
print("=" * 50)

print(f"Student Name :{name}")
print(f"Roll Number  :{roll_no}")
print("-" * 50)
print(f"Total Marks  :{total, ".1f"}", "/ 500.0")
print(f"Percentage   :{percentage, ".2f"}" "+" "%")
print(f"Result       :{result}")
print(f"Grade        :{grade}")
print("Remarks      :{remark}")
print("=" * 50)
