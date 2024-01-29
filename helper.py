import math
# Function Name : input_array
# Note          : get input array from user
# Param         : none
# Return        : arr
# Created       : 2024/01/28
# Modified      :
def input_array():
    arr = []
    number_element = int(input("Enter number of elements: "))
    for index in range(number_element):
        ele = int(input(""))
        arr.append(ele)
    return arr

# Function Name : check_number_prime
# Note          : check number is prime
# Param         : number
# Return        : is_number_prime
# Created       : 2024/01/29
# Modified      :
def check_number_prime(number):
    if number < 2:
        return False
    number_sqrt = int(math.sqrt(number))
    for index in range(2, number_sqrt + 1):
        if number % index == 0:
            return False
    return True