

# Importing Modules

from turtle import *
from time import sleep,time
import threading
import math
from tkinter import *
import tkinter.messagebox as Mb
import random
import pickle
import os
import ForgotPassword
import winsound
import csv
from tkinter import ttk 

# Checking if required files are present in the folder, else creating new folders to be used.
try:
    f1 = open("register.cm" , 'rb')
    f1.close()
    f = open("Highscores.csv" , 'r')
    f.close()
except:
    f = open("register.cm" , 'wb')
    f.close() 
    f = open("Highscores.csv" , 'w' , newline = '')
    w = csv.writer(f)
    w.writerow(['NAME' , 'EMAIL ID' , 'HIGHSCORE_1' , "HIGHSCORE_2" , "HIGHSCORE_3"])
    f.close()

def divide_list(l):
    for i in range(0, len(l), 10):
        yield l[i:i + 10]

# Tuple for Knight images

knight = [["SNinja_Atk 1L.gif", "SNinja_Atk 2L.gif", "SNinja_Atk 3L.gif", "SNinja_Atk 4L.gif", "SNinja_Atk 5L.gif",
           "SNinja_Atk 6L.gif"],
          ["SNinja_Atk 1Ll.gif", "SNinja_Atk 2Ll.gif", "SNinja_Atk 3Ll.gif", "SNinja_Atk 4Ll.gif", "SNinja_Atk 5Ll.gif",
           "SNinja_Atk 6Ll.gif"],
          ["SNinja_idle 1L.gif", "SNinja_idle 2L.gif", "SNinja_idle 3L.gif", "SNinja_idle 4L.gif", "SNinja_idle 5L.gif",
           "SNinja_idle 6L.gif"],
          ["SNinja_idle 1Ll.gif", "SNinja_idle 2Ll.gif", "SNinja_idle 3Ll.gif", "SNinja_idle 4Ll.gif",
           "SNinja_idle 5Ll.gif", "SNinja_idle 6Ll.gif"],
          ["SNinja_jumpatk 1L.gif", "SNinja_jumpatk 2L.gif", "SNinja_jumpatk 3L.gif", "SNinja_jumpatk 4L.gif",
           "SNinja_jumpatk 5L.gif", "SNinja_jumpatk 6L.gif"],
          ["SNinja_jumpatk 1Ll.gif", "SNinja_jumpatk 2Ll.gif", "SNinja_jumpatk 3Ll.gif", "SNinja_jumpatk 4Ll.gif",
           "SNinja_jumpatk 5Ll.gif", "SNinja_jumpatk 6Ll.gif"],
          ["SNinja_run 01L.gif", "SNinja_run 02L.gif", "SNinja_run 03L.gif", "SNinja_run 04L.gif", "SNinja_run 05L.gif",
           "SNinja_run 06L.gif", "SNinja_run 07L.gif", "SNinja_run 08L.gif", "SNinja_run 09L.gif", "SNinja_run 10L.gif",
           "SNinja_run 11L.gif"],
          ["SNinja_run 01Ll.gif", "SNinja_run 02Ll.gif", "SNinja_run 03Ll.gif", "SNinja_run 04Ll.gif",
           "SNinja_run 05Ll.gif", "SNinja_run 06Ll.gif", "SNinja_run 07Ll.gif", "SNinja_run 08Ll.gif",
           "SNinja_run 09Ll.gif", "SNinja_run 10Ll.gif", "SNinja_run 11Ll.gif"],
          ["SNinja_strike 1L.gif", "SNinja_strike 2L.gif", "SNinja_strike 3L.gif", "SNinja_strike 4L.gif",
           "SNinja_strike 5L.gif", "SNinja_strike 6L.gif", "SNinja_strike 7L.gif", "SNinja_strike 8L.gif"],
          ["SNinja_strike 1Ll.gif", "SNinja_strike 2Ll.gif", "SNinja_strike 3Ll.gif", "SNinja_strike 4Ll.gif",
           "SNinja_strike 5Ll.gif", "SNinja_strike 6Ll.gif", "SNinja_strike 7Ll.gif", "SNinja_strike 8Ll.gif"],
          ["SNinja_crouch 3L.gif",], ["SNinja_crouch 3Ll.gif",], ["SNinja_crouchdash 2L.gif",],
          ["SNinja_crouchdash 2Ll.gif",], ["SNinja_jump 3L.gif",], ["SNinja_jump 3Ll.gif",],
          ["Practice level tilemap.gif", "lvl 1 backdrop.gif", "Pro health copy.gif" , 'chakra.gif' , "Trap lvl tile map.gif" , "spike ball.gif" , "troll unit icon.gif",
           "Troll Level Map.gif"]]

for i in knight:
    for j in range(len(i)):
        i[j] = "Knight\\" + i[j]

trollsr = ['trollsr2\\' + i for i in os.listdir(os.path.dirname(os.path.abspath(__file__)) + "\\trollsr2")]
trollsr = list(divide_list(trollsr[::2] + trollsr[1::2]))


# Trap Level Groundmapping
ground_x_trap = (6150, 5871, 4936, 4825, 4660, 4563, 3915, 3790, 3633, 3496, 3278, 3146, 3019, 2870, 2652, 882, 719, 595,441 ,300, 150 ,20 , -129 , -252 , -406 ,-790 , -940 , - 1079 , -1228 , -1368 , -1600 ,  -1750 , -1902 ,-2040 ,-2186,-2463,-4265 ,-4507 , -5400 ,-6150)  
ground_y_trap = (-250, -250, -300, -160, -300, -260, -210, -160, -210, -300, -210, -160, -110, -300, -260, -210, -260, -150, -260 ,-210,-260, -150 ,  -260 , -210 ,-260 , -150 , -260,-150 , -260,-150 ,-260 , -150  ,  -260  , -150 , -300 , -260 , -300 , -260 , -260,-260)
ground_y2_trap = (-350, -350, -400, -260, -500, -360, -310, -260, -310, -500, -310, -260, -210, -500, -360, -310, -360, -310, -360 ,-310 ,-360 , -250, -360, -310 , -360, -250 , -360, - 250 , -360,-250 , -360 , -250 , -360 , -250 , -400, -360 ,  -400 ,-360 , -360 ,-360)

obstacles_trap = (((-700, -600), (-600, 600), (5381, 5381), (100, 100)),((0,0),(-300 , -251),(4925 , 5391),(100 , 100)),((0,0),(-300 , -161),(4650 , 4835),(100 , 100)),((0,0),(-300 , -261),(3905 , 4573),(100 , 100)),
((0,0),(-300 , -211),(3780 , 3925),(100 , 100)),((0,0),(-300 , -161),(3623 , 3800),(100 , 100)),((0,0),(-300 , -211),(3486 , 3643),(100 , 100)),
((0,0),(-300 , -211),(3146 , 3288),(100 , 100)),((0,0),(-300 , -161),(3009 , 3156),(100 , 100)),((0,0),(-300 , -111),(2860 , 3029),(100 , 100)),((0,0),(-300 , -261),(-2176 , 2662),(100 , 100)),
((0,0),(-300 , -211),(709 , 892),(100 , 100)),((0,0),(-300 , -151),(431 , 605),(100 , 100)),((0,0),(-300 , -211),(140 , 310),(100 , 100)),((0,0),(-300 , -151),(-139 , 30),(100 , 100)),
((0,0),(-300 , -211),(-416 , -242),(100 , 100)),((0,0),(-300 , -151),(-950 , -780),(100 , 100)),((0,0),(-300 , -151),(-1238 , -1069),(100 , 100)),((0,0),(-300 , -151),(-1610 , -1358),(100 , 100)),((0,0),(-300 , -151),(-1912 , -1740),(100 , 100)),
((0,0),(-300 , -151),(-2196 , -2030),(100 , 100)),((0,0),(-300 , -261),(-4275 , -2453),(100 , 100)),((0,0),(-300 , -261),(-5400 , -4497),(100 , 100)), ((600, 700), (-600, 600), (-5399, -5399), (100, 100)))

spikes_trap = ( ((0, 0), (-300, -275), (4835, 4925), (100, 100)),((0, 0), (-300, -275), (4573, 4650), (100, 100)),((0, 0), (-300, -275), (3288, 3486), (100, 100)),((0, 0), (-300, -275), (2662, 2860), (100, 100)),
((0, 0), (-260, -235), (605, 709), (100, 100)),((0, 0), (-260, -235), (310, 431), (100, 100)),((0, 0), (-260, -235), (30, 140), (100, 100)),((0, 0), (-260, -235), (-242, -139), (100, 100)),((0, 0), (-300, -275), (-2453, -2196), (100, 100)),
((0, 0), (-300, -275), (-4497, -4275), (100, 100))) 
postuple_trap = (([-4739 , 175] , [-4739 , -125]),([-3387 , 145] , [-3387 , -155]),([-2751 , 175] , [-2751 , -125]),([-2317 , -260] , [-1217 , -260]),([-661 , 135] , [-661 , -165]),([-361 , 135] , [-361 , -165]),([-61 , 135] , [-61 , -165]),([239 , 135] , [239 , -165]),
([872 , -110] , [1472 , -110]),([1498 , -110] , [2098 , -110]),([3530 , 175] , [3530 , -175]),([4375 , 100] , [4375 , -200]))

# Practice Level Groundmapping
ground_x_prac = (6150, 5871, 4505, 4285, 4120, 3876, 3776, 2195, 2050, 1605, 1437, 1226, 430, 245, -265, -395, -610, -770,-6150)  
ground_y_prac = (-250, -250, -180, -800, -50, -800, -260, -180, -105, -180, -300, -250, -800, -250, -800, -115, -800, -250, -260)

ground_y2_prac = (-450, -450, -250, -1000, -90, -1000, -460, -250, -360, -360, -560, -460, -900, -460, -900, -145, -900, -460, -460)

obstacles_prac = (((-700, -600), (-600, 600), (5398, 5398), (100, 100)), ((0, 0), (-350, -251), (4295, 6150), (100, 100)),
             ((0, 0), (-350, -181), (4295, 4506), (100, 100)), ((0, 0), (-200, -51), (3896, 4091), (100, 100)),
             ((0, 0), (-350, -261), (2195, 3777), (100, 100)), ((0, 0), (-350, -181), (2050, 2196), (100, 100)),
             ((0, 0), (-350, -106), (1595, 2051), (100, 100)),
             ((0, 0), (-350, -181), (1427, 1596), (100, 100)), ((0, 0), (-350, -301), (1226, 1428), (100, 100)),
             ((0, 0), (-350, -251), (408, 1227), (100, 100)),
             ((0, 0), (-350, -251), (-275, 251), (100, 100)),
             ((0, 0), (-300, -117), (-620, -394), (100, 100)),
             ((0, 0), (-350, -251), (-3655, -769), (100, 100)), ((0, 0), (180, 600), (-1888, -769), (100, 100)),
             ((0, 0), (-350, -251), (-4464, -3654), (100, 100)),
             ((0, 0), (-350, -251), (-5392, -4463), (100, 100)), ((600, 700), (-600, 600), (-4001, -4001), (100, 100)))

