a = int(input('first element : '))
b = int(input('second element : '))
n = int(input('enter the number of elements : '))
print(a,b, end=" ")
 
while n-2:
       c = a + b
       a = b
       b = c
       print(c, end=" ")
       n = n-1
