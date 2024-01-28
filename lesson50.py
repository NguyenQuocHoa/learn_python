# https://blog.luyencode.net/1000-bai-tap-lap-trinh-c-cua-thay-khang/#de-bai-1000-bai-tap-lap-trinh-cua-thay-khang
# Method 1:
# Function Name : calc_number_reverse1
# Name          : calculate number reverse
# Param         : number
# Return        : number_reversed
# Created       : 2024/01/28
# Modified      :
def calc_number_reverse1(number):
    number_reversed = 0
    while number > 0:
        number_mode = number % 10
        number_reversed = number_reversed * 10 + number_mode
        number = number // 10
    return number_reversed

# Method 2:
# Function Name : calc_number_reverse2
# Name          : calculate number reverse
# Param         : number
# Return        : number_reversed
# Created       : 2024/01/28
# Modified      :
def calc_number_reverse2(number):
    str_number = str(number)
    return str_number[::-1]

# Check results
number = int(input())
print("Method 1 is: {}".format(calc_number_reverse1(number)))
print("Method 2 is: {}".format(calc_number_reverse2(number)))