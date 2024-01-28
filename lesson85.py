# https://blog.luyencode.net/1000-bai-tap-lap-trinh-c-cua-thay-khang/#de-bai-1000-bai-tap-lap-trinh-cua-thay-khang
# Function Name : calc_month
# Name          : calculate character is maximum number
# Param         : number
# Return        : number_reversed
# Created       : 2024/01/28
# Modified      :
def calc_month(month):
    if month >= 1 and month <= 12:
        if month >= 1 and month <= 3:
            return "I"
        else:
            if month >= 4 and month <= 6:
                return "II"
            else:
                if month >= 7 and month <= 9:
                    return "III"
                else:
                    if month >= 10 and month <= 12:
                        return "IV"
    else:
        return "NONE"

# Check results
print("Input your month: ")
month = int(input())
print("Result is: {}".format(calc_month(month)))