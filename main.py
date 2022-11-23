# control of grades

class Student():
    def __init__(self, name: str, grade1: float, grade2: float):
        self.name = name
        self.grade1 = grade1
        self.grade2 = grade2

        self.average = (self.grade1 + self.grade2) / 2.0

        if(self.average >= 6.0):
            self.approved = 1
        else:
            self.approved = 0
    
    def __repr__(self) -> str:
        if self.approved == 0:
            approved = 'NOT APPROVED'
        else:
            approved = 'APPROVED'

        return f"Name is {self.name}, grade for the first two months is {self.grade1:.2f}, " \
            f"and for the second {self.grade2:.2f}.\nAverage = {self.average:.2f} and student is {approved}\n"

if __name__ == "__main__":
    students = []

    