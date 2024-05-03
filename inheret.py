class person:
    #assigning attributes
    def __init__(self, name, age, cid):
        self.name = name #referencing to the input name
        self.age = age
        self.cid = cid
    #defining beheviours
    def walk(self):
        print(self.name, 'is walking')
    def talk(self):
        print(self.name, 'is talking')
    def sleep(self):
        print(self.name, 'is sleeping')
    def eat(self):
        print(self.name, 'is eating')

class teacher(person): # Student is inheriting from Person
    def __inti__(self, name, age, cid, subject, salary, department, designation):
        # super is referring to the parent class
        super().__init__(name, age, cid)
        self.subject = subject
        self.salary = salary
        self.department = department
        self.designation = designation

    #defining beheviours
    def teach(self):
        print(self.name, 'is teaching')
    def grading_std(self):
        print(self.name, 'is grading')
    def attend_meeting(self):
        print(self.name, 'is attending meeting')

class Student(person): # Student is inheriting from Person
    # specific attributes here
    def __init__(self, name, age, cid, student_id, course, year, gpa):
        # super is referring to the parent class
        super().__init__(name, age, cid)
        self.student_id = student_id
        self.course = course
        self.year = year
        self.gpa = gpa
    
    # specific behaviours / methods for student
    def study(self):
        print(f"{self.name} is studying")
    
    def attend_class(self):
        print(f"{self.name} is attending class")
    
    def write_exam(self):
        print(f"{self.name} is writing exam")

tashi = Student("Tashi", 20, "1234", "123", "BSc", 2, 3.5)
dorji = Student("Dorji", 21, "1235", "124", "BSc", 3, 3.8)

if tashi.gpa > dorji.gpa:
    print(tashi, 'is better than', dorji)
    student_info = 'year' + tashi.year + 'course' + tashi.course
    print(student_info)
else:
    print(dorji, 'is better than', tashi)
    student_info = 'year' + str(dorji.year) + 'course' + dorji.course
    print(student_info)
