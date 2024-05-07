
##filter function

number = [1,2,3,4,5,6,7,8]

def even_number(x):
   return x%2==0


y=list(filter(even_number,number))

print(y)

#using lambda function

y= list(filter(lambda x:x%2==0,number))
print(y)


##map function

z=list(map(lambda x:x*2,number))
print(z)

##reduce function

from functools import reduce
y=reduce(lambda x,y: x+y,number)
print(y)
y=reduce(lambda x,y: x*y,number)
print(y)