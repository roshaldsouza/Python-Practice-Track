class StudentProfile:
    def __init__(self, student_name, student_course, student_email, student_skills):
        self.student_name = student_name
        self.student_course = student_course
        self.student_email = student_email
        self.student_skills = student_skills

student1 = StudentProfile("Rose", "Python", "rose@gmail.com", ["Python", "Java"])
print(student1.student_name)
print(student1.student_course)
print(student1.student_email)
print(student1.student_skills)

student2 = StudentProfile("Alex", "Data Science", "alex@gmail.com", ["Python", "SQL", "R"])
print(student2.student_name)
print(student2.student_course)
print(student2.student_email)
print(student2.student_skills)

student3 = StudentProfile("John", "Web Development", "john@gmail.com", ["HTML", "CSS", "JavaScript"])
print(student3.student_name)
print(student3.student_course)
print(student3.student_email)
print(student3.student_skills)

