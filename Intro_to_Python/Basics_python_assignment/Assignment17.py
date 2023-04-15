#17.Write a Python program to find the number of characters present the given string.

str1 = 'ana78mikam'
count = 0
for i in str1:
    if i.isalpha():
        count=count+1
    else:
        pass    
print(count)    