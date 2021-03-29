print('Lesson 2: Numbers')
#integers
a = 12
print(a)
b = 22
print(a + b)
c = 3
print(a/c)
print(a//c)

#Floating
d = 1.5
print(a/d)
#print(a//d)??
#casting float -> int
e = int(d) # 1
print(a//e)
#print(int(a/d))

s1 = '123'
s2 = '456'
print(s1 + s2)
print(int(s1) + int(s2))

#f = input('Please give a number\n')
#print(type(f))

num1 = 12345
num2 = 67890
# I would like to get the number 1234567890

print(num1 + num2) #not correct
#casting int -> tring and use concatenation
print(str(num1) + str(num2))

#power by 2
print(c*c)
print(c ** 2)
#built in math functions and constants
import math
p = math.pi
print(p)
f = 16
fs = math.sqrt(f)
print(fs)

#modulo operator %, reminder
print(10 % 3)
print(10 % 2)
print(11 % 2)
