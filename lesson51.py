# https://blog.luyencode.net/1000-bai-tap-lap-trinh-c-cua-thay-khang/#de-bai-1000-bai-tap-lap-trinh-cua-thay-khang
# Method 1:
# Function Name : calc_character_maximum1
# Name          : calculate character is maximum number
# Param         : number
# Return        : number_reversed
# Created       : 2024/01/28
# Modified      :
def calc_character_maximum1(number):
    number_max = 0
    while number > 0:
        number_mode = number % 10
        if number_mode > number_max:
            number_max = number_mode
        number = number // 10
    return number_max

# Method 2:
# Function Name : calc_character_maximum2
# Name          : calculate character is maximum number
# Param         : number
# Return        : number_reversed
# Created       : 2024/01/28
# Modified      :
def calc_character_maximum2(number):
    str_number = str(number)
    number_max = 0
    for num in str_number:
        num = int(num)
        if num > number_max:
            number_max = num
    return number_max

# Check results
number = int(input())
print("Method 1 is: {}".format(calc_character_maximum1(number)))
print("Method 2 is: {}".format(calc_character_maximum2(number)))