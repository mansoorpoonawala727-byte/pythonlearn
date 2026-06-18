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

        
       
s1 = Student("Mansoor", 85, "Cybersecurity")
s2 = Student("Ali", 40, "Maths")

s1.display()
s1.passed()
s2.display()
s2.passed()