import random
import numpy as np
import cv2

from test import Character, Aggressor, Egoist,Altruist
from utils import atack


class Wall:
    def __init__(self,w,h):
        self.w = w
        self.h = h
        self.step = 20
        self.image = self.__create_surface()
        #self.wall = [[1] * h for i in range(w)]
        self.wall = [[1 if i==0 or j==0 or i ==w or j==h else 0 for j in range(h+1)]for i in range(w+1)]
        #print(self.wall)
        self.color = (55, 55, 55)

    def __create_surface(self):
        surface = np.zeros([(self.h+1)*self.step, (self.w+1)*self.step, 3], dtype=np.uint8)
        surface.fill(255)
        return surface

    def draw_box(self):
        #image = self.__create_surface()
        #self.image = self.__create_surface()
        for i in range(self.w+1):
            for j in range(self.h+1):
                if self.wall[i][j] == 1:
                    #cv2.rectangle(image, (i*self.step, j*self.step), ((i+1)*self.step, (j+1)*self.step), self.color, cv2.FILLED)
                    cv2.rectangle(self.image, (i*self.step, j*self.step), ((i+1)*self.step, (j+1)*self.step), self.color, cv2.FILLED)
        #cv2.imshow('image',image)
        cv2.imshow('image',self.image)
        cv2.waitKey(0)
        return None

    #def draw(self, i, j):
    #    cv2.rectangle(self.image, (i*self.step, j*self.step), ((i+1)*self.step, (j+1)*self.step), (0,255,0), cv2.FILLED)
    #    return None

    #def undraw(self, i, j):
    #    cv2.rectangle(self.image, (i*self.step, j*self.step), ((i+1)*self.step, (j+1)*self.step), (255,255,255), cv2.FILLED)
    #    return None

    def draw_walls(self, x1, y1, x2, y2):
        if x2 == -1:
            self.wall[x1][y1] = 1
        else:
            if x1 == x2:
                for i in range(min(y1,y2),max(y1,y2)+1):
                    self.wall[x1][i] = 1
            else:
                for i in range(min(x1,x2),max(x1,x2)+1):
                    self.wall[i][y1] = 1
        return None
    def add_walls(self, wstr):
        #print(wstr[0:2])
        na4 = True
        razr = False
        x1, y1 = -1, -1
        x2, y2 = -1, -1
        for i in range(len(wstr)):
            #print(wstr[i])
            if wstr[i].isdigit():
                if na4 == True:
                    fst = i
                    snd = i
                    na4 = False
                else:
                    pass
            else:
                if not razr:
                    if na4 == False:
                        na4 = True
                        snd = i
                        #print(wstr[fst:snd])
                        if x1 == -1:
                            x1 = int(wstr[fst:snd])
                        elif y1 == -1:
                            y1 = int(wstr[fst:snd])
                        else:
                            pass#?
                    elif wstr[i] == ':':
                        razr = True
                    elif wstr[i] == ',':
                        #print(i,' ','1st ',x1,';',y1,'   ',x2,y2)
                        self.draw_walls(x1,y1,x2,y2)
                        x1, y1 = -1, -1
                else:
                    if wstr[i] == '(':
                        continue
                    if na4 == False:
                        na4 = True
                        snd = i
                        #print(wstr[fst:snd])
                        if x2 == -1:
                            x2 = int(wstr[fst:snd])
                        elif y2 == -1:
                            y2 = int(wstr[fst:snd])
                        else:
                            pass#?
                    elif wstr[i] == ':':
                        #do razrez
                        #print('2nd ',x1,';',y1,':',x2,';',y2)
                        self.draw_walls(x1,y1,x2,y2)
                        x1, y1 = x2, y2
                        x2, y2 = -1, -1
                    else:
                        #do razrez
                        #print('3rd ',x1,';',y1,':',x2,';',y2)
                        self.draw_walls(x1,y1,x2,y2)
                        razr = False
                        x1, y1, x2, y2 = -1, -1, -1, -1
        if x2 == -1:
            #print('last1 ',x1,';',y1,'   ',x2,y2)
            self.draw_walls(x1,y1,x2,y2)
        else:
            #print('last2 ',x1,';',y1,':',x2,';',y2)
            self.draw_walls(x1,y1,x2,y2)

        return None



a = Wall(20, 20)
#a.draw_box()
test = '(3;9):(20;9),(1;2),(2;4):(2;6),(5;4):(7;4):(7;6):(5;6)'
#test = '(10;7):(10;13),(7;10):(13;10),(7;7):(7;10),(13;13):(13;10),(7;13):(10;13),(10;7):(13;7)'

