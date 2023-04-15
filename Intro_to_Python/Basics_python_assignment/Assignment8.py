'''8. Write a Python function check_amicable_numbers(num1, num2) that accepts two numbers num1 and num2 as arguments and returns True if the given pair of numbers are amicable numbers else return false. Invoke the function and 
based on return value print the numbers are amicable numbers or not.
num1 and num2 are said to be amicable numbers if sum of all the proper devisors (except num1 itself) of num1 is equal to num2 and sum of all the proper devisors of num2 (except num1 itself) is equal to num1.'''

def amicable_num(num1,num2):
    sum1=0 
    sum2=0
    for i in range(1,num1):
        if num1%i==0:
            sum1=sum1+i
    print("sum of diviser of num1 {}".format(sum1))
    for i in range(1,num2):
        if num2%i==0:
            sum2=sum2+i 
    print("sum of diviser of num2 {}".format(sum2))

    if num1==sum2 and num2==sum1:
        return True
    else:
            return False              
            
print(amicable_num(220,287))  