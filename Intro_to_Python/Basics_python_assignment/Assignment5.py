#5.An organization has decided to provide salary hike to its employees based on their job level. Employees can be in job levels 3 , 4 or 5. Hike percentage based on job levels are given below:
def salary(current_salary, job_level):
    if job_level == 3:
            updated_salary = current_salary*1.15
    if job_level == 4:
            updated_salary = current_salary*1.07
    if job_level == 5:
            updated_salary = current_salary*1.04
    else:
        updated_salary = current_salary
    return updated_salary


a=salary(30000,2)
print(a)