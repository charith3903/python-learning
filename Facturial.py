result =1
j =int(input("enter number you want to find factorial"))

for i in range (1,j+1):
    result = result * i
    
    
print(result)

## usin reccuresioon funtion 

n = int(input("enter number you want to find factorial"))

def fact(n):
    if n==0:
        return 1
    return n*fact(n-1)  

print(fact(n))
