from Tkinter import *
import ttk

window = Tk()
canvas = Canvas(window, width=854, height=480, bg='white')
canvas.pack()

#Creates window and centers to any screen
window.geometry('{}x{}'. format(874, 670))
window.withdraw()
window.update_idletasks()
w = window.winfo_screenwidth()
h = window.winfo_screenheight() - 70
winsize = tuple(int(_) for _ in window.geometry().split('+')[0].split('x'))
x = w/2 - winsize[0]/2
y = h/2 - winsize[1]/2
window.geometry("%dx%d+%d+%d" % (winsize + (x, y)))
window.title('Sloths - Virtual Robot Treasure Hunt')
window.resizable(width=FALSE, height=FALSE)
window.deiconify()

class Timer():
    def __init__(self, label):
        self.second = 0
        self.minute = 0
        self.hour = 0
        self.stop = False
        self.label = label
        self.sections = {}

    def Stop(self):
        self.stop = True

    def Count(self):
        if self.stop == False:
            self.second = self.second + 1
            if self.second == 60:
                self.minute = self.minute + 1
                self.second = 0
            if self.minute == 60:
                self.hour = self.hour + 1
                self.minute = 0

            #if self.second % 5 == 0:
                #Generate 4 random numbers between 1 - 3

            if self.hour < 10:
                if self.minute < 10:
                    if self.second < 10:
                        exec str(self.label.config(text=("0" + str(self.hour) + ":0" + str(self.minute) + ":0" + str(self.second))))
                    else:
                        exec str(self.label.config(text=("0" + str(self.hour) + ":0" + str(self.minute) + ":" + str(self.second))))
                else:
                    if self.second < 10:
                        exec str(self.label.config(text=("0" + str(self.hour) + ":" + str(self.minute) + ":0" + str(self.second))))
                    else:
                        exec str(self.label.config(text=("0" + str(self.hour) + ":" + str(self.minute) + ":" + str(self.second))))
            else:
                if self.minute < 10:
                    if self.second < 10:
                         exec str(self.label.config(text=(str(self.hour) + ":0" + str(self.minute) + ":0" + str(self.second))))
                    else:
                        exec str(self.label.config(text=(str(self.hour) + ":0" + str(self.minute) + ":" + str(self.second))))
                else:
                    if self.second < 10:
                        exec str(self.label.config(text=(str(self.hour) + ":" + str(self.minute) + ":0" + str(self.second))))
                    else:
                        exec str(self.label.config(text=(str(self.hour) + ":" + str(self.minute) + ":" + str(self.second))))
            self.label.after(1000, self.Count)
        else:
            exec str(self.label.config(text="00:00:00"))

class Lights(Timer):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.sectionWidth = self.width/4

    def CreateLights(self):
        sectionWidth = self.width/4
        light1=canvas.create_rectangle(2, 2, sectionWidth, 23, fill="#2ecc71", tag="1")
        light2=canvas.create_rectangle(sectionWidth, 2, sectionWidth * 2, 23, fill="#f39c12", tag="2")
        light3=canvas.create_rectangle(sectionWidth * 2, 2, sectionWidth * 3, 23, fill="#e74c3c", tag="3")
        light4=canvas.create_rectangle(sectionWidth * 3, 2, ((sectionWidth * 4) - 1), 23, fill="#2ecc71", tag="4")

        light1Text=Label(font=('Helvetica', 8), text='Green', bg="#2ecc71")
        light2Text=Label(font=('Helvetica', 8), text='Amber', bg="#f39c12")
        light3Text=Label(font=('Helvetica', 8), text='Red', bg="#e74c3c")
        light4Text=Label(font=('Helvetica', 8), text='Green', bg="#2ecc71")
        light1Text.place(x=100, y=13)
        light2Text.place(x=310, y=13)
        light3Text.place(x=530, y=13)
        light4Text.place(x=740, y=13)

        whole=canvas.create_rectangle(2, self.height, (self.width - 3), 2)

        section1=canvas.create_rectangle(0, self.height, sectionWidth, 23, dash=(10,10), tag="s1")
        section2=canvas.create_rectangle(sectionWidth, self.height, sectionWidth * 2, 23, dash=(10,10), tag="s2")
        section3=canvas.create_rectangle(sectionWidth * 2, self.height, sectionWidth * 3, 23, dash=(10,10), tag="s3")
        section4=canvas.create_rectangle(sectionWidth * 3, self.height, ((sectionWidth * 4) - 1), 23, dash=(10,10), tag="s4")
                
