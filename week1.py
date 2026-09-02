
# week 1 homework

# Method Examples

# class Student:
#     university = "kabul university"
#     def __init__(self,name):
#             self.name = name
#     def display(self):
#         return self.name
#     @classmethod
#     def university_name(cls):
#         return cls.university
#     @staticmethod
#     def valid_age(age):
#         print(cls.university_name())
#         return age >= 16
#
# s = Student("Kabul university")
# s.display()
# print(s.display())

# class Attribution

# class Student:
#     university = "kabul university"
#
#     def __init__(self, name):
#         self.name = name
#         a = Student("Ahmad")
#         b = Student("Sahra")
#
#     S = Student("Sahra")
#     print(a.name)
#     print(b.name)
#     print(a.university)
#     print(b.university)


# polymorphism Example


# def make_sound(animal):
#     print(animal.speak())
#     animals = [cat(),Dog()]
#     for animal in animals:
#         make_sound(animal)
#         print(cat.speak("meo"))

# practical Lab  Student management Model

# from ABC import ABC, abstractmethod
# class person(ABC):
#     def __init__(self, name,email):
#         self.name = name
#         self.email = email
#         @abstractmethod
#         def role_info(self):
#             Pass
#         class Student(person):
#             def __init__(self, name, email, Student_id):
#                 super().__init__(name,email)
#                 self.Student_id = Student_id
#
#                 def role_info(self):
#                     return f"Student: {self.student_id}"
#                 a = Student("Ahmad","Ahmadyar@gmail.com","200010")
#                 print(a)
