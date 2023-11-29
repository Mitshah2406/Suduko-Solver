'''from tkinter import*
root=Tk()
root.title("Sudoku Solver beta-VVM1")
root.geometry("700x380")
##"324x550"yeh og dimenstion hai for my grids
label=Label(root,text="Fill in the numabers and click solve").grid(row=0,column=1,columnspan=10)
errLabel=Label(root,text="",fg="red")
errLabel.grid(row=15,column=1,columnspan=10,pady=5)
solvedLabel=Label(root,text="",fg="green")
solvedLabel.grid(row=15,column=1,columnspan=10,pady=5)
cell={}
cells={}
def ValidateNumber(P):
    out=(P.isdigit() or P=="")and len(P)<2
    return out

def draw3x3Grid(row,coloum,bgcolour):
     for i in range(3):
         for j in range(3):
             e=Entry(root,width=5,bg=bgcolour,justify="center",validate="key",validatecommand=(reg,"%P"))
             e.grid(row=row+i+1,column=coloum+j+1,sticky="nsew",padx=1,pady=1,ipady=5)
             cells[(row+i+1,coloum+j+1)]=e
def draw9x9Grid():
    color="#F0FFFF"
    for rowNo in range(1,10,3):
        for colNo in range(0,9,3):
            draw3x3Grid(rowNo,colNo,color)
            if color=="#F0FFFF":
                color="#4194FF"
            else:
                color="#F0FFFF"
def clearValues():
    errLabel.configure(text="")
    solvedLabel.configure(text="")
    for row in range(2,11):
        for col in range(1,10):
            cell=cells[(row,col)]
            cell.delete(0,"end")
def getValues():
    board=[]
    errLabel.configure(text="")
    solvedLabel.configure(text="")
    for row in range(2,11):
        row=[]
        rows=[]
        for col in range(1,10):
            val=cells[(row,col)].get()
            if val=="":
                rows.append(0)
            else:
                rows.append(int(val))
        board.append(rows)
reg=root.register(ValidateNumber)
btn=Button(root,command=getValues,text="Solve",width=15,height=2,foreground="white",background="#4194FF")
btn.grid(row=13,column=1,columnspan=5,pady=20)

btn=Button(root,command=getValues,text="Clear",width=15,height=2,foreground="white",background="#4194FF")
btn.grid(row=13,column=5,columnspan=5,pady=20)

draw9x9Grid()
root.mainloop()'''           

from tkinter import *
import tkinter as tk


# Create the main window
root = tk.Tk()
root.title("Sudoku Solver")
root.configure(bg="#194972")
root.geometry("650x320")

#fonts used
font_=("Bookman Old Style",9)
font01=("Comic Sans MS",10)
font02=("Cambria",9)
font03=("Comic Sans MS",12,"bold")


#create another frame for sudoku board
frame01=tk.Frame(root,padx=10,pady=10)
frame01.configure(bg="#194972")
cells={}

#creating sudoku board
def ValidateNumber(P):
    out=(P.isdigit() or P=="")and len(P)<2
    return out
reg=root.register(ValidateNumber)
def draw3x3Grid(row,coloum,bgcolour):
     for i in range(3):
         for j in range(3):
             
             e=Entry(frame01,width=5,bg=bgcolour,justify="center",validate="key",validatecommand=(reg,"%P"))
             e.grid(row=row+i+1,column=coloum+j+1,sticky="nsew",padx=1,pady=1,ipady=5)
             cells[(row+i+1,coloum+j+1)]=e
def draw9x9Grid():
    color="#F0FFFF"
    for rowNo in range(1,10,3):
        for colNo in range(0,9,3):
            draw3x3Grid(rowNo,colNo,color)
            if color=="#F0FFFF":
                color="#4194FF"
            else:
                color="#F0FFFF"
            
draw9x9Grid()


# Create a frame (panel) for numpad
frame = tk.Frame(root, padx=10, pady=10)
frame.configure(bg="#194972")

# creating numpad
cells02={}


def draw3x3Grid01(row,column,bgcolor):
    for i in range(3):
        if i==0:
            y=i+1
        elif i==1:
            y=i+3
        else:
            y=i+5
        for j in range(3):
            x=y+j
            b=Button(frame,text=x,width=4,bg=bgcolor,relief="groove",activebackground="#dce3ed",justify="center",font=font_,fg="#5a7bc0",command=lambda x=x: button_click(x))
            b.grid(row=row+i+1,column=column+j+1,sticky="nsew",padx=1,pady=1,ipady=5)
            cells02[(row+i+1,column+j+1)]=b

draw3x3Grid01(0,0,"#eaeef4")

#adding functionstion to undo,remove,clear and numpad buttons:
#numpad button:
def button_click(button_text):
    a = root.focus_get()
    if isinstance(a, tk.Entry):
        b= a.get()
        a.delete(0, tk.END)
        a.insert(tk.END, b + str(button_text))

#remove button:
def button_click01(button_text):
    a = root.focus_get()
    if isinstance(a, tk.Entry):
        b = a.get()
        a.delete(0, tk.END)

#clear button:
def clear_entry():

    for b,a in cells.items():
        a.delete(0,tk.END)
    

#creating the solve cell,solve, undo ,remove,clear buttons,labels and placing the frames created on the screen:
b1=Button(root,text="Solve Cell",width=10,bg="#a8a8aa",justify=CENTER,relief="groove",activebackground="#dce3ed",font=font01,fg="White")
b2=Button(root,text="Clear",width=10,bg="#a8a8aa",justify=CENTER,relief="groove",activebackground="#dce3ed",font=font01,fg="White",command=clear_entry)
b3=Button(root,text="Undo",width=10,bg="#a8a8aa",justify=CENTER,relief="groove",activebackground="#dce3ed",font=font01,fg="White")
b4=Button(root,text="Remove",width=10,bg="#a8a8aa",justify=CENTER,relief="groove",activebackground="#dce3ed",font=font01,fg="White",command=lambda X=X: button_click01(X))
b5=Button(root,text="Solve",width=22,height=1,bg="#5a7bc0",justify=CENTER,relief="groove",activebackground="#dce3ed",font=font03,fg="White")

L1=Label(root,text="Functions:",justify=LEFT,font=font02,fg="White",bg="#194972")
#L2=Label(root,text="Note:To enter your question choose a cell and use the number pad given below to give the input:",justify=LEFT,wraplength=300,bg="#194972",font=font02,fg="White")

frame01.place(x=20,y=10)
L1.place(x=370,y=10)
b1.place(x=400,y=30)
b2.place(x=500,y=30)
b3.place(x=400,y=70)
b4.place(x=500,y=70)
#L2.place(x=370,y=105)
frame.place(x=420,y=110)
b5.place(x=380,y=270)

#Run the Tkinter event loop
root.mainloop()