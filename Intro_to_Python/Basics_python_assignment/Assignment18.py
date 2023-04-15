#18.Write a Python program to find the numbers of words present in the given sentence.

def count_word(msg):
    msg1=msg.split()
    msg2= len(msg1)
    #res = msg.count(" ")
    return msg2

print(count_word("My name is @@ anamika.!!!!"))