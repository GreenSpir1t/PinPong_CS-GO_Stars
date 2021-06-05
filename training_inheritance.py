from pygame import *
from time import sleep
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *

app = QApplication([])
widget1 = QWidget()
button1 = QPushButton("ИГРАТЬ")
button1.resize(100, 60)
label1 = QLabel("Привет! Ты запустил игру PinPong, где ты можешь посоревноваться с другом в ловкости и проверить свою реакцию")
label1.resize(50, 50)
line1 = QVBoxLayout()
line1.addWidget(label1)
line1.addWidget(button1, alignment = Qt.AlignCenter)
widget1.setLayout(line1)
widget1.resize(400, 400)
widget1.show()
widget2 = QWidget()
button2 = QPushButton("Играть")
button3 = QPushButton("Играть")
button4 = QPushButton("Правила игры")
button5 = QPushButton("Правила игры")
label2 = QLabel("АРКАДА")
label3 = QLabel("КЛАССИКА")
label4 = QLabel("ВЫБЕРИ РЕЖИМ. ВНИМАТЕЛЬНО ОЗНАКОМСЯ С ПРАВИЛАМИ И НАЖМИ ИГРАТЬ")
line2 = QVBoxLayout()
line3 = QHBoxLayout()
line4 = QHBoxLayout()
line5 = QHBoxLayout()
line6 = QHBoxLayout()
line3.addWidget(label4, alignment = Qt.AlignCenter)
line6.addWidget(label2, alignment = Qt.AlignCenter)
line6.addWidget(label3, alignment = Qt.AlignCenter)
line4.addWidget(button2)
line4.addWidget(button3)
line5.addWidget(button4)
line5.addWidget(button5)
line2.addLayout(line3)
line2.addLayout(line6)
line2.addLayout(line4)
line2.addLayout(line5)
widget2.setLayout(line2)
widget2.resize(400, 400)
widget3 = QWidget()
widget3.resize(400, 400)
widget4 = QWidget()
widget4.resize(400, 400)
label5 = QLabel("1) Ракетка правой команды управляется W,S")
label6 = QLabel("2) Ракетка левой команды управляется UP,DOWN")
label7 = QLabel("3) Победу одерживает игрок, первый забившей 3 гола")
label8 = QLabel("4) После 1 гола мяч увеличивается в размерах. После 2 увеличивается скорость. После 3 мяч становится маленький")
button6 = QPushButton("Вернуться")
label9 = QLabel("1) Ракетка правой команды управляется W,S")
label10 = QLabel("2) Ракетка левой команды управляется UP,DOWN")
label11 = QLabel("3) Победу одерживает игрок, первый забившей 3 гола")
label12 = QLabel("4) После 1 гола мяч увеличивается в размерах. После 2 увеличивается скорость. После 3 мяч становится маленький")
button7 = QPushButton("Вернуться")
line7 = QVBoxLayout()
line13 = QVBoxLayout()
line8 = QHBoxLayout()
line9 = QHBoxLayout()
line10 = QHBoxLayout()
line11 = QHBoxLayout()
line12 = QHBoxLayout()
line14 = QHBoxLayout()
line15 = QHBoxLayout()
line16 = QHBoxLayout()
line17 = QHBoxLayout()
line1 = QHBoxLayout()
line8.addWidget(label5, alignment = Qt.AlignCenter)
line9.addWidget(label6, alignment = Qt.AlignCenter)
line10.addWidget(label7, alignment = Qt.AlignCenter)
line11.addWidget(button6, alignment = Qt.AlignCenter)
line14.addWidget(label9, alignment = Qt.AlignCenter)
line15.addWidget(label10, alignment = Qt.AlignCenter)
line16.addWidget(label11, alignment = Qt.AlignCenter)
line17.addWidget(label12, alignment = Qt.AlignCenter)
line12.addWidget(button7, alignment = Qt.AlignCenter)
line7.addLayout(line8)
line7.addLayout(line9)
line7.addLayout(line10)
line7.addLayout(line11)
line13.addLayout(line14)
line13.addLayout(line15)
line13.addLayout(line16)
line13.addLayout(line17)
line13.addLayout(line12)
widget3.setLayout(line13)
widget4.setLayout(line7)





