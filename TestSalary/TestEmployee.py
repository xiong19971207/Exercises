import unittest
from TestSalary.salary import Employee


class TestEmp(unittest.TestCase):
    def setUp(self) -> None:
        self.my_salary = Employee('a', 'b')

    def test_default_salary(self):
        self.my_salary.give_raise()
        self.assertEqual(self.my_salary.salary, 5000)

    def test_add_salary(self):
        self.my_salary.give_raise(2000)
        self.assertEqual(self.my_salary.salary, 2000)
