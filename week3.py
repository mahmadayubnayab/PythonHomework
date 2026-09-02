# week 3

# print('what is your name? ')
# name = input()
# print('Hi ' + name )
# print('what is your favorite color?')
# color = input()
# print(name + ' your favorite color is : ' + color)

# address = input(' where are you from dear : ')
# job = input('what is your job? ')
# print('welcome dear from ' + address)

# patiant_name =input( ' what is patiant name ? ' )
# age = input('how is patiant years old? ')
#
# print(patiant_name + ' you are ' + age + " years old ")


# wheight  = input(' enter the wheight by lbd : ')
# kilogram = int(wheight) * 0.45
# print( wheight  + ' wheight_lbd =  ' + str(kilogram) + " kg ")

# wheight_lbd = 65
# kilogram = 0.45
# convert = wheight_lbd * kilogram
# print(str(wheight_lbd) + ' wheight_lbd = ' + str(convert) + ' Kg')

# name  = input('what is your name? ')
# print('hellow ' + name )
# color = input('what is your favorite color?')
# print(name + " your favorite color is " + color )

# number1 = 20
# number2 = 30
# print(number1 + number2)
#
# num1= int(input('enter your number1 '))
# num2 = int(input('enter your number2 '))
# print( num1 + num2 )

# number = int(input(' enter the number : '))
# if number % 2 == 0:
#     print('the number is even' + number )
# else:
#     print('the number is odd' + number )

# num1 = int(input(' enter number1 :'))
# num2 = int(input(' enter number2 :' ))
# if num1 > num2:
#     print('number1 is greater than number2 ')
# else:
#     print('number2 is greater than number1')

# for numbers in range(1,11):
#     print(numbers * 2 )

# num = input(' enter the number for multiplication table : ')
# for i in range(1,11):
#     print( i , ' x ', num , '= ' , i * int(num))

# total = 0
# for i in range(1,1001):
#     total += 'i'
# print(total)

# password = input('enter the password : ')
#
# if password == 'ayub':
#     print('the password is correct ')
# else :
#     print('the password is incorrect and try again later')

# for i in range(1,4):
#     num = input('enter number : ')
#
# print( "the maximum number is : " + max(num) )

# names = ['Ahmad','wigar', 'faryadi', 'sardar shah']
# for name in names:
#     print(name)

 # student course registration manage


# from typing import TypeVar,Generic,Dict,Set,List
# T = TypeVar('T')
#
# class  CollectionManager(Generic[T]):
#     def __init__(self) -> None:
#         self.items: List[T] = []
#         def add(self, item: T) -> None:
#             self.items.append(item)
#             def get_all(self) -> List[T]:
#                 return self.items
#             class StudentRegistrationManager:
#                 def __init__(self) -> None:
#                     self.students : Dict[int,Dict[str,object]] = {}
#                     def add_student(self, student_id: int, name : str) -> None:
#                         if studnet_id in self.students:
#                             print('student already exists')
#                         else : self.students[student_id] = { "name " : name , "course" : set() }
#                         print("student added successfully")
#
#                         def register_student(self, student_id: int, course  : str) -> None:
#                             if student_id not in self.students:
#                                 print("student does not exist")
#                                 return
#                             courses : Set[str] = self.students[student_id]["course"]
#                             courses.add(course)
#                             print('course registered successfully')
#
#                             def drop_course(self,student_id: int, course : str) -> None:
#                                 if student_id not in self.students:
#                                     print("student not found")
#                                     return
#                                 course : Set[str] = self.students[student_id]["course"]
#                                 if course in courses:
#                                     courses.remove(course)
#                                     print('course dropped successfully')
#                                 else :
#                                     print('student is not registered in this course  ')
#                                     def search_student(self,student_id: int) -> None:
#                                         if student_id not in self.students:
#                                             print("student not found")
#                                             return
#                                         student = self.students[student_id]
#                                         print('student id ' , student_id)
#                                         print('name ', student['name'])
#                                         print('course:',",".join(student['course']))
#
#                                         def display_student(self) -> None:
#                                             sorted_students = sorted(self.students.items(),key=lambda x: x[1]['name'])
#
#                                             print(" student sorted by name ")
#                                             for student_id ,student in sorted_students:
#                                                 print(student_id , student['name'],)
#
#                                                 def display_all_courses(self) -> None:
#                                                     all_courses = {course for student in self.students.values() for course in student['course']}
#                                                     print(" all  unique courses ")
#                                                     for course in sorted(all_courses):
#                                                         print(course)
#                                                         def find_student_by_course(self,course : str) -> None:
#                                                             studetns = [student["name"] for student in self.students.values() if course in student ['course']]
#                                                             print ("student registered in coures ")
#                                                             if studentns :
#                                                                 for name in studentns:
#                                                                     print(name)
#                                                                 else:
#                                                                     print("no student found ")
#
#                                                                     manager = StudentRegistrationManager()
#                                                                     manager.add_student(101,"Ahmad ")
#                                                                     manager.add_student(1020," sami khan ")
#                                                                     manager.add_student(1025," samiullah ")
#                                                                     manager.register_course(10,"python")
#                                                                     manager.register_course(1," Java ")
#                                                                     manager.register_course(11, " Database ")
#                                                                     manager.drop_course(11,"Database")
#                                                                     manager.search_student(101)
#                                                                     manager.display_students()
#                                                                     manager.display_all_courses()
#                                                                     manager.find_students_by_course("python")

 # --------------------------- practice

# number = input('enter one number : ')
# if int(number) > 0:
#     print( number , "number is positive")
# elif int(number) == 0 :
#         print( number , "number is zero ")
# else:
#     print( number , ' number is negative :')
#


# num1 = int(input('  enter the first numbers : '))
# num2 = int(input('enter the second number : '))
# num3 = int(input('enter the third number :'))
# if num1>num2 & num1>num3:
#         print(num1 , 'the first number is greater that other two numbers')
# elif num2>num1 & num2>num3:
#         print(num2 , 'the second number is greater than other two numbers ')
# else:
#         print(num3 , 'the third number is greater than other two numbers :')

# for i in range(1,11):
#     for j in range(1,11):
#         print(i , 'x' , j , ' = ' , i * j )
#         if j == 10 :
#             print('------------------------')

# number = int(input('enter any number for multiplication table  : '))
# for i in range(1,11):
#      print(i , ' x ' , number , ' = ' , i * number )


# for i in range(1 , 101 ):
#     if i % 2 == 0:
#         print(i)

# text = input(' enter text : ')
# print( 'this text has ',text.__len__() , ' characters ' )