def df1():
    widget1.hide()
    widget2.show()


def df2():
    widget1.hide()
    widget2.hide()
    widget3.show()


def df3():
    widget1.hide()
    widget2.hide()
    widget4.show()

def back():
    widget1.hide()
    widget4.hide()
    widget3.hide()
    widget2.show()

def pinpong1():
    class Player(sprite.Sprite):
        def __init__(self, player_image, player_x, player_y, player_speed, size_x, size_y):
            super().__init__()
            self.image = transform.scale(image.load(player_image), (size_x, size_y))
            self.speed = player_speed
            self.rect = self.image.get_rect()
            self.rect.x = player_x
            self.rect.y = player_y
        def reset(self):
            window.blit(self.image, (self.rect.x, self.rect.y))



    class Player2(Player):
        def update1(self):
            keys = key.get_pressed()
            if keys[K_w] and self.rect.y > 5:
                self.rect.y -= self.speed
            if keys[K_s] and self.rect.y < 500:
                self.rect.y += self.speed
        def update2(self):
            keys = key.get_pressed()
            if keys[K_UP] and self.rect.y > 5:
                self.rect.y -= self.speed
            if keys[K_DOWN] and self.rect.y < 500:
                self.rect.y += self.speed


    sprite1 = Player2("1200px-NAVI_logo.png", 20, 250, 10, 65, 65)
    sprite2 = Player2("Astralis_logo.png", 600, 250, 10, 65, 65)    
    ball = Player("Myach.png", 350, 250, 10, 50, 50)

    window = display.set_mode((700, 500))
    background = transform.scale(image.load("m3Ao_FJPWVo.jpg"),(700, 500))

    font.init()

    font1 = font.SysFont("Arial", 30)
    font2 = font.SysFont("Arial", 30)
    font3 = font.SysFont("Arial", 70)
    font4 = font.SysFont("Arial", 70)
    font5 = font.SysFont("Arial", 70)


    pnavi = 0
    pastr = 0

    speed_x = 6
    speed_y = 6

    finish = False


    winNavi = font3.render("NAVI WIN!", True, (255, 223, 0))
    winAstr = font4.render("ASTRALIS WIN!", True, (255, 0, 14))
    goal = font5.render("GOAL!", True, (255, 255, 255))


    game = True
    while game:
        for e in event.get():
            if e.type == QUIT:
                game = False 

        if finish != True:
            window.blit(background,(0, 0))
            sprite1.update1()
            sprite2.update2()
            sprite1.reset()
            sprite2.reset()
            ball.reset()


            ball.rect.x += speed_x
            ball.rect.y += speed_y

            pNavi = font1.render("Очки Navi:" + str(pnavi), True, (255, 255, 255))
            window.blit(pNavi, (2, 2))
            pAstr = font2.render("Очки Astralis:" + str(pastr), True, (255, 255, 255))
            window.blit(pAstr,(500,2))
            
            if pnavi == 3:
                window.blit(pNavi, (2, 2))
                
                
                window.blit(winNavi, (200, 200))
                display.update()
                finish = True
                
                
                time.delay(3000)
                game = False
                
                

            if pastr == 3:
                window.blit(winAstr, (110, 200))
                finish = True

            if ball.rect.y > 450 or ball.rect.y < 0:
                speed_y *= -1

            if sprite.collide_rect(sprite1, ball) or sprite.collide_rect(sprite2, ball):
                speed_x *= -1

            if ball.rect.x > 700:
                pnavi += 1
                ball.rect.x = 350
                ball.rect.y = 250
                time.delay(500)
                     
                    

            if ball.rect.x < 0:
                pastr += 1
                ball.rect.x = 350
                ball.rect.y = 250
                time.delay(500)
                
                

            display.update()
            time.delay(10)
    










