from Tkinter import *
import ttk
import random

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

intPlay = 0

class landmark():                                   # Landmark class being created

    def __init__(self, x1, y1, x2, y2):             # this sets out the layout of how all future objects will be set in order to be created
        self.x1 = x1                                # whatever the objects name.x1 or x2 or y1 or y2, store the value in x1, which then places it in the user interface
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        self.colour  = "green"                      # the background colour for all landmarks is set here to green in the user interface
        self.outline = "black"                      # the outline colour of all landmarks is set to black in the user interface

    def create(self):
        self.lndmrk = canvas.create_rectangle(self.x1,self.y1,self.x2,self.y2, fill=self.colour, outline = self.outline) # creates the landmark with the given coordinates and colours, but they're pre-set.
        

def MapOneLandMarks():                              #creating a new function which will store all the landmarks in the first map
    M1L1 = landmark(30, 50, 180, 95)                 # the coordinate placement of the first landmark, in the first map
    M1L2 = landmark(600,50,800,200)                 # the coordinate placement of the second landmark, in the first map
    M1L3 = landmark(150,200,370,250) 
    M1L4 = landmark(370,50,440,150)                              
    M1L5 = landmark(50,350,110,400)             
    M1L6 = landmark(450,250,600,400)        
    M1L7 = landmark(700,250,750,380)                
    M1L1.create()                                   # this draws the landmark for the first landmark
    M1L2.create()
    M1L3.create()
    M1L4.create()
    M1L5.create()
    M1L6.create()
    M1L7.create()
    
#MapOneLandMarks()                                  # this calls the first map function which loads and creates the first map

def MapTwoLandMarks():                              # this function stores all the landmarks for the second map
    M2L1 = landmark(50, 200, 350, 30)
    M2L2 = landmark(450, 100, 750, 35)
    M2L3 = landmark(400, 280, 780, 230)             # this line of code creates the third landmark and positions it accordingly with the given coordinates
    M2L4 = landmark(350, 350, 550, 430)
    M2L5 = landmark(30, 230, 80, 400)
    M2L6 = landmark(220, 250, 290, 290)
    M2L7 = landmark(690, 400, 750, 350)
    M2L1.create()                                   # this line of code draws out the first landmark
    M2L2.create()
    M2L3.create()
    M2L4.create()
    M2L5.create()
    M2L6.create()
    M2L7.create()
#MapTwoLandMarks()                                   # this line of code calls the funcion which creates and draws out the landmarks for the second map


def MapThreeLandMarks():
    M3L1 = landmark(40, 50, 120, 95)
    M3L2 = landmark(270, 50, 480, 100)
    M3L3 = landmark(750, 54, 800, 105)
    M3L4 = landmark(750, 154, 800, 300)
    M3L5 = landmark(750, 350, 800, 400)
    M3L6 = landmark(220, 150, 550, 300)
    M3L7 = landmark(40, 350, 90, 400)
    M3L1.create()
    M3L2.create()
    M3L3.create()
    M3L4.create()
    M3L5.create()
    M3L6.create()
    M3L7.create()
#MapThreeLandMarks()


def MapFourLandMarks():
    M4L1 = landmark(30, 50, 90, 380)
    M4L2 = landmark(160, 50, 260, 95)
    M4L3 = landmark(550, 50, 600, 225)
    M4L4 = landmark(550, 270, 600, 430)
    M4L5 = landmark(130, 370, 260, 420)
    M4L6 = landmark(130, 200, 280, 250)
    M4L7 = landmark(670, 180, 800, 300)
    M4L1.create()
    M4L2.create()
    M4L3.create()
    M4L4.create()
    M4L5.create()
    M4L6.create()
    M4L7.create()
MapFourLandMarks()

class Robot:
    def __init__(self):
        self.vx = 10.0
        self.vy = 5.0
        self.rXPos = random.randint(1, 100)
        self.rYPos = random.randint(1, 100)

    def robotSpawn(self):
        self.robot = canvas.create_rectangle(self.rXPos, self.rYPos, self.rXPos + 10, self.rYPos + 10, fill = "cyan", outline = "blue")

    def robotMove(self, treasure):
        global x1
        global x2
        global x3
        global x4

        x1, y1, x2, y2 = canvas.coords(self.robot)

        # GENERAL ROBOT MOVEMENT
        if x2 < treasure and y1 > treasure:
            self.vx = 10.0
            self.vy = -5.0
        if x1 > treasure and y1 > treasure:
            self.vx = -10.0
            self.vy = -5.0
        if x2 > treasure and y2 < treasure:
            self.vx = 10.0
            self.vy = 5.0
        if x1 > treasure and y2 < treasure:
            self.vx = -10.0
            self.vy = 5.0

        '''  
        # TRAFFIC LIGHT RESPONSE               
        if x1 > 0.0 and x2 < (213.5 - 10.0): # Checks if Robot is in section 1.
            if section1 == "3": # Check is section 1 is red.
                self.vx = 0.0
                self.vy = 0.0
            if section1 == "2":
                self.vx = 5.0
                self.vy = 2.5
        if x1 > (213.5 + 10.0) and x2 < (427.0 - 10.0):
            if section2 == "3":
                self.vx = 0.0
                self.vy = 0.0
            if section1 == "2":
                self.vx = 5.0
                self.vy = 2.5
        if x1 > (427.0 + 10.0) and x2 < (640.5 - 10.0):
            if section3 == "3":
                self.vx = 0.0
                self.vy = 0.0
            if section1 == "2":
                self.vx = 5.0
                self.vy = 2.5
        if x1 > (640.5 + 10.0) and x2 < (854.0 - 10.0):
            if section4 == "3":
                self.vx = 0.0
                self.vy = 0.0
            if section1 == "2":
                self.vx = 5.0
                self.vy = 2.5'''

class Treasure():
    #create random spawn location of treasure, coordinates need adjusting with landmarks 
    def __init__(self, x,y,size = 12,colour='#ffd700'):
        
        self.x = random.randint(0,840) # coordinates for width of random spawn 
        self.y = random.randint(23,450) # coordinates for height of random spawn 
        self.colour = colour
        self.size = size
        
    def DrawTreasure(self, canvas): #creating the attributes for the treasure
        Treasure1 = canvas.create_oval(self.x,self.y,self.x + self.size, self.y + self.size,outline = self.colour, fill=self.colour,tag= "Treasure")
        # creating object, size goes against each x and y coordinates. tag inplace to call for deletion 

        
class Timer():
    def __init__(self, label):
        self.second = 0
        self.minute = 0
        self.hour = 0
        self.stop = False
        self.label = label
        self.sections = {}

    def Stop(self):
        global intPlay
        intPlay = 0
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

            #Generate 4 random numbers between 1 - 3 for lights
            if self.second % 5 == 0:
                light1.ChangeLight()
                light2.ChangeLight()
                light3.ChangeLight()
                light4.ChangeLight()

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

class Light():
    def __init__(self, number):
        self.width = 854
        self.height = 480
        self.sectionWidth = 213.5
        self.number = number
        self.colour = ""

    def CreateLight(self):
        global lightcolour1
        global lightcolour2
        global lightcolour3
        global lightcolour4
        global section1
        global section2
        global section3
        global section4
        global light1Text
        global light2Text
        global light3Text
        global light4Text
        
        if self.number == 1:
            lightcolour1=canvas.create_rectangle(2, 2, self.sectionWidth, 23, fill="#2ecc71", tag="1")
            section1=canvas.create_rectangle(0, self.height, self.sectionWidth, 23, dash=(10,10), tag="Green")
            light1Text=Label(font=('Helvetica', 8), text='Green', bg="#2ecc71")
            light1Text.place(x=100, y=13)
            self.colour = "Green"
        elif self.number == 2:
            lightcolour2=canvas.create_rectangle(self.sectionWidth, 2, self.sectionWidth * self.number, 23, fill="#f39c12", tag="2")
            section2=canvas.create_rectangle(self.sectionWidth, self.height, self.sectionWidth * 2, 23, dash=(10,10), tag="Amber")
            light2Text=Label(font=('Helvetica', 8), text='Amber', bg="#f39c12")
            light2Text.place(x=310, y=13)
            self.colour = "Amber"
        elif self.number == 3:
            lightcolour3=canvas.create_rectangle(self.sectionWidth * (self.number - 1), 2, self.sectionWidth * self.number, 23, fill="#e74c3c", tag="3")
            section3=canvas.create_rectangle(self.sectionWidth * 2, self.height, self.sectionWidth * 3, 23, dash=(10,10), tag="Red")
            light3Text=Label(font=('Helvetica', 8), text='Red', bg="#e74c3c")
            light3Text.place(x=530, y=13)
            self.colour = "Red"
        elif self.number == 4:
            lightcolour4=canvas.create_rectangle(self.sectionWidth * (self.number - 1), 2, ((self.sectionWidth * self.number) - 1), 23, fill="#2ecc71", tag="4")
            section4=canvas.create_rectangle(self.sectionWidth * 3, self.height, ((self.sectionWidth * 4) - 1), 23, dash=(10,10), tag="Green")
            light4Text=Label(font=('Helvetica', 8), text='Green', bg="#2ecc71")
            light4Text.place(x=740, y=13)
            self.colour = "Green"
        
    def ChangeLight(self):
        intColour = random.randrange(1,4,1)
        global canvas
        
        lightname = "lightcolour" + str(self.number)
        section = "section" + str(self.number)
        
        if intColour == 1:
            self.colour = "Green"
            if self.number == 1:
                light1Text.config(text='Green', bg="#2ecc71")
                canvas.itemconfig(lightcolour1, fill="#2ecc71")
                canvas.itemconfig(section1, tag="Green")
            elif self.number == 2:
                light2Text.config(text='Green', bg="#2ecc71")
                canvas.itemconfig(lightcolour2, fill="#2ecc71")
                canvas.itemconfig(section2, tag="Green")
            elif self.number == 3:
                light3Text.config(text='Green', bg="#2ecc71")
                canvas.itemconfig(lightcolour3, fill="#2ecc71")
                canvas.itemconfig(section3, tag="Green")
            elif self.number == 4:
                light4Text.config(text='Green', bg="#2ecc71")
                canvas.itemconfig(lightcolour4, fill="#2ecc71")
                canvas.itemconfig(section4, tag="Green")
        elif intColour == 2:
            self.colour = "Amber"
            if self.number == 1:
                light1Text.config(text='Amber', bg="#f39c12")
                canvas.itemconfig(lightcolour1, fill="#f39c12")
                canvas.itemconfig(section1, tag="Amber")
            elif self.number == 2:
                light2Text.config(text='Amber', bg="#f39c12")
                canvas.itemconfig(lightcolour2, fill="#f39c12")
                canvas.itemconfig(section2, tag="Amber")
            elif self.number == 3:
                light3Text.config(text='Amber', bg="#f39c12")
                canvas.itemconfig(lightcolour3, fill="#f39c12")
                canvas.itemconfig(section3, tag="Amber")
            elif self.number == 4:
                light4Text.config(text='Amber', bg="#f39c12")
                canvas.itemconfig(lightcolour4, fill="#f39c12")
                canvas.itemconfig(section4, tag="Amber")
        elif intColour == 3:
            self.colour = "Red"
            if self.number == 1:
                light1Text.config(text='Red', bg="#e74c3c")
                canvas.itemconfig(lightcolour1, fill="#e74c3c")
                canvas.itemconfig(section1, tag="Red")
            elif self.number == 2:
                light2Text.config(text='Red', bg="#e74c3c")
                canvas.itemconfig(lightcolour2, fill="#e74c3c")
                canvas.itemconfig(section2, tag="Red")
            elif self.number == 3:
                light3Text.config(text='Red', bg="#e74c3c")
                canvas.itemconfig(lightcolour3, fill="#e74c3c")
                canvas.itemconfig(section3, tag="Red")
            elif self.number == 4:
                light4Text.config(text='Red', bg="#e74c3c")
                canvas.itemconfig(lightcolour4, fill="#e74c3c")
                canvas.itemconfig(section4, tag="Red")
            
def Start():
    global intPlay
    intPlay += 1
    if intPlay <= 1:
        global main
        global rb1T
        global rb2T
        global T1
        global T2
        global T3
        global T4
        main = Timer(timer)
        rb1T = Timer(rb1Timer)
        rb2T = Timer(rb2Timer)
        main.Count()
        rb1T.Count()
        rb2T.Count()
        treasuretest= [] # creating an empty array for number of treasures using for loop 
        for n in range (0,4): #giving a range between 0 - 4 
            treasuretest.append(Treasure(0,0)) #update empty array with given argument 
            treasuretest[n].DrawTreasure(canvas)# draw treasure onto canvas 
        R1 = Robot()
        R1.robotSpawn()
        R1.robotMove()
        
def Stop():
    global main
    global rb1T
    global rb2T
    main.Stop()
    rb1T.Stop()
    rb2T.Stop()
    canvas.delete("Treasure")
                  
   
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


light1 = Light(1)
light2 = Light(2)
light3 = Light(3)
light4 = Light(4)
light1.CreateLight()
light2.CreateLight()
light3.CreateLight()
light4.CreateLight()
whole=canvas.create_rectangle(2, 480, 851, 2)

window.mainloop()
