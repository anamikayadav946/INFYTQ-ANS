# LIBRARIES AND BUILTIN FUNCTIONS
'''16. Write a python function, encrypt_sentence(msg) which accepts a message and encrypts it based on rules given below and returns the encrypted message.
 Words at odd position -> Reverse It
Words at even position -> Rearrange the characters so that all consonants appear before the vowels and their order should not change
Note: Assume that the sentence would begin with a word and there will be only a single space between the words.
Perform case sensitive string operations wherever necessary.
Example: msg=the sun rises in the east    output=eht snu sesir ni eht stea'''

def encrypt_sentence(msg):
    encrypt_list=[]
    vowel_list= ['a','e','i','o','u','A','E','I','O','U']
    list_msg = msg.split()
    #print(list_msg)
    for i in range(0,len(list_msg)):
        if i%2==0: #as the list start count with 0 position which is odd position for us
            odd_position_str=list_msg[i]
            rev_word=odd_position_str[::-1]
            #print(rev_word)
            encrypt_list.append(rev_word)
        else:
            even_position_str=list_msg[i]
            str1='' #declared two empty string so that each and ever time it should take empty string not old string
            str2=''
            for j in even_position_str:
                if j in vowel_list:
                   str1=str1+j
                else:
                    str2= str2+j
            str3 = str2+str1
            #print(str3)    
            encrypt_list.append(str3)
            listtostring = ' '.join(map(str,encrypt_list))
    return listtostring
                   
data = encrypt_sentence("the sun rise in the east")
print(data)