import tkinter as tk
from visualizer import start

def scan_cube():
    start()

def helpwin():
    roo = tk.Tk()
    roo.geometry("250x180+0+0")
    roo.title("Help")
    fr = tk.Frame(roo,width = 170,height=160,bg="black",relief=tk.SUNKEN,padx=10,pady=10)
    fr.pack(fill=tk.BOTH, expand=True)
    lbl1 = tk.Label(fr,
                 text="Help",
                 fg="white",
                 bg="black",
                 font=("Verdana",16,"bold")
                 ).pack()

    lbl2 = tk.Label(fr,
                 text="""1)Press the scan button.\n2)Align the rubik's cube with\n the on screen grid.\n3)Input all the six sides of cube.\n4)Press the solve button.\n5)Get your result.""",
                 fg="white",
                 bg="black",
                 font=("Verdana",10),
                 justify=tk.LEFT
                 ).pack()

    button1 = tk.Button(fr,
                text="Exit",
                width=8,
                bg="blue",
                fg="yellow",
                highlightcolor="white",
                font=("Verdana",14),
                command=roo.destroy
                ).pack()

    roo.mainloop()

def aboutwin():
    roo1 = tk.Tk()
    roo1.geometry("250x180+0+0")
    roo1.title("About")
    fr1 = tk.Frame(roo1,width = 170,height=160,bg="black",relief=tk.SUNKEN,padx=10,pady=10)
    fr1.pack(fill=tk.BOTH, expand=True)
    lbl1 = tk.Label(fr1,
                 text="About",
                 fg="white",
                 bg="black",
                 font=("Verdana",16,"bold")
                 ).pack()

    lbl2 = tk.Label(fr1,
                 text="""Project made by Group 160\n\nMembers\nPratham Sachdev(20BCE10444)\nGaurav Tilwani(20BCE10429)\nNihar Goyal(20BCE10936)\nUtkarsh Swarup(20BCE10101)\nTanmay Kachroo(20BCE10142)""",
                 fg="white",
                 bg="black",
                 font=("Verdana",10),
                 justify=tk.LEFT
                 ).pack()

    button1 = tk.Button(fr1,
                text="Exit",
                width=8,
                bg="blue",
                fg="yellow",
                highlightcolor="white",
                font=("Verdana",14),
                command=roo1.destroy
                ).pack()

    roo1.mainloop()

window = tk.Tk()
window.geometry('380x140')
logo = tk.PhotoImage(master=window,file="cube1.gif")
window.title("Rubik Cube Solver")

"""window.columnconfigure([0,1], minsize=50)
window.rowconfigure([0, 1], minsize=50)"""


f1 = tk.Frame(window,width = 170,height=160,bg="black",relief=tk.SUNKEN,padx=10,pady=10)
f1.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

f2 = tk.Frame(window ,width = 170,height=160,bg="black", relief=tk.SUNKEN,pady=10)
f2.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

"""bottoms = tk.Frame(window,bg="white",width = 340,height=80,relief=tk.SUNKEN)
bottoms.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)"""

menu = tk.Menu(window)
window.config(menu=menu)
filemenu = tk.Menu(menu)
menu.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label='Scan', command=scan_cube)
filemenu.add_command(label='Exit', command=window.quit)
helpmenu = tk.Menu(menu)
menu.add_cascade(label='Help', menu=helpmenu)
helpmenu.add_command(label='Help', command=helpwin)
helpmenu.add_command(label='About', command=aboutwin)

label1 = tk.Label(f2,
                 image=logo,
                 height=100,
                 width=100
                 ).pack()

label2 = tk.Label(f1,
                 text="Rubik's Cube Solver",
                 fg="white",
                 bg="black",
                 font=("Verdana",16,"bold")
                 ).pack()

label3 = tk.Label(f1,
                 text="A Simple App to Solve\nYour 3x3 Cubes",
                 fg="white",
                 bg="black",
                 font=("Verdana",12)
                 ).pack()

button = tk.Button(f1,
                text="Scan",
                width=10,
                bg="blue",
                fg="yellow",
                highlightcolor="white",
                font=("Verdana",16),
                command=scan_cube
                ).pack()

"""button1 = tk.Button(window,
    text="Quit",
    width=10,
    bg="blue",
    fg="yellow",
    highlightcolor="white",
    command=window.quit
)"""
"""label1.grid(row=0,column=1)
label2.grid(row=0,column=0)
button.grid(row=1,column=0,columnspan = 2)
#button1.grid(row=1,column=1,sticky="n")"""
window.mainloop()