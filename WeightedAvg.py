print("Enter the marks scored by the students")
written_test = int(input("Written test"))
lab_exams = int(input("Lab exams "))
Assingment = int(input("Assignments"))
overall = (written_test*70)/100+(lab_exams*20)/100+(Assingment*10)/100
print("Grade of the student is",overall)