a.add_walls(test)
a.draw_box()


n = 25
d = [i for i in range(n)]
#print(d)
kal,keg,kagr = 1,1,3
n3 = int(n/(kal+keg+kagr))
#print(n3)
ost = n - n3*kal- n3*keg-n3*kagr
ostt = int(ost/3)
#print('ost',ost/3)
ost1,ost2,ost3 = ostt,ostt,ostt
#print(ost-ostt*3)
if ost-ostt*3 == 1:
    ost3+=1
elif ost-ostt*3 ==2:
    ost3+=1
    ost2+=1
bg1 = n3*kal+ost1
bg2 = bg1 + n3*keg+ost2

for i in d[:bg1]:
    while True:
        rx, ry = random.randint(1,19),random.randint(1,19)
        if a.wall[rx][ry] != 1:
            break
    d[i] = Altruist(rx, ry)
    d[i].draw(d[i].x,d[i].y,a.image,a.step)
for i in d[bg1:bg2]:
    while True:
        rx, ry = random.randint(1,19),random.randint(1,19)
        if a.wall[rx][ry] != 1:
            break
    d[i] = Egoist(rx, ry)
    d[i].draw(d[i].x,d[i].y,a.image,a.step)
for i in d[bg2:n]:
    while True:
        rx, ry = random.randint(1,19),random.randint(1,19)
        if a.wall[rx][ry] != 1:
            break
    d[i] = Aggressor(rx, ry)
    d[i].draw(d[i].x,d[i].y,a.image,a.step)

#рандомные персонажи
"""for i in spis:
    #d[i] = Character(random.randint(1,19),random.randint(1,19))
    k = random.randint(1,3)
    while True:
        rx, ry = random.randint(1,19),random.randint(1,19)
        if a.wall[rx][ry] != 1:
            break
    if k == 1:
        d[i] = Aggressor(rx, ry)
    elif k == 2:
        d[i] = Egoist(rx, ry)
    else:
        d[i] = Altruist(rx, ry)
    print(d[i].x,d[i].y, d[i].who)
    d[i].draw(d[i].x,d[i].y,a.image,a.step)
cv2.imshow('img',a.image)
cv2.waitKey(0)
cv2.destroyAllWindows()"""

TEMP = False
while True:
    random.shuffle(d)
    for first in d:
        #a.undraw(first.x,first.y)
        first.undraw(first.x,first.y,a.image,a.step)
        #first.untext(first.x,first.y,a.image, a.step)
        if first.who == "Aggressor":
            if first.inspection(a.wall, d) == False:
                first.step(a.wall)
        else:
            first.step(a.wall)


        #a.draw(first.x,first.y)
        first.draw(first.x,first.y,a.image,a.step)

        """cv2.imshow('img',a.image)
        key = cv2.waitKey(0)
        if key == 27:  # if ESC is pressed, exit loop
            cv2.destroyAllWindows()
            TEMP = True
            break"""


        for second in d:
            if first!=second and first.x == second.x and first.y == second.y:
                #print("popalBefore",first.who, first.hp,second.who,second.hp)
                atack(first,second)
                #print("popalAfter",first.who, first.hp,second.who,second.hp)
                if first.hp <= 0 and second.hp <= 0:
                    #print('both dead',i,j)
                    print(F'{first.who} #{first.k} died with {second.who} #{first.k}')
                    first.undraw(first.x,first.y,a.image,a.step)
                    d.remove(first)
                    d.remove(second)
                    break
                    #continue ???
                elif first.hp <= 0:
                    print('{} #{} died from {} #{}'.format(first.who,first.k,second.who,second.k))
                    d.remove(first)
                    #del first
                    break
                    #continue ???
                elif second.hp <= 0:
                    #print('dead %s# %i'%second.who%j)
                    print('{2} #{3} killd by {0} #{1}'.format(first.who,first.k,second.who,second.k))
                    d.remove(second)
                    #del second
                    break
                    #continue ???
    #print(d)
    if len(d) == 1:
        print('{0} #{1} Winner!'.format(d[0].who,d[0].k))
        break
    elif len(d) == 0:
        print("No Winners!")
    if TEMP == True:
        break
    cv2.imshow('img',a.image)
    key = cv2.waitKey(50)
    if key == 27:  # if ESC is pressed, exit loop
        cv2.destroyAllWindows()
        break
