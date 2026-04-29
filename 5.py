class students:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    def display__info(self):
        print(f"student name{self.name}  and marks:{self.marks}")

s1 = students("sandy","82")
s1.display__info() 
    