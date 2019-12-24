import random
import numpy as np
import cv2

class Character:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.hp = 100
        self.color = (0, 255, 0)
        self.damage = 200
        self.defence = 20
        self.who = "Character"


    def step(self, wall):
        while True:
            direction = random.choice(['left', 'right', 'top', 'bot', 'lt','lb','rt','rb'])
            if direction == 'left':
                if wall[self.x - 1][self.y] != 1:
                    self.x -= 1
                    break
            if direction == 'right':
                if wall[self.x + 1][self.y] != 1:
                    self.x += 1
                    break
            if direction == 'top':
                if wall[self.x][self.y - 1] != 1:
                    self.y -= 1
                    break
            if direction == 'bot':
                if wall[self.x][self.y + 1] != 1:
                    self.y += 1
                    break
            if direction == 'lt':
                if wall[self.x - 1][self.y - 1] != 1:
                    self.x -= 1
                    self.y -= 1
                    break
            if direction == 'lb':
                if wall[self.x - 1][self.y + 1] != 1:
                    self.x -= 1
                    self.y += 1
                    break
            if direction == 'rt':
                if wall[self.x + 1][self.y - 1] != 1:
                    self.x += 1
                    self.y -= 1
                    break
            if direction == 'rb':
                if wall[self.x + 1][self.y + 1] != 1:
                    self.x += 1
                    self.y += 1
                    break
        #print(self.x,self.y)
        return direction

    def draw(self, i, j, img, step):
        self.checkout()
        cv2.rectangle(img, (i*step, j*step), ((i+1)*step, (j+1)*step), self.color, cv2.FILLED)
        #cv2.circle(img, (int((i+0.5)*step), int((j+0.5)*step)), 10, (0,255,0), cv2.FILLED)
        return None

    def undraw(self, i, j, img, step):
        cv2.rectangle(img, (i*step, j*step), ((i+1)*step, (j+1)*step), (255,255,255), cv2.FILLED)
        return None

    def text(self, i, j, img, step):
        cv2.putText(img, "wut", (i*step + 3, j*step + 3), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)
        return None
    def untext(self, i, j, img, step):
        cv2.putText(img, "wut", (i*step + 3, j*step + 3), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
        return None
    def checkout(self):
        if self.hp <= 75 and self.hp >= 25:
            self.color = (0, 255, 255)
        elif self.hp <= 25:
            self.color = (0, 0, 255)
    def inspection(self, wall, d):
        pass

"""
    def step(self):
        while True:
            direction = random.choice(['left', 'right', 'top', 'bot', 'lt','lb','rt','rb'])
            if direction == 'left':
                if self.x - 1 >= 0:
                    self.x -= 1
                    #return direction
                    #return None
            if direction == 'right':
                if self.x + 1 <= 20:
                    self.x += 1
                    #return direction
                    #return None
            if direction == 'top':
                if self.y - 1 >= 0:
                    self.y -= 1
                    #return direction
                    #return None
            if direction == 'bot':
                if self.y + 1 <= 20:
                    self.y += 1
                    #return direction
                    #return None
            if direction == 'lt':
                if self.x - 1 >= 0 and self.y - 1 >= 0:
                    self.x -= 1
                    self.y -= 1
            if direction == 'lb':
                if self.x - 1 >= 0 and self.y + 1 <= 20:
                    self.x -= 1
                    self.y += 1
            if direction == 'rt':
                if self.x + 1 <= 20 and self.y - 1 >= 0:
                    self.x += 1
                    self.y -= 1
            if direction == 'rb':
                if self.x + 1 <= 20 and self.y + 1 <= 20:
                    self.x += 1
                    self.y += 1
            print("e ",self.x,self.y)
            return direction
            break
"""

class Aggressor(Character):
    def __init__(self, x, y):
        Character.__init__(self,x,y)
        self.who = "Aggressor"
        self.damage = 300
        self.defence = 15
        global k
        self.k = k
        k+=1
        #print(k)
    def inspection(self, wall, d):
        for i in d:
            if self != i and i.who != "Aggressor":
                if self.x - 1 == i.x and self.y == i.y :
                    self.x -= 1
                    #print("Im {} #{} see {} #{}".format(self.who,self.k,i.who,i.k))
                    return True
                if self.x + 1 == i.x and self.y == i.y:
                    self.x += 1
                    #print("Im {} #{} see {} #{}".format(self.who,self.k,i.who,i.k))
                    return True
                if self.x == i.x and self.y - 1 == i.y:
                    self.y -= 1
                    #print("Im {} #{} see {} #{}".format(self.who,self.k,i.who,i.k))
                    return True
                if self.x == i.x and self.y + 1 == i.y:
                    self.y += 1
                    #print("Im {} #{} see {} #{}".format(self.who,self.k,i.who,i.k))
                    return True
                if self.x - 1 == i.x and self.y - 1 == i.y:
                    self.x -= 1
                    self.y -= 1
                    #print("Im {} #{} see {} #{}".format(self.who,self.k,i.who,i.k))
                    return True
                if self.x - 1 == i.x and self.y + 1 == i.y:
                    self.x -= 1
                    self.y += 1
                    #print("Im {} #{} see {} #{}".format(self.who,self.k,i.who,i.k))
                    return True
                if self.x + 1 == i.x and self.y - 1 == i.y:
                    self.x += 1
                    self.y -= 1
                    #print("Im {} #{} see {} #{}".format(self.who,self.k,i.who,i.k))
                    return True
                if self.x + 1 == i.x and self.y + 1 == i.y:
                    self.x += 1
                    self.y += 1
                    #print("Im {} #{} see {} #{}".format(self.who,self.k,i.who,i.k))
                    return True
        return False
class Egoist(Character):
    def __init__(self, x, y):
        Character.__init__(self,x,y)
        self.who = "Egoist"
        self.damage = 100
        self.defence = 25
        global k1
        self.k = k1
        k1+=1
    def draw(self, i, j, img, step):
        self.checkout()
        cv2.circle(img, (int((i+0.5)*step), int((j+0.5)*step)), 10, self.color, cv2.FILLED)
        return None

class Altruist(Character):
    def __init__(self, x, y):
        Character.__init__(self,x,y)
        self.who = "Altruist"
        self.damage = 200
        self.defence = 20
        global k2
        self.k = k2
        k2+=1
    def draw(self, i, j, img, step):
        pt1 = (int((i+0.5)*step),j*step)
        pt2 = ((i+1)*step,(j+1)*step)
        pt3 = (i*step,(j+1)*step)
        triangle_cnt = np.array( [pt1, pt2, pt3] )
        self.checkout()
        cv2.drawContours(img, [triangle_cnt], 0, self.color, -1)
        return None


k,k1,k2 = 1,1,1
