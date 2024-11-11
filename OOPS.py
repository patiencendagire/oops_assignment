#opps
# it always has classes and objects
# A class always has properties/attributes
# objects come from class


#things u want the class to do are the methods
#1)creating classes
#cohort class
#class name starts witha csapital letter and always in singular
# class Cohort:
#  from datetime import date

# class Cohort:
#     def __init__(self, name, description, start_date, end_date):
#         """
#         Constructor for the Cohort class.

#         Parameters:
#             name (str): Name of the cohort.
#             description (str): Description of the cohort.
#             start_date (date): Start date of the cohort.
#             end_date (date): End date of the cohort.
#         """
#         self.name = name  # Name of the cohort
#         self.description = description  # Description of the cohort
#         self.start_date = start_date  # Start date of the cohort
#         self.end_date = end_date  # End date of the cohort
#         self.members = []  # List to store cohort members

#     def add_member(self, member):
#         """Adds a new member to the cohort."""
#         self.members.append(member)

#     def cohort_info(self):
#         """
#         Prints the cohort name and the total number of students in the cohort.
#         """
#         print(f"Cohort Name: {self.name}")
#         print(f"Total Number of Students: {len(self.members)}")

# #     def __str__(self):
# #         """
# #         String representation of the cohort, summarizing its details.
# #         """
# #         return f"Cohort '{self.name}' - {self.description} (From {self.start_date} to {self.end_date})"

# # # Example usage:

# # # Create a new instance of the Cohort class
# # spring_cohort = Cohort(
# #     name="Spring 2024",
# #     description="A cohort for students joining in the spring semester of 2024.",
# #     start_date=date(2024, 3, 1),
# #     end_date=date(2024, 6, 30)
# # )

# # # Add members
# # spring_cohort.add_member("Alice")
# # spring_cohort.add_member("Bob")

# # # Print cohort information
# # spring_cohort.cohort_info()  # Cohort Name: Spring 2024, Total Number of Students: 2

# # # Print the cohort summary
# # print(spring_cohort)  # Cohort 'Spring 2024' - A cohort for students joining in the spring semester of 2024 (From 2024-03-01 to 2024-06-30)

   

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