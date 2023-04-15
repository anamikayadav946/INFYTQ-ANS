#7.Write a Python Function is_palindrome(num) that accepts an integer num as argument and returns True if the num is palindrome else returns false. Invoke the function and based on return value print the output.


def is_palindrome(num):
    new_num = 0
    old_num =num
    for i in range(0,len(str(num))):
        rem= num%10
        new_num = new_num*10+rem
        num = num//10
    print(new_num)
    if new_num == old_num:
        return True
    else:
        return False      
    
print(is_palindrome(56475))