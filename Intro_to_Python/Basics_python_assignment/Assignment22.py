#22.Reading the content of file into list using readlines() function, for reading single line readline()
fhk = open("data.txt","r")
list_var=fhk.readlines()
for line in list_var:
    print(line, end='')
fhk.close() 
print(type(list_var)) 