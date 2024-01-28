# https://blog.luyencode.net/1000-bai-tap-lap-trinh-c-cua-thay-khang/#de-bai-1000-bai-tap-lap-trinh-cua-thay-khang
# Method 1:
# Function Name : count_number_character1
# Name          : calculate number of character
# Param         : number
# Return        : count_character
# Created       : 2024/01/28
# Modified      :
def count_number_character1(number):
    count_character = 0
    while number > 0:
        number_mode = number % 10
        if number_mode % 2 == 0:
            count_character += 1
        number = number // 10
    return count_character

# Method 2:
# Function Name : count_number_character2
# Name          : calculate number of character
# Param         : number
# Return        : count_character
# Created       : 2024/01/28
# Modified      :
def count_number_character2(number):
    str_number = str(number)
    count_character = 0
    for num in str_number:
        num = int(num)
        if num % 2 == 0:
            count_character += 1
    return count_character

# Check results
number = int(input())
print("Method 1 is: {}".format(count_number_character1(number)))
print("Method 2 is: {}".format(count_number_character2(number)))