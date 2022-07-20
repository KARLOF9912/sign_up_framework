
from msilib.schema import File
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk
import ast

root=Tk()
root.title('App_Login_Page')
root.geometry('925x500+300+200')
root.configure(bg="#fff")
root.resizable(False,False)

def sign_in():
    usernames=user.get()
    passwords=Code.get()

    file=open('Datasheet.txt','r',encoding="UTF-8")
    d=file.read()
    r=ast.literal_eval(d)
    file.close

    if usernames in r.keys() and passwords==r[usernames]:
        screen=Toplevel(root)
        screen.title("App")
        screen.geometry('925x500+300+200')
        screen.config(bg='white')

        Label(screen,text='Hello',bg='#fff',font=('Calibri(Body)',50,'bold')).pack(expand=True)
        screen.mainloop()
    elif usernames != 'admin' and passwords != 'hello1234':
        messagebox.showerror("Invalid_Warning","Invalid Username or Password")

def signup_cmd():
    PROGRAM_WINDOW = Toplevel(root)
    PROGRAM_WINDOW.title("Sign up")
    PROGRAM_WINDOW.geometry('925x500+300+200')
    PROGRAM_WINDOW.configure(bg='#fff')
    PROGRAM_WINDOW.resizable(False,False)

    importimage = ImageTk.PhotoImage(file='./Assest/Met.png')
    Label(PROGRAM_WINDOW,image=importimage,border=0,bg='white').place(x=50,y=90)

    frame=Frame(PROGRAM_WINDOW,width=350,height=390,bg='#fff')
    frame.place(x=480,y=50)

    heading=Label(frame,text='Sign up',fg='#57a1f8',bg='white',font=('Microsoft Yahei UI Light',23,'bold'))
    heading.place(x=100,y=5)

    def signup():
         usernames=user.get()
         passwords=code.get()
         conform_password=Conform.get()

         if passwords==conform_password:
             try:
                 file=open('Datasheet.txt','r+',encoding="UTF-8")
                 d=file.read()
                 r=ast.literal_eval(d)

                 dict2={usernames:passwords}
                 r.update(dict2)
                 file.truncate(0)
                 file.close

                 file=open('Datasheet.txt','w')
                 w=file.write(str(r))

                 messagebox.showinfo('Signup','Successfully')
             except:
                file=open('Datasheet.txt','w')
                pp=str({'Username':'password'})
                file.write(pp)
                file.close()
             else:
                 messagebox.showerror('Invalid',"Both Password should match!")
    def sign():
     PROGRAM_WINDOW.destroy()

#################################################

    def on_enter(e):
     user.delete(0,'end')

    def on_leave(e):
     if user.get()=='':
        user.insert(0,'Username')

    user = Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft Yahei UI Light',11))
    user.place(x=30,y=80)
    user.insert(0,'Username')
    user.bind("<FocusIn>",on_enter)
    user.bind("<FocusOut>",on_leave)

    Frame(frame,width=295,height=2,bg='black').place(x=25,y=107)

#################################################

    def on_enter(e):
        code.delete(0,'end')

    def on_leave(e):
     if code.get()=='':
        code.insert(0,'Password')

    code = Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft Yahei UI Light',11))
    code.place(x=30,y=150)
    code.insert(0,'Password')
    code.bind("<FocusIn>",on_enter)
    code.bind("<FocusOut>",on_leave)

    Frame(frame,width=295,height=2,bg='black').place(x=25,y=177)

#################################################

    Conform = Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft Yahei UI Light',11))
    Conform.place(x=30,y=220)
    Conform.insert(0,'Confirm Password')


    Frame(frame,width=295,height=2,bg='black').place(x=25,y=247)

###########################3

    Button(frame,width=39,pady=7,text='Sign up',bg='#57a1f8',fg='white',border=0,cursor='hand2',command=signup).place(x=35,y=280)
    Justtext = Label(frame,text="I have an account",fg='black',bg='white',font=('Microsoft Yahei UI Light',9))
    Justtext.place(x=90,y=340)


    signin=Button(frame,width=6,text='Sign in',border=0,bg='white',cursor='hand2',fg='#57a1f8',command=sign)
    signin.place(x=200,y=340)

    PROGRAM_WINDOW.mainloop()   

IMG =  ImageTk.PhotoImage(file="./Assest/Icon.png")
Label(root,image=IMG,bg='white').place(x=50,y=50)

frame=Frame(root,width=350,height=350,bg="white")
frame.place(x=480,y=70)


heading=Label(frame,text='Sign in',fg='#57a1f8',bg='white',font=('Microsoft YaHei UI Light',23,'bold'))
heading.place(x=100,y=5)

def on_enter(e):
    user.delete(0,'end')

def on_leave(e):
    name=user.get()
    if name=='':
        user.insert(0,'Username')


##################################################################

user = Entry(frame,width=25,fg='black',border=0,bg="white",font=('Microsoft YaHei UI Light',11,))
user.place(x=30,y=80)
user.insert(0,'Username')
user.bind('<FocusIn>',on_enter)
user.bind('<FocusOut>',on_leave)

Frame(frame,width=295,height=2,bg='black').place(x=25,y=107)

##################################################################

def on_enter(e):
    Code.delete(0,'end')

def on_leave(e):
    name=Code.get()
    if name=='':
        Code.insert(0,'Password')

Code = Entry(frame,width=25,fg='black',border=0,bg="white",font=('Microsoft YaHei UI Light',11,))
Code.place(x=30,y=150)
Code.insert(0,'Password')
Code.bind('<FocusIn>',on_enter)
Code.bind('<FocusOut>',on_leave)


X = Frame(frame,width=295,height=2,bg='black').place(x=25,y=177)

##################################################################

Button(frame,width=39,pady=7,text='Sign in',bg='#57a1f8',fg='white',border=0,command=sign_in,cursor='hand2').place(x=35,y=204)
label=Label(frame,text="Don't have an account?",bg='white',fg='black',font=('Microsoft YaHei UI Light',9))
label.place(x=75,y=270)

sign_up=Button(frame,width=6,text="Sign up",border=0,bg='white',cursor='hand2',fg='#57a1f8',command=signup_cmd)
sign_up.place(x=215,y=270)

root.mainloop()
