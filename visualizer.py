import cube
import solver
import moves
import cv2
import numpy as np
from tkinter import *
from PIL import Image, ImageTk

state=  {
            'up':['white','white','white','white','white','white','white','white','white',],
            'right':['white','white','white','white','white','white','white','white','white',],
            'front':['white','white','white','white','white','white','white','white','white',],
            'down':['white','white','white','white','white','white','white','white','white',],
            'left':['white','white','white','white','white','white','white','white','white',],
            'back':['white','white','white','white','white','white','white','white','white',]
        }

def process(operation):
    replace = {
        "F":[moves.F, 1],
        "U":[moves.U, 1],
        "R":[moves.R, 1],
        "D":[moves.D, 1],
        "B":[moves.B, 1],
        "L":[moves.L, 1],
        "F2":[moves.F, 2],
        "U2":[moves.U, 2],
        "R2":[moves.R, 2],
        "D2":[moves.D, 2],
        "B2":[moves.B, 2],
        "L2":[moves.L, 2],
        "F'":[moves.F, 3],
        "U'":[moves.U, 3],
        "R'":[moves.R, 3],
        "D'":[moves.D, 3],
        "B'":[moves.B, 3],
        "L'":[moves.L, 3]
    }
    
    a = 0
    for i in operation:
        replace[i][0](replace[i][1])
        cv2.putText(preview, i, (700,a+50), font,1,(0,255,0), 1, cv2.LINE_AA)  
        fill_stickers(preview, stickers, state)
        solution.append(preview)
        cv2.imshow('solution', preview)
        cv2.waitKey()
        cv2.putText(preview, i, (700,50), font,1,(0,0,0), 1, cv2.LINE_AA)

color = {
    'red': (0, 0, 255), 
    'green': (0, 255, 0), 
    'blue': (255, 0, 0), 
    'orange': (0, 165, 255), 
    'white': (255, 255, 255), 
    'yellow': (0, 255, 255)
}

stickers = {
    'main': [
        [200, 120], [300, 120], [400, 120],
        [200, 220], [300, 220], [400, 220],
        [200, 320], [300, 320], [400, 320]
    ],
    'current': [
        [20, 20], [54, 20], [88, 20],
        [20, 54], [54, 54], [88, 54],
        [20, 88], [54, 88], [88, 88]
    ],
    'preview': [
        [20, 130], [54, 130], [88, 130],
        [20, 164], [54, 164], [88, 164],
        [20, 198], [54, 198], [88, 198]
    ],
    'left': [
        [50, 280], [94, 280], [138, 280],
        [50, 324], [94, 324], [138, 324],
        [50, 368], [94, 368], [138, 368]
    ],
    'front': [
        [188, 280], [232, 280], [276, 280],
        [188, 324], [232, 324], [276, 324],
        [188, 368], [232, 368], [276, 368]
    ],
    'right': [
        [326, 280], [370, 280], [414, 280],
        [326, 324], [370, 324], [414, 324],
        [326, 368], [370, 368], [414, 368]
    ],
    'up': [
        [188, 128], [232, 128], [276, 128],
        [188, 172], [232, 172], [276, 172],
        [188, 216], [232, 216], [276, 216]
    ],
    'down': [
        [188, 434], [232, 434], [276, 434],
        [188, 478], [232, 478], [276, 478],
        [188, 522], [232, 522], [276, 522]
    ],
    'back': [
        [464, 280], [508, 280], [552, 280],
        [464, 324], [508, 324], [552, 324],
        [464, 368], [508, 368], [552, 368]
    ]
}

font = cv2.FONT_HERSHEY_SIMPLEX  
text_points =  {
            'up':[['U',242, 202],['W',(255,255,255),260,208]],
            'right':[['R',380, 354],['R',(0,0,255),398,360]],
            'front':[['F',242, 354],['G',(0,255,0),260,360]],
            'down':[['D',242, 508],['Y',(0,255,255),260,514]],
            'left':[['L',104,354],['O',(0,165,255),122,360]],
            'back':[['B',518, 354],['B',(255,0,0),536,360]],
        }

def draw_stickers(frame, stickers, name):
        for x, y in stickers[name]:
            cv2.rectangle(frame, (x, y), (x+30, y+30), (255, 255, 255), 2)

def draw_preview_stickers(frame, stickers):
        stick = ['front', 'back', 'left', 'right', 'up', 'down']
        for name in stick:
            for x, y in stickers[name]:
                cv2.rectangle(frame, (x, y), (x+40, y+40), (255, 255, 255), 2)

