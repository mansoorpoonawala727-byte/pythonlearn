def factorial(n):
    if n==0 or n==1:
        return 1
    elif n<0:
        return "there is no factorial for negative numbers"
    else:
       return n * factorial(n-1)
    

print(factorial(5))   
print(factorial(4))   
print(factorial(0))  
print(factorial(-3))  