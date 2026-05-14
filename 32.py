class employee:
    def __init__(self, number_employee, salary, tips):
        self.number_employee  = number_employee
        self.salary = salary
        self.tips = tips

    def provide_salary(self):
        print("number of employee:",self.number_employee)
        print("The given salary is:",self.salary)
        print("owner provided tips:",self.tips)

    def money_loss(self):
        result = self.salary-500
        print(result)
        
    def money_given(self):
        if self.salary >= 1000:
            print("money given to beggar")
        else:
            print("sorry! I don't have money")



e1 = employee(5,10000,5000)
e1.provide_salary()
e1.money_loss()
e1.money_given()

        
