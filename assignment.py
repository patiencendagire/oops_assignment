
class cohort:
    def __init__(self, name, description, start_date, end_date):
        self.name = name  
        self.description = description  
        self.start_date = start_date  
        self.end_date = end_date 
p=cohort("patience","witu student","20/8/2024","20/6/2026")
print(p.name)
print(p.description)
print(p.start_date)
print(p.end_date)

    
# #b
class cohort:
    def __init__(self,cohort_name,total_number_of_students):
        self.cohort_name=cohort_name
        self.total_number_of_students=total_number_of_students
    def myfunc(self):
        print("The cohort name is " + self.cohort_name + " and the total number of students is "  + str(self.total_number_of_students))
p=cohort("cohort4",60)  
p.myfunc()   


    #c    
class cohort:
    def __init__(self, name, description, start_date, end_date):
        self.name = name  
        self.description = description  
        self.start_date = start_date  
        self.end_date = end_date 
cohortfive=cohort("Kwagala","Diploma in computer science","20/8/2026","20/6/2028")
print(cohortfive.name)
print(cohortfive.description)
print(cohortfive.start_date)
print(cohortfive.end_date)