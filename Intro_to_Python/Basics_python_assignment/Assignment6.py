#6.Write a Python function factorial(num) which returns the factorial of a given number.

def fact(num):
    Factorial = 1
    if num>0:
        for i in range(1,num+1):
            Factorial = i*Factorial
        return Factorial 
    else:
        return "Invalid number"
       
print(fact(-1))