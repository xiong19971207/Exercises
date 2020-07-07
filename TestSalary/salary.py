class Employee():

    def __init__(self, fist_name, last_name, salary=0):
        self.fist_name = fist_name
        self.last_name = last_name
        self.salary = salary

    def give_raise(self, add_salary=5000):
        self.salary = self.salary + add_salary
