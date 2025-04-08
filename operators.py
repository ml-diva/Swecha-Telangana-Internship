'''Arithmetic Operators in python'''
print('Arithmetic Operators ')
a= int(input('Enter a value : '))
b= int(input('Enter b value : '))
print('Sum :',a+b)
print('Difference :',a-b)
print('Product :',a*b)
print('Quotient :',a/b)
print('Division(floor value) :',a//b)
print('Power :',a**b)
print('Modulus :',a%b)

'''Logical Operators in python'''
print('Logical Operators ')
c= int(input('Enter c value : '))
if a>=b and a>=c :
    print('a is Largest')
elif b>=a and b>=c :
    print('b is Largest')
else :
    print('c is Largest') 

#Assignment Operators
print('Assignment Operators ')
a+=b
print('a+=b : ',a)
a-=b
print('a-=b : ',a)
a/=b
print('a/=b : ',a)
a*=b
print('a*=b : ',a)
a**=b
print('a**=b : ',a)

#Comparision Operators
a= int(input('Enter a value : '))
b= int(input('Enter b value : '))

print('a == b =', a == b)
print('a != b =', a != b)
print('a > b =', a > b)
print('a < b =', a < b)
print('a >= b =', a >= b)
print('a <= b =', a <= b)

x1 = 5
y1 = 5
x2 = 'Hello'
y2 = 'Hello'
x3 = [1,2,3]
y3 = [1,2,3]

print(x1 is not y1)  

print(x2 is y2)  

print(x3 is y3)  
