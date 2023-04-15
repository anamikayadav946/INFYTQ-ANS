#13.Write a Python program to generate the next 15 leap years starting from a given year.
# Populate the leap years into a list and display the list.

def generate_leapyear(year):
    count=0
    leap_year=[]
    while count<15:
        if year%4==0:
            count=count+1
            leap_year.append(year) 
        year=year+1  
    return (leap_year)             


print(generate_leapyear(2000))