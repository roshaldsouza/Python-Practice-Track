class Course:
    def __init__(self,name,duration,trainer_name,technologies,start_date):
        self.name = name
        self.duration = duration
        self.trainer_name = trainer_name
        self.technologies = technologies
        self.start_date = start_date
    def display_course(self):
        print(f"Course Name - {self.name} , Duration - {self.duration} , Trainer Name - {self.trainer_name}, Technologies - {self.technologies}, Start Date - {self.start_date} ")
    def is_tech_covered(self,technology):
        if technology in self.technologies:
            return True
        else:
            return False
name = input("enter your name ")
duration = int(input("enter duration "))
trainer_name = input("enter trainer name ")
technologies = list(map(str,input("enter technologies ").split()))
start_date = input("enter date ")

c = Course(name,duration,trainer_name,technologies,start_date)
c.display_course()
print(c.is_tech_covered("mongo"))