def pinpong2():
    class Player(sprite.Sprite):
        def __init__(self, player_image, player_x, player_y, player_speed, size_x, size_y):
            super().__init__()
            self.image = transform.scale(image.load(player_image), (size_x, size_y))
            self.speed = player_speed
            self.rect = self.image.get_rect()
            self.rect.x = player_x
            self.rect.y = player_y
        def reset(self):
            window.blit(self.image, (self.rect.x, self.rect.y))


    class Player2(Player):
        def update1(self):
            keys = key.get_pressed()
            if keys[K_w] and self.rect.y > 5:
                self.rect.y -= self.speed
            if keys[K_s] and self.rect.y < 500:
                self.rect.y += self.speed
        def update2(self):
            keys = key.get_pressed()
            if keys[K_UP] and self.rect.y > 5:
                self.rect.y -= self.speed
            if keys[K_DOWN] and self.rect.y < 500:
                self.rect.y += self.speed


    sprite1 = Player2("1200px-NAVI_logo.png", 20, 250, 10, 65, 65)
    sprite2 = Player2("Astralis_logo.png", 600, 250, 10, 65, 65)    
    ball = Player("Myach.png", 350, 250, 10, 50, 50)

    window = display.set_mode((700, 500))
    background = transform.scale(image.load("m3Ao_FJPWVo.jpg"),(700, 500))

    font.init()

    font1 = font.SysFont("Arial", 30)
    font2 = font.SysFont("Arial", 30)
    font3 = font.SysFont("Arial", 70)
    font4 = font.SysFont("Arial", 70)


    pnavi = 0
    pastr = 0

    speed_x = 6
    speed_y = 6

    finish = False


    winNavi = font3.render("NAVI WIN!", True, (255, 223, 0))
    winAstr = font4.render("ASTRALIS WIN!", True, (255, 0, 14))


    game = True
    while game:
        for e in event.get():
            if e.type == QUIT:
                game = False 

        if finish != True:
            window.blit(background,(0, 0))
            sprite1.update1()
            sprite2.update2()
            sprite1.reset()
            sprite2.reset()
            ball.reset()


            ball.rect.x += speed_x
            ball.rect.y += speed_y

            pNavi = font1.render("Очки Navi:" + str(pnavi), True, (255, 255, 255))
            window.blit(pNavi, (2, 2))
            pAstr = font2.render("Очки Astralis:" + str(pastr), True, (255, 255, 255))
            window.blit(pAstr,(500,2))
            
            if pnavi == 3:
                window.blit(pNavi, (2, 2))
                
                
                window.blit(winNavi, (200, 200))
                display.update()
                finish = True
                
                
                time.delay(3000)
                game = False
                
                

            if pastr == 3:
                window.blit(winAstr, (110, 200))
                finish = True

            if ball.rect.y > 450 or ball.rect.y < 0:
                speed_y *= -1

            if sprite.collide_rect(sprite1, ball) or sprite.collide_rect(sprite2, ball):
                speed_x *= -1

            if ball.rect.x > 700:
                pnavi += 1
                ball.rect.x = 350
                ball.rect.y = 250
                time.delay(500)
    
                              

            if ball.rect.x < 0:
                pastr += 1
                ball.rect.x = 350
                ball.rect.y = 250
                time.delay(500)

            if pnavi == 1 or pastr == 1:
                ball.size_x = 80
                ball.size_y = 80

            if pnavi == 1 and pastr == 1 or pnavi == 2 or pastr == 2:
                ball.speed_x = 8
                ball.speed_y = 8

            if pnavi == 1 and pastr == 2 or pnavi == 2 and pastr == 1:
                ball.size_x = 20
                ball.size_y = 20

            display.update()
            time.delay(10)


button1.clicked.connect(df1)
button2.clicked.connect(pinpong2)
button3.clicked.connect(pinpong1)
button4.clicked.connect(df2)
button5.clicked.connect(df3)
button6.clicked.connect(back)
button6.clicked.connect(back)

app.exec_()











