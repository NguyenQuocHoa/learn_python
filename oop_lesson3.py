# https://v1study.com/python-bai-tap-bai-tap-phan-class.html
import helper
# Class Name    : PrimeNumber
# Note          : Class prime number
# Created       : 2024/01/29
# Modified      :
class PrimeNumber:
    __prime_number = 0

    # Function Name : __init__
    # Note          : constructor
    # Param         : self
    # Param         : prime_number
    # Return        : none
    # Created       : 2024/01/29
    # Modified      :
    def __init__(self, prime_number):
        if helper.check_number_prime(prime_number):
            self.__prime_number = prime_number
        else:
            print("{} is not a prime number".format(prime_number))
    
    # Function Name : is_prime_number
    # Note          : check is a prime number
    # Param         : self
    # Param         : number
    # Return        : is_prime_number
    # Created       : 2024/01/29
    # Modified      :
    def is_prime_number(self, number):
        return helper.check_number_prime(number)
    
    # Function Name : calc_next_prime_number
    # Note          : calc next prime number by self input number
    # Param         : self
    # Return        : next_prime_number
    # Created       : 2024/01/29
    # Modified      :
    def calc_next_prime_number(self):
        next_prime_number = self.__prime_number + 1
        while not self.is_prime_number(next_prime_number):
            next_prime_number += 1
        return next_prime_number

# Check results
number = int(input("Type your number: "))
prime_number = PrimeNumber(number)
if prime_number.is_prime_number(number):
    print("Next prime number of {} is {}".format(number, prime_number.calc_next_prime_number()))