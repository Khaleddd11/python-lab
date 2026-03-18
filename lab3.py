#task1
# Create and write to students.txt
students_file = open("students.txt", "w")
students_file.write("1,Ahmed Ali\n")
students_file.write("2,Sara Mohamed\n")
students_file.write("3,Omar Hassan\n")
students_file.close()

# Create and write to grades.txt
grades_file = open("grades.txt", "w")
grades_file.write("1,Python,85\n")
grades_file.write("1,Math,90\n")
grades_file.write("2,Python,78\n")
grades_file.write("3,Python,92\n")
grades_file.write("3,Math,88\n")
grades_file.close()

print("files created successfully")

#task2
print("\n Student names")
fl = open("students.txt", "r")

for line in fl:
    # ['1', 'Ahmed Ali']
    data = line.split(",") 
    
    name = data[1]
    print(name)

fl.close()

#task 3
print("\n Python grades")
grades = open("grades.txt", "r")

for line in grades:
    data = line.split(",")
    subject = data[1]
    grade = data[2] 
    
    if subject == "Python":
        print("Grade:", grade)

grades.close()



#task4
print("\n student search ")
search_id = input("enter a student_id: ")

# Search for naame
students = open("students.txt", "r")
for line in students:
    data = line.split(",")
    if data[0] == search_id:
        name = data[1] 
        print("Student Name:", name)
        break
students.close()

print("subjects and grades:")

# Search for their Grades
grades = open("grades.txt", "r")
for line in grades:
    data = line.split(",")
    if data[0] == search_id:
        subject = data[1]
        grade = data[2] 
        print("- " + subject + ": " + grade)
grades.close()


#bonus
print("\n average grades")
grades_dict = {}

grades = open("grades.txt", "r")
for line in grades:
    data = line.split(",")
    student_id = data[0]
    grade = int(data[2]) 
    
    if student_id in grades_dict:
        grades_dict[student_id].append(grade)
    else:
        grades_dict[student_id] = [grade]
grades.close()

for student_id in grades_dict:
    grades_list = grades_dict[student_id]
    
    total = 0
    for g in grades_list:
        total += g
        
    average = total / len(grades_list)
    print("Student ID " + student_id + " Average: " + str(average))