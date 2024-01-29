# https://v1study.com/python-bai-tap-bai-tap-phan-class.html
# Class Name    : Employee
# Note          : store information of employee
# Created       : 2024/01/29
# Modified      :
class Employee:
    __employee_name = None
    __employee_age = None
    __employee_address = None
    __employee_salary = None
    __employee_hours = None

    def __init__(self, employee_name, employee_age, employee_address, employee_salary, employee_hours):
        self.__employee_name = employee_name
        self.__employee_age = employee_age
        self.__employee_address = employee_address
        self.__employee_salary = employee_salary
        self.__employee_hours = employee_hours

    def __init__(self):
        pass

    def input_info(self):
        self.__employee_name = input("Input employee name: ")
        self.__employee_age = int(input("Input employee age: "))
        self.__employee_address = input("Input employee address: ")
        self.__employee_salary = float(input("Input employee salary: "))
        self.__employee_hours = float(input("Input employee hours: "))

    def print_info(self):
        print("==================> EMPLOYEE INFORMATION <==================")
        print("Employee name is     : {}".format(self.__employee_name))
        print("Employee age is      : {}".format(self.__employee_age))
        print("Employee address is  : {}".format(self.__employee_address))
        print("Employee salary is   : {}".format(self.__employee_salary))
        print("Employee hours is    : {}".format(self.__employee_hours))
        print("==================> EMPLOYEE INFORMATION <==================")

    def calc_bonus(self):
        bonus = 0
        if self.__employee_hours >= 200:
            bonus = self.__employee_salary * 0.2
        else:
            if self.__employee_hours >= 100 and self.__employee_hours < 200:
                bonus = self.__employee_salary * 0.1
        return bonus

# Check results
emp = Employee()
emp.input_info()
emp.print_info()
print("Bonus is: {}".format(emp.calc_bonus()))