import tkinter as tk


window  = tk.Tk()
window.title(' first GUI project ')
window.geometry("600x600")
window.configure(background='white')

header = tk.Label(window , text = "System Login " , font = ("Arial", 30, 'bold') )
header.grid(row = 0 , column = 0 , columnspan=5 , padx= 100 ,pady = 0)


def login():

    username = usernameEntry.get()
    password = passwordEntry.get()
    if username == "admin" and password == "123":
        message.config( background="yellow", text = "you loggined successfully ")
    else:
       message.config(background="red", text =  "username or password is wrong ")

usernamelabel = tk.Label(window , text = " username : " ,padx = 10, pady = 1)
usernamelabel.grid(row=1 , column = 0 , padx = 10 , pady = 1)

passwordlabel = tk.Label(window , text = " password : " ,padx = 10, pady = 1)
passwordlabel.grid(row = 2 , column = 0 , padx = 10 , pady = 10)

button = tk.Button (window , text ="login" , command = login , padx= 10 )
button.grid(row=5 , column = 6 , padx = 10 , pady = 10 )

usernameEntry  = tk.Entry(window )
usernameEntry.grid(row = 1 , column = 1 , padx= 10 , pady = 10)

passwordEntry  = tk.Entry(window )
passwordEntry.grid(row  = 2 , column = 1 , padx = 10 , pady = 10)

message = tk.Label(window , text = "" , font = ("Arial " , 13 , 'bold'))
message.grid(row = 8 , column = 1 , padx = 10 , pady = 10)

window.mainloop()
