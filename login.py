from tkinter import * 
#defining login function
def login():
    #getting form data
    global un,pwd
    un=username.get()
    pwd=password.get()
    #applying empty validation
    if un=='' or pwd=='':
        message.set("fill the empty field!!!")
    else:
      if un=="san123" and pwd=="san":
          message.set("Login success")
          login_screen.destroy()
      else:
       message.set("Wrong username or password!!!")
#defining loginform function
def Loginform():
    global login_screen
    login_screen = Tk()
    #Setting title of screen
    login_screen.title("Login Form")
    #setting height and width of screen
    login_screen.geometry("800x600")
    Label(login_screen,width="300", text="Admin Login", bg="#732CAF",fg="black",font=("arial", 15, "bold")).pack()
    #declaring variable
    photo=PhotoImage(file='logo.gif')
    Photo1=Label(login_screen,image=photo)
    Photo1.pack()
    global  message;
    global username
    global password
    username = StringVar()
    password = StringVar()
    message=StringVar()
    #Username Label
    Label(login_screen, text="Username * ",font=("arial", 15, "bold")).place(x=220,y=40)
    #Username textbox
    Entry(login_screen, textvariable=username).place(x=350,y=42)
    #Password Label
    Label(login_screen, text="Password * ",font=("arial", 15, "bold")).place(x=220,y=80)
    #Password textbox
    Entry(login_screen, textvariable=password ,show="*").place(x=350,y=82)
    #Label for displaying login status[success/failed]
    Label(login_screen, text="",textvariable=message).place(x=290,y=100)
    #Login button
    Button(login_screen, text="Login", width=10, height=1, bg="#732CAF",font=("arial", 15, "bold"),command=login).place(x=300,y=140)
    login_screen.mainloop()
#calling function Loginform
Loginform()
import MP1
