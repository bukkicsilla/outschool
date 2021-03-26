print('Lesson 1: Strings')

#define a text
s = 'California'

#output text
print('This is a sentence.')
print("This ia another sentense.")
print(s)
#*****************************

#conncatenation
fname = 'Luna'
lname = 'Saturni'
print(fname + lname)
#*****************************

#formatting
a = 'Katy'
b = 15
print('My name is Katy')
print('My name is', a)
print('My name is '+ a)
print('My name Katy is beautiful.')
print('My name', a, 'is nice.')
print('My name is', a, 'and I am', b, 'years old.')
#********************************
print('My name {} is amazing.'.format(a))
print("My name {} is amazing and I'm {} years old.".format(a,b))
print(f'My name {a} is cool.')
print(f"My name {a} is cool and I'm {b} years old.")
#****************************************

#indexing
c0 = s[0]
print(c0)
c1 = s[1]
c2 = s[2]
print(c1+c2)
print('The length of California is', len(s))
#clast = s[10] ?? why error?
clast = s[9]
print(clast)
clast = s[-1]
print(clast)
print(s[-3])
#*********************************************

#slicing
c3 = s[3]
print(c1+c2+c3)
sl = s[1:4] #starts at index 1 and ends at index 3
print(sl)
print(s[0: 6])
print(s[:6])
print(s[3:-1])
print(s[3:])
print(s[:])
#start, end, step
#print(s[0:-1:2])
#print(s[::-1])
#**********************************************

#some functions on Strings
u = s.upper()
print(u)
l = u.lower()
print(l)
#ca = s.capitalize
#print(ca)
ca = s.capitalize()
print(ca)
#*********************************************
