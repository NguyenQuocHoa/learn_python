# https://blog.luyencode.net/1000-bai-tap-lap-trinh-c-cua-thay-khang/#de-bai-1000-bai-tap-lap-trinh-cua-thay-khang
import math
# Function Name : get_arr_prime
# Note          : get array prime from 2 to number
# Param         : number
# Return        : arr_prime
# Created       : 2024/01/28
# Modified      :
def get_arr_prime(number):
    if number == 2:
        return [2]
    else:
        arr_prime = []
        for index in range(2, number  + 1):
            if check_number_prime(index):
                arr_prime.append(index)
        return arr_prime

# Function Name : check_number_prime
# Note          : check number is prime
# Param         : number
# Return        : is_number_prime
# Created       : 2024/01/28
# Modified      :
def check_number_prime(number):
    number_sqrt = int(math.sqrt(number))
    for index in range(2, number_sqrt + 1):
        if number % index == 0:
            return False
    return True

# Check results
print("Input your number: ")
number = int(input())
print("Array prime is: ", get_arr_prime(number))
