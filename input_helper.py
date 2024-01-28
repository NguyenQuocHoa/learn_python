# Function Name : input_array
# Name          : get input array from user
# Param         : none
# Return        : arr
# Created       : 2024/01/28
# Modified      :
def input_array():
    arr = []
    number_element = int(input("Enter number of elements: "))
    for index in range(number_element):
        ele = int(input(""))
        arr.append(ele)
    return arr
