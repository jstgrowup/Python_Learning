class Student:
    def __init__(self,name,age,grade):
        self.name=name
        self.age=age
        self.grade=grade
    def introduce(self):
        return f"Hi i am {self.name}"
    def get_status(self):
        if self.grade>=90:
            return "excellent"
        elif self.grade>=90:
            return "Good"
student1=Student("Alice",20,96)
student2=Student("bob",20,96)
print(student1.name)  
print(student1.introduce())   
print(student1.get_status())   
print(student2.get_status())