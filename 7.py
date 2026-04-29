class employe:
    def __init__ (self,name,post,salary=15000):
        self.name = name
        self.post = post
        self.salary = salary

    def display__info(self):
        print(f"The employe is name {self.name} and is post {self.post} and is salary is {self.salary}")


e1 = employe("sandy","CEO",30000)
e1.display__info()