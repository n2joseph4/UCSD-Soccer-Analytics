from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,NavigationToolbar2Tk)
from mplsoccer import Pitch
import matplotlib.pyplot as plt 
import csv
import sys
import pandas as pd

try:
    df = pd.read_csv("ucsbShots.csv")
    numOpportunities = df.get("numOpportunity").max()+1
except FileNotFoundError:
    with open("ucsbShots.csv","w") as f:
                dataWriter = csv.writer(f)
                dataWriter.writerow(["Game","numOpportunity","Event","Result","Start Pos","End Pos","Team","Player"])
                numOpportunities = 0
print(numOpportunities)
#GUI
window = Tk()
window.geometry("1200x1200")
window.configure(bg = "white")
#row_1 = Frame(window,height=100,bg="white")
row_2 = Frame(window,height=100,bg="white")
title = Label(window,text="Stat Collector", font=("Arial",25,),bg="black", fg="white")

game = StringVar(window)
game.set("Enter a game")
gameEntry = ttk.Entry(window,textvariable=game)

player = StringVar(window)
player.set("Enter a player")
playerEntry = ttk.Entry(window,textvariable=player)

def eventSelect(event):
    eventSelected = event.widget.get()
    # eventResults = eventOptionWithResults[eventSelected]

eventOptions = ["Shot(foot)","Shot(head)", "Pass","Tackle", "Save","Throw-in","Set Piece","1st Ball","2nd Ball"]
eventSelected = StringVar(window)
eventSelected.set("Select an event")
eventOption = ttk.Combobox(window,textvariable=eventSelected,values = eventOptions,)
eventOption.bind("<<ComboboxSelected>>",eventSelect)

def eventResultSelect(event):
    eventResult = event.widget.get()
eventResults = ["Successful", "Unsuccessful"]
# eventOptionWithResults = {"Shot":["OnFrame","OffFrame","Goal","Blocked"], "Pass":["Received","Intercepted","Select an event","Select an event"], "Cross":["Int by 1st Man","Int Past 1st Man","Received"],"Run":["Played","Dragged","None"],\
#     "Tackle":["Won","Lost","Cleared","Foul"], "Save":["Held","Parried","Tipped"], "Punt":["Kept","Lost"],"Throw":["Kept", "Lost"],"Corner":["Received", "Cleared", "Other"],\
#     "SetPiece":["Pass","Cross","Shot","Select an event"],"Throw-in":["Kept","Lost","Select an event","Select an event"],"Select an event": ["Select an event","Select an event","Select an event","Select an event"]}
eventResult = StringVar(window)
eventResult.set("Select a result")
eventResultOption = ttk.Combobox(window,textvariable=eventResult,values = eventResults)
eventResultOption.bind("<<ComboboxSelected>>",eventResultSelect)


def playerSelect(event):
    playerSelected = event.widget.get()
playerOptions = ["Jonah","Woody","Quin","Nolan","Adam","Evan","Matt","Carter","Cole","UCSD","Opponent"]
teamOptions = ["UCSD","Opponent"]
playerSelected = StringVar(window)
playerSelected.set("Select a team")
playerOption = ttk.Combobox(window,textvariable=playerSelected,values = teamOptions)
playerOption.bind("<<ComboboxSelected>>",playerSelect)

# def receiverSelect(event):
#     receiverSelected = event.widget.get()
# receiverOptions = ["Dylan Huy","Nic Thiele","Evan Wellerstein","Matt Lin","Andrew Valverde","Brian Arens",
#     "Quinn Sellers","Nolan Sanchez","Peter Santos","Jonah Kawamura","Nate Morgan","Connor Place","Max Carvalho",
#     "Carter Jacobus","Keenai Braun","Elliott Hill","Andrew McGee","James Redington","Nikita","Joey Asfari","UCSD","Opponent"]
# receiverSelected = StringVar(window)
# receiverSelected.set("Select a reveiver")
# receiverOption = ttk.Combobox(row_1,textvariable=receiverSelected,values = receiverOptions,)
# receiverOption.bind("<<ComboboxSelected>>",receiverSelect)

# def bodPartSelect(event):
#     bodyPartSelected = event.widget.get()
# bodyPartOptions = ["Right Foot","Left Foot","Head","Other"]
# bodyPartSelected = StringVar(window)
# bodyPartSelected.set("Right Foot")
# bodyPartOption = ttk.Combobox(row_2,textvariable=bodyPartSelected,values=bodyPartOptions)
# bodyPartOption.bind("<<ComboboxSelected>>",bodPartSelect)

# def heightSelect(event):
#     heightSelected = event.widget.get()
# heightOptions = ["Ground", "Air"]
# heightSelected = StringVar(window)
# heightSelected.set("Ground")
# heightOption = ttk.Combobox(row_2,textvariable=heightSelected,values=heightOptions)
# heightOption.bind("<<ComboboxSelected>>",heightSelect)

canvasFrame = Frame(window,width=800,height=800)
pitch = Pitch(positional=True, axis=True,label=True)
fig, ax = plt.subplots(figsize = (10,6))
pitch.draw(ax=ax)
canvas = FigureCanvasTkAgg(fig,master= canvasFrame)
canvas.draw()


first_click = True
start_pos = [-1,-1]
end_pos = [-1,-1]
def click(event):
    global first_click
    global start_pos
    global end_pos
    x_pos = event.xdata
    y_pos = event.ydata
    try:
        if 0<=x_pos<=120 and 0<=y_pos<=80:
            
            if first_click:
                
                start_pos[0] = x_pos
                start_pos[1] = y_pos
                first_click = False
                ax.cla()
                pitch.draw(ax=ax,)
                plt.plot(x_pos,y_pos, 'ro')
            else:
                
                end_pos[0] = x_pos
                end_pos[1] = y_pos
                plt.arrow(start_pos[0],start_pos[1],end_pos[0]-start_pos[0],end_pos[1]-start_pos[1],width = .3)
                first_click = True
        canvas.draw()
    except TypeError as e:
        print(e.message)
keyPressToEvent = {" ": "Pass","f":"Tackle","d":"Throw-in","s":"Shot","a":"Save","c":eventResults[0],"v":eventResults[1]}
# def press(e):
#     try:
#         print(e)
#         if e.keycode == 16:
#             submit()
#         if e.char in " fdas":
#             eventSelected.set(keyPressToEvent[e.char])
#         elif e.char in "cv":
#             eventResult.set(keyPressToEvent[e.char])
#         elif e.char =='r':
#             playerSelected.set("UCSD")
#         elif e.char == 't':
#             playerSelected.set("Opponent")
        
            
#     except KeyError:
#         pass
#     except IndexError:
#         pass
# window.bind("<KeyPress>",press)
            
canvas.mpl_connect('button_press_event',click)

def incrementOpportunity():
    global numOpportunities
    numOpportunities+=1
incrementButton = ttk.Button(text="Increment Opportunity",command=incrementOpportunity)

def submit():
    global start_pos
    global end_pos
    global numEvents
    if -1 not in start_pos:
        with open("ucsbShots.csv","a") as f:
            dataWriter = csv.writer(f)
            dataWriter.writerow([game.get(),numOpportunities,eventSelected.get(),eventResult.get(),start_pos,end_pos,playerSelected.get(),player.get()])#,receiverSelected.get(),numEvents,heightSelected.get(),bodyPartSelected.get()])
        print(start_pos,end_pos)
        ax.cla()
        pitch.draw(ax = ax)
        first_click = True
        canvas.draw()
        start_pos = [-1,-1]
        end_pos = [-1,-1]
        # playerSelected.set(receiverSelected.get())
        # receiverSelected.set("Select a receiver")
    else:
        messagebox.showinfo("Error","You need to select a position")

    
submitButton = ttk.Button(text="Submit Stat",command=submit)
window.bind("")
#submitButton.config({"width":50,"height":30})


def close():
    window.destroy()
    sys.exit()
closeButton = ttk.Button(text="Close Program",command=close)

#row_1.pack(fill=X,)
#title.pack(fill=X)
title.grid(row=0,column=0,columnspan=3,pady=10)

#eventOption.pack( padx= 30, pady= 30,)
eventOption.grid(row=1,column=0)
#eventResultOption.pack(padx= 30,pady= 30)
eventResultOption.grid(row=1,column=1)
# receiverOption.pack(side = RIGHT,padx= 30,pady= 30)
#playerOption.pack(side = LEFT, padx= 30,pady= 30)
playerOption.grid(row=1,column=2)

#row_2.pack(fill=X)
#gameEntry.pack(padx=70, pady=30)
gameEntry.grid(row=2,column=0,pady=10)
incrementButton.grid(row=2,column=1,pady=10)
playerEntry.grid(row=2,column=2,pady=10)
# bodyPartOption.pack(side=RIGHT,padx=70,pady=30)
# heightOption.pack(side = RIGHT, padx= 70, pady = 30)

canvasFrame.grid(row=3,column=0,columnspan=3)
canvas.get_tk_widget().pack(fill=BOTH)
submitButton.grid(row=4, column=1)
closeButton.grid(row=5,column=1,pady=20)
mainloop()