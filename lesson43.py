# https://blog.luyencode.net/1000-bai-tap-lap-trinh-c-cua-thay-khang/#de-bai-1000-bai-tap-lap-trinh-cua-thay-khang
# Method 1:
# Function Name : count_number_character1
# Note          : calculate number of character
# Param         : number
# Return        : count_character
# Created       : 2024/01/28
# Modified      :
def count_number_character1(number):
    count_character = 0
    while number > 0:
        count_character += 1
        number = number // 10
    return count_character

# Method 2:
# Function Name : count_number_character2
# Note          : calculate number of character
# Param         : number
# Return        : count_character
# Created       : 2024/01/28
# Modified      :
def count_number_character2(number):
    return len(str(number))

# Check results
number = int(input())
print("Method 1 is: {}".format(count_number_character1(number)))
print("Method 2 is: {}".format(count_number_character2(number)))