import os

from platform import system

class Student():
    def __init__(self, id: int, name: str, grade1: float, grade2: float):
        self.id     = id
        self.name   = name
        self.grade1 = grade1
        self.grade2 = grade2

        self.average = (self.grade1 + self.grade2) / 2.0

        if(self.average >= 6.0):
            self.approved = 1
        else:
            self.approved = 0
    
    def Approved(self) -> str:
        if self.approved == 0:
            return 'NOT APPROVED'
        else:
            return 'APPROVED'

    def __repr__(self) -> str:
        return "\033[1;34m" + f"\nStudent ID = {self.id + 1}\n" + "\033[0;0m" \
            f"Name is {self.name.title()}, grade for the first two months is {self.grade1:.2f}, " \
            f"and for the second {self.grade2:.2f}.\n" \
            f"Average = {self.average:.2f} and student is {self.Approved()}."

    def PrintGrades(self) -> str:
        return f"\n{self.name.title()} got {self.grade1:.2f} in the first two months and {self.grade2:.2f} in the second.\n" \
            f"His final average is {self.average:.2f} and it's {self.Approved()}."

def clear() -> None:
    if system() == 'Windows':
        os.system("cls")
    else:
        os.system("clear")

def RegisterStudent() -> list:
    students = []

    for i in range(0, 2): # alter to 20 after
        print("\033[1;34m" + "\nStudent %d" % (i + 1) + "\033[0;0m")
        name = str(input("Enter the name...\n"))

        try:
            grade1 = float(input("Enter the grade for the first two months...\n"))
        except ValueError: # letters and other non-numeric characters
            while(True):
                grade1 = input("Enter a valid numeric value for the grade...\n")

                try:
                    grade1 = int(grade1)
                except ValueError:
                    continue
                break
        while((grade1 < 0) or (grade1 > 10)):
            print("\033[1;31m" + "\nThe grade must be in a range of 0 to 10!" + "\033[0;0m")
            try:
                grade1 = float(input("Enter the grade for the first two months...\n"))
            except ValueError:
                while(True):
                    grade1 = input("Enter a valid numeric value for the grade...\n")

                    try:
                        grade1 = int(grade1)
                    except ValueError:
                        continue
                    break

        try:
            grade2 = float(input("Enter the grade for the first two months...\n"))
        except ValueError:
            while(True):
                grade2 = input("Enter a valid numeric value for the grade...\n")

                try:
                    grade2 = int(grade2)
                except ValueError:
                    continue
                break
        while((grade2 < 0) or (grade2 > 10)):
            print("\033[1;31m" + "\nThe grade must be in a range of 0 to 10!" + "\033[0;0m")
            try:
                grade2 = float(input("Enter the grade for the first two months...\n"))
            except ValueError:  # letters and other non-numeric characters
                while(True):
                    grade2 = input("Enter a valid numeric value for the grade...\n")

                    try:
                        grade2 = int(grade2)
                    except ValueError:
                        continue
                    break
        
        students.append(Student(id=i, name=name, grade1=grade1, grade2=grade2))
    
    print()
    return students

def ListStudents(students: list) -> None:
    for student in students:
        print(student)

    print("")

def GradesByStudentName(students: list, name: str):
    control = 0 # check if printed or no

    for student in students:
        if name.lower() in student.name.lower().split():
            print(student.PrintGrades() + "\n")
            control = 1

    if control == 0:
        print("\nStudent not found! :(\n")

if __name__ == "__main__":
    students = []

    while(True):
        print("\033[0;32m" + "\tOPTIONS" + "\033[0;0m")
        print("1 - Register student (store name and grades)")
        print("2 - List all students")
        print("3 - See grade by student name")
        print("0 - Exit\n")

        # exception handling
        try:
            option = int(input("Choose an option value: "))
        except ValueError:
            try:
                option = int(input("Please enter a valid value: "))
            except ValueError:
                clear()
                continue
            
        # validation selection option
        if((option < 0) or (option > 3)):
            print("\n\033[0;93m" + "The range of option choice must be between 0 and 3" + "\033[0;0m\n")
            continue

        if (option == 1):
            clear()

            if(students != []):
                overwrite = str(input("\nDo you want to overwrite students? Y/y or N/n\n"))

                if((overwrite == 'S') or (overwrite == 's')):
                    students = RegisterStudent()
                else:
                    print("\nMaintained students.\n")
            else:
                students = RegisterStudent()
        elif (option == 2):
            clear()
            
            if (students == []):
                print("\nNo students registered!\n")
            else:
                ListStudents(students)
        elif (option == 3):
            clear()

            name_student = str(input("\nEnter the name for search...\n"))

            GradesByStudentName(students, name_student)
        elif (option == 0):
            clear()
            break