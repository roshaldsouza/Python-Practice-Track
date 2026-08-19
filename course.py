class Course:
    def __init__(self,name,duration,trainer_name,technologies,start_date):
        self.name = name
        self.duration = duration
        self.trainer_name = trainer_name
        self.technologies = technologies
        self.start_date = start_date
    def display_course(self):
        print(f"Course Name - {name} , Duration - {duration} , Trainer Name - {trainer_name}, Technologies - {technolgies}, Start Date - {start_date} ")
name = input("enter your name ")
duration = int(input("enter duration "))
trainer_name = input("enter trainer name ")
technolgies = list(map(str,input("enter technolgies ").split()))
start_date = input("enter date ")

c = Course(name,duration,trainer_name,technolgies,start_date)
c.display_course()