spikes_prac = (((0, 0), (-300, -270), (1227, 1427), (100, 100)),)


# Getting Maps 

def getgroundx(level):
    if level == 2:
        return ground_x_trap
    elif level == 1:
        return ground_x_prac

def getgroundy(level):
    if level == 2:
        return ground_y_trap
    elif level == 1:
        return ground_y_prac

def getgroundy2(level):
    if level == 2:
        return ground_y2_trap
    elif level == 1:
        return ground_y2_prac

def getobstacles(level):
    if level == 1:
        return obstacles_prac
    elif level == 2:
        return obstacles_trap
    else:
        return tuple()

def getspikes(level = 2):
    if level == 2:
        return spikes_trap
    elif level == 1:
        return spikes_prac

def getpostuple(level = 2):
    if level == 2:
        return postuple_trap


# Game Behaviour Functions

# Calculates the ground height for each frame
def ground():
    global ground_level, ground_marker
    if pro.facing:
        if bg.x > ground_x[ground_marker] - 10:
            ground_marker -= 1

    else:
        if bg.x < ground_x[ground_marker + 1]:
            ground_marker += 1
    ground_level = ground_y[ground_marker]

# Checks if player is inside walls
def obstaclehit():  
    global i
    for i in obstacles:
        if bg.x >= i[2][0] and bg.x <= i[2][1] and pro.y >= i[1][0] and pro.y <= i[1][1] and pro.x >= i[0][0] and pro.x <= i[0][1] and bg.y >= i[3][0] and bg.y <= i[3][1]:
            return True

# To bring player outside walls from right side
def rightobs():
    for i in obstacles:
        if bg.x == i[2][1] and i[1][0] <= pro.y <= i[1][1] and pro.x == i[0][0] and i[3][0] <= bg.y <= i[3][1]:
            return True

# To bring player outside walls from left side
def leftobs():
    for i in obstacles:
        if bg.x == i[2][0] and i[1][0] <= pro.y <= i[1][1] and pro.x == i[0][1] and i[3][0] <= bg.y <= i[3][1]:
            return True

# To check if player collides with stationary spikes
def spikehit():
    global pro
    if not(pro.recoil):
        for i in spikes:
            if  bg.x >= i[2][0] and bg.x <= i[2][1] and pro.y >= i[1][0] and pro.y <= i[1][1] and pro.x >= i[0][0] and pro.x <= i[0][1] and bg.y >= i[3][0] and bg.y <= i[3][1]:
                takedamage(25)
                sleep(0.2)
                pro.recoil = True
                pro.blinkcount = 1
                break

# To check if player collides with moving traps
def traphit(radius = 75):
    global pro
    if not(pro.recoil):
        for i in traplist:
            if (i.xcor() - pro.xcor()) ** 2 + (i.ycor() - pro.ycor()) ** 2 < radius ** 2:
                takedamage(25)
                sleep(0.2)
                pro.recoil = True
                pro.blinkcount = 1
                break

# Taking Damage
def takedamage(damage):
    global pro
    pro.health -= damage

# Reducing Enemy health
def tstakedamage(damage):
    global ts
    ts.health -= damage

# To avoid glitches

def timedelay():
    sleep(0.05)
    pro.killstate = True

def timedelay2():
    pro.canattack = False
    sleep(0.5)
    pro.canattack = True

def timedelay3():
    ts.attackcan = False
    sleep(0.2)
    ts.attackcan = True

