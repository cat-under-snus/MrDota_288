print("Lesson 5")
class Employee:
    def __init__(self, surname, name, age, experience):
        self.Surname = surname
        self.Name = name
        self.Age = age
        self.Experience = experience
        self.Stavca = 400
        self.calc_salary();

    def print_employee_info(self):
        print("Прізвище:", self.Surname)
        print("Імя:", self.Name)
        print("Досвід:", self.Experience)
    def calc_salary(self):
        self.Salary = self.Experience * self.Stavca + 8000

    def to_receive_a_salary(self):
        print("Ваша ЗП:", self.Salary)
emloyee1=Employee("Sigma","Oleksand",37,7)
emloyee1.print_employee_info()
emloyee1.to_receive_a_salary()

class Driver(Employee):

    def __init__(self,surname, name, age, experience,transport):
        super().__init__(surname,name,age,experience)
        self.Transport=transport
        self.Stavca=1100
        self.calc_salary()

    def show_transport(self):
        print("Транспорт:", self.Transport)
        print()

emloyee2=Driver("Kogut","Oleg",27,8,"AboBus Bohdan")
emloyee2.print_employee_info()
emloyee2.show_transport()
emloyee2.to_receive_a_salary()

class controller(Employee):
    def __init__(self,surname, name, age, experience,license):
        super().__init__(surname,name,age,experience)
        self.License = license
        self.Stavca = 1200
        self.calc_salary()

    def show_license(self):
        print("Ліцензія:", self.License)
        print()

emloyee3=controller("володиме","Ваня",30,5,"AboBus Bohdan")
emloyee3.print_employee_info()
emloyee3.show_license()
emloyee3.to_receive_a_salary()
