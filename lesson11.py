# source from: https://blog.luyencode.net/1000-bai-tap-lap-trinh-c-cua-thay-khang/#de-bai-1000-bai-tap-lap-trinh-cua-thay-khang
# Function Name : calc_sum
# Note          : calculate sum of number 1.1 + 1.2 + 1.3 + ...
# Param         : number
# Return        : sum
# Created       : 2024/01/28
# Modified      :
def calc_sum(number):
    sum = 1
    for index in range(1, number + 1):
        sub_sum = 1
        for sub_index in range(1, index + 1):
            sub_sum *= sub_index
        sum += sub_sum
    return sum

# Check result
number = int(input())
print(calc_sum(number))