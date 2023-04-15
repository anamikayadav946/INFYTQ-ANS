'''10.Write a Python function check_strong_number(num) that accepts a positive integer as argument and returns True 
if the number is strong number else false. Invoke the function and based on return value print the number is
 strong number or not.
A number is said to be strong number, if the sum of factorial of each digit of the number is equal to the given number.'''

def is_Strongnum(num):
    old_num=num
    sum=0
    for i in range(0,len(str(num))):
        rem=num%10
        fact=1
        for j in range(1,rem+1):
            fact=fact*j
        num = num//10
        sum=sum+fact
       
    if sum == old_num:
        return True
    else: 
        return False    

print(is_Strongnum(145))