import tkinter, threading, math, time, random
from random import choice as randChoice
from PIL import Image, ImageTk

canvasHeight = 400
canvasWidth = 600
imageCoordsX = 300
imageCoordsY = 200
sleepTime = 2
timeConversionConstant = 60
nameQuestionCoordsX = canvasWidth / 2
nameQuestionCoordsY = 40
textCoordsX = 300
textCoordsY = 200


class Tehlicky(tkinter.Canvas):

    def __init__(self):
        self.playerName = ""
        self.canvas = tkinter.Canvas(bg="light cyan", height=canvasHeight, width=canvasWidth)
        self.canvas.pack()

        numOfLoadingPictures = 16
        for loadingPic in range(numOfLoadingPictures):
            self.canvas.delete("all")
            picture = ImageTk.PhotoImage(Image.open("load{}.bmp".format(loadingPic)))
            self.canvas.create_image(imageCoordsX, imageCoordsY, image=picture)
            self.canvas.update()
            self.canvas.after(random.randrange(80, 300))
        self.canvas.delete("all")

        self.farby = ["Navy", "medium blue", "blue", "RoyalBlue1", "SteelBlue1", "SkyBlue1"]
        self.tehly, self.tehla, self.tehlyCoords = [], "", []
        self.tehlaWidth, self.tehlaHeight = 30, 15
        self.readyGame()
        self.canvas.mainloop()

    def readyGame(self):
        self.canvas.create_text(textCoordsX, 30,
                                text="Welcome, player!", font="Papyrus 30")
        self.canvas.create_text(60, 80,
                                text="Some Info:", font="Papyrus 15 bold")
        self.canvas.create_text(217, 110,
                                text="* you move the               left & right with mouse", font="Papyrus 15")
        self.canvas.create_text(185, 110,
                                text="platform", fill="gold", font="Papyrus 15 bold")
        self.canvas.create_text(275, 140,
                                text="* you can hit the             once, meaning you have 1 extra life",
                                font="Papyrus 15")
        self.canvas.create_text(193, 140,
                                text="ground", fill="green3", font="Papyrus 15 bold")
        self.canvas.create_text(225, 170, text="* but then the               breaks and          appears",
                                font="Papyrus 15")
        self.canvas.create_text(170, 170,
                                text="ground", fill="green3", font="Papyrus 15 bold")
        self.canvas.create_text(340, 170, text="lava", fill="red", font="Papyrus 15 bold")
        self.canvas.create_text(450, 200, text="und das ist nicht gut", fill="red", font="Papyrus 15 bold")
        self.canvas.create_text(100, 240, text="Goal of this game?", font="Papyrus 15 bold")
        self.canvas.create_text(260, 270, text="* break through the Earth`s atmosphere and go to space",
                                font="Papyrus 15")
        self.canvas.create_text(185, 300, text="* btw, do not destroy it all or you will lose", font="Papyrus 15")
        self.canvas.create_text(300, 330,
                                text="* we down here will still need some of it to protect us from UV & stuff",
                                font="Papyrus 15")
        self.canvas.create_text(300, 370, text="Press Enter whenever you feel like it~", font="Papyrus 15 bold")

        self.canvas.bind_all("<Key>", self.delete)

    def delete(self, event):
        self.canvas.delete("all")
        self.canvas["bg"] = "light cyan"
        self.canvas.create_text(nameQuestionCoordsX, nameQuestionCoordsY, text="What is your name?", font="Papyrus 30")
        self.canvas.bind_all("<Key>", self.namePlayer)
        self.canvas.bind_all("<Return>", self.buildGame)

    def namePlayer(self, event):
        self.canvas.bind_all("<Return>", self.buildGame)
        key = event.keysym

        if key.isalnum():
            self.canvas.delete("all")
            self.canvas.create_text(nameQuestionCoordsX, nameQuestionCoordsY, text="What is your name?",
                                    font="Papyrus 30")
            self.playerName += key
            self.canvas.create_text(textCoordsX, textCoordsY, text=self.playerName, font="Papyrus 20")

        elif key == "BackSpace":
            self.canvas.delete("all")
            self.canvas.create_text(nameQuestionCoordsX, nameQuestionCoordsY, text="What is your name?",
                                    font="Papyrus 30")
            self.playerName = self.playerName[0:len(self.playerName) - 1]
            self.canvas.create_text(textCoordsX, textCoordsY, text=self.playerName, font="Papyrus 20")

    def buildGame(self, event):
        self.canvas.delete("all")
        self.canvas["bg"] = "light cyan"
        self.canvas.unbind_all('<Key>')
        tempTehlyCoords = []
        tempTehly = []
        x, y = 0, 0
        for farba in range(len(self.farby)):
            while (x + self.tehlaWidth) <= canvasWidth:
                self.tehla = self.canvas.create_rectangle(x, y,
                                                          x + self.tehlaWidth, y + self.tehlaHeight,
                                                          fill=self.farby[farba], outline="")
                tempTehlyCoords.append((x, y))
                tempTehly.append(self.tehla)
                x += self.tehlaWidth
            self.tehlyCoords.append(tempTehlyCoords)
            self.tehly.append(tempTehly)
            x = 0
            y += self.tehlaHeight

        grassTop = canvasHeight - 40
        grassBottom = canvasHeight - 30
        groundBottom = canvasHeight - 20
        self.grass = self.canvas.create_rectangle(0, grassTop, canvasWidth, grassBottom,
                                                  fill="green3", outline="")
        self.ground = self.canvas.create_rectangle(0, grassBottom, canvasWidth, groundBottom,
                                                   fill="NavajoWhite4", outline="")
        self.lava = self.canvas.create_rectangle(0, groundBottom, canvasWidth, canvasHeight,
                                                 fill="red", outline="")
        self.groundLevel = [self.grass]
        self.platformBuild()
        stopky = threading.Thread(target=self.time, args=())
        stopky.start()

    def accelerationCounter(self):
        accelerationLimit = 0.009
        self.acceleration = 0.035
        while self.acceleration > accelerationLimit:
            self.acceleration -= 0.002
            time.sleep(sleepTime / 2)

    ## ----- platform:

    def platformBuild(self):
        self.platformX, self.platformY, self.platformWidth, self.platformHeight = 300, 350, 80, 10
        self.platform = self.canvas.create_rectangle(self.platformX - (self.platformWidth // 2),
                                                  self.platformY - (self.platformHeight // 2),
                                                  self.platformX + (self.platformWidth // 2),
                                                  self.platformY + (self.platformHeight // 2),
                                                  fill="gold")

    def platformMove(self, event):
        distance = event.x - self.platformX
        self.canvas.move(self.platform, distance, 0)
        self.platformX = event.x

    ## ----- circle:

    def circleBuild(self):
        directions = (-2, -1, 1, 2)
        self.ballX, self.ballY, self.ballXDirection, self.ballYDirection, self.ballWidth, self.ballHeight = 300, 200, randChoice(
            directions), randChoice(directions), 20, 20
        self.ball = self.canvas.create_oval(self.ballX - (self.ballWidth // 2), self.ballY - (self.ballHeight // 2),
                                            self.ballX + (self.ballWidth // 2), self.ballY + (self.ballHeight // 2),
                                            fill="grey", outline="")

    def circleMove(self):
        while self.gameOngoing:
            self.canvas.move(self.ball, self.ballXDirection, self.ballYDirection)
            self.ballX, self.ballY = self.ballX + self.ballXDirection, self.ballY + self.ballYDirection
            time.sleep(self.acceleration)
            ballYLimit = 100
            if self.ballY < ballYLimit:
                for tehla in range(len(self.tehlyCoords)):
                    for tehlaCoords in range(len(self.tehlyCoords[tehla])):
                        if self.tehly[tehla][tehlaCoords] != None:
                            tehlaCoordsX = self.tehlyCoords[tehla][tehlaCoords][0]
                            tehlaCoordsY = self.tehlyCoords[tehla][tehlaCoords][1]
                            if (tehlaCoordsX) <= self.ballX <= ((tehlaCoordsX) + self.tehlaWidth) and (tehlaCoordsY) <= self.ballY - (self.ballHeight // 2) <= ((tehlaCoordsY) + self.tehlaHeight):
                                if self.ballX >= (tehlaCoordsX + self.tehlaWidth) or self.ballX <= (tehlaCoordsX):
                                    self.ballXDirection = -self.ballXDirection
                                else:
                                    self.ballYDirection = -self.ballYDirection

                                rowTehly = self.tehly.pop(tehla)
                                brokenTehla = rowTehly.pop(tehlaCoords)
                                rowTehly.insert(tehlaCoords, None)
                                self.canvas.delete(brokenTehla)
                                self.tehly.insert(tehla, rowTehly)
                                self.canvas.move(self.ball, self.ballXDirection, self.ballYDirection)
                                self.ballX, self.ballY = self.ballX + self.ballXDirection, self.ballY + self.ballYDirection
                                time.sleep(self.acceleration)


            elif (self.ballX - (self.ballWidth // 2) <= 1) or self.ballX + (self.ballWidth // 2) >= canvasWidth - 1:
                self.ballXDirection = -self.ballXDirection
                self.canvas.move(self.ball, self.ballXDirection, self.ballYDirection)
                self.ballX, self.ballY = self.ballX + self.ballXDirection, self.ballY + self.ballYDirection
                time.sleep(self.acceleration)

            elif self.ballY >= (canvasHeight - ballYLimit):
                platformCoords = self.canvas.coords(self.platform)

                if ((platformCoords[0] <= self.ballX <= platformCoords[2]) or (
                     platformCoords[0] <= self.ballX - math.ceil(self.ballWidth / 2) <= platformCoords[2]) or (
                     platformCoords[0] <= self.ballX + math.ceil(self.ballWidth / 2) <= platformCoords[2])) and \
                     platformCoords[1] <= self.ballY + 1 + math.ceil(self.ballHeight / 2):
                    if self.ballX + math.ceil(self.ballWidth / 2) <= platformCoords[0] or self.ballX - math.ceil(
                            self.ballWidth / 2) >= platformCoords[2]:
                        self.ballXDirection = -self.ballXDirection
                    else:
                        self.ballYDirection = -self.ballYDirection

                if self.grass in self.groundLevel:
                    if self.ballY + (self.ballHeight // 2) >= canvasHeight - 39:
                        self.ballYDirection = -self.ballYDirection
                        self.canvas.move(self.ball, self.ballXDirection, self.ballYDirection)
                        self.ballX, self.ballY = self.ballX + self.ballXDirection, self.ballY + self.ballYDirection
                        time.sleep(self.acceleration)
                        self.grassTouched = threading.Thread(target=self.firstFall, args=())
                        self.grassTouched.start()

                elif self.lava in self.groundLevel:
                    if self.ballY + (self.ballHeight // 2) >= canvasHeight - 20:
                        self.gameLost()

            elif self.ballY - self.tehlaHeight <= 0:
                self.gameWon()

    ## ----------------------

    def firstFall(self):
        self.groundLevel.pop()
        self.groundLevel.append(self.lava)
        self.canvas.delete(self.grass)
        self.canvas.delete(self.ground)
        text = self.canvas.create_text(textCoordsX, textCoordsY,
                                       text="Uh oh. Is it so hot in here or is it just me?",
                                       font="Papyrus 20 bold",
                                       fill="red")
        time.sleep(5)
        self.canvas.delete(text)

    def gameLost(self):
        self.end = round(time.time() - self.start)
        self.canvas.delete("all")
        self.gameOngoing = False
        self.canvas.unbind_all('<Key>')
        self.canvas["bg"] = "black"
        endSpeech = ("*sad music starts playing*",
                     "So... ", "You didn`t make it, huh?",
                     "I`m sorry about that..", "that`s life, though.",
                     "But... ", "*hopeful music starts playing*", "Always look on the bright side of life, right?",
                     "...and start the game again, ok?",
                     "Good luck.")
        text = ""
        for word in range(len(endSpeech)):
            time.sleep(sleepTime)
            self.canvas.delete(text)
            farba = "white"
            if "*" in endSpeech[word]:
                farba = "grey"
            text = self.canvas.create_text(textCoordsX, textCoordsY,
                                           text=endSpeech[word],
                                           font="Papyrus 20 bold",
                                           fill=farba)
        time.sleep(sleepTime)
        self.canvas.delete("all")
        self.highScore()

    def gameWon(self):
        self.end = round(time.time() - self.start)
        self.gameOngoing = False
        Word(self.end, self.playerName)
        self.canvas.unbind_all('<Key>')
        self.canvas.delete("all")
        self.canvas["bg"] = "black"
        endSpeech = ("*happy music starts playing*", "Player!",
                     "You did it! ^^", "Humans of this realm are proud of you.",
                     "You may now procceed to the--", "~",
                     "Thank you for playing.", "Have a nice day. :)")
        text = ""
        for word in endSpeech:
            time.sleep(sleepTime)
            self.canvas.delete(text)
            farba = "SteelBlue1"
            if "~" in word:
                farba = "gold"
                text = self.canvas.create_text(textCoordsX, textCoordsY,
                                               text=word,
                                               font="Papyrus 35 bold",
                                               fill=farba)
                spacePicture = ImageTk.PhotoImage(Image.open("SpaceCore.jpg"))
                self.canvas.create_image(imageCoordsX, imageCoordsY, image=spacePicture)
                time.sleep(sleepTime / 2)
                text = self.canvas.create_text(textCoordsX, textCoordsY + 150,
                                               text="I`m in space! Need to see it all!",
                                               font="Papyrus 15 bold",
                                               fill="grey")
                time.sleep(sleepTime)
                self.canvas.delete("all")
            else:
                text = self.canvas.create_text(textCoordsX, textCoordsY,
                                               text=word,
                                               font="Papyrus 20 bold",
                                               fill=farba)

        time.sleep(sleepTime)
        self.canvas.delete("all")
        self.highScore()

    def highScore(self):
        with open("tabulka.txt", "r") as txt:
            row = txt.readline().strip()
            score = []
            while row:
                nameEnd = row.find(" ")
                name = row[0:nameEnd]
                timeMiddle = row.find(":")
                minutes = row[nameEnd + 1:timeMiddle]
                seconds = row[timeMiddle + 1:len(row)]
                score.append((minutes, seconds, name))
                row = txt.readline().strip()

        sortedScore = sorted(score)

        self.canvas.create_text(textCoordsX, 50, text="The Best of The Best:", font="Papyrus 30 bold", fill="gold")
        text = sortedScore[0][2] + " " + str(sortedScore[0][0]) + ":" + str(sortedScore[0][1])
        self.canvas.create_text(textCoordsX, 110, text=text, font="Papyrus 20 bold", fill="gold")
        text = sortedScore[1][2] + " " + str(sortedScore[1][0]) + ":" + str(sortedScore[1][1])
        self.canvas.create_text(textCoordsX, 140, text=text, font="Papyrus 18", fill="azure2")
        text = sortedScore[2][2] + " " + str(sortedScore[2][0]) + ":" + str(sortedScore[2][1])
        self.canvas.create_text(textCoordsX, 170, text=text, font="Papyrus 17", fill="tan1")

        for line in range(3, 9):
            text = sortedScore[line][2] + " " + str(sortedScore[line][0]) + ":" + str(sortedScore[line][1])
            self.canvas.create_text(textCoordsX, 140 + line * 25, text=text, font="Papyrus 15", fill="white")

    ## ----- general

    def time(self):
        countDown = None
        countDownStart = 3
        countDownFinish = 0
        countDownReduction = -1
        for numCountDown in range(countDownStart, countDownFinish, countDownReduction):
            self.canvas.delete(countDown)
            countDown = self.canvas.create_text(textCoordsX, textCoordsY,
                                                text=str(numCountDown), font="Papyrus 40 bold")
            time.sleep(sleepTime / 2)
        self.canvas.delete(countDown)
        countDown = self.canvas.create_text(textCoordsX, textCoordsY,
                                            text="Start!", font="Papyrus 40 bold")
        time.sleep(sleepTime / 2)
        self.canvas.delete(countDown)
        self.circleBuild()
        time.sleep(0.3)

        self.canvas.bind('<Button-1>', self.platformMove)

        self.time = threading.Thread(target=self.accelerationCounter, args=())
        self.time.start()
        self.start = time.time()

        self.gameOngoing = True
        self.circleMove()


class Word:

    def __init__(self, time, name):
        self.time = time
        if name == "":
            self.name = "Unknown"
        else:
            self.name = name
        self.createEntry(self.time, self.name)

    def createEntry(self, time, name):
        minutes = time // timeConversionConstant
        seconds = time % timeConversionConstant
        if len(str(seconds)) == 1:
            seconds = "0" + str(seconds)
        entry = str(name) + " " + str(minutes) + ":" + str(seconds) + "\n"
        self.write(entry)

    def write(self, entry):
        with open("tabulka.txt", "a") as leaderBoard:
            leaderBoard.write(entry)


Tehlicky()

##import tkinter, time, threading, math, time, random
##from random import choice as rc
##from PIL import Image, ImageTk
##
##
##class Tehlicky(tkinter.Canvas):    
##    def __init__(self):
##        self.canvas = tkinter.Canvas(bg="light cyan", height=400, width=600)
##        self.w, self.h = canvasWidth
# , canvasHeig
##        self.canvas.pack()   
##        
##        for i in range(16):
##            self.canvas.delete("all")
##            obr = ImageTk.PhotoImage(Image.open("load{}.bmp".format(i)))
##            self.canvas.create_image(300,200, image=obr)
##            self.canvas.update()
##            self.canvas.after(random.randrange(80,300))
##        self.canvas.delete("all")
##
##        self.farby = ["Navy", "medium blue", "blue", "RoyalBlue1", "SteelBlue1", "SkyBlue1"]
##        self.pole, self.chibipole, self.tehla, self.polecoords, self.polecoordshelp = [], [], "", [], []
##        self.x, self.y, self.a, self.b = 0, 0, 30, 15
##        self.get_ready()        
##        self.canvas.mainloop()
##
##    def get_ready(self):
##        self.canvas.create_text(self.w / 2, 30,
##                                text="Welcome, player!", font="Papyrus 30")
##        self.canvas.create_text(60, 80,
##                                text="Some Info:", font="Papyrus 15 bold")
##        self.canvas.create_text(217, 110,
##                                text="* you move the               left & right with mouse", font="Papyrus 15")
##        self.canvas.create_text(185, 110,
##                                text="platform", fill="gold", font="Papyrus 15 bold")
##        self.canvas.create_text(275, 140,
##                                text="* you can hit the             once, meaning you have 1 extra life", font="Papyrus 15")
##        self.canvas.create_text(193, 140,
##                                text="ground", fill="green3", font="Papyrus 15 bold")
##        self.canvas.create_text(225, 170, text="* but then the               breaks and          appears", font="Papyrus 15")
##        self.canvas.create_text(170, 170,
##                                text="ground", fill="green3", font="Papyrus 15 bold")
##        self.canvas.create_text(340, 170, text="lava", fill="red", font="Papyrus 15 bold")
##        self.canvas.create_text(450, 200, text="und das ist nicht gut", fill="red", font="Papyrus 15 bold")
##        self.canvas.create_text(100, 240, text="Goal of this game?", font="Papyrus 15 bold")
##        self.canvas.create_text(260, 270, text="* break through the Earth`s atmosphere and go to space", font="Papyrus 15")
##        self.canvas.create_text(185, 300, text="* btw, do not destroy it all or you will lose", font="Papyrus 15")
##        self.canvas.create_text(300, 330, text="* we down here will still need some of it to protect us from UV & stuff", font="Papyrus 15")
##        self.canvas.create_text(300, 370, text="Press Enter whenever you feel like it~", font="Papyrus 15 bold")
##
##        self.canvas.bind_all("<Key>", self.delete)        
##    
##    menom = ""
##
##    def delete(self, event):
##        self.canvas.delete("all")
##        self.canvas["bg"] = "light cyan"
##        self.canvas.create_text(self.w//2, 40, text = "What is your name?", font = "Papyrus 30")
##        self.canvas.bind_all("<Key>", self.meno)
##        self.canvas.bind_all("<Return>", self.build)
##
##    def meno(self, event):              
##        self.canvas.bind_all("<Return>", self.build)             
##        pismeno = event.keysym
##        
##        if pismeno in "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM0123456789":
##            self.canvas.delete("all")
##            self.canvas.create_text(self.w//2, 40, text = "What is your name?", font = "Papyrus 30")
##            self.menom += pismeno
##            self.canvas.create_text(300, 200, text = self.menom, font = "Papyrus 20")                   
##            
##        elif pismeno == "BackSpace":
##            self.canvas.delete("all")
##            self.canvas.create_text(self.w//2, 40, text = "What is your name?", font = "Papyrus 30")
##            self.menom = self.menom[0:len(self.menom)-1]
##            self.canvas.create_text(300, 200, text = self.menom, font = "Papyrus 20")
##            
##        else:
##            pass      
##        
##                      
##    def build(self, event):        
##        self.canvas.delete("all")
##        self.canvas["bg"] = "light cyan"
##        self.canvas.unbind_all('<Key>')
##        for i in range(6):
##            while (self.x + self.a) <= self.w:
##                self.tehla = self.canvas.create_rectangle(self.x, self.y,
##                                                          self.x + self.a, self.y + self.b,
##                                                          fill=self.farby[i], outline="")
##                self.polecoordshelp.append((self.x, self.y))
##                self.chibipole.append(self.tehla)
##                self.x += self.a
##            self.polecoords.append(self.polecoordshelp)
##            self.polecoordshelp = []
##            self.pole.append(self.chibipole)
##            self.chibipole = []
##            self.x = 0
##            self.y += self.b
##
##        self.y = self.x = 0
##
##        self.grass = self.canvas.create_rectangle(0, self.h - 40, self.w, self.h - 30,
##                                                  fill="green3", outline="")
##        self.ground = self.canvas.create_rectangle(0, self.h - 30, self.w, self.h - 20,
##                                                   fill="NavajoWhite4", outline="")
##        self.lava = self.canvas.create_rectangle(0, self.h - 20, self.w, self.h,
##                                                 fill="red", outline="")
##
##        self.zlepole = [self.grass]
##
##        self.build_platform()
##        stopky = threading.Thread(target=self.time, args=())
##        stopky.start()
##
##
##    def icko(self):
##        self.i = 0.035        
##        while self.i > 0.009:
##            self.i -= 0.002        
##            time.sleep(1)
##        
##
#### ----- platform:
##
##    def build_platform(self):
##        self.xd, self.yd, self.dxd, self.wd, self.hd = 300, 350, 1, 80, 10
##        self.idd = self.canvas.create_rectangle(self.xd - (self.wd // 2), self.yd - (self.hd // 2),
##                                                self.xd + (self.wd // 2), self.yd + (self.hd // 2),
##                                                fill="gold")
##
##    def platform_move(self, event):
##        d = event.x - self.xd
##        self.canvas.move(self.idd, d, 0)
##        self.xd = event.x
##
####    def pohyb_platform(self, event):
####        kliknute = event.keysym
####        if(self.canvas.coords(self.idd)[2] < self.w - 3 and (kliknute=='D' or kliknute == 'd')):
####            self.canvas.move(self.idd,5,0)
####        elif(self.canvas.coords(self.idd)[0] > 3 and (kliknute == 'A' or kliknute == 'a')):
####            self.canvas.move(self.idd,-5,0)
##
##
#### ----- circle:
##
##    def build_circle(self):
##        tup = (-2, -1, 1, 2)
##        self.xc, self.yc, self.dxc, self.dyc, self.wc, self.hc = 300, 200, rc(tup), rc(tup), 20, 20
##        self.idc = self.canvas.create_oval(self.xc - (self.wc // 2), self.yc - (self.hc // 2),
##                                           self.xc + (self.wc // 2), self.yc + (self.hc // 2),
##                                           fill="grey", outline="")
##
##    def move_circle(self):
##        while self.true:
##            self.canvas.move(self.idc, self.dxc, self.dyc)
##            self.xc, self.yc = self.xc + self.dxc, self.yc + self.dyc
##            time.sleep(self.i)
##            if self.yc < 100:
##                for i in range(len(self.polecoords)):
##                    for j in range(len(self.polecoords[i])):
##                        if self.pole[i][j] != None:
##                            if (self.polecoords[i][j][0]) <= self.xc <= ((self.polecoords[i][j][0]) + self.a) and (self.polecoords[i][j][1]) <= self.yc - (self.hc // 2) <= ((self.polecoords[i][j][1]) + self.b):
##                                if self.xc >= (self.polecoords[i][j][0] + self.a) or self.xc <= (self.polecoords[i][j][0]):
##                                    self.dxc = -self.dxc
##                                else:
##                                    self.dyc = -self.dyc
##
##                                a = self.pole.pop(i)
##                                b = a.pop(j)
##                                a.insert(j, None)
##                                self.canvas.delete(b)
##                                self.pole.insert(i, a)
##                                self.canvas.move(self.idc, self.dxc, self.dyc)
##                                self.xc, self.yc = self.xc + self.dxc, self.yc + self.dyc
##                                time.sleep(self.i)
##
##
##            if (self.xc - (self.wc // 2) <= 1) or self.xc + (self.wc // 2) >= self.w - 1:
##                self.dxc = -self.dxc
##                self.canvas.move(self.idc, self.dxc, self.dyc)
##                self.xc, self.yc = self.xc + self.dxc, self.yc + self.dyc
##                time.sleep(self.i)
##
##            elif self.yc >= (self.h - 100):
##                platformcoords = self.canvas.coords(self.idd)
##               
##                if ((platformcoords[0]  <= self.xc <= platformcoords[2] ) or (platformcoords[0] <= self.xc - math.ceil(self.wc/2) <= platformcoords[2]) or (platformcoords[0]<= self.xc + math.ceil(self.wc/2) <= platformcoords[2])) and  platformcoords[1] <= self.yc + 1 + math.ceil(self.hc / 2):
##                    if self.xc + math.ceil(self.wc/2) <= platformcoords[0] or self.xc - math.ceil(self.wc/2) >= platformcoords[2] :
##                        self.dxc = -self.dxc
##                    else:
##                        self.dyc = -self.dyc
##
##
##                if self.grass in self.zlepole:
##                    if self.yc + (self.hc // 2) >= self.h - 39:
##                        self.dyc = -self.dyc
##                        self.canvas.move(self.idc, self.dxc, self.dyc)
##                        self.xc, self.yc = self.xc + self.dxc, self.yc + self.dyc
##                        time.sleep(self.i)
##                        self.ops = threading.Thread(target=self.oops, args=())
##                        self.ops.start()
##
##                elif self.lava in self.zlepole:
##                    if self.yc + (self.hc // 2) >= self.h - 20:                        
##                        self.you_lost()
##
##            elif self.yc - self.b <= 0:
##                self.you_won()
##
##                
#### ----------------------
##                
##    def oops(self):
##        self.end = round(time.time() - self.start, 0)
##        self.zlepole.pop()
##        self.zlepole.append(self.lava)
##        self.canvas.delete(self.grass)
##        self.canvas.delete(self.ground)
##        text = self.canvas.create_text(canvasWidth
# // 2, canvasHeight // 2,
##                                       text="Uh oh. Is it so hot in here or is it just me?",
##                                       font="Papyrus 20 bold",
##                                       fill="red")
##        time.sleep(5)
##        self.canvas.delete(text)
##
##
##    def you_lost(self):        
##        self.canvas.delete("all")
##        self.true = False
##        self.canvas.unbind_all('<Key>')
##        self.canvas["bg"] = "black"
##        vety = ("*sad music starts playing*",
##                "So... ", "You didn`t make it, huh?",
##                "I`m sorry about that..", "that`s life, though.",
##                "But... ", "*hopeful music starts playing*", "Always look on the bright side of life, right?",
##                "...and start the game again, ok?",
##                "Good luck.")
##        text = ""
##        for i in range(len(vety)):
##            time.sleep(2)
##            self.canvas.delete(text)
##            farba = "white"
##            if "*" in vety[i]: farba = "grey"
##            text = self.canvas.create_text(canvasWidth
# // 2, canvasHeight // 2,
##                                           text=vety[i],
##                                           font="Papyrus 20 bold",
##                                           fill=farba)
##        time.sleep(2)
##        self.canvas.delete("all")
##        self.high_score()
##
##    def you_won(self):
##        self.end = round(time.time() - self.start)
##        self.true = False
##        Word(self.end, self.menom)
##        self.canvas.unbind_all('<Key>')
##        self.canvas.delete("all")
##        self.canvas["bg"] = "black"
##        vety = ("*happy music starts playing*", "Player!",
##                "You did it! ^^", "Humans of this realm are proud of you.",
##                "You may now procceed to the--", "~",
##                "Thank you for playing.", "Have a nice day. :)")
##        text = ""        
##        for i in vety:
##            time.sleep(2)
##            self.canvas.delete(text)
##            farba = "SteelBlue1"
##            if "~" in i:
##                farba = "gold"
##                text = self.canvas.create_text(canvasWidth
# // 2, canvasHeight // 2,
##                                               text=i,
##                                               font="Papyrus 35 bold",
##                                               fill=farba)
##                obr2 = ImageTk.PhotoImage(Image.open("SpaceCore.jpg"))
##                self.canvas.create_image(300,200, image=obr2)                
##                time.sleep(1)
##                text = self.canvas.create_text(canvasWidth
# // 2, canvasHeight // 2 + 150,
##                                               text="I`m in space! Need to see it all!",
##                                               font="Papyrus 15 bold",
##                                               fill="grey")
##                time.sleep(2)
##                self.canvas.delete("all")
##            else:
##                text = self.canvas.create_text(canvasWidth
# // 2, canvasHeight // 2,
##                                               text=i,
##                                               font="Papyrus 20 bold",
##                                               fill=farba)
##
##        time.sleep(2)
##        self.canvas.delete("all")
##        ## sem daj obrazok bySetsumi
##        self.high_score()
##
##    def high_score(self):
##        with open("tabulka.txt", "r") as txt:
##            radek = txt.readline().strip()
##            pole = []
##            while radek:                
##                m = radek.find(" ")
##                meno = radek[0:m]
##                d = radek.find(":")
##                minut = radek[m+1:d]
##                sek = radek[d+1:len(radek)]
##                pole.append((minut, sek, meno))
##                radek = txt.readline().strip()
##        a = sorted(pole)
##
##        self.canvas.create_text(self.w//2, 50, text = "The Best of The Best:", font = "Papyrus 30 bold", fill = "gold")
##        text = a[0][2] + " " + str(a[0][0]) + ":" + str(a[0][1])
##        self.canvas.create_text(self.w//2, 110, text = text, font = "Papyrus 20 bold", fill = "gold")
##        text = a[1][2] + " " + str(a[1][0]) + ":" + str(a[1][1])
##        self.canvas.create_text(self.w//2, 140, text = text, font = "Papyrus 18", fill = "azure2")
##        text = a[2][2] + " " + str(a[2][0]) + ":" + str(a[2][1])
##        self.canvas.create_text(self.w//2, 170, text = text, font = "Papyrus 17", fill = "tan1")
##
##        for abc in range(3, 9):
##            text = a[abc][2] + " " + str(a[abc][0]) + ":" + str(a[abc][1])
##            self.canvas.create_text(self.w//2, 140 + abc*25, text = text, font = "Papyrus 15", fill = "white")
##        
##        
##
##    
#### ----- general
##
##    def time(self):
##        self.cislo = None
##
##        for i in range(3, 0, -1):
##            self.canvas.delete(self.cislo)
##            self.cislo = self.canvas.create_text(canvasWidth
# // 2,
##                                                 canvasHeight // 2,
##                                                 text=str(i), font="Papyrus 40 bold")
##            time.sleep(1)
##        self.canvas.delete(self.cislo)
##        self.cislo = self.canvas.create_text(canvasWidth
# // 2,
##                                             canvasHeight // 2,
##                                             text="Start!", font="Papyrus 40 bold")
##        time.sleep(1)
##        self.canvas.delete(self.cislo)        
##        self.build_circle()
##        time.sleep(0.3)       
##        
##
##        self.canvas.bind('<Button-1>', self.platform_move)
##        #self.canvas.bind_all('<Key>',self.pohyb_platform)
##        
##        self.time = threading.Thread(target=self.icko, args=())
##        self.time.start()
##        self.start = time.time()
##
##        self.true = True        
##        self.move_circle()
##
##
##
##class Word:
##    def __init__(self, time, meno):
##        self.time = time
##        self.meno = meno
##        if self.meno == "":
##            self.meno = "Unknown"
##        self.zmen(self.time, self.meno)
##
##    def zmen(self, zle, menoa):
##        self.minuty = zle // 60
##        self.sekundy = zle % 60
##        if len(str(self.sekundy)) ==1: self.sekundy = "0" + str(self.sekundy)
##        self.napis = str(menoa) + " " + str(self.minuty) + ":" + str(self.sekundy) + "\n"
##        self.zapis(self.napis)
##        
##    def zapis(self, xxxx):
##        with open("tabulka.txt", "a") as txt:
##            txt.write(xxxx)            
##           
##                
##
##Tehlicky()
##
##
