


class student:
    def __init__(self,time,habits="good"):
        self.time = time
        self.habits = habits
    def study(self):
        if self.time >= 5 and self.habits == "good":
            print("You will be successful")
        else:
            print("You need to work harder")


s = student(5)
s.study()

    
