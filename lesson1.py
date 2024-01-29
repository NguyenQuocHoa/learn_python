# source from: https://blog.luyencode.net/1000-bai-tap-lap-trinh-c-cua-thay-khang/#de-bai-1000-bai-tap-lap-trinh-cua-thay-khang
# Function Name : calc_sum
# Note          : calculate sum of number 1 + 2 + 3 + ... + n
# Param         : number
# Return        : sum
# Created       : 2024/01/28
# Modified      :
def calc_sum(number):
    sum = 0
    for index in range(1, number + 1):
        sum += index
    return sum

# Check result
number = int(input())
print(calc_sum(number))