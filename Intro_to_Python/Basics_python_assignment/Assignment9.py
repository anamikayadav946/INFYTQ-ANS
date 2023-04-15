'''9.Write a Python function right_shift(num, n) that takes two numbers num and n as  arguments and returns value 
of the integer num rotated to the right by n positions. Assume both the numbers are unsigned. 
Invoke the function and print the return value.

Hint: use >> binary operator to shift the bits.'''

def right_shift(num,n):
    a = num>>n
    return a

print(right_shift(60,2))