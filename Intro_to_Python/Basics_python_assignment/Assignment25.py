'''25.Write a python function find_common_characters(msg1,msg2) to display all the common characters between given two strings. Return -1 if there are no matching characters.
Note: Ignore blank spaces if there are any. Perform case sensitive string comparison wherever necessary.'''
def string_match(msg1,msg2):
    str1 = ""
    msg3=msg2.replace(" ","")
    #print(msg3)
    for letter in msg1:
        if letter in msg3:
            str1 += letter

    return str1
print(string_match("I like Python","Java is a very popular language"))