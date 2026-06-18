class Student:
    def __init__(self, name, grade, subject):
        self.name = name       
        self.grade = grade     
        self.subject = subject  
     
    def display(self):
        print(f"Name: {self.name} | Subject: {self.subject} | Grade: {self.grade}")
    
    def passed(self):
        if self.grade >= 50:
            print(f"{self.name} passed!")
        else:
            print(f"{self.name} failed!")

class collegestudent(Student):
     def __init__(self,name,grade,subject,collegename,gpa):
         super().__init__(name,grade,subject)
         self.collegename = collegename
         self.gpa = gpa
     def display(self):
         print(f"name-{self.name} | college-{self.collegename} | gpa-{self.gpa}")  
cs1 = collegestudent("Mansoor", 85, "Cybersecurity", "MIT", 3.8)
cs1.display()
cs1.passed()             