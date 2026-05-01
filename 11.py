class students:
    def __init__(self,name,roll_no,subject,marks):
        self.name = name
        self.roll_no = roll_no
        self.subject = subject
        self.marks = marks

    def calculate_averge(self):
        averge = self.marks/self.subject
        print(averge)
    def calculate_percentage(self):
        percentage=self.calculate_averge/100
        print(percentage)

s1 = students("sandeep",22,3,34)
s1.calculate_percentage()

            
        
        
   



    