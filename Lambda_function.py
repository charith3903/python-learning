def area(n):
    return n*n

print(area(4))

##using lambda function 

Area =lambda x: x*x
print(Area(4))

Area2 = lambda x,y: x*y
print(Area2(4,5))


##lamda inside the function

def apple(unit_prise):
    return (lambda number_of_apple : number_of_apple*unit_prise)

x =apple(12)
print(x(10))