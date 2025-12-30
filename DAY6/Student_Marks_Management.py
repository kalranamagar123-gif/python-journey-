while True:
    print("\n Student Marks Management")
    name = input("Enter Students Name:")
    subject_01 = int(input("Enter marks for Science: "))
    subject_02 = int(input("Enter marks for Math:  "))
    subject_03 = int(input("Enter marks for Social Science: "))
    subject_04 = int(input("Enter marks for Moral Science: "))
    subject_05 = int(input("Enter marks for English: "))

    total_marks_obtained = subject_01 + subject_02 + subject_03 + subject_04 + subject_05
    total_marks = 500
    total_percentage = float((total_marks_obtained/total_marks)*100)
    

    if total_percentage >= 90:
        print(f"Congratulation {name}, you got a {total_percentage} which is Grade A")
    elif total_percentage >= 80:
        print(f"{name}, you got a {total_percentage} which is Grade B")
    elif total_percentage >= 70:
        print(f"{name}, you got a {total_percentage} which is Grade C")
    elif total_percentage >= 60:
        print(f"{name}, you got a {total_percentage} which is Grade D")
    else:
        print("Fail")
