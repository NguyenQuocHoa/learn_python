# https://blog.luyencode.net/1000-bai-tap-lap-trinh-c-cua-thay-khang/#de-bai-1000-bai-tap-lap-trinh-cua-thay-khang
import input_helper
# Function Name : calc_max_of_arr
# Name          : get element max of array
# Param         : none
# Return        : number_max
# Created       : 2024/01/28
# Modified      :
def calc_max_of_arr():
    number_max = -1
    input_arr = input_helper.input_array()
    for element in input_arr:
        if element > number_max:
            number_max = element
    return number_max

# Check results
print("Number max of array is: {}".format(calc_max_of_arr()))
