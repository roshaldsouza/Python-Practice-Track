class StudentProfile:
    def __init__(self,student_id,student_name,student_score):
        self.student_id = student_id
        self.student_name = student_name
        self.__score = student_score

        def get_score(self):
            return self.__score
        
        def update_score(self,new_score):
            if 0<= new_score <= 100:
                self.__score = new_score
            else:
                print("invalid score")
        def get_status(self):
            if self.__score  >= 60:
                return "Ready"
            else:
                return "Needs Practice"
        def __str__(self):
            return f"name:{self.student_name}  id:{self.student_id}  score:{self.__score}  status:{self.get_status()}"
            