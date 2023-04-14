import math
import statistics
from mymodule import x, y

import mymodule

mymodule.Shule(" eMobilis Mobile Technology")
print(mymodule.x + mymodule.y)
print(mymodule.x - mymodule.y)
print(mymodule.x / mymodule.y)
print(mymodule.x * mymodule.y)
print(x + y)
# These are inbuilt modules
print(math.sqrt(144))
dataset = [6, 2, 47, 847, 90, 87, 56, 78]
print(statistics.mean(dataset))
x = statistics.mean(dataset)
print("mean is", x)

print(statistics.fmean(dataset))
print(statistics.median(dataset))
print(statistics.median_low(dataset))
print(statistics.mode(dataset))
print(statistics.median_high(dataset))
print(statistics.geometric_mean(dataset))
