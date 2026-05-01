class Student:
    def __init__(self, name, roll_no, marks):
        self.name = name
        self.roll_no = roll_no
        self.marks = marks  # dictionary {subject: marks}

    def total_marks(self):
        return sum(self.marks.values())

    def average_marks(self):
        return self.total_marks() / len(self.marks)


class GradeCalculator:
    def calculate_grade(self, avg):
        if avg >= 90:
            return "A+"
        elif avg >= 75:
            return "A"
        elif avg >= 60:
            return "B"
        elif avg >= 50:
            return "C"
        else:
            return "Fail"


class ReportCard:
    def __init__(self, student, grade_calculator):
        self.student = student
        self.grade_calculator = grade_calculator

    def generate(self):
        print("\n------ REPORT CARD ------")
        print(f"Name     : {self.student.name}")
        print(f"Roll No  : {self.student.roll_no}")

        print("\nMarks:")
        for subject, mark in self.student.marks.items():
            print(f"{subject} : {mark}")

        total = self.student.total_marks()
        avg = self.student.average_marks()
        grade = self.grade_calculator.calculate_grade(avg)

        print("\nTotal    :", total)
        print("Average  :", round(avg, 2))
        print("Grade    :", grade)
        print("--------------------------")


# 🔹 Taking Input from User
name = input("Enter student name: ")
roll = input("Enter roll number: ")

subjects = ["Maths", "Science", "English"]
marks = {}

for sub in subjects:
    marks[sub] = int(input(f"Enter marks for {sub}: "))

# 🔹 Create objects
student = Student(name, roll, marks)
grade_calculator = GradeCalculator()
report = ReportCard(student, grade_calculator)

# 🔹 Generate Report Card
report.generate()