# https://blog.luyencode.net/1000-bai-tap-lap-trinh-c-cua-thay-khang/#de-bai-1000-bai-tap-lap-trinh-cua-thay-khang
import helper
# Function Name : calc_max_prime_of_arr
# Note          : get element max prime of array
# Param         : none
# Return        : number_max
# Created       : 2024/01/29
# Modified      :
def calc_max_prime_of_arr():
    number_max = -1
    input_arr = helper.input_array()
    for element in input_arr:
        if helper.check_number_prime(element) and element > number_max:
            number_max = element
    return number_max

# Check results
print("Number prime max of array is: {}".format(calc_max_prime_of_arr()))