# To move objects every frame
def move(level):
    global pro
    if pro.atk:
        if pro.facing:
            pro.shape(knight[1][pro.atkcount])
        else:
            pro.shape(knight[0][pro.atkcount])
        if pro.atkcount < 5:
            pro.atkcount += 1
        else:
            pro.atk = False
            pro.atkcount = 0
    if pro.jmpatk:
        if pro.facing:
            pro.shape(knight[5][pro.jmpatkcount])
        else:
            pro.shape(knight[4][pro.jmpatkcount])
        if pro.jmpatkcount < 5:
            pro.jmpatkcount += 1
        else:
            pro.jmpatk = False
            pro.jmpatkcount = 0

    if pro.stk:
        if pro.facing:
            pro.shape(knight[9][pro.stkcount // 2])
        else:
            pro.shape(knight[8][pro.stkcount // 2])
        if pro.stkcount < 15:
            pro.stkcount += 1
        else:
            pro.stk = False
            pro.stkcount = 0

    if (pro.isjump or pro.freefall) and not (pro.jmpatk):
        if pro.facing:
            pro.shape(knight[15][0])
        else:
            pro.shape(knight[14][0])

    if pro.crouchstatus:
        if level == 3:
            if pro.facing:
                pro.shape(knight[11][0])
            else:
                pro.shape(knight[10][0])


    elif pro.slide:
        if pro.facing:
            pro.shape(knight[13][0])
        else:
            pro.shape(knight[12][0])

    if pro.idle and not (pro.atk or pro.isjump or pro.freefall or pro.stk or (pro.crouchstatus and level == 3) or pro.slide or pro.slidestatus):
        if pro.right:
            pro.shape(knight[6][pro.runcount // 2])
            if pro.runcount < 21:
                pro.runcount += 1
            else:
                pro.runcount = 0

        elif pro.left:
            pro.shape(knight[7][pro.runcount // 2])
            if pro.runcount < 21:
                pro.runcount += 1
            else:
                pro.runcount = 0

        else:
            if pro.facing:
                pro.shape(knight[3][pro.idlecount // 3])
            else:
                pro.shape(knight[2][pro.idlecount // 3])
            if pro.idlecount < 17:
                pro.idlecount += 1
            else:
                pro.idlecount = 0
    pro.goto(pro.x, pro.y)
    if level != 3:
        bg.goto(bg.x, bg.y)
    if level == 1:
        bg1.goto((bg.x*0.5), bg.y)

# To calculate position of traps every frame
def iterate(trap):
    if trap.counter == 1:
        Dest = trap.Ep
    else:
        Dest = trap.Sp
    if [trap.x , trap.y] == Dest:
        trap.counter = -trap.counter
    else:
        if trap.x != Dest[0]:
            trap.x += (Dest[0] - trap.x)/math.fabs(Dest[0] - trap.x) * trap.speed
        if trap.y != Dest[1]:
            trap.y += (Dest[1] - trap.y)/math.fabs(Dest[1] - trap.y) * trap.speed

# Enemy AI
def troll_brain():

    ts.goto(ts.x, ts.y)
    # Troll executing it's decision
    if ts.state: 

        # Jump Attack
        if ts.state == 1:
            if ts.attackcan:
                if 2 < ts.jumpcount < 7:
                    ts.y += ((7 - ts.jumpcount) * 2) ** 2
                elif 7 < ts.jumpcount < 12:
                    ts.y -= ((ts.jumpcount - 7) * 2) ** 2
                elif ts.jumpcount == 18:
                    ts.jumpcount = 1
                    ts.state = 0
                if ts.refresh_rate == 1:
                    ts.shape(trollsr[4 + ts.head * 6][ts.jumpcount // 2])
                    if ts.jumpcount > 10 and abs(ts.x - pro.x) < 100 and not pro.recoil and not ts.blinkcount:
                        takedamage(35)
                        pro.recoil = True
                        pro.blinkcount = 1
                ts.jumpcount += 1

        # Normal Attack
        elif ts.state == 2:
            if ts.attackcan:
                if ts.refresh_rate and not ts.stuck_count:
                    ts.shape(trollsr[0 + ts.head * 6][ts.attackcount])
                    ts.attackcount += 1
                    if ts.attackcount > 9:
                        ts.attackcount = 0
                        ts.state = 0
                    if ts.attackcount > 5 and abs(ts.x - pro.x) < 375 and not pro.recoil and not ts.blinkcount:
                        if pro.x < 150:
                            takedamage(20)  # -5
                        else:
                            takedamage(10)
                        pro.recoil = True
                        pro.blinkcount = 1
                    elif ts.attackcount == 9 and not pro.recoil and not ts.blinkcount:
                        ts.stuck_count = 50
                elif ts.stuck_count:
                    ts.stuck_count -= 1

        # Walk Towards Player
        elif ts.state == 3:
            if ts.refresh_rate:
                ts.shape(trollsr[5 + ts.head * 6][ts.walkcount])
                ts.walkcount += 1
                if ts.walkcount > 9:
                    ts.walkcount = 0
            ts.x += (2 * ts.head - 1) * 5
            if abs(ts.x - pro.x) < 300 or (abs(ts.x - pro.x) > 600 and ts.mad_repeat):
                ts.state = 0

        # Mad Attack (falling spike balls)
        else:
            if ts.mad_attk_count < 10:
                if 1 < ts.jumpcount < 4:
                    ts.y += ((4 - ts.jumpcount) * 2) ** 3
                elif 3 < ts.jumpcount < 6:
                    ts.y -= ((ts.jumpcount - 3) * 2) ** 3
                elif ts.jumpcount == 9:
                    ts.jumpcount = 1
                    ts.mad_attk_count += 1
                if ts.refresh_rate:
                    ts.shape(trollsr[4 + ts.head * 6][ts.jumpcount])
                ts.jumpcount += 1

                if spike.y > -250:
                    spike.goto(spike.x, spike.y)
                    if spike.y < -200:
                        if pro.x + 30 > spike.x > pro.x - 30:
                            takedamage(5)
                    spike.y -= 80
                else:
                    spike.y = 560
                    spike.x = pro.x + random.random() * 10 * ((pro.facing / 90) - 1)
            else:
                ts.state = 0
                spike.y = 0
                spike.goto(0, 560)

        if ts.refresh_rate == 0:
            ts.refresh_rate = 1
        else:
            ts.refresh_rate = 0

    else:  # Troll thinking... (Decision making process)
        sep_dist = abs(ts.x - pro.x)
        if sep_dist > ts.x - pro.x + 5:
            ts.head = 1  # 1 => heading right
        else:
            ts.head = 0  # 0 => heading left

        if sep_dist < 100:  # Jump Desicion
            ts.state = 1
            t6 = threading.Thread(target=timedelay3)
            t6.start()
            ts.jumpcount = 0

        elif sep_dist < 300:  # Attack
            ts.state = 2
            ts.mad_repeat = 1
            t5 = threading.Thread(target=timedelay3)
            t5.start()

        elif sep_dist < 500:  # Walk
            ts.state = 3
            ts.walkcount = 0

        else:  # Mad Attack
            temp = random.random()
            if temp < 0.7 and ts.mad_repeat:
                ts.state = 4
                ts.jumpcount = 0
                ts.mad_attk_count = 0
                ts.mad_repeat = 0
                spike.x = pro.x + 5 * ((pro.facing / 90) - 1)
                spike.y = 560
            else:
                ts.state = 3
                ts.walkcount = 0
                ts.mad_repeat = 0


#--------------------------------------------------------------------------------------
# ------------------------- Mainloop for the second level ------------------------------
def mainloop2():
    global game , result , prev_health

    while game:
        tracer(3,0)

        #GAME OVER
        if pro.health <= 0:
            pro.health = 0
            game  = False
            result = 0

        #LEVEL COMPLETE
        if bg.x < -5190:
            game = False
            result = 1

        # movement and controls
        ground()

        spikehit()
        traphit()

        
        if pro.blinkcount > 0 and pro.blinkcount <= 6:
            if pro.blinkcount % 2 == 0:
                pro.showturtle()
            elif pro.blinkcount % 2 == 1:
                pro.hideturtle()
            pro.blinkcount += 0.5
        if pro.blinkcount == 6.5:
            pro.blinkcount = 0
            pro.recoil = False
        




        if pro.y == ground_level:  
            pro.idle = True
            pro.dashready = True

        if not (pro.slide or pro.slidestatus):

            if pro.atkstatus and not (pro.atk):
                if pro.idle:
                    pro.atk = True
                    pro.atkstatus = False

            elif pro.jmpatkstatus and not (pro.jmpatk):
                pro.jmpatk = True
                pro.jmpatkstatus = False

            elif pro.stkstatus and not (pro.stk):
                pro.stk = True
                pro.stkstatus = False

            elif pro.dashstatus:
                pro.dash = True
                pro.dashstatus = False

        if not (pro.atk or pro.stk or pro.dash or pro.slidestatus or pro.slide):  # He can move only if he doesnt attack

            if not (pro.jmpatk):
                if pro.rightstatus:  
                    pro.right = True
                    pro.facing = 0
                    pro.left = False
                    if bg.x >= -5398 and pro.x >= 0:
                        pro.x = 0
                        bg.x -= pro.vel
                        if bg.x < -5398:
                            pro.x += bg.x + 5398
                            bg.x = -5399
                    else:
                        pro.x += pro.vel
                    if obstaclehit():  
                        pro.x = i[0][0]  
                        bg.x = i[2][1]  
                    if pro.vel < 20.1:
                        pro.vel += 1
                elif pro.leftstatus:  
                    pro.left = True
                    pro.facing = 180
                    pro.right = False
                    if bg.x <= 5380 and pro.x <= 0:
                        bg.x += pro.vel
                        pro.x = 0
                        if bg.x > 5380:
                            pro.x -= bg.x - 5380
                            bg.x = 5381
                    else:
                        pro.x -= pro.vel
                    if obstaclehit():
                        pro.x = i[0][1]
                        bg.x = i[2][0]
                    if pro.vel < 20.1:
                        pro.vel += 1
                else:
                    pro.left = False
                    pro.right = False
                    pro.vel = 15

            if not (pro.isjump):  
                if pro.y == ground_level:  
                    pro.idle = True

                    if pro.jumpstatus:
                        pro.isjump = True
                        pro.idle = False
                        pro.left = False
                        pro.right = False
                        pro.killstate = False

            else:

                if pro.isjump:

                    if pro.jumpcount > 0:  
                        pro.y += pro.jumpcount ** 2
                        pro.jumpcount -= 1


                    else:
                        pro.isjump = False
                        pro.jumpcount = 8

                        if pro.y != ground_level:  
                            pro.freefall = True
                        else:
                            pro.idle = True

            if pro.y > ground_level and not pro.isjump: 
                pro.freefall = True
                pro.killstate = False

            if pro.freefall:
                if pro.y > ground_level or pro.y < ground_y2[ground_marker]:  
                    pro.y -= pro.fallcount ** 2
                    pro.fallcount += 1
                    if ground_level > pro.y > ground_y2[ground_marker]:
                        pro.y = ground_level

                else:
                    pro.fallcount = 1
                    pro.y = ground_level 
                    pro.freefall = False
                    pro.idle = True
                    pro.vel = 15
                    t = threading.Thread(target=timedelay)
                    t.start()

        if pro.dash:
            if pro.dashcount > 0:
                if pro.facing:
                    if bg.x <= 5380 and pro.x <= 0:
                        pro.x = 0
                        bg.x += pro.dashcount ** 2 * 0.7
                        if bg.x > 5380:
                            pro.x += bg.x - 5380
                            bg.x = 5381
                    else:
                        pro.x -= pro.dashcount ** 2 * 0.7
                else:
                    if bg.x >= -5398 and pro.x >= 0:
                        pro.x = 0
                        bg.x -= pro.dashcount ** 2 *  0.7
                        if bg.x < -5398:
                            pro.x += bg.x + 5398
                            bg.x = -5399
                    else:
                        pro.x += pro.dashcount ** 2 * 0.7
                if obstaclehit():
                    if pro.facing:
                        pro.x = i[0][1]
                        bg.x = i[2][0]
                    else:
                        pro.x = i[0][0]  
                        bg.x = i[2][1]
                    pro.dashcount = 1

                pro.dashcount -= 1
            if pro.dashcount == 0:
                pro.dash = False
                pro.dashcount = 10
                pro.isjump = False
                pro.freefall = True
                pro.jumpcount = 8
                dashready = False

        if pro.slidestatus:
            pro.slide = True
            if pro.vel == 15:
                pro.slidecount = pro.vel - 15
            else:
                pro.slidecount = pro.vel - 5
            pro.slidestatus = False

        if pro.slide:
            if pro.slidecount > 0 and pro.y == ground_level:
                if pro.facing:
                    if bg.x <= 5380 and pro.x <= 0:
                        pro.x = 0
                        bg.x += pro.slidecount ** 2 * 0.2
                        if bg.x > 5380:
                            pro.x += bg.x - 5380
                            bg.x = 5381
                    else:
                        pro.x -= pro.slidecount ** 2 * 0.2
                else:
                    if bg.x >= -5398 and pro.x >= 0:
                        pro.x = 0
                        bg.x -= pro.slidecount ** 2 * 0.2
                        if bg.x < -5398:
                            pro.x += bg.x + 5398
                            bg.x = -5399
                    else:
                        pro.x += pro.slidecount ** 2 * 0.2
                if obstaclehit():
                    if pro.facing:
                        pro.x = i[0][1]
                        bg.x = i[2][0]
                    else:
                        pro.x = i[0][0]  
                        bg.x = i[2][1]

                pro.slidecount -= 1

            else:
                pro.slide = False

        
        
        # UPDATING HEALTH BARS ...
        if pro.health != prev_health:
            if pro.health < 0:
                pro.health = 0
            prev_health = pro.health
            health.goto(-321 + (pro.health - 100) * 1.075, 273)
            health.shapesize(1, (100.1 - pro.health) * 0.1075)

        
        move(2)
        for trap in traplist:
            iterate(trap)
        for trap in traplist:
            if -1000 < trap.x + bg.x < 1000:
                trap.goto(trap.x + bg.x , trap.y)

        update()

#--------------------------------------------------------------------------------------
# ------------------------- Mainloop for the third level ------------------------------
def mainloop3():
    # mainloop
    global game, prev_health , result
    while game:
        tracer(3,0)

        if pro.crouchstatus and pro.health < 100:
            pro.health += 0.2

        # Checking whether Pro and Troll are dead
        if pro.health <= 0:
            pro.health = 0
            game = False
            result = 0

        if ts.health <= 0:
            ts.health = 0
            game = False
            result = 1

        # Pro movement and controls...
        if 0 < pro.blinkcount <= 6:
            if pro.blinkcount % 2 == 0:
                pro.showturtle()
            elif pro.blinkcount % 2 == 1:
                pro.hideturtle()
            pro.blinkcount += 0.5
        if pro.blinkcount == 6.5:
            pro.blinkcount = 0
            pro.recoil = False

        if 0 < ts.blinkcount <= 12:
            if ts.blinkcount % 2 == 0:
                ts.showturtle()
            elif ts.blinkcount % 2 == 1:
                ts.hideturtle()
            ts.blinkcount += 0.5
        if ts.blinkcount == 12.5:
            ts.blinkcount = 0
            ts.showturtle()

        if pro.y == ground_level:
            pro.idle = True
            pro.dashready = True

        if not (pro.crouchstatus or pro.slide or pro.slidestatus):

            if pro.atkstatus and not pro.atk:
                if pro.idle:
                    pro.atk = True
                    t2 = threading.Thread(target=timedelay2)
                    t2.start()
                    if abs(ts.x - pro.x) < 150: 
                        tstakedamage(5)
                        ts.blinkcount += 0.5
                    pro.atkstatus = False

            elif pro.jmpatkstatus and not pro.jmpatk:
                pro.jmpatk = True
                t3 = threading.Thread(target=timedelay2)
                t3.start()
                if abs(ts.x - pro.x) < 200: 
                    tstakedamage(15)
                    ts.blinkcount += 0.5
                pro.jmpatkstatus = False

            elif pro.stkstatus and not pro.stk:
                pro.stk = True
                t4 = threading.Thread(target=timedelay2)
                t4.start()
                if abs(ts.x - pro.x) < 200:
                    tstakedamage(10)
                    ts.blinkcount += 0.5
                pro.stkstatus = False

            elif pro.dashstatus:
                pro.dash = True
                pro.dashstatus = False

        if not (pro.atk or pro.stk or pro.dash or pro.slidestatus or pro.slide):  # He can move only if he doesnt attack

            if not (pro.jmpatk or pro.crouchstatus):
                if pro.rightstatus:
                    pro.right = True
                    pro.facing = 0
                    pro.left = False
                    pro.x += pro.vel
                    if pro.x > 660:
                        pro.x = 660

                    if pro.vel < 15.1:
                        pro.vel += 0.5
                elif pro.leftstatus:
                    pro.left = True
                    pro.facing = 180
                    pro.right = False
                    pro.x -= pro.vel
                    if pro.x < -660:
                        pro.x = -660
                    if pro.vel < 15.1:
                        pro.vel += 0.5

                else:
                    pro.left = False
                    pro.right = False
                    pro.vel = 10

            if not pro.isjump:

                if pro.y == ground_level:
                    pro.idle = True

                    if pro.jumpstatus:
                        pro.isjump = True
                        pro.idle = False
                        pro.left = False
                        pro.right = False
                        pro.killstate = False
                        pro.crouchstatus = False

            else:

                if pro.isjump:

                    if pro.jumpcount > 0:
                        pro.y += pro.jumpcount ** 2
                        pro.jumpcount -= 1

                    else:
                        pro.isjump = False
                        pro.jumpcount = 8

                        if pro.y != ground_level:
                            pro.freefall = True
                        else:
                            pro.idle = True

            if pro.y > ground_level and not pro.isjump:
                pro.freefall = True
                pro.killstate = False

            if pro.freefall:
                if pro.y > ground_level:
                    pro.y -= pro.fallcount ** 2
                    pro.fallcount += 1
                    if ground_level > pro.y:
                        pro.y = ground_level

                else:
                    pro.fallcount = 1
                    pro.y = ground_level
                    pro.freefall = False
                    pro.idle = True
                    pro.vel = 10
                    t = threading.Thread(target=timedelay)
                    t.start()

        if pro.dash:
            if pro.dashcount > 0:
                if pro.facing:
                    pro.x -= pro.dashcount ** 2 * 0.5
                else:
                    pro.x += pro.dashcount ** 2 * 0.5
                if pro.x > 660:
                    pro.x = 660
                    pro.dashcount = 1
                elif pro.x < -660:
                    pro.x = -660
                    pro.dashcount = 1

                pro.dashcount -= 1
            if pro.dashcount == 0:
                pro.dash = False
                pro.dashcount = 10
                pro.isjump = False
                pro.freefall = True
                pro.jumpcount = 8

        if pro.slidestatus:
            pro.slide = True
            if pro.vel == 10:
                pro.slidecount = pro.vel - 10
            else:
                pro.slidecount = pro.vel
            pro.slidestatus = False

        if pro.slide:
            if pro.slidecount > 0 and pro.y == ground_level:
                if pro.facing:
                    pro.x -= pro.slidecount ** 2 * 0.2
                else:
                    pro.x += pro.slidecount ** 2 * 0.2
                if pro.x > 660:
                    pro.x = 660
                elif pro.x < -660:
                    pro.x = -660
                if abs(ts.x - pro.x) < 70 and not pro.recoil and not ts.blinkcount:
                    tstakedamage(2)
                    ts.blinkcount += 0.5

                pro.slidecount -= 1

            else:
                pro.slide = False


        # UPDATING HEALTH BARS ...
        if [pro.health, ts.health] != prev_health:
            prev_health = [pro.health, ts.health]
            health.goto(-321 + (pro.health - 100) * 1.075, 273)
            health.shapesize(1, (100.1 - pro.health) * 0.1075)

            thealth.goto(311 - (ts.health - 100) * 1.075, 274)
            thealth.shapesize(1, (100.01 - ts.health) * 0.1075)

        move(3)
        troll_brain()
        update()
#--------------------------------------------------------------------------------------
# ------------------------- Mainloop for the first level ------------------------------
def mainloop1():

    global prev_health , result , game
    while game:

        tracer(3,0)
        if pro.health <= 0:
            pro.health = 0
            game = False
            result = 0
        elif pro.x >= 240 :
            game = False
            result = 1

        # movement and controls
        ground()

        spikehit()

        if pro.blinkcount > 0 and pro.blinkcount <= 6:
            if pro.blinkcount % 2 == 0:
                pro.showturtle()
            elif pro.blinkcount % 2 == 1:
                pro.hideturtle()
            pro.blinkcount += 0.5
        if pro.blinkcount == 6.5:
            pro.blinkcount = 0
            pro.recoil = False

        if pro.y == ground_level:  
            pro.idle = True
            pro.dashready = True

        if not (pro.slide or pro.slidestatus):

            if pro.atkstatus and not (pro.atk):
                if pro.idle:
                    pro.atk = True
                    pro.atkstatus = False

            elif pro.jmpatkstatus and not (pro.jmpatk):
                pro.jmpatk = True
                pro.jmpatkstatus = False

            elif pro.stkstatus and not (pro.stk):
                pro.stk = True
                pro.stkstatus = False

            elif pro.dashstatus:
                pro.dash = True
                pro.dashstatus = False

        if not (pro.atk or pro.stk or pro.dash or pro.slidestatus or pro.slide):

            if not (pro.jmpatk):
                if pro.rightstatus: 
                    pro.right = True
                    pro.facing = 0
                    pro.left = False
                    if bg.x >= -4000 and pro.x >= 0: 
                        pro.x = 0
                        bg.x -= pro.vel
                        if bg.x < -4000:
                            pro.x += bg.x + 4000
                            bg.x = -4001
                    else:
                        pro.x += pro.vel
                    if obstaclehit():  
                        pro.x = i[0][0]  
                        bg.x = i[2][1]  
                    if pro.vel < 20.1:
                        pro.vel += 1
                elif pro.leftstatus:  
                    pro.left = True
                    pro.facing = 180
                    pro.right = False
                    if bg.x <= 5380 and pro.x <= 0:
                        bg.x += pro.vel
                        pro.x = 0
                        if bg.x > 5380:
                            pro.x -= bg.x - 5380
                            bg.x = 5381
                    else:
                        pro.x -= pro.vel
                    if obstaclehit():
                        pro.x = i[0][1]
                        bg.x = i[2][0]
                    if pro.vel < 20.1:
                        pro.vel += 1
                else:
                    pro.left = False
                    pro.right = False
                    pro.vel = 15

            if not (pro.isjump):  

                if pro.y == ground_level:  
                    pro.idle = True

                    if pro.jumpstatus:
                        pro.isjump = True
                        pro.idle = False
                        pro.left = False
                        pro.right = False
                        pro.killstate = False

            else:

                if pro.isjump:

                    if pro.jumpcount > 0: 
                        pro.y += pro.jumpcount ** 2
                        pro.jumpcount -= 1


                    else:
                        pro.isjump = False
                        pro.jumpcount = 8

                        if pro.y != ground_level:  
                            pro.freefall = True
                        else:
                            pro.idle = True

            if pro.y > ground_level and not pro.isjump:  
                pro.freefall = True
                pro.killstate = False

            if pro.freefall:
                if pro.y > ground_level or pro.y < ground_y2[ground_marker]:  
                    pro.y -= pro.fallcount ** 2
                    pro.fallcount += 1
                    if ground_level > pro.y > ground_y2[ground_marker]:
                        pro.y = ground_level

                else:
                    pro.fallcount = 1
                    pro.y = ground_level 
                    pro.freefall = False
                    pro.idle = True
                    pro.vel = 15
                    t = threading.Thread(target=timedelay)
                    t.start()

        if pro.dash:
            if pro.dashcount > 0:
                if pro.facing:
                    if bg.x <= 5380 and pro.x <= 0:
                        pro.x = 0
                        bg.x += pro.dashcount ** 2
                        if bg.x > 5380:
                            pro.x += bg.x - 5380
                            bg.x = 5381
                    else:
                        pro.x -= pro.dashcount ** 2
                else:
                    if bg.x >= -4000 and pro.x >= 0:
                        pro.x = 0
                        bg.x -= pro.dashcount ** 2
                        if bg.x < -4000:
                            pro.x += bg.x + 4000
                            bg.x = -4001
                    else:
                        pro.x += pro.dashcount ** 2
                if obstaclehit():
                    if pro.facing:
                        pro.x = i[0][1]
                        bg.x = i[2][0]
                    else:
                        pro.x = i[0][0] 
                        bg.x = i[2][1]
                    pro.dashcount = 1

                pro.dashcount -= 1
            if pro.dashcount == 0:
                pro.dash = False
                pro.dashcount = 8
                pro.isjump = False
                pro.freefall = True
                pro.jumpcount = 8
                dashready = False

        if pro.slidestatus:
            pro.slide = True
            if pro.vel == 15:
                pro.slidecount = pro.vel - 15
            else:
                pro.slidecount = pro.vel - 5
            pro.slidestatus = False


        if pro.slide:
            if pro.slidecount > 0 and pro.y == ground_level:
                if pro.facing:
                    if bg.x <= 5380 and pro.x <= 0:
                        pro.x = 0
                        bg.x += pro.slidecount ** 2 * 0.2
                        if bg.x > 5380:
                            pro.x += bg.x - 5380
                            bg.x = 5381
                    else:
                        pro.x -= pro.slidecount ** 2 * 0.2
                else:
                    if bg.x >= -4000 and pro.x >= 0:
                        pro.x = 0
                        bg.x -= pro.slidecount ** 2 * 0.2
                        if bg.x < -4000:
                            pro.x += bg.x + 4000
                            bg.x = -4001
                    else:
                        pro.x += pro.slidecount ** 2 * 0.2
                if obstaclehit():
                    if pro.facing:
                        pro.x = i[0][1]
                        bg.x = i[2][0]
                    else:
                        pro.x = i[0][0]  
                        bg.x = i[2][1]

                pro.slidecount -= 1

            else:
                pro.slide = False

        if pro.y < -500:
            takedamage(100)
            

        # UPDATING HEALTH BARS ...
        if pro.health != prev_health:
            if pro.health < 0:
                pro.health = 0
            prev_health = pro.health
            health.goto(-321 + (pro.health - 100) * 1.075, 273)
            health.shapesize(1, (100.1 - pro.health) * 0.1075)


        move(1)
        update()

# Character Control functions

def null():
    pass

def rightyes():
    global pro
    pro.rightstatus = True


def rightno():
    global pro
    pro.rightstatus = False


def leftyes():
    global pro
    pro.leftstatus = True


def leftno():
    global pro
    pro.leftstatus = False


def jumpyes():
    global pro
    pro.jumpstatus = True


def jumpno():
    global pro
    pro.jumpstatus = False


def atkyes():
    global pro
    if pro.y == ground_level:  
        if not(pro.atk or pro.stk or pro.stkstatus) and pro.killstate:
            pro.atkstatus = True
    elif not(pro.jmpatk or pro.dashstatus or pro.dash):
        if not (pro.freefall):
            pro.jmpatkstatus = True

def stkyes():
    global pro
    if pro.y == ground_level: 
        if not(pro.atk or pro.stk or pro.stkstatus) and pro.killstate:
            pro.stkstatus = True
    
def crouchyes():
    global pro
    if pro.y == ground_level and not (pro.atk or pro.stk or pro.atkstatus or pro.stkstatus or pro.slide or pro.slidestatus):
        pro.crouchstatus = True


def crouchno():
    global pro
    pro.crouchstatus = False


def slideyes():
    global pro
    if pro.y == ground_level and not (pro.atk or pro.stk or pro.atkstatus or pro.stkstatus or pro.slide or pro.slidestatus or (pro.crouchstatus and level == 3) or obstaclehit()) and pro.killstate:
        pro.slidestatus = True
    if pro.y != ground_level and not(pro.jmpatk or pro.jmpatkstatus or pro.dash or obstaclehit()) and pro.dashready:
        pro.dashstatus = True
        pro.dashready = False


def gamecontrols():
    onkeypress(rightyes, "Right")
    onkeyrelease(rightno, "Right")
    onkeypress(leftyes, "Left")
    onkeyrelease(leftno, "Left")
    onkeypress(jumpyes, "space")
    onkeyrelease(jumpno, "space")
    onkeypress(atkyes, "x")
    onkeypress(stkyes, "d")
    onkeypress(crouchyes, "a")
    onkeyrelease(crouchno, "a")
    onkeypress(slideyes, 'c')
    onkeypress(atkyes, "X")
    onkeypress(stkyes, "D")
    onkeypress(crouchyes, "A")
    onkeyrelease(crouchno, "A")
    onkeypress(slideyes, 'C')
    listen()


def stopcontrols():
    onkeypress(null, "Right")
    onkeyrelease(null, "Right")
    onkeypress(null, "Left")
    onkeyrelease(null, "Left")
    onkeypress(null, "space")
    onkeyrelease(null, "space")
    onkeypress(null, "x")
    onkeypress(null, "d")
    onkeypress(null, "a")
    onkeyrelease(null, "a")
    onkeypress(null, 'c')
    onkeypress(null, "X")
    onkeypress(null, "D")
    onkeypress(null, "A")
    onkeyrelease(null, "A")
    onkeypress(null, 'C')
    listen()

def menucontrols():
    onkeypress(nav_up, 'Up')
    onkeypress(nav_dn, 'Down')
    onkeypress(select, 'space')
    listen()


# Loading Functions 

def loadlevel(level):
    global ground_x , ground_y , ground_y2 , spikes , postuple , traplist , status ,count , game , obstacles , ground_level , ground_marker , the_level
    ground_x = getgroundx(level)
    ground_y = getgroundy(level)
    ground_y2 = getgroundy2(level)
    spikes = getspikes(level)
    postuple = getpostuple(level)
    obstacles = getobstacles(level)
    traplist = []
    game = True
    ground_marker = 1
    ground_level = 100
    if level == 3:
        ground_level = -300
    for i in knight:
        for j in i:
            win.addshape(j)
    if level == 3:
        for i in trollsr:
            for j in i:
                win.addshape(j)
    
    initialise_level(level)
    stopcontrols()
    gamecontrols()

    # Plays Mainloop and handles win and loss
    if level == 1:
        start = time()
        mainloop1()
        end = time()
        if result == 0:
            status = 'gameover'
            stopcontrols()
            win.clear()
            menucontrols()
            win.bgcolor("black")
            win.bgpic("Other Assets\\Final You Lose2.gif")
        elif result == 1:
            status = 'won'
            count = 0
            the_level = 2
            stopcontrols()
            win.clear()
            initialise_menu()
            menucontrols()
            win.bgcolor("black")
            win.bgpic("Other Assets\\You win.gif")
            arrow.goto(-100,-60)
            arrow.color("white")
            tim = round(end - start,2)
            arrow.write(str(tim) + ' s' , font = ("Comic Sans MS" , 50)  )
            arrow.goto(-200,-230)

            f = open("Highscores.csv" , 'r')
            r = list(csv.reader(f))
            f1 = open("tEMPORARY.csv" , 'w' , newline = '')
            w = csv.writer(f1)
            w.writerow(r[0])
            for i in r[1:]:
                if i[1] == profdetails['EMAIL']:
                    if i[2] == '' or float(i[2]) > tim :
                        w.writerow([i[0] , i[1] , tim , i[3] , i[4] ])
                    else:
                        w.writerow(i)
                else:
                    w.writerow(i)
            f.close()
            f1.close()
            os.remove("Highscores.csv")
            os.rename("tEMPORARY.csv" , "Highscores.csv")
            
            if profdetails['LEVEL'] < 4:
                profdetails['LEVEL'] += 1
            f = open("register.cm" , 'rb')
            f1 = open("temporary.cm" , 'wb')
            while True:
                try:
                    d = pickle.load(f)
                    if d['EMAIL'] == profdetails['EMAIL']:
                        if d['LEVEL'] < 3:
                            d['LEVEL'] += 1
                    pickle.dump(d , f1)
                except:
                    break
            f.close()
            f1.close()
            os.remove("register.cm")
            os.rename("temporary.cm","register.cm")

    elif level == 2:
        start = time()
        mainloop2()
        end = time()
        initialise_menu()
        if result == 0:
            status = 'gameover'
            win.clear()
            stopcontrols()
            win.clear()
            menucontrols()
            win.bgcolor("black")
            win.bgpic("Other Assets\\Final You Lose2.gif")
        elif result == 1:
            status = 'won'
            count = 0
            the_level = 3
            stopcontrols()
            win.clear()
            initialise_menu()
            menucontrols()
            win.bgcolor("black")
            win.bgpic("Other Assets\\You win.gif")
            arrow.goto(-100,-60)
            arrow.color("white")
            tim = round(end - start,2)
            arrow.write(str(tim) + ' s' , font = ("Comic Sans MS" , 50)  )
            arrow.goto(-200,-230)

            f = open("Highscores.csv" , 'r')
            r = list(csv.reader(f))
            f1 = open("tEMPORARY.csv" , 'w' , newline = '')
            w = csv.writer(f1)
            w.writerow(r[0])
            for i in r[1:]:
                if i[1] == profdetails['EMAIL']:
                    if  i[4] == '' or float(i[3]) > tim:
                        w.writerow([i[0] , i[1] , i[2] , tim , i[4] ])
                    else:
                        w.writerow(i)
                else:
                    w.writerow(i)
            f.close()
            f1.close()
            os.remove("Highscores.csv")
            os.rename("tEMPORARY.csv" , "Highscores.csv")

            if profdetails['LEVEL'] < 4:
                profdetails['LEVEL'] += 1
            f = open("register.cm" , 'rb')
            f1 = open("temporary.cm" , 'wb')
            while True:
                try:
                    d = pickle.load(f)
                    if d['EMAIL'] == profdetails['EMAIL']:
                        if d['LEVEL'] < 3:
                            d['LEVEL'] += 1
                    pickle.dump(d , f1)
                except:
                    break
            f.close()
            f1.close()
            os.remove("register.cm")
            os.rename("temporary.cm","register.cm")
    elif level == 3:
        start = time()
        mainloop3()
        end = time()
        initialise_menu()
        if result == 0:
            status = 'gameover'
            count = 0
            win.clear()
            stopcontrols()
            win.clear()
            menucontrols()
            win.bgcolor("black")
            win.bgpic("Other Assets\\Final You Lose2.gif")
        elif result == 1:
            status = 'won'
            the_level = 4
            stopcontrols()
            win.clear()
            initialise_menu()
            menucontrols()
            win.bgcolor("black")
            win.bgpic("Other Assets\\You win.gif")
            arrow.goto(-100,-60)
            arrow.color("white")
            tim = round(end - start,2)
            arrow.write(str(tim) + ' s' , font = ("Comic Sans MS" , 50)  )
            arrow.goto(-200,-230)

            f = open("Highscores.csv" , 'r')
            r = list(csv.reader(f))
            f1 = open("tEMPORARY.csv" , 'w',newline = '')
            w = csv.writer(f1)
            w.writerow(r[0])
            for i in r[1:]:
                if i[1] == profdetails['EMAIL']:
                    if i[4] == '' or float(i[4]) > tim :
                        w.writerow([i[0] , i[1] , i[2] , i[3] , tim ])
                    else:
                        w.writerow(i)
                else:
                    w.writerow(i)
            f.close()
            f1.close()
            os.remove("Highscores.csv")
            os.rename("tEMPORARY.csv" , "Highscores.csv")
        
            if profdetails['LEVEL'] < 4:
                profdetails['LEVEL'] += 1
            f = open("register.cm" , 'rb')
            f1 = open("temporary.cm" , 'wb')
            while True:
                try:
                    d = pickle.load(f)
                    if d['EMAIL'] == profdetails['EMAIL']:
                        if d['LEVEL'] < 3:
                            d['LEVEL'] += 1
                    pickle.dump(d , f1)
                except:
                    break
            f.close()
            f1.close()
            os.remove("register.cm")
            os.rename("temporary.cm","register.cm")

def credits():
    global status , win
    status = 'credits'
    win = Screen()
    win.setup(height = 1.0,width = 1.0)
    win.clear()
    win.bgcolor("black")
    stopcontrols()
    menucontrols()
    for i in ('Other Assets\\load 1.gif' , 'Other Assets\\load2.gif' , 'Other Assets\\load3.gif'):
        win.addshape(i)
    # The Load Turtle
    load = Turtle()
    load.shape("Other Assets\\load 1.gif")

    # Playing BG music
    winsound.PlaySound("Other Assets\\audio.wav", winsound.SND_ASYNC | winsound.SND_ALIAS)

    win.addshape("Other Assets\\making of cm.gif")
    win.addshape("Other Assets\\creditsprotaganists.gif")
    win.addshape("Other Assets\\creditsvillans.gif")
    win.addshape("Other Assets\\creditsbackgrounds.gif")

    # setting up turtles
    c = Turtle(visible=False)
    c.pu()
    r = Turtle(visible=False)
    r.pu()
    y = Turtle(visible=False)
    y.pu()
    p = Turtle(visible=False)
    p.pu()
    t = Turtle(visible=False)
    t.pu()
    i = Turtle(visible=False)
    i.pu()
    m = Turtle(visible=False)
    m.pu()
    o = Turtle(visible=False)
    o.pu()
    r2 = Turtle(visible=False)
    r2.pu()
    r3 = Turtle(visible=False)
    r3.pu()
    r4 = Turtle(visible=False)
    r4.pu()
    i2 = Turtle(visible=False)
    i2.pu()
    c2 = Turtle(visible=False)
    c2.pu()
    p11 = Turtle(visible=False)
    p11.pu()
    p11.color("white")
    p12 = Turtle(visible=False)
    p12.pu()
    p12.color("white")
    p13 = Turtle(visible=False)
    p13.pu()
    p13.color("white")
    p1 = Turtle(visible=False)
    p1.pu()
    p1.speed(0)
    p2 = Turtle(visible=False)
    p2.pu()
    p2.speed(0)
    p3 = Turtle(visible=False)
    p3.pu()
    p3.speed(0)
    p4 = Turtle(visible=False)
    p4.pu()
    p4.speed(0)
    p5 = Turtle(visible=False)
    p5.pu()
    p5.speed(0)
    p6 = Turtle(visible=False)
    p6.pu()
    p6.speed(0)
    p7 = Turtle(visible=False)
    p7.pu()
    p7.speed(0)
    p8 = Turtle(visible=False)
    p8.pu()
    p8.speed(0)
    p1.color("red")
    p2.color("red")
    p3.color("red")
    p4.color("red")
    p5.color("red")
    p6.color("red")
    p7.color("red")
    p8.color("red")
    p1.goto(-25, 160)
    p1.setheading(0)
    p2.goto(-25, 160)
    p2.setheading(180)
    p3.goto(-25, 170)
    p3.setheading(0)
    p4.goto(-25, 170)
    p4.setheading(180)
    p5.goto(210, 0)
    p5.setheading(270)
    p6.goto(210, 0)
    p6.setheading(90)
    p7.goto(-250, 0)
    p7.setheading(90)
    p8.goto(-250, 0)
    p8.setheading(270)

    load.shape("Other Assets\\load2.gif")

    # Bigger letters
    # Y
    y_larger = Turtle()
    y_larger.hideturtle()
    y_larger.pu()
    larger_y = PhotoImage(file="Other Assets\\Y.gif").zoom(3, 3)
    win.addshape("larger_y", Shape("image", larger_y))
    y_larger.shape("larger_y")
    # P
    p_larger1 = Turtle()
    p_larger2 = Turtle()
    p_larger1.hideturtle()
    p_larger2.hideturtle()
    p_larger1.pu()
    p_larger2.pu()
    larger_p = PhotoImage(file="Other Assets\\P.gif").zoom(2, 2)
    win.addshape("larger_p", Shape("image", larger_p))
    p_larger1.shape("larger_p")
    p_larger2.shape("larger_p")
    # T
    t_larger = Turtle()
    t_larger.hideturtle()
    t_larger.pu()
    larger_t = PhotoImage(file="Other Assets\\T.gif").zoom(2, 2)
    win.addshape("larger_t", Shape("image", larger_t))
    t_larger.shape("larger_t")
    # R
    r_larger = Turtle()
    r_larger.hideturtle()
    r_larger.pu()
    larger_r = PhotoImage(file="Other Assets\\R.gif").zoom(2, 2)
    win.addshape("larger_r", Shape("image", larger_r))
    r_larger.shape("larger_r")

    # Here starts the animation
    y_larger.goto(-500, 200)
    p_larger1.goto(-850, 0)
    t_larger.goto(700, 0)
    r_larger.goto(-575, 600)
    y_larger.speed(0)
    p_larger1.speed(0)
    r_larger.speed(0)
    t_larger.speed(0)
    y_larger.setheading(270)
    p_larger1.setheading(0)
    t_larger.setheading(180)
    r_larger.setheading(270)
    p_larger2.goto(575, -600)
    p_larger2.setheading(90)

    # Setting small sizes for letters
    load.shape("Other Assets\\load3.gif")
    # C
    smaller_c = PhotoImage(file="Other Assets\\C.gif").subsample(5, 5)
    win.addshape("smaller_c", Shape("image", smaller_c))
    c.shape("smaller_c")
    c2.shape("smaller_c")

    # R
    smaller_r = PhotoImage(file="Other Assets\\R.gif").subsample(6, 6)
    win.addshape("smaller_r", Shape("image", smaller_r))
    r.shape("smaller_r")
    r2.shape("smaller_r")
    r3.shape("smaller_r")
    r4.shape("smaller_r")

    # Y
    smaller_y = PhotoImage(file="Other Assets\\Y.gif").subsample(6, 6)
    win.addshape("smaller_y", Shape("image", smaller_y))
    y.shape("smaller_y")

    # P
    smaller_p = PhotoImage(file="Other Assets\\P.gif").subsample(6, 6)
    win.addshape("smaller_p", Shape("image", smaller_p))
    p.shape("smaller_p")

    # T
    smaller_t = PhotoImage(file="Other Assets\\T.gif").subsample(6, 6)
    win.addshape("smaller_t", Shape("image", smaller_t))
    t.shape("smaller_t")

    # I
    smaller_i = PhotoImage(file="Other Assets\\I.gif").subsample(6, 6)
    win.addshape("smaller_i", Shape("image", smaller_i))
    i.shape("smaller_i")
    i2.shape("smaller_i")

    # M
    smaller_m = PhotoImage(file="Other Assets\\M.gif").subsample(6, 6)
    win.addshape("smaller_m", Shape("image", smaller_m))
    m.shape("smaller_m")

    # O
    smaller_o = PhotoImage(file="Other Assets\\O.gif").subsample(6, 6)
    win.addshape("smaller_o", Shape("image", smaller_o))
    o.shape("smaller_o")

    load.hideturtle()

    p11.goto(-300, 0)
    p11.write("A  S.R.M Original ", False, font=("Bookman Old Style", 50))

    # Small letter placing
    c.goto(-745, 100)
    c.setheading(0)
    c.speed(0)
    i.goto(132, 90)
    i.setheading(270)
    i.speed(0)
    c2.goto(735, 95)
    c2.setheading(180)
    c2.speed(0)
    m.goto(-715, 0)
    m.setheading(0)
    m.speed(0)
    r.goto(-175, 90)
    r.setheading(270)
    r.speed(0)
    r2.goto(-70, -415)
    r2.setheading(90)
    r2.speed(0)
    o.goto(90, -415)
    o.setheading(90)
    o.speed(0)
    i2.goto(-140, -2)
    i2.setheading(90)
    i2.speed(0)
    r4.goto(725, -2)
    r4.setheading(180)
    r4.speed(0)
    y.goto(-95, 415)
    y.setheading(270)
    y.speed(0)
    r3.goto(10, -2)
    r3.setheading(90)
    r3.speed(0)
    p.goto(-15, 415)
    p.setheading(270)
    p.speed(0)
    t.goto(65, 435)
    t.setheading(270)
    t.speed(0)

    p11.clear()

    # y animation
    p11.goto(0, -350)
    y_larger.showturtle()

    # Displays names of creators in random order. 
    name_list = ['Vighnesh', 'Charu','Harshika','Sivasri']
    name = ''
    for x in range(4):
        name += name_list.pop(random.randint(0, len(name_list) - 1)) + '\n' + '    ' * (x + 1)

    for x in range(150):
        if x == 25:
            p11.write(name, font=("Tekton Pro", 60,"bold","italic"))

        elif x == 125:
            p11.clear()
        y_larger.fd(2)
    y_larger.hideturtle()

    # p & t animation
    p11.goto(-300, -250)
    p12.goto(-150, -170)
    t_larger.showturtle()
    p_larger1.showturtle()
    for x in range(150):
        if x == 25:
            p12.write("Thank You", False, font=("Tekton Pro", 35,"bold"))
            p11.write("For Your Support", False, font=("Tekton Pro", 60, "bold", "italic"))  # select * from
        elif x == 125:
            p12.clear()
            p11.clear()
        p_larger1.fd(2)
        t_larger.fd(2)
    p_larger1.hideturtle()
    t_larger.hideturtle()

    # p & r animation
    p12.goto(0, 270)
    p11.goto(100, 200)
    p13.goto(-500, -250)
    p_larger2.showturtle()
    r_larger.showturtle()
    for x in range(150):
        if x == 25:
            p12.write("Process is Always Harder ", False, font=("Tekton Pro", 35,"italic"))
            p11.write("Than the results", False, font=("Tekton Pro", 50, "bold", "italic"))
        elif x == 125:
            p11.clear()
            p12.clear()
            p13.clear()
        p_larger2.fd(2)
        r_larger.fd(2)
    p_larger2.hideturtle()
    r_larger.hideturtle()

    # Final title animation
    sleep(1)
    i.showturtle()
    sleep(1)
    p.showturtle()
    c.showturtle()
    c2.showturtle()
    r.showturtle()
    sleep(1)
    t.showturtle()
    m.showturtle()
    o.showturtle()
    r3.showturtle()
    sleep(1)
    r2.showturtle()
    r4.showturtle()
    y.showturtle()
    i2.showturtle()
    sleep(1)


    for _ in range(132):
        y.fd(2.441)
        o.fd(3.101)
        c.fd(3.641)
        c2.fd(4.001)
        m.fd(3.881)
        r4.fd(4.181)
        if _ > 17:
            p.fd(2.82)
            t.fd(3)
            r2.fd(3.58)
    r2.fd(3.58)
    p1.pd()  
    p2.pd()
    p3.pd()
    p4.pd()
    p5.pd()
    p6.pd()
    p7.pd()
    p8.pd()

    for x in range(100):
        p1.fd(3)
        p2.fd(3)
        p3.fd(3)
        p4.fd(3)
        if x >= 86 and x < 88:
            p5.fd(2.5)
            p6.fd(2.5)
            p7.fd(2.5)
            p8.fd(2.5)
        elif x == 88:
            p5.setheading(0)
            p6.setheading(0)
            p7.setheading(180)
            p8.setheading(180)
        elif x > 88:
            p5.fd(3)
            p6.fd(3)
            p7.fd(3)
            p8.fd(3)
    p1.setheading(90)
    p2.setheading(90)
    p3.setheading(270)
    p4.setheading(270)
    p5.setheading(90)
    p6.setheading(270)
    p7.setheading(270)
    p8.setheading(90)

    for x in range(5):
        p1.fd(2)
        p2.fd(2)
        p3.fd(2)
        p4.fd(2)
        p5.fd(2)
        p6.fd(2)
        p7.fd(2)
        p8.fd(2)

    sleep(14)

    
    p1.clear()
    p2.clear()
    p3.clear()
    p4.clear()
    p5.clear()
    p6.clear()
    p7.clear()
    p8.clear()
    c.hideturtle()
    r.hideturtle()
    y.hideturtle()
    p.hideturtle()
    t.hideturtle()
    i.hideturtle()
    c2.hideturtle()
    m.hideturtle()
    i2.hideturtle()
    r2.hideturtle()
    r3.hideturtle()
    o.hideturtle()
    r4.hideturtle()

    p11.goto(-400, 30)
    for i in 'IT IS MORE THAN A GAME.':
        p11.write(i, True, font=("Tekton Pro", 50))
        winsound.PlaySound("Other Assets\\type.wav", winsound.SND_ASYNC | winsound.SND_ALIAS)

        sleep(.25)
    sleep(.25)
    p11.clear()

    

    p1.shape("Other Assets\\making of cm.gif")
    p1.st()
    p1.pu()
    p1.goto(0, 0)
    sleep(5)
    p1.shape("Other Assets\\creditsbackgrounds.gif")
    sleep(7)
    p1.shape("Other Assets\\creditsvillans.gif")
    sleep(7)
    p1.shape("Other Assets\\creditsprotaganists.gif")
    sleep(7)
    p1.hideturtle()
    mainmenu()

def playcutscene(level):
    global arrow
    arrow.clear()
    if level == 1:
        cutscene1()
    elif level == 2:
        cutscene2()
    elif level == 3:
        cutscene3()
    elif level == 4:
        cutscene4()

def cutscene1():
    global status
    status = 'cutscene1'
    arrow.ht()
    win.bgpic('Other Assets\\cutscene1.png')

def cutscene2():
    global status
    status = 'cutscene2'
    arrow.ht()
    win.bgpic("Other Assets\\cutscene2.png")

def cutscene3():
    global status
    status = 'cutscene3'
    arrow.ht()
    win.bgpic("Other Assets\\cutscene4.png")

def cutscene4():
    global status
    status = 'cutscene4'
    arrow.ht()
    win.bgpic("Other Assets\\cutscene3.png")

# Menu Functions

# Quit Application
def quit():
    response = Mb.askyesno("CONFIRMATION" , "Are you sure you want to quit? Progress will be saved!")
    if response:
        bye()

# Function below is called when user presses space
def select():
    global profdetails , the_level , s
    if status == 'profselect':
        if count == 0:
            login()
        elif count == 1:
            createnew()
        elif count == 2:
            bye()
            scores()
        else:
            quit()
    elif status == 'mainmenu':
        if count == 0:
            play()
        elif count == 1:
            controls()
        elif count == 3:
            response = Mb.askokcancel("PERMISSION" , "Are you sure you want to delete your account? All progress will be lost!")
            if response:
                f = open('register.cm', 'rb')
                f1 = open('temp.txt', 'wb')
                while True:
                    try:
                        d = pickle.load(f)
                        if d != profdetails:
                            pickle.dump(d, f1)
                    except:
                        break
                f.close()
                f1.close()
                os.remove('register.cm')
                os.rename('temp.txt', 'register.cm')
                
                f = open("Highscores.csv" , 'r')
                r = list(csv.reader(f))
                f1 = open("tEMPORARY.csv" , 'w' , newline = '')
                w = csv.writer(f1)
                w.writerow(r[0])
                for i in r[1:]:
                    if i[1] != profdetails['EMAIL']:
                        w.writerow(i)
                f.close()
                f1.close()
                os.remove("Highscores.csv")
                os.rename("tEMPORARY.csv" , "Highscores.csv")
                profdetails = {'EMAIL' : None , 'USERNAME': None, 'PASSWORD': None , 'LEVEL' : None}
                profileselection()

        elif count == 2:
            profdetails = {'EMAIL' : None , 'USERNAME': None, 'PASSWORD': None , 'LEVEL' : None}
            profileselection()
        elif count == 4: # CREDITS
            credits()
        else:
            quit()
    elif status == 'lvlselect':
        if count < 3:
            if count + 1 <= profdetails['LEVEL']:
                if count == 2:
                    playcutscene(4)
                else:
                    playcutscene(count + 1)
            else:
                Mb.showerror("LOAD ERROR" , "Progress Insufficient")
        else:
            mainmenu()
    elif status[0:8] == 'cutscene':
        if status == 'cutscene4':
            playcutscene(3)
        else:
            win.clear()
            win.bgcolor("black")
            t = Turtle(visible = False)
            t.color("red")
            t.pu()
            t.speed(0)
            t.goto(-250 , -100)
            t.write("LOADING ..." , move = False ,font = ("Comic Sans MS" , 75) )
            loadlevel(int(status[-1]))
    elif status == 'gameover':
        mainmenu()
    elif status == 'won':
        if count == 0:
            if the_level == 4:
                Mb.showwarning("ALERT","ALL LEVELS COMPLETED !!!")
            elif the_level == 3:
                playcutscene(4)
            else:
                playcutscene(the_level)
        elif count == 1:
            if profdetails['LEVEL'] == 4:
                profdetails['LEVEL'] = 3
            if the_level == 4:
                the_level = 3
            mainmenu()

    elif status == 'controls':
        mainmenu()
    elif status == 'credits':
        win.bye()
        winsound.PlaySound(None,winsound.SND_PURGE)
        mainmenu()

# Called when uses presses arrow keys
def navigate(factor):
    global count
    total = menudict[status][0]
    if count + factor > total - 1:
        count = 0
    elif count + factor < 0:
        count = total - 1
    else:
        count += factor
    arrow.goto(arrow.xcor(), menudict[status][1] - (menudict[status][2] * count))

# Screen for login or signup page
def profileselection():
    global status, count
    initialise_screen()
    initialise_menu()
    stopcontrols()
    menucontrols()
    arrow.goto(-20, -85)
    count = 0
    status = 'profselect'
    win.bgpic("Other Assets\\Final Main Menu.png")

# Screen for game main menu
def mainmenu():
    global status, count
    initialise_screen()
    win.clear()
    win.bgcolor("black")
    initialise_menu()
    stopcontrols()
    menucontrols()
    arrow.goto(-50 , 40)
    count = 0
    status = "mainmenu"
    win.bgpic("Other Assets\\Final Game Menu.png")

# Selecting Level
def play():
    global status , count
    count = 0
    status = 'lvlselect'
    arrow.goto(20 , 225)
    win.bgpic("Other Assets\\level selector.gif")

# Showing Player Controls
def controls():
    global status
    status = 'controls'
    arrow.ht()
    arrow.goto(400 , -310)
    win.bgpic("Other Assets\\cutscene6.png")

# Login Page Conformation
def newlogin():
    global new_user, new_password, profdetails, new
    user_id = new_user.get().strip()
    password = new_password.get().strip()
    f = open("register.cm", 'rb')
    while True:
        try:
            d = pickle.load(f)
            if d['EMAIL'] == user_id:
                if d['PASSWORD'] == password:
                    profdetails = d
                    response = Mb.showinfo("INFO","Login Successful")
                    new.destroy()
                    mainmenu()
                    break
                else:
                    Mb.showerror("LOGIN ERROR","Password Incorrect")
                    new.after(1, lambda: new.focus_force())
                    break
        except:
            Mb.showwarning("LOGIN ALERT","User Not Found")
            break
    f.close()
    

def destroynew():
    global new
    new.destroy()
    profileselection()

def destroyroot():
    global root
    root.destroy()
    profileselection()

# Login Page
def login():
    global new_user, new_password , new , win
    win.bye()
    new = Tk()
    new.title("new user window")
    new.geometry("2000x2000")
    canvas = Canvas(new, borderwidth=1, relief='raised', width=2000, height=2000)
    canvas.place(x = 0, y = 0)

    my_image = PhotoImage(file="Other Assets\\LOGIN Final.png")
    canvas.create_image(0, 0, anchor=NW, image=my_image)
    new["bg"] = "black"
    new_user = Entry(new,bg="white", fg="black", font=("Comic Sans MS", 20))
    new_user.place(x=625, y=375)
    new_password = Entry(new, bg="white", fg="black", font=("Comic Sans MS", 20), show="*")
    new_password.place(x=625, y=475)
    cre = Button(new, text="LOGIN", font=("Comic Sans MS", 30 , 'bold'), bg="black", fg="red", command=newlogin)
    cre.place(x=650, y=575)
    fp = Button(new, text="FORGOT PASSWORD", font=("Comic Sans MS", 15 , 'bold'), bg="black", fg="red", command=forgotpassword)
    fp.place(x=625, y=700)
    back = Button(new, text="BACK", font=("Comic Sans MS", 20 , 'bold'), bg="black", fg="red", command=destroynew)
    back.place(x=1200, y=700)
    new.after(1, lambda: new.focus_force())
    new_user.focus_set()
    new.mainloop()

# Forgot Password Page
def forgotpassword():
    global root , email_id , new
    new.destroy()
    root = Tk()
    root.title("Forgot Password")
    root['bg'] = 'black'
    root.geometry("2000x2000")
    em = Label(root, text="FORGOT PASSWORD", bg="black", fg="white", font=("Comic Sans MS", 40))
    em.place(x=450, y=100)
    email_label = Label(root, text="ENTER EMAIL ID ", bg="black", fg="red", font=("Comic Sans MS", 20))
    email_label.place(x=400, y=350)
    email_id = Entry(root,bg="white", fg="black", font=("Comic Sans MS", 20))
    email_id.place(x=725, y=350)
    sub = Button(root, text="SUBMIT", font=("Comic Sans MS", 30 , 'bold'), bg="black", fg="red", command=fpsubmit)
    sub.place(x=650, y=650)
    back = Button(root, text="BACK", font=("Comic Sans MS", 20 , 'bold'), bg="black", fg="red", command=destroyroot)
    back.place(x=1200, y=700)
    root.after(1, lambda: root.focus_force())
    email_id.focus_set()
    root.mainloop()

# Forgot password Confirmation
def fpsubmit():
    global root , email_id
    userid = email_id.get().strip()
    f = open("register.cm" , 'rb')
    while True:
        try:
            d = pickle.load(f)
            if d['EMAIL'] == userid.lower():
                try:
                    f1 = open("CMS.cm" , 'rb')
                    d1 = pickle.load(f1)
                    f1.close()
                    l = 'ntalddbsuiwqknof'
                    ForgotPassword.MailNow(d['EMAIL'],d['USERNAME'],l , d['PASSWORD'])
                    
                except:
                    Mb.showerror("EMAIL ERROR" , "There seems to be a problem in sending an email. Check your email adress or try again later.")
                    break
                Mb.showinfo("PASSWORD RESET" , "Your Password has been sent to the given email id !!")
                root.destroy()
                profileselection()
                break
        except:
            Mb.showerror("ERROR" , "User Not Found")
            root.after(1, lambda: root.focus_force())
            
            break
    f.close()

# Signup Page Confirmation
def newuser():
    global new_user, new_password, new , new_username
    user_name = new_username.get().strip()
    user_id = new_user.get().strip()
    password = new_password.get().strip()
    f = open("register.cm" , 'rb')
    ok = 'ok'
    if not(user_id and user_name):
        ok = 'not ok'
    while True:
        try:
            d = pickle.load(f)
            if d['EMAIL'].lower() == user_id.lower():
                ok = 'not ok'
                break
        except:
            break
    if ok == 'ok':

        f = open('register.cm', 'ab')
        d = {}
        d['EMAIL'] = user_id.lower()
        d['USERNAME'] = user_name
        d['PASSWORD'] = password
        d['LEVEL'] = 1
        pickle.dump(d, f)
        f.close()

        f = open("Highscores.csv" , 'r')
        f1 = open("tEMPORARY.csv" , 'w' , newline = '')
        w = csv.writer(f1)
        r = list(csv.reader(f))
        for i in r:
            w.writerow(i)   
        w.writerow([d['USERNAME'] , d['EMAIL'] , None , None , None])
        f.close()
        f1.close()
        os.remove("Highscores.csv")
        os.rename("tEMPORARY.csv" , "Highscores.csv")

        Mb.showinfo("USER CREATED" , "Your account has successfully been created in THE CRYPTIC MIRROR's servers.")
        new.destroy()
        profileselection()

    else:
        if not(user_id and user_name):
            Mb.showerror("USER ERROR" , "All Fields are mandatory !!")
        else:
            Mb.showerror("USER ERROR" , "Account Already Exists !!")

# Signup Page
def createnew():
    global new_user, new_password, new , win , new_username
    win.bye()
    new = Tk()

    new.title("new user window")
    new.geometry("2000x2000")
    canvas = Canvas(new, borderwidth=1, relief='raised', width=2000, height=2000)
    canvas.place(x = 0, y = 0)

    my_image = PhotoImage(file="Other Assets\\CREATE FINAL.png")
    canvas.create_image(0, 0, anchor=NW, image=my_image)
    new["bg"] = "black"
    new_username = Entry(new, bg="white", fg="black", font=("Comic Sans MS", 20))
    new_username.place(x=775, y=300)
    new_user = Entry(new, bg="white", fg="black", font=("Comic Sans MS", 20))
    new_user.place(x=775, y=375)
    new_password = Entry(new, fg="black", bg="white", font=("Comic Sans MS", 20), show="*")
    new_password.place(x=775, y=450)
    cre = Button(new, text="CREATE USER", font=("Comic Sans MS", 30 , 'bold'), fg="red", bg="black", command=newuser)
    cre.place(x=650, y=650)
    back = Button(new, text="BACK", font=("Comic Sans MS", 20 , 'bold'), fg="red", bg="black", command=destroynew)
    back.place(x=1200, y=700)
    new.after(1, lambda: new.focus_force())
    new_username.focus_set()
    new.mainloop()

# Printing Highscores
def scores():
    global root
    try:
        root.destroy()
    except:
        pass
    f = open("Highscores.csv" , 'r')
    r = list(csv.reader(f))
    f.close()
    root = Tk()
    root.geometry("800x400+400+200")
    root['bg'] = 'black'
    root.title("Highscores")

    style = ttk.Style()
    style.configure("Treeview")
    style.theme_use("clam")
    if len(r) %2:
        color = "grey"
    else:
        color = 'silver'
    style.configure("Treeview" , font = "Consolas" , background = "silver" ,foreground = "red" , rowheight = '35', fieldbackground = color )
    style.map("Treeview" , background = [('selected' , 'black')])
    style.configure("Horizontal.TScrollbar" , background = "grey" , foreground = "black")

    frame = Frame(root , background = "black")
    

    scrollbar = Scrollbar(frame)
    scrollbar.pack(side = RIGHT , fill = Y)
    scrollbar2 = Scrollbar(frame , orient = 'horizontal')
    scrollbar2.pack(side = BOTTOM , fill = X)


    tree = ttk.Treeview(frame , height = 5 , yscrollcommand = scrollbar.set ,xscrollcommand = scrollbar2.set ,  selectmode = 'browse')
    tree['columns'] = ("Name" , "Email ID" , "Highscore1" , "Highscore2" , "Highscore3")

    scrollbar.config(command = tree.yview)
    scrollbar2.config(command = tree.xview)


    tree.column("#0" , width = 0 , minwidth = 0)
    tree.column("Name" , anchor = CENTER , width = 120 , minwidth = 120)
    tree.column("Email ID" , anchor = CENTER , width = 300 , minwidth = 300)
    tree.column("Highscore1" , anchor = CENTER , width = 120 , minwidth = 120)
    tree.column("Highscore2" , anchor = CENTER , width = 120 , minwidth = 120)
    tree.column("Highscore3" , anchor = CENTER , width = 120 , minwidth = 120)

    tree.heading("Name" , text = "Username" , anchor = CENTER)
    tree.heading("Email ID" , text = "Email ID" , anchor = CENTER)
    tree.heading("Highscore1" , text = "Journey of Curiosity" , anchor = CENTER)
    tree.heading("Highscore2" , text = "Path to Eternity" , anchor = CENTER)
    tree.heading("Highscore3" , text = "Test of Destiny" , anchor = CENTER)

    tree.tag_configure("oddrow" ,background =  'grey')
    tree.tag_configure("evenrow" ,background =  'silver')


    
    for i in r[1:]:
        if i[2] == '':
            _2 = '-'
        else:
            _2 = str(i[2])+' s' 
        if i[3] == '':
            _3 = '-'
        else:
            _3 = str(i[3])+' s' 
        if i[4] == '':
            _4 = '-'
        else:
            _4 = str(i[4])+' s' 
        if r.index(i) % 2:
            color = 'oddrow'
        else:
            color = 'evenrow'

        tree.insert(parent = '' ,index = 'end' , iid = r.index(i) , text = '', values = (i[0],i[1] ,_2 , _3,_4 ) , tags = (color,))

    lab = Label(root, text="HIGHSCORES", bg="black", fg="red", font=("Comic Sans MS", 20 , "bold"))
    lab.pack()
    tree.pack()
    frame.pack(pady = 10 )
    quitb = Button(root, text="EXIT", font=("Comic Sans MS", 20 , 'bold'), bg="black", fg="red", command=destroyroot)
    quitb.pack(pady = 20)
    root.after(1, lambda: root.focus_force())
    quitb.focus_set()
    root.mainloop()

def nav_up():
    navigate(-1)


def nav_dn():
    navigate(1)

#---------------------------------------------------------------------------------------------------------
#---------------------------------- Setting Up required Objects for each level ----------------------------

def initialise_level(level):
    global pro , bg , bg1 , health , prev_health , ts , thealth , spike
    pro = Turtle()
    pro.up()
    pro.speed(0)
    pro.goto(-200, ground_level)
    pro.vel = 15
    pro.x = -200 
    pro.y = ground_level  
    pro.facing = 0
    pro.idle = True
    pro.right = False
    pro.left = False
    pro.isjump = False
    pro.freefall = False
    pro.atk = False
    pro.jmpatk = False
    pro.stk = False
    pro.rightstatus = False
    pro.leftstatus = False
    pro.jumpstatus = False
    pro.atkstatus = False
    pro.jmpatkstatus = False
    pro.stkstatus = False
    pro.jumpcount = 8
    pro.fallcount = 1
    pro.atkcount = 0
    pro.jmpatkcount = 0
    pro.stkcount = 0
    pro.runcount = 0
    pro.idlecount = 0
    pro.killstate = True
    pro.dash = False
    pro.dashstatus = False
    pro.dashcount = 8
    pro.dashready = True
    pro.crouchstatus = False
    pro.slide = False
    pro.slidestatus = False
    pro.health = 100
    pro.recoil = False
    pro.blinkcount = 0
    pro.canattack = True

    

    if level == 3:
        # TROLL SR. turtle
        ts = Turtle()
        ts.up()
        ts.speed(0)
        ts.x = 500
        ts.y = ground_level + 165
        ts.state = 0  # 1= jump on top ,2= attack ,3= walk, 4= spl attack
        ts.walkcount = 0
        ts.attackcount = 0
        ts.jumpcount = 0
        ts.refresh_rate = 1
        ts.mad_attk_count = 0
        ts.mad_repeat = 0
        ts.stuck_count = 0
        ts.health = 100
        ts.blinkcount = 0
        ts.attackcan = True


    
    if level == 1:
        bg1 = Turtle()
        bg1.shape('Knight\\lvl 1 backdrop.gif')
        bg1.up()
        bg1.speed(0)
        
    bg = Turtle()
    bg.up()
    bg.speed(0)
    bg.x = 5398  
    bg.y = 100
    if level == 1:
        bg.shape("Knight\\Practice level tilemap.gif")
        prev_health = 100
    elif level == 2:
        bg.shape("Knight\\Trap lvl tile map.gif")
        prev_health = 100

        for i in range(len(postuple)):
            trap = Turtle()
            trap.shape('Knight\\chakra.gif')
            trap.speed(0)
            trap.up()

            trap.Sp = postuple[i][0]
            trap.Ep = postuple[i][1]
            trap.counter = 1
            trap.x = trap.Sp[0]
            trap.y = trap.Sp[1]
            if i != 3:
                trap.speed = 25
            else:
                trap.speed = 50
            trap.goto(trap.x + bg.x , trap.y)
            traplist.append(trap)

    elif level == 3:
        bg.shape("Knight\\Troll Level Map.gif")
        bg.goto(0,40)

        # Troll health
        thealth = Turtle(shape="Knight\\troll unit icon.gif", visible=False)
        thealth.pu()
        thealth.speed(0)
        thealth.goto(490, 280)
        thealth.stamp()
        thealth.shape("square")
        thealth.goto(417, 273)
        thealth.resizemode("user")
        thealth.shapesize(1, 10.8)
        thealth.color('darkorange')
        thealth.stamp()
        thealth.color('dimgrey')
        thealth.shapesize(1, 0.001)
        thealth.goto(312, 273)
        thealth.showturtle()

        prev_health = [100, 100]

        # Spike Turtle
        spike = Turtle(shape='Knight\\spike ball.gif')
        spike.pu()
        spike.speed(0)
        spike.goto(0, 560)
        spike.y = 560
        spike.x = 0
        


    
    


    health = Turtle(shape="Knight\\Pro health copy.gif", visible=False)
    health.speed(0)
    health.pu()
    health.goto(-490, 280)
    health.stamp()
    health.shape('square')
    health.goto(-430, 272)
    health.resizemode("user")
    health.shapesize(1, 10.8)
    health.color('lawngreen')
    health.stamp()
    health.color('dimgrey')
    health.shapesize(1, 0.001)
    health.goto(-319, 272)
    health.showturtle()




def initialise_menu():
    global arrow , win
    try:
        arrow.ht()
    except:
        pass
    ar = PhotoImage(file = "Other Assets\\Project Arrow.gif").subsample(4,4)
    win.addshape("arr", Shape("image", ar))
    arrow = Turtle()
    arrow.shape("arr")
    arrow.width(7)
    arrow.speed(0)
    arrow.pu()
    arrow.color("red")

def initialise_screen():
    global win   
    win = Screen()
    win.title("Cryptic Mirror")
    win.setup(height=850, width=1535)
    win.bgcolor("black")

profdetails = {'EMAIL' : None , 'USERNAME': None, 'PASSWORD': None , 'LEVEL' : None}

menudict = {'profselect': (4, -75 , 75), 'mainmenu': (6, 40 , 60) , 'lvlselect' : (4 , 225 , 165) , 'controls' : (1 , -310 , 0) , 
'cutscene1' : (1 , 0 , 0) , 'cutscene2' : (1 , 0 , 0) , 'cutscene3' : (1 , 0 , 0) , 'gameover' : (1 , 0 , 0) , 'won' : (2 , -230 , 85)}

menucontrols()

initialise_screen()
win.bgcolor("black")
nep = Turtle(visible = False)
nep.goto(-350,0)
nep.up()
nep.speed(0)
nep.color("red")
for i in "PLEASE WAIT WHILE WE ARE LOADING":
    nep.write(i ,align = "left", font = ("Consolas" , 30) , move = True)
    sleep(0.01)
for i in range(3):
    sleep(0.5)
    nep.write(" ." , align = 'left' , font = ("Consolas" , 30) , move = True)
sleep(0.5)
nep.clear()

profileselection()
win.mainloop()

