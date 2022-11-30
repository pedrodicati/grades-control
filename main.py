import os

from platform import system

class Student():
    def __init__(self, id: int, name: str, grade1: float, grade2: float):
        self.id       = id
        self.name     = name
        self.__grade1 = grade1
        self.__grade2 = grade2

        self.__average = (self.__grade1 + self.__grade2) / 2.0
    
    @property
    def average(self):
        return self.__average

    @property
    def grade1(self):
        return self.__grade1

    @grade1.setter
    def grade1(self, newGrade: float) -> None:
        if((newGrade >= 0) and (newGrade <= 10)):
            self.__grade1 = newGrade
            self.__average = (self.__grade1 + self.__grade2) / 2.0
            # preciso colocar os 2 underline mesmo tendo o getter que retorna o valor?

    @property
    def grade2(self):
        return self.__grade2

    @grade2.setter
    def grade2(self, newGrade: float) -> None:
        if((newGrade >= 0) and (newGrade <= 10)):
            self.__grade2 = newGrade
            self.__average = (self.__grade1 + self.__grade2) / 2.0
            # preciso colocar os 2 underline mesmo tendo o getter que retorna o valor?

    def Approved(self) -> str:
        if self.average < 6.0:
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

def checkStudent(students: list, name: str) -> bool:
    for student in students:
        if name.lower() == student.name.lower():
            return True 

    return False

def RegisterStudent() -> list:
    students = []

    for i in range(0, 3): # alter to 20 after
        print("\033[1;34m" + "\nStudent %d" % (i + 1) + "\033[0;0m")
        
        name = str(input("Enter the name...\n"))
        while(checkStudent(students=students, name=name)):
            print("Student is already registered!")
            name = str(input("Enter the name...\n"))

        try:
            grade1 = float(input("Enter the grade for the first two months...\n"))
        except ValueError: # letters and other non-numeric characters
            while(True):
                grade1 = input("Enter a valid numeric value for the grade...\n")

                try:
                    grade1 = float(grade1)
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
                        grade1 = float(grade1)
                    except ValueError:
                        continue
                    break

        try:
            grade2 = float(input("Enter the grade for the second two months...\n"))
        except ValueError:
            while(True):
                grade2 = input("Enter a valid numeric value for the grade...\n")

                try:
                    grade2 = float(grade2)
                except ValueError:
                    continue
                break

        while((grade2 < 0) or (grade2 > 10)):
            print("\033[1;31m" + "\nThe grade must be in a range of 0 to 10!" + "\033[0;0m")
            try:
                grade2 = float(input("Enter the grade for the second two months...\n"))
            except ValueError:  # letters and other non-numeric characters
                while(True):
                    grade2 = input("Enter a valid numeric value for the grade...\n")

                    try:
                        grade2 = float(grade2)
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

def EditStudent(students: list, idStudent: int) -> None:
    for student in students:
        if(student.id == idStudent):
            print("")
            print("1 - Name")
            print("2 - Grade to first two months")
            print("3 - Grade to second two months")

            selection = int(input("Chosse an option value: "))

            if(selection == 1):
                student.name = str(input("Enter with the new name...\n"))
            elif(selection == 2):
                student.grade1 = int(input("Enter with the new grade to first two months...\n"))
            elif(selection == 3):
                student.grade2 = int(input("Enter with the new grade to second two months...\n"))

if __name__ == "__main__":
    clear()
    students = []

    while(True):
        print("\033[0;32m" + "\tOPTIONS" + "\033[0;0m")
        print("1 - Register student (store name and grades)")
        print("2 - List all students")
        print("3 - See grade by student name")
        print("4 - Edit student")
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
        if((option < 0) or (option > 4)):
            print("\n\033[0;93m" + "The range of option choice must be between 0 and 3" + "\033[0;0m\n")
            continue

        if (option == 1):
            clear()

            if(students != []):
                overwrite = str(input("\nDo you want to overwrite the students? Y or N\n"))

                if(overwrite.lower() == 'y'):
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
            if(students == []):
                print("\nNo students registered!\n")
            else:    
                clear()

                name_student = str(input("\nEnter the name for search...\n"))

                GradesByStudentName(students, name_student)
        elif (option == 4):
            clear()

            if(students == []):
                print("\nNo students registered!\n")
            else:
                ListStudents(students)
                idStudent = (int(input("Select student ID to edit...\n")) - 1)
                
                clear()

                EditStudent(students=students, idStudent=idStudent)
        elif (option == 0):
            clear()
            break