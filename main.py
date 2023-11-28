from tkinter import*
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
root.mainloop()           