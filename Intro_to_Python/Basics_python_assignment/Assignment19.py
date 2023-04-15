'''19.program to count number of repated word and return in dict'''
def word_count(str):
     counts = dict()
     words = str.split()
     
     for i in words:
         if i in counts:
            counts[i] += 1
         else:
            counts[i] = 1
     return counts
         
print( word_count('the quick brown the fox jumps over the lazy dog. fox'))