def texton_preview_stickers(frame, stickers):
        stick = ['front', 'back', 'left', 'right', 'up', 'down']
        for name in stick:
            for x, y in stickers[name]:
                sym, x1, y1 = text_points[name][0][0], text_points[name][0][1], text_points[name][0][2]
                cv2.putText(preview, sym, (x1,y1), font, 1, (0, 0, 0), 1, cv2.LINE_AA)  
                sym, col, x1, y1 = text_points[name][1][0], text_points[name][1][1], text_points[name][1][2], text_points[name][1][3]             
                cv2.putText(preview, sym, (x1,y1), font, 0.5, col, 1, cv2.LINE_AA)  

def fill_stickers(frame, stickers, sides):    
    for side, colors in sides.items():
        num = 0
        for x, y in stickers[side]:
            cv2.rectangle(frame, (x,y), (x+40,y+40), color[colors[num]], -1)
            num += 1

def color_detect(h,s,v):
    # print(h,s,v)
    if h in range(150,179): #and s in range(132,255) and v in range(175,255):
        return 'red'
    elif h in range(0,25): #and s in range(160,255) and v in range(152,255):
        return 'orange'
    elif h in range(25,40): #and h>10:
        return 'yellow'
    elif h in range(42,70): #and s in range(90,255) and v in range(0,255):
        return 'green'
    elif h in range(78,106): #and s in range(90,255) and v in range(0,255):
        return 'blue'
    elif h in range(107,148): #and s<10 and v<200:
        return 'white'

    return 'white'

check_state = []
solution = []
solved = False

def setSide(side):
    state[side] = current_state
    check_state.append(side)

def solve():
    if len(set(check_state)) == 6:    
            try:
                solved = solver.solve(state)
                if solved:
                    operation = solved.split(' ')
                    process(operation)
            except:
                print("Error in side detection. You may have not followed sequence or some color not detected well. Try again")
    else:
        print("All sides are not scanned. Check other window for finding which side(s) are left to be scanned")
        print("Left to scan:", 6-len(set(check_state)))

window = Tk()
window.title("Rubix Cube Solver")
window.resizable(0, 0)

frame1 = LabelFrame(window)
frame1.grid(row=0, column=0)
label1 = Label(frame1)
label1.pack()
frame2 = LabelFrame(window)
frame2.grid(row=0, column=1,rowspan=2)
label2 = Label(frame2)
label2.pack()
frame3 = LabelFrame(window)
frame3.grid(row=1, column=0)
button1 = Button(frame3, text="Send to Front", command= lambda: setSide("front"))
button1.grid(row=0, column=0, padx=2, pady=2)
button2 = Button(frame3, text="Send to Back", command= lambda: setSide("back"))
button2.grid(row=1, column=0, padx=2, pady=2)
button3 = Button(frame3, text="Send to Up", command= lambda: setSide("up"))
button3.grid(row=2, column=0, padx=2, pady=2)
button4 = Button(frame3, text="Send to Down", command= lambda: setSide("down"))
button4.grid(row=0, column=1, padx=2, pady=2)
button5 = Button(frame3, text="Send to Left", command= lambda: setSide("left"))
button5.grid(row=1, column=1, padx=2, pady=2)
button6 = Button(frame3, text="Send to Right", command= lambda: setSide("right"))
button6.grid(row=2, column=1, padx=2, pady=2)
button7 = Button(frame3, text="Solve", command=solve)
button7.grid(row=0, column=2, padx=2, pady=2)
button8 = Button(frame3, text="Quit", command=window.destroy)
button8.grid(row=1, column=2, padx=2, pady=2)

cap = cv2.VideoCapture(0)

def main():
    global preview
    preview = np.zeros((700,800,3), np.uint8)
    
    while(True):
        global current_state
        success, vid = cap.read()
        current_state=[]
        frame = cv2.cvtColor(vid, cv2.COLOR_BGR2HSV)
        k = cv2.waitKey(1) & 0xFF
        draw_stickers(vid, stickers, 'main')
        draw_stickers(vid, stickers, 'current')
        draw_preview_stickers(preview, stickers)
        
        hsv=[]
        for i in range(9):
            hsv.append(frame[stickers['main'][i][1]+10][stickers['main'][i][0]+10])
        
        a=0
        for x,y in stickers['current']:
            color_name = color_detect(hsv[a][0],hsv[a][1],hsv[a][2])
            cv2.rectangle(vid,(x,y),(x+30,y+30),color[color_name],-1)
            a+=1
            current_state.append(color_name)
        
        fill_stickers(preview, stickers, state)
        texton_preview_stickers(preview, stickers)
        
        vid1 = cv2.cvtColor(vid, cv2.COLOR_BGR2RGB)
        vid1 = ImageTk.PhotoImage(Image.fromarray(vid1))
        label1["image"] = vid1
        
        vid2 = cv2.cvtColor(preview, cv2.COLOR_BGR2RGB)
        vid2 = ImageTk.PhotoImage(Image.fromarray(vid2))
        label2["image"] = vid2
        
        window.update()
        
    cap.release()
    cv2.destroyAllWindows()

def start():
    main()