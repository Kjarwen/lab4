#1
import math
def my_function(degrees):
    radian = math.pi * degrees / 180
    return radian
degrees = float(input())
radian = my_function(degrees)
print(radian)

#2
import math
def my_function(h, a, b):
    area = (a+b)/2*h
    return area
h = float(input())
a = float(input())
b = float(input())
area = my_function(h, a, b)
print(area)

#3
import math
def my_function(n, l):
    a = l/2*math.tan(math.pi/n)
    area = n*l*a/2
    return area
n = float(input())
l = float(input())
area = my_function(n, l)
print(area)

#4
import math
def my_function(b, h):
    area = b*h
    return area
b = float(input())
h = float(input())
area = my_function(b, h)
print(area)