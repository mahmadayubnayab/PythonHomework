# practical lab week 6 : first tkinter window


# import tkinter as tk
# # print(tk.TkVersion)
#
# root = tk.Tk()
# root.title("Advanced programing lab ")
# root.geometry("500x500")
#
# label = tk.Label(root, text= "it is a heading label" )
# label.pack()
#
# root.configure(background="Blue")
# button1 = tk.Button(root,text=" Button Click ")
# button1.place(x=100 , y=100)
# button1.pack()
# button2 = tk.Button(root, text = "close the window ")
# button2.place(x=200 , y=200)
# button2.pack()
# button3 = tk.Button(root , text = "window stay open " )
# button3.place(x=300 , y= 300 )
# button3.pack()
#
# root.mainloop()
#

# examples : more practice

# name = 'ayub'
# print('only you have 3 chances ')
# counter =3
# while counter > 0:
#     guess = input('guess for enter right name : ')
#     counter = counter - 1
#     if guess == name :
#         print('congregulation for win')
#         print('the hide name was ' , name , 'and you entered right name', name )
#         break
#     elif  counter == 0:
#            print('sorry you lose and right name is ' , name )
#     else:
#        print('it is wrong name and try again ')
#        print('only you have ', counter, 'chance ')

#  practical lab 2 : student grade validator


# Custom Exception

# class InvalidGradeError(Exception):
#     pass
#
#
# # Validation Logic
# def validate_grade(value):
#     try:
#         grade = float(value)
#     except (ValueError, TypeError):
#         raise InvalidGradeError("Grade must be a numeric value.")
#
#     if grade < 0 or grade > 100:
#         raise InvalidGradeError("Grade must be between 0 and 100.")
#
#     return grade
#
#
# # User Interface Logic
# def main():
#     print("===== Student Grade Validator =====")
#
#     while True:
#         value = input("Enter student grade (0-100): ")
#
#         try:
#             grade = validate_grade(value)
#             print(f"Valid grade: {grade}")
#             break
#
#         except InvalidGradeError as e:
#             print(f"Invalid Grade: {e}")
#
#
# # Test Cases
# print("\n===== Test Cases =====")
#
# test_values = [85, "92.5", "abc", -10, 150]
#
# for value in test_values:
#     try:
#         result = validate_grade(value)
#         print(f"{value} -> Valid grade: {result}")
#
#     except InvalidGradeError as e:
#         print(f"{value} -> Invalid Grade: {e}")
#
#
# # Run program
# print()
# main()

# practical lab 3 : Robust file reader

# class DocumentReadError(Exception):
#     """Custom exception for document reading failures."""
#     pass
#
#
# def read_document():
#     filename = input("Enter filename: ").strip()
#
#     try:
#         # Context manager
#         with open(filename, "r", encoding="utf-8") as file:
#             content = file.read()
#
#     except FileNotFoundError:
#         print("Error: File not found.")
#
#     except PermissionError:
#         print("Error: Permission denied.")
#
#     except UnicodeDecodeError:
#         print("Error: The file is not valid UTF-8 text.")
#
#     except OSError as error:
#         print(f"Error while reading the file: {error}")
#
#     else:
#         # Only runs when reading succeeds
#         print("\nFile read successfully!")
#         print("----- File Content -----")
#         print(content)
#         print("-----------------------")
#
#
# if __name__ == "__main__":
#     read_document()

# more practise in computer lab :

# number = int(input('enter any number for multiplication table:  '))
# for i in range (1,11):
#     print(i ,'x' , number , '= ', i * number)
# else :
#     print('the program ended ')

# num1 = int(input('enter first number: '))
# num2 = int(input('enter second number: '))
# num3 = int(input('enter third number: '))
#
# if num1 > num2 and num1 > num3:
#     print('the first number is greater than other two numbers', num1)
# elif num2 > num1 and num2 > num3:
#     print('the second number is greater than other two number', num2)
# else:
#     print('the last number is greater than other two numbers ', num3)
#
# print('the program is ended')

# passed = 0
# failed = 0
# for sco in range (1,11):
#     scores = int(input('enter the students score : '))
#
#     if scores >= 60:
#       passed = passed + 1
#
#     else:
#        failed = failed + 1
# print('the ', failed,'students failed')
# print('the ', passed,'students successfuly passed')

# n = 0b1111
# s= 0O23
# print('it is decimal ',n)
# print('it is decimal ', s)

# w = 1020
# print('it is a decimal number ', w)
# print('by binary ',bin(w))
# print('by hexadecimal ', hex(w))
# print('by octal ', oct(w))

# number =int(input('enter any number for saying to it is odd or even : '))
#
# if number % 2 ==0:
#     print('the number is even ', number)
# else:
#     print('the number is odd ', number)


# def method1(id , name , salary ):
#     print('this is method 1 ')
#     print('thid is your id : ' , id)
#     print('this is your name : ' , name )
#     print('your salary is : ' , salary)
#
# # method1(12,'ayub' , 300)
#
# def method2(id = 122 , name = 'Mohammad' , salary = 200):
#     print('this is method 2 ')
#     print('this is your id : ' , id)
#     print('this is your name : ' , name )
#     print('your salary is : ' , salary )
#
# #method2(23, 'Mudasir ahmad' , 350)
#
# def method3(id , name ,  salary = 200 ,):
#     print('this is method 3 ')
#     print('this is your id : ' , id)
#     print('this is your name : ' , name)
#     print('your salary is : ' , salary)
#
# method3(2,'Samiullah ')
