class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def printDetails(self):
        print("The persons age and name", self.age, self.name)


class Employee(Person):
    def __init__(self, name, age, salary):
        self.salary = salary
        # super().__init__(name, age)
        # Person.__init__(self, name, age)
        super(Employee, self).__init__(name,age)

    def printSalary(self):
        print("The employee salary is : ", self.salary)

    def printDetails(self):
        print("The persons salary, age and name", self.salary, self.age, self.name)


emp1 = Employee("Poorna", "28", 5000)
emp1.printSalary()
emp1.printDetails()
