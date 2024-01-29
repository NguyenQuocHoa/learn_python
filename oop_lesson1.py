# https://v1study.com/python-bai-tap-bai-tap-phan-class.html
# Class Name    : Number
# Note          : operator on number
# Created       : 2024/01/29
# Modified      :
class Number:
    __number1 = 0
    __number2 = 0

    # Function Name : __init__
    # Note          : constructor
    # Param         : self
    # Param         : number1
    # Param         : number2
    # Return        : none
    # Created       : 2024/01/29
    # Modified      :
    def __init__(self, number1, number2):
        self.__number1 = number1
        self.__number2 = number2

    # Function Name : __init__
    # Note          : constructor
    # Param         : self
    # Return        : none
    # Created       : 2024/01/29
    # Modified      :
    def __init__(self):
        self.__number1 = 0
        self.__number2 = 0

    # Function Name : number1
    # Note          : get number1
    # Param         : self
    # Return        : number1
    # Created       : 2024/01/29
    # Modified      :
    def number1(self):
        return self.__number1

    # Function Name : number1
    # Note          : set number1
    # Param         : self
    # Param         : number1
    # Return        : none
    # Created       : 2024/01/29
    # Modified      :
    def number1(self, number1):
        self.__number1 = number1

    # Function Name : number2
    # Note          : get number2
    # Param         : self
    # Return        : number2
    # Created       : 2024/01/29
    # Modified      :
    def number2(self):
        return self.__number2

    # Function Name : number2
    # Note          : set number2
    # Param         : self
    # Param         : number2
    # Return        : none
    # Created       : 2024/01/29
    # Modified      :
    def number2(self, number2):
        self.__number2 = number2

    # Function Name : input_info
    # Note          : set value for number1 and number2
    # Param         : self
    # Return        : none
    # Created       : 2024/01/29
    # Modified      :
    def input_info(self):
        self.__number1 = int(input("Input number 1: "))
        self.__number2 = int(input("Input number 2: "))

    # Function Name : input_info
    # Note          : print value of number1 and number2
    # Param         : self
    # Return        : none
    # Created       : 2024/01/29
    # Modified      :
    def print_input_info(self):
        print(self)

    # Function Name : addition
    # Note          : addition number1 and number2
    # Param         : self
    # Return        : addition
    # Created       : 2024/01/29
    # Modified      :
    def addition(self):
        return self.__number1 + self.__number2

    # Function Name : subtraction
    # Note          : subtraction number1 and number2
    # Param         : self
    # Return        : subtraction
    # Created       : 2024/01/29
    # Modified      :
    def subtraction(self):
        return self.__number1 - self.__number2

    # Function Name : multi
    # Note          : multi number1 and number2
    # Param         : self
    # Return        : multi
    # Created       : 2024/01/29
    # Modified      :
    def multi(self):
        return self.__number1 * self.__number2

    # Function Name : division
    # Note          : division number1 and number2
    # Param         : self
    # Return        : division
    # Created       : 2024/01/29
    # Modified      :
    def division(self):
        return self.__number1 / self.__number2

    # Function Name : print_result
    # Note          : print value of operator
    # Param         : self
    # Return        : none
    # Created       : 2024/01/29
    # Modified      :
    @staticmethod
    def print_result(number):
        print("Result is: {}".format(number))
    
    # Function Name : __str__
    # Note          : print stringify of instance
    # Param         : self
    # Return        : none
    # Created       : 2024/01/29
    # Modified      :
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