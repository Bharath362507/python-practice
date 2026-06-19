class Student:
    def __init__(self,name,rollno,marks):
        self.name = name
        self.rollno = rollno
        self.marks = marks
    def talk(self):
        print("hello my name is:",self.name)
        print("my roll no is:",self.rollno)
        print("my marks are:",self.marks)
s1=Student("prateek",101,80)
s1.talk()