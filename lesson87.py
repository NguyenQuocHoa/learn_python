# https://blog.luyencode.net/1000-bai-tap-lap-trinh-c-cua-thay-khang/#de-bai-1000-bai-tap-lap-trinh-cua-thay-khang
# Function Name : calc_number_over_10000
# Name          : calculate index of sum over 10000
# Param         : number
# Return        : number_reversed
# Created       : 2024/01/28
# Modified      :
def calc_number_over_10000():
    sum = 0
    index = 1
    while sum < 10000:
        sum += index
        if index > 140:
            print(sum)
        index += 1
    return index

# Check results
print("Result is: {}".format(calc_number_over_10000()))