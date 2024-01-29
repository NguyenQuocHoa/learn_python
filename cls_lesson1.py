# https://v1study.com/python-bai-tap-bai-tap-phan-class.html
# Class Name    : Number
# Note          : operator on number
# Created       : 2024/01/29
# Modified      :
class Number:
    __number1 = 0
    __number2 = 0

    def __init__(self, number1, number2):
        self.__number1 = number1
        self.__number2 = number2

    def __init__(self):
        self.__number1 = 0
        self.__number2 = 0

    def number1(self, number1):
        self.__number1 = number1

    def number1(self):
        return self.__number1

    def number2(self, number2):
        self.__number2 = number2

    def number2(self):
        return self.__number2
    
    def input_info(self):
        self.__number1 = int(input("Input number 1: "))
        self.__number2 = int(input("Input number 2: "))

    def print_input_info(self):
        print(self)

    def addition(self):
        return self.__number1 + self.__number2
    
    def subtraction(self):
        return self.__number1 - self.__number2
    
    def multi(self):
        return self.__number1 * self.__number2
    
    def division(self):
        return self.__number1 / self.__number2
    
    @staticmethod
    def print_result(number):
        print("Result is: {}".format(number))
    
    def __str__(self):
        return "Number one is: {}, number two is: {}".format(self.__number1, self.__number2)

# Check results
num = Number()
num.input_info()
num.print_input_info()
Number.print_result(num.addition())
Number.print_result(num.subtraction())
Number.print_result(num.multi())
Number.print_result(num.division())