def Start():
    global main
    global rb1T
    global rb2T
    main = Timer(timer)
    rb1T = Timer(rb1Timer)
    rb2T = Timer(rb2Timer)
    main.Count()
    rb1T.Count()
    rb2T.Count()

def Stop():
    global main
    global rb1T
    global rb2T
    main.Stop()
    rb1T.Stop()
    rb2T.Stop()
    
#Creating frames to seperate controls
Section1 = Frame(bd=1, relief=SUNKEN, height=121, width=161)
Section1.place(x=11, y=500)
Section2 = Frame(bd=1, relief=SUNKEN, height=37, width=161)
Section2.place(x=11, y=623)
Section3 = Frame(bd=1, relief=SUNKEN, height=79, width=689)
Section3.place(x=174, y=500)
Section4 = Frame(bd=1, relief=SUNKEN, height=79, width=689)
Section4.place(x=174, y=581)

#Creating Buttons
btnStart=Button(window, text='Start', height=1, width=20, command=Start)
btnStop=Button(window, text='Stop', height=1, width=20, command=Stop)
btnMap1=Button(window, text='1', height=1, width=2)
btnMap2=Button(window, text='2', height=1, width=2)
btnMap3=Button(window, text='3', height=1, width=2)
btnMap4=Button(window, text='4', height=1, width=2)

#Places buttons in correct positions
btnStart.place(x=16, y=505)
btnStop.place(x=16, y=535)
btnMap1.place(x=16, y=629)
btnMap2.place(x=59, y=629)
btnMap3.place(x=101, y=629)
btnMap4.place(x=141, y=629)

#Creates timer label
timer=Label(font=('Helvetica', 28), text='00:00:00')
timer.place(x=15, y=568)

#Creating robot1 labels
rb1Name=Label(font=('Helvetica', 10, 'underline'), text='Robot 1:')
rb1Position=Label(font=('Helvetica', 10), text='Position:')
rb1Status=Label(font=('Helvetica', 10), text='Status:')
rb1Landmark=Label(font=('Helvetica', 10), text='Landmark:')
rb1Visited=Label(font=('Helvetica', 10), text='Visited:')
rb1TreasurePos=Label(font=('Helvetica', 10), text='Treasure Position:')
rb1Points=Label(font=('Helvetica', 10), text='Points:')
rb1Time=Label(font=('Helvetica', 10), text='Time:')
rb1Timer=Label(font=('Helvetica', 10))

#Places robot1 labels in correct positions
rb1Name.place(x=179, y=505)
rb1Position.place(x=179, y=530)
rb1Status.place(x=179, y=555)
rb1Landmark.place(x=425, y=505)
rb1Visited.place(x=425, y=530)
rb1TreasurePos.place(x=425, y=555)
rb1Points.place(x=700, y=505)
rb1Time.place(x=700, y=530)
rb1Timer.place(x=735, y=530)

#Creating robot2 labels
rb2Name=Label(font=('Helvetica', 10, 'underline'), text='Robot 2:')
rb2Position=Label(font=('Helvetica', 10), text='Position:')
rb2Status=Label(font=('Helvetica', 10), text='Status:')
rb2Landmark=Label(font=('Helvetica', 10), text='Landmark:')
rb2Visited=Label(font=('Helvetica', 10), text='Visited:')
rb2TreasurePos=Label(font=('Helvetica', 10), text='Treasure Position:')
rb2Points=Label(font=('Helvetica', 10), text='Points:')
rb2Time=Label(font=('Helvetica', 10), text='Time:')
rb2Timer=Label(font=('Helvetica', 10))

#Places robot1 labels in correct positions
rb2Name.place(x=179, y=582)
rb2Position.place(x=179, y=607)
rb2Status.place(x=179, y=632)
rb2Landmark.place(x=425, y=582)
rb2Visited.place(x=425, y=607)
rb2TreasurePos.place(x=425, y=632)
rb2Points.place(x=700, y=582)
rb2Time.place(x=700, y=607)
rb2Timer.place(x=735, y=607)

#Padds canvas
canvas.pack(padx=10, pady=10)

lights = Lights(854, 480)
lights.CreateLights()

window.mainloop()
