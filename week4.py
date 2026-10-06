# practical lab  : text file student record
#
# def creat_file():
#     records = [
#         "id , name , faculty , age "
#         "1001, Ahmad , computer science , 19 "
#         "100, Mohammad , information technology , 21"
#         " 2001, Najibullah , information system , 22"
#         " 201 , Abdul wali , software Engineering , 19"
#         " 455, Mudasir Ahmad , information system , 20"
#
#     ]
#     with open("student.txt", "w" , encoding="utf-8") as file:
#         for record in records:
#             file.write(record + "\n")
#             def read_records():
#                 try:
#                     with open ("student.txt", "r", encoding = "utf-8") as file:
#                         records = file.readlines()
#                         print("\n ---------- all student records ---------")
#                         if not records:
#                             print("no records found! ")
#                         else :
#                             for record in records:
#                                 print(record.rstrip())
#                 except FileNotFoundError:
#
#                                 print("student.txt does not exist!")
#                                 def search_student():
#                                     student_id = input("enter student id to search:").strip()
#                                     try:
#                                         with open("student.txt", "r", encoding = "utf-8") as file:
#                                             for record in file:
#                                                 fields = record.strip().split(",")
#                                                 if fields[0] == student_id:
#                                                     print("student found : " , record.strip())
#                                                     return
#                                                 print("student not found !")
#                                     except FileNotFoundError :
#                                                 print("student.txt does not exsit ")
#                                                 def append_student():
#                                                     student_id = input("enter id ").strip()
#                                                     name = input("enter name").strip()
#                                                     department = input("enter department ").strip()
#                                                     age = input("enter age").strip()
#                                                     try:
#                                                          with open("student.txt", "a", encoding = "utf-8") as file:
#                                                              file.write(f"{student_id},{name},{department},{age}")
#                                                              print("new student added successfully ")
#                                                     except FileNotFoundError:
#                                                                          print("student.txt does not exist!")
#                                                                          def main():
#                                                                              creat_file()
#                                                                              print("student.txt created successfully ")
#                                                                              read_records()
#                                                                              search_student()
#                                                                              append_student()
#                                                                              print("\n ---------- records after adding new student -----------")
#                                                                              read_records()
#                                                                              if __name__ == "__main__":
#                                                                                  main()
#                                                                                  print(records)
#                                                                                  print(read_records())
#
#
#
#
#
# from operator import truediv

# hackerRank examples

# name = input('enter your name ? ')
#
# if name.__eq__('ayub'):
#     print('Hellow welcome to dear ' , name)
# else:
#     print('your name is wrong and try again  ' , name)
#


# advanced Exercise

# from typing import Generic , TypeVar
# T = TypeVar('T')
# class Stack (Generic[T]):
#     def __init__(self) :
#         self._items: list[T] = []
#
#         def push(self,item : T) -> None:
#             self._items.append(item)
#             def pop(self) -> T:
#              if not self._items:
#                 raise IndexError('Stack is empty')
#             return self._items.pop()

# if else statement examples

# tempreature = int(input('the tempreature of today '))
#
# if tempreature > 30 :
#     print('it is a hot day')
# elif tempreature <10:
#     print('it is a cold day ')
# else :
#     print('it is a good day ')

# price = 1000000
# has_good_credit = False
#
# if has_good_credit:
#     payment = price * 10 /100
#     print(f"buyer should be pay  ${ payment } to you")
# else:
#     payment = price * 20 /100
#     print(f"buyer should be pay  ${ payment } to you ")

# name = input(" enter name  : " )
#
# if len(name) < 5:
#     print('name must be short ' , len(name))
# elif len(name) > 30:
#     print('name must be long ' , len(name))
#
# else:
#     print('name is very good not short and not long ' , len(name))

# small game

# secret_number = 9
# number = 0
# chance  = 3
# while number < chance :
#     guess = int(input('guess : '))
#     number += 1
#     if guess == secret_number:
#         print(' you win dear ')
#         break
# else :
#     print('you faild in guess')

# else if statement

# weight = int(input('enter your weight : '))
# convert = input('convert to (L)lb or (K)kg : ')
#
# if convert == 'l':
#     pounds = weight / 0.45
#     print(f"your weight is { pounds } lb")
# else:
#     kilograms = weight * 0.45
#     print(f"your weight is {kilograms } kg ")

# car = ""
#
# while car != 'quit':
#  car = input(' > ')
#  if car == "help":
#     print('start - to start the car ')
#     print('stop - to stop the car ')
#     print('quit - to exit the car')
#  elif car == "start":
#     print('car is ready to started ...')
#  elif car == "stop":
#      print('Car stopped. ')
#  else:
#      print(' sorry, i do not understand ')

# find maximum number in lists

# numbers = [2,3,5,1000,87,53,67,199]
# max = numbers[0]
#
# for number in numbers:
#     if number > max:
#       max = number
#       print(max)


# age = int(input('enter the person age: '))
# if age >=18 :
#     print('you are an adult ')
# else:
#     print('you are not a teenager')

# number = int(input("Enter a number: "))
# if number >  0:
#     print('the number is positive')
# elif number < 0:
#     print('the number is negative ')
# else :
#     print('the number is zero')

# score = int(input('enter the score : '))
# if score >= 90:
#     print('you are in grade A ')
# elif score >= 80:
#     print('you are in grade B')
# elif score >=70:
#     print('you are in grade C')
# else:
#     print('you are in grade D')

# for i in range(1,20):
#
#     if i % 2 == 0:
#      print(i)
#

# count = 0
# for i in range(1,50):
#     if i % 5 == 0:
#         print(i)
#         count += i
# print(count)

