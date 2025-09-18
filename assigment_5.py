#TASK_1

#Creata a dictionay with student names and their marks
student_marks = {"Alice":85, "Bob":75, "Charlie":75}

#Ask the user to input student name
student_name = input("Enter the student name:")

#Retrive and display marks or show "not found" message
if student_name in student_marks:
    print(f"{student_name}'marks: {student_marks[student_name]}")
else:
    print("Student not found.")

#TASK

#create list of number from 1 to 10
number = list(range(1,11))
print("Original list:", number)

#Extract the first five elements from the list
first_five = number[:5]
print("Extracted first five elements:", first_five)
second_number = number[:5]

#Reverse these extracted elements
reversed_list = first_five[::-1]
print("Reversed list:", reversed_list)
