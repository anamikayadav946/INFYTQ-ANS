#23.Readin the content of file into string using read() function

fhk = open("data.txt", "r")
list_var = fhk.read(17)
for line in list_var:
    print(line,end='')
fhk.close()    
print(type(list_var)) 