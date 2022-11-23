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
        return f"Student ID = {self.id}" \
            f"Name is {self.name.title()}, grade for the first two months is {self.grade1:.2f}, " \
            f"and for the second {self.grade2:.2f}.\n" \
            f"Average = {self.average:.2f} and student is {self.Approved()}\n"

    def PrintGrades(self) -> str:
        return f"{self.name.title()} got {self.grade1:.2f} in the first two months and {self.grade2:.2f} in the second" \
            f"His final average is {self.average:.2f} and it's {self.Approved()}"


def clear() -> None:
    if system() == 'Windows':
        os.system("cls")
    else:
        os.system("clear")

def RegisterStudent(students: list) -> list:
    clear()
    
    for i in range(0, 5): # alter to 20 after
        print("\nStudent %d" % i)
        name = str(input("Enter the name...\n"))

        grade1 = float(input("Enter the grade for the first two months...\n"))
        while((grade1 < 0) or (grade1 > 10)):
            print("\nThe grade must be in a range of 0 to 10!")
            grade1 = float(input("Retype the grade for the first two months...\n"))

        grade2 = float(input("Enter the grade for the second two months...\n"))
        while((grade2 < 0) or (grade2 > 10)):
            print("\nThe grade must be in a range of 0 to 10!")
            grade2 = float(input("Retype the grade for the second two months...\n"))
        
        students.append(Student(id=i, name=name, grade1=grade1, grade2=grade2))
    
    return students

def ListStudents(students: list) -> None:
    clear()
    
    for student in students:
        print(student)

if __name__ == "__main__":
    students = []

    while(True):
        print("\tMENU")
        print("1 - Register student (store name and grades)")
        print("2 - List all students")
        print("3 - See grade by studant name")
        print("0 - Exit\n")

        option = int(input("Choose an option: "))

        if (option == 1):
            students = RegisterStudent(students)
        elif (option == 2):
            ListStudents(students)
        elif (option == 3):
            pass
        elif (option == 4):
            pass
        elif (option == 0):
            break