#27.
def find_average(mark_list):
    total=0
    try:
       for i in range(0, len(mark_list)):

         total+=mark_list[i]
         marks_avg=total/len(mark_list)
         return marks_avg
    except NameError:
       print("Name  error occured")
    except TypeError:
       print("type error occured")
   
try:
  
   #m_list=[mark1,2,3,4]
   m_list=[1,2,3,4]
   #m_list=[]
   print("Average marks:", find_average(m_list))

except ValueError:
       print("the value error occured")