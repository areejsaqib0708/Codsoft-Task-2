import tkinter
from tkinter import *
#**********************MAIN WINDOW***********************
root = Tk()
root.title("Simple Calculator")
root.geometry("440x520+100+200")
root.resizable(False,False)
root.configure(bg="#17161b")
equation=""
#******************* FUNCTION TO CLEAR**********************
def clear():
    global equation
    equation=""
    label_result.config(text=equation)

#******************* FUNCTION TO SHOW***********************
def show(value):
    global equation
    if value == '÷':
        equation += '/'
    else:
        equation += value
    label_result.config(text=equation.replace('/', '÷'))

#******************* FUNCTION TO CALCULATE**********************

def calculate():
    global equation
    result=""
    if equation!="":
        try:
            result=eval(equation)
        except:
            result="Error"
            equation=""
    label_result.config(text=result)

label_result=Label(root,width=25,height=2,text="",font=("ariel",30),bg="#D3D3D3")
label_result.pack()
Button(root,width=8,height=1,text="C",font=("ariel",30,"bold"),bd=1,fg="#fff",bg="#4682B4",command=lambda :clear() ).place(x=11,y=105)
Button(root,width=4,height=1,text="÷",font=("ariel",30),bd=1,fg="#000000",bg="#FFFFFF",command=lambda :show("÷") ).place(x=220,y=106)
Button(root,width=4,height=1,text="×",font=("ariel",30),bd=1,fg="#000000",bg="#FFFFFF",command=lambda :show("*")).place(x=330,y=106)

Button(root,width=4,height=1,text="7",font=("ariel",30),bd=1,fg="#fff",bg="#808080",command=lambda :show("7")).place(x=9,y=188)
Button(root,width=4,height=1,text="8",font=("ariel",30),bd=1,fg="#fff",bg="#808080",command=lambda :show("8")).place(x=115,y=188)
Button(root,width=4,height=1,text="9",font=("ariel",30),bd=1,fg="#fff",bg="#808080",command=lambda :show("9")).place(x=222,y=188)
Button(root,width=4,height=1,text="-",font=("ariel",30),bd=1,fg="#000000",bg="#FFFFFF",command=lambda :show("-")).place(x=330,y=188)

Button(root,width=4,height=1,text="4",font=("ariel",30),bd=1,fg="#fff",bg="#808080",command=lambda :show("4")).place(x=9,y=270)
Button(root,width=4,height=1,text="5",font=("ariel",30),bd=1,fg="#fff",bg="#808080",command=lambda :show("5")).place(x=115,y=270)
Button(root,width=4,height=1,text="6",font=("ariel",30),bd=1,fg="#fff",bg="#808080",command=lambda :show("6")).place(x=222,y=270)
Button(root,width=4,height=1,text="+",font=("ariel",30),bd=1,fg="#000000",bg="#FFFFFF",command=lambda :show("+")).place(x=330,y=270)

Button(root,width=4,height=1,text="1",font=("ariel",30),bd=1,fg="#fff",bg="#808080",command=lambda :show("1")).place(x=9,y=351)
Button(root,width=4,height=1,text="2",font=("ariel",30),bd=1,fg="#fff",bg="#808080",command=lambda :show("2")).place(x=115,y=351)
Button(root,width=4,height=1,text="3",font=("ariel",30),bd=1,fg="#fff",bg="#808080",command=lambda :show("3")).place(x=222,y=351)
Button(root,width=4,height=3,text="=",font=("ariel",30),bd=1,fg="#fff",bg="#FF8C00",command=lambda :calculate() ).place(x=331,y=351)

Button(root,width=4,height=1,text="0",font=("ariel",30),bd=1,fg="#fff",bg="#808080",command=lambda :show("0")).place(x=8,y=433)
Button(root,width=9,height=1,text=".",font=("ariel",30),bd=1,fg="#fff",bg="#808080",command=lambda :show(".")).place(x=112,y=433)


root.mainloop()