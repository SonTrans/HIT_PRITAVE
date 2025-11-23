class Person:
    def __init__(self,name, yob):
        self.name = name
        self.yob = yob
    def describe(self):
        print(f"Name : {self.name} - Yob : {self.yob}")
class Student(Person):
    def __init__(self, name, yob,grade):
        super().__init__(name, yob)
        self.grade = grade
    def describe(self):
        print(f"Student - Name : {self.name} - Yob : {self.yob} - Grade : {self.grade}")
class Teacher(Person):
    def __init__(self, name, yob,subject):
        super().__init__(name, yob)
        self.subject = subject        
    def describe(self):
        print(f"Teacher - Name : {self.name} - Yob : {self.yob} - subject : {self.subject}")
class Doctor(Person):
    def __init__(self, name, yob,specialist):
        super().__init__(name, yob)
        self.specialist = specialist
    def describe(self):
        print(f"Doctor - Name : {self.name} - Yob : {self.yob} - specialist : {self.specialist}")
class Ward:
    def __init__(self,name):
        self.name = name
        self.people = []
    def addPerson(self,person):
        self.people.append(person)
    def countDoctor(self):
        demso = 0
        for i in self.people:
            if isinstance(i,Doctor) == True:
                demso += 1
        return demso
    def sortAge(self):
        self.people.sort(key = lambda x : x.yob)
    def aveTeacherYearOfBirth(self):
        demso = 0
        tong = 0
        for i in self.people:
            if isinstance(i,Teacher) == True:
                tong += i.yob
                demso += 1
        return tong/demso
    def describe(self):
        print(self.name, " : ")
        for i in self.people:
            i.describe()
student1 = Student(name="studentA", yob=2010, grade="7") 
student1.describe()
student2 = Student(name="son", yob = 2006, grade= 13)
student2.describe()
teacher1 = Teacher(name="teacherA", yob=1969, subject="Math") 
teacher1.describe()
teacher2 = Teacher(name="teacherB", yob=1995, subject="History")
teacher2.describe() 
doctor1 = Doctor(name="doctorA", yob=1945, specialist="Endocrinologists") 
doctor1.describe()
doctor2 = Doctor(name="doctorB", yob=1975, specialist="Cardiologists")
doctor2.describe()
ward1 = Ward(name="Ward1")
ward1.addPerson(student1)
ward1.addPerson(teacher1) 
ward1.addPerson(teacher2) 
ward1.addPerson(doctor1) 
ward1.addPerson(doctor2) 
ward1.describe()
print(f"so luon Doctor trong {ward1.name} : {ward1.countDoctor()}")
print(f"nam sinh tb cua Teacher trong {ward1.name} : {ward1.aveTeacherYearOfBirth()}")
ward1.sortAge()
ward1.describe()
