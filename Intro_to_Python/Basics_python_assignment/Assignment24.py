#24.Given a list of numbers, write a Python function to return the list of prime numbers present in it.
#Example: input:[7,9,11,13,15,20,23] output:[7,11,13,23]

def prime_number(list1):
    new_list=[]
    for num in list1:
        for fact in range(2,num):
            #print(fact)
            if num % fact == 0:
                #print(num,"not prime num")
                break   
        else:
                new_list.append(num)      
           
    return new_list  

input11 = [7,9,11,13,15,20,23]
print(prime_number([7,9,11,13,15,20,23]))  