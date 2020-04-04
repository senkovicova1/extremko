import tkinter, time, threading, math, time, random
from random import choice as rc
from PIL import Image, ImageTk


class Tehlicky(tkinter.Canvas):    
    def __init__(self):
        self.canvas = tkinter.Canvas(bg="light cyan", height=400, width=600)
        self.w, self.h = int(self.canvas["width"]), int(self.canvas["height"])
        self.canvas.pack()   
        
        for i in range(16):
            self.canvas.delete("all")
            obr = ImageTk.PhotoImage(Image.open("load{}.bmp".format(i)))
            self.canvas.create_image(300,200, image=obr)
            self.canvas.update()
            self.canvas.after(random.randrange(80,300))
        self.canvas.delete("all")

        self.farby = ["Navy", "medium blue", "blue", "RoyalBlue1", "SteelBlue1", "SkyBlue1"]
        self.pole, self.chibipole, self.tehla, self.polecoords, self.polecoordshelp = [], [], "", [], []
        self.x, self.y, self.a, self.b = 0, 0, 30, 15
        self.get_ready()        
        self.canvas.mainloop()

    def get_ready(self):
        self.canvas.create_text(self.w / 2, 30,
                                text="Welcome, player!", font="Papyrus 30")
        self.canvas.create_text(60, 80,
                                text="Some Info:", font="Papyrus 15 bold")
        self.canvas.create_text(217, 110,
                                text="* you move the               left & right with mouse", font="Papyrus 15")
        self.canvas.create_text(185, 110,
                                text="platform", fill="gold", font="Papyrus 15 bold")
        self.canvas.create_text(275, 140,
                                text="* you can hit the             once, meaning you have 1 extra life", font="Papyrus 15")
        self.canvas.create_text(193, 140,
                                text="ground", fill="green3", font="Papyrus 15 bold")
        self.canvas.create_text(225, 170, text="* but then the               breaks and          appears", font="Papyrus 15")
        self.canvas.create_text(170, 170,
                                text="ground", fill="green3", font="Papyrus 15 bold")
        self.canvas.create_text(340, 170, text="lava", fill="red", font="Papyrus 15 bold")
        self.canvas.create_text(450, 200, text="und das ist nicht gut", fill="red", font="Papyrus 15 bold")
        self.canvas.create_text(100, 240, text="Goal of this game?", font="Papyrus 15 bold")
        self.canvas.create_text(260, 270, text="* break through the Earth`s atmosphere and go to space", font="Papyrus 15")
        self.canvas.create_text(185, 300, text="* btw, do not destroy it all or you will lose", font="Papyrus 15")
        self.canvas.create_text(300, 330, text="* we down here will still need some of it to protect us from UV & stuff", font="Papyrus 15")
        self.canvas.create_text(300, 370, text="Press Enter whenever you feel like it~", font="Papyrus 15 bold")

        self.canvas.bind_all("<Key>", self.delete)        
    
    menom = ""

    def delete(self, event):
        self.canvas.delete("all")
        self.canvas["bg"] = "light cyan"
        self.canvas.create_text(self.w//2, 40, text = "What is your name?", font = "Papyrus 30")
        self.canvas.bind_all("<Key>", self.meno)
        self.canvas.bind_all("<Return>", self.build)

    def meno(self, event):              
        self.canvas.bind_all("<Return>", self.build)             
        pismeno = event.keysym
        
        if pismeno in "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM0123456789":
            self.canvas.delete("all")
            self.canvas.create_text(self.w//2, 40, text = "What is your name?", font = "Papyrus 30")
            self.menom += pismeno
            self.canvas.create_text(300, 200, text = self.menom, font = "Papyrus 20")                   
            
        elif pismeno == "BackSpace":
            self.canvas.delete("all")
            self.canvas.create_text(self.w//2, 40, text = "What is your name?", font = "Papyrus 30")
            self.menom = self.menom[0:len(self.menom)-1]
            self.canvas.create_text(300, 200, text = self.menom, font = "Papyrus 20")
            
        else:
            pass      
        
                      
    def build(self, event):        
        self.canvas.delete("all")
        self.canvas["bg"] = "light cyan"
        self.canvas.unbind_all('<Key>')
        for i in range(6):
            while (self.x + self.a) <= self.w:
                self.tehla = self.canvas.create_rectangle(self.x, self.y,
                                                          self.x + self.a, self.y + self.b,
                                                          fill=self.farby[i], outline="")
                self.polecoordshelp.append((self.x, self.y))
                self.chibipole.append(self.tehla)
                self.x += self.a
            self.polecoords.append(self.polecoordshelp)
            self.polecoordshelp = []
            self.pole.append(self.chibipole)
            self.chibipole = []
            self.x = 0
            self.y += self.b

        self.y = self.x = 0

        self.grass = self.canvas.create_rectangle(0, self.h - 40, self.w, self.h - 30,
                                                  fill="green3", outline="")
        self.ground = self.canvas.create_rectangle(0, self.h - 30, self.w, self.h - 20,
                                                   fill="NavajoWhite4", outline="")
        self.lava = self.canvas.create_rectangle(0, self.h - 20, self.w, self.h,
                                                 fill="red", outline="")

        self.zlepole = [self.grass]

        self.build_doska()
        stopky = threading.Thread(target=self.cas, args=())
        stopky.start()


    def icko(self):
        self.i = 0.035        
        while self.i > 0.009:
            self.i -= 0.002        
            time.sleep(1)
        

## ----- platform:

    def build_doska(self):
        self.xd, self.yd, self.dxd, self.wd, self.hd = 300, 350, 1, 80, 10
        self.idd = self.canvas.create_rectangle(self.xd - (self.wd // 2), self.yd - (self.hd // 2),
                                                self.xd + (self.wd // 2), self.yd + (self.hd // 2),
                                                fill="gold")

    def doska_move(self, event):        
        d = event.x - self.xd
        self.canvas.move(self.idd, d, 0)
        self.xd = event.x

##    def pohyb_doska(self, event):
##        kliknute = event.keysym
##        if(self.canvas.coords(self.idd)[2] < self.w - 3 and (kliknute=='D' or kliknute == 'd')):
##            self.canvas.move(self.idd,5,0)
##        elif(self.canvas.coords(self.idd)[0] > 3 and (kliknute == 'A' or kliknute == 'a')):
##            self.canvas.move(self.idd,-5,0)


## ----- circle:

    def build_circle(self):
        tup = (-2, -1, 1, 2)
        self.xc, self.yc, self.dxc, self.dyc, self.wc, self.hc = 300, 200, rc(tup), rc(tup), 20, 20
        self.idc = self.canvas.create_oval(self.xc - (self.wc // 2), self.yc - (self.hc // 2),
                                           self.xc + (self.wc // 2), self.yc + (self.hc // 2),
                                           fill="grey", outline="")

    def move_circle(self):
        while self.true:
            self.canvas.move(self.idc, self.dxc, self.dyc)
            self.xc, self.yc = self.xc + self.dxc, self.yc + self.dyc
            time.sleep(self.i)
            if self.yc < 100:
                for i in range(len(self.polecoords)):
                    for j in range(len(self.polecoords[i])):
                        if self.pole[i][j] != None:
                            if (self.polecoords[i][j][0]) <= self.xc <= ((self.polecoords[i][j][0]) + self.a) and (self.polecoords[i][j][1]) <= self.yc - (self.hc // 2) <= ((self.polecoords[i][j][1]) + self.b):
                                if self.xc >= (self.polecoords[i][j][0] + self.a) or self.xc <= (self.polecoords[i][j][0]):
                                    self.dxc = -self.dxc
                                else:
                                    self.dyc = -self.dyc

                                a = self.pole.pop(i)
                                b = a.pop(j)
                                a.insert(j, None)
                                self.canvas.delete(b)
                                self.pole.insert(i, a)
                                self.canvas.move(self.idc, self.dxc, self.dyc)
                                self.xc, self.yc = self.xc + self.dxc, self.yc + self.dyc
                                time.sleep(self.i)


            if (self.xc - (self.wc // 2) <= 1) or self.xc + (self.wc // 2) >= self.w - 1:
                self.dxc = -self.dxc
                self.canvas.move(self.idc, self.dxc, self.dyc)
                self.xc, self.yc = self.xc + self.dxc, self.yc + self.dyc
                time.sleep(self.i)

            elif self.yc >= (self.h - 100):
                doskacoords = self.canvas.coords(self.idd)
               
                if ((doskacoords[0]  <= self.xc <= doskacoords[2] ) or (doskacoords[0] <= self.xc - math.ceil(self.wc/2) <= doskacoords[2]) or (doskacoords[0]<= self.xc + math.ceil(self.wc/2) <= doskacoords[2])) and  doskacoords[1] <= self.yc + 1 + math.ceil(self.hc / 2):
                    if self.xc + math.ceil(self.wc/2) <= doskacoords[0] or self.xc - math.ceil(self.wc/2) >= doskacoords[2] :
                        self.dxc = -self.dxc
                    else:
                        self.dyc = -self.dyc


                if self.grass in self.zlepole:
                    if self.yc + (self.hc // 2) >= self.h - 39:
                        self.dyc = -self.dyc
                        self.canvas.move(self.idc, self.dxc, self.dyc)
                        self.xc, self.yc = self.xc + self.dxc, self.yc + self.dyc
                        time.sleep(self.i)
                        self.ops = threading.Thread(target=self.oops, args=())
                        self.ops.start()

                elif self.lava in self.zlepole:
                    if self.yc + (self.hc // 2) >= self.h - 20:                        
                        self.you_lost()

            elif self.yc - self.b <= 0:
                self.you_won()

                
## ----------------------
                
    def oops(self):
        self.end = round(time.time() - self.start, 0)
        self.zlepole.pop()
        self.zlepole.append(self.lava)
        self.canvas.delete(self.grass)
        self.canvas.delete(self.ground)
        text = self.canvas.create_text(int(self.canvas["width"]) // 2, int(self.canvas["height"]) // 2,
                                       text="Uh oh. Is it so hot in here or is it just me?",
                                       font="Papyrus 20 bold",
                                       fill="red")
        time.sleep(5)
        self.canvas.delete(text)


    def you_lost(self):        
        self.canvas.delete("all")
        self.true = False
        self.canvas.unbind_all('<Key>')
        self.canvas["bg"] = "black"
        vety = ("*sad music starts playing*",
                "So... ", "You didn`t make it, huh?",
                "I`m sorry about that..", "that`s life, though.",
                "But... ", "*hopeful music starts playing*", "Always look on the bright side of life, right?",
                "...and start the game again, ok?",
                "Good luck.")
        text = ""
        for i in range(len(vety)):
            time.sleep(2)
            self.canvas.delete(text)
            farba = "white"
            if "*" in vety[i]: farba = "grey"
            text = self.canvas.create_text(int(self.canvas["width"]) // 2, int(self.canvas["height"]) // 2,
                                           text=vety[i],
                                           font="Papyrus 20 bold",
                                           fill=farba)
        time.sleep(2)
        self.canvas.delete("all")
        self.high_score()

    def you_won(self):
        self.end = round(time.time() - self.start)
        self.true = False
        Word(self.end, self.menom)
        self.canvas.unbind_all('<Key>')
        self.canvas.delete("all")
        self.canvas["bg"] = "black"
        vety = ("*happy music starts playing*", "Player!",
                "You did it! ^^", "Humans of this realm are proud of you.",
                "You may now procceed to the--", "~",
                "Thank you for playing.", "Have a nice day. :)")
        text = ""        
        for i in vety:
            time.sleep(2)
            self.canvas.delete(text)
            farba = "SteelBlue1"
            if "~" in i:
                farba = "gold"
                text = self.canvas.create_text(int(self.canvas["width"]) // 2, int(self.canvas["height"]) // 2,
                                               text=i,
                                               font="Papyrus 35 bold",
                                               fill=farba)
                obr2 = ImageTk.PhotoImage(Image.open("SpaceCore.jpg"))
                self.canvas.create_image(300,200, image=obr2)                
                time.sleep(1)
                text = self.canvas.create_text(int(self.canvas["width"]) // 2, int(self.canvas["height"]) // 2 + 150,
                                               text="I`m in space! Need to see it all!",
                                               font="Papyrus 15 bold",
                                               fill="grey")
                time.sleep(2)
                self.canvas.delete("all")
            else:
                text = self.canvas.create_text(int(self.canvas["width"]) // 2, int(self.canvas["height"]) // 2,
                                               text=i,
                                               font="Papyrus 20 bold",
                                               fill=farba)

        time.sleep(2)
        self.canvas.delete("all")
        ## sem daj obrazok bySetsumi
        self.high_score()

    def high_score(self):
        with open("tabulka.txt", "r") as txt:
            radek = txt.readline().strip()
            pole = []
            while radek:                
                m = radek.find(" ")
                meno = radek[0:m]
                d = radek.find(":")
                minut = radek[m+1:d]
                sek = radek[d+1:len(radek)]
                pole.append((minut, sek, meno))
                radek = txt.readline().strip()
        a = sorted(pole)

        self.canvas.create_text(self.w//2, 50, text = "The Best of The Best:", font = "Papyrus 30 bold", fill = "gold")
        text = a[0][2] + " " + str(a[0][0]) + ":" + str(a[0][1])
        self.canvas.create_text(self.w//2, 110, text = text, font = "Papyrus 20 bold", fill = "gold")
        text = a[1][2] + " " + str(a[1][0]) + ":" + str(a[1][1])
        self.canvas.create_text(self.w//2, 140, text = text, font = "Papyrus 18", fill = "azure2")
        text = a[2][2] + " " + str(a[2][0]) + ":" + str(a[2][1])
        self.canvas.create_text(self.w//2, 170, text = text, font = "Papyrus 17", fill = "tan1")

        for abc in range(3, 9):
            text = a[abc][2] + " " + str(a[abc][0]) + ":" + str(a[abc][1])
            self.canvas.create_text(self.w//2, 140 + abc*25, text = text, font = "Papyrus 15", fill = "white")
        
        

    
## ----- general

    def cas(self):
        self.cislo = None

        for i in range(3, 0, -1):
            self.canvas.delete(self.cislo)
            self.cislo = self.canvas.create_text(int(self.canvas["width"]) // 2,
                                                 int(self.canvas["height"]) // 2,
                                                 text=str(i), font="Papyrus 40 bold")
            time.sleep(1)
        self.canvas.delete(self.cislo)
        self.cislo = self.canvas.create_text(int(self.canvas["width"]) // 2,
                                             int(self.canvas["height"]) // 2,
                                             text="Start!", font="Papyrus 40 bold")
        time.sleep(1)
        self.canvas.delete(self.cislo)        
        self.build_circle()
        time.sleep(0.3)       
        

        self.canvas.bind('<Button-1>', self.doska_move)
        #self.canvas.bind_all('<Key>',self.pohyb_doska)
        
        self.cas = threading.Thread(target=self.icko, args=())
        self.cas.start()
        self.start = time.time()

        self.true = True        
        self.move_circle()



class Word:
    def __init__(self, cas, meno):
        self.cas = cas
        self.meno = meno
        if self.meno == "":
            self.meno = "Unknown"
        self.zmen(self.cas, self.meno)

    def zmen(self, zle, menoa):
        self.minuty = zle // 60
        self.sekundy = zle % 60
        if len(str(self.sekundy)) ==1: self.sekundy = "0" + str(self.sekundy)
        self.napis = str(menoa) + " " + str(self.minuty) + ":" + str(self.sekundy) + "\n"
        self.zapis(self.napis)
        
    def zapis(self, xxxx):
        with open("tabulka.txt", "a") as txt:
            txt.write(xxxx)            
           
                

Tehlicky()

    

