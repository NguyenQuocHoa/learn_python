import numpy
from scipy import stats

speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]

# calculate average of array
mean = numpy.mean(speed)
print(mean)

# calculate middle value of array
median = numpy.median(speed)
print(median)

# find most value appear of array
mode = stats.mode(speed)
print(mode)

speed = [86,87,88,86,87,85,86]
print(numpy.mean(speed))



