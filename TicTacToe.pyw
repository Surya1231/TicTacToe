from graphics import *
from random import *

win=GraphWin("Tic Tac Toe",400,400)
win.setCoords(0,0,200,200)
base=Rectangle(Point(0,200), Point(200,145))
base.setFill('cyan')
base.draw(win)
me=Text(Point(90,155),' O X')
me.draw(win)
player1='Player 1'
player2='Player 2'

def init():
    t=Text(Point(100,180),'Tic Tac Toe')
    t.setTextColor('blue')
    t.setSize(30)
    t.draw(win)

def init1(s1,s2,s3):
    r=Rectangle(Point(0,145),Point(200,0))
    r.setFill('white')
    r.draw(win)
    me.setSize(20)
    r1=Rectangle(Point(50,120),Point(150,100))
    r1.setFill('yellow')
    r1.setWidth(2)
    r1.draw(win)
    r2=r1.clone()
    r2.move(0,-30)
    r2.draw(win)
    r3=r1.clone()
    r3.move(0,-60)
    r3.draw(win) 
    s1=Text(Point(100,110),s1)
    s1.setTextColor('red')
    s1.setSize(16)
    s1.draw(win)
    s2=Text(Point(100,80),s2)
    s2.setTextColor('red')
    s2.setSize(16)
    s2.draw(win)
    s3=Text(Point(100,50),s3)
    s3.setTextColor('red')
    s3.setSize(16)
    s3.draw(win)
    r=0
    while r==0:
        p=win.getMouse()
        if 50<=p.getX()<=150:
            if 100<=p.getY()<=120:
                r=1
            if 70<=p.getY()<=90:
                r=2
            if 40<=p.getY()<=60:
                r=3
    r1.undraw()
    r2.undraw()
    s1.undraw()
    s2.undraw()
    r3.undraw()
    s3.undraw()
    return r

def board(n):
    r=Rectangle(Point(0,145),Point(200,0))
    r.setFill('yellow')
    r.draw(win)
    l1=Line(Point(70,5),Point(70,140))
    l1.setWidth(2)
    l2=l1.clone()
    l2.move(60,0)
    l3=Line(Point(10,50),Point(180,50))
    l3.setWidth(2)
    l4=l3.clone()
    l4.move(0,45)
    l1.draw(win)
    l2.draw(win)
    l3.draw(win)
    l4.draw(win)
    if n==0:
        r=Rectangle(Point(0,200),Point(200,0))
        r.setFill('white')
        r.draw(win)
        
def winner(a):
    if a[1]==a[2] and a[2]==a[3] and a[1]!=0:
        return 1
    elif a[4]==a[5] and a[4]==a[6] and a[4]!=0:
        return 1
    elif a[7]==a[8] and a[8]==a[9] and a[7]!=0:
        return 1
    elif a[1]==a[4] and a[4]==a[7] and a[1]!=0:
        return 1
    elif a[2]==a[8] and a[5]==a[8] and a[2]!=0:
        return 1
    elif a[3]==a[6] and a[6]==a[9] and a[3]!=0:
        return 1
    elif a[1]==a[5] and a[5]==a[9] and a[1]!=0:
        return 1
    elif a[3]==a[5] and a[5]==a[7] and a[3]!=0:
        return 1
    elif 0 not in a:
        return 2
    else:
        return 0

def winn(a,s):
    k=winner(a)
    if k==0:
        return 0
    else:
        w=Text(Point(100,72),s)
        w.setTextColor('blue')
        w.setSize(35)
        if k==2:
            w.setText("Draw")
        w.draw(win)
        return 1
      
def pos(x,y):
    v=1
    n=0
    if 95<=y<=140:
        y=118
        n=0
    elif 50<=y<=95:
        y=72
        n=3
    elif 5<=y<=50:
        y=27
        n=6
    else:
        v=0
        
    if 10<=x<=70:
        x=40
        n+=1
    elif 70<=x<=130:
        x=100
        n+=2
    elif 130<=x<=190:
        x=160
        n+=3
    else:
        v=0
    return [v,n,x,y]

def mouse(mark):
    if mark==1 or mark==2:
        return win.getMouse()
    else:
        x=randint(10,190)
        y=randint(5,145)
        return Point(x,y)

def chance(pl,ch,color,mark,a):
    v=0
    base.setFill(color)
    while v==0:
        me.setText(pl)
        p=mouse(mark)
        x,y=p.getX(),p.getY()
        b=pos(x,y)
        v,n,x,y=b[0],b[1],b[2],b[3]
        if a[n]!=0:
            v=0
        if v==1:
            zero=Text(Point(x,y),ch)
            zero.setTextColor(color)
            zero.setSize(30)
            zero.draw(win)
            a[n]=mark
        else:
            if mark==1 or mark ==0:
                me.setText('Invalide Move Click Me')
                win.getMouse()

def entry():
    global player2
    global player1
    r=Rectangle(Point(0,145),Point(200,0))
    r.setFill('white')
    r.draw(win)
    p1=Entry(Point(100,110),20)
    p1.setText(player1)
    p1.setFill('yellow')
    p2=p1.clone()
    p2.setText(player2)
    p2.move(0,-30)
    p2.draw(win)
    p1.draw(win)
    r1=Rectangle(Point(50,50),Point(150,30))
    r1.setFill('yellow')
    r1.setWidth(2)
    r1.draw(win)
    s1=Text(Point(100,40),'Done')
    s1.setTextColor('red')
    s1.setSize(16)
    s1.draw(win)
    while True:
        p=win.getMouse()
        if 50<=p.getX()<=150 and 30<=p.getY()<=50:
            break
    player1=p1.getText()
    player2=p2.getText()
    p1.undraw()
    p2.undraw()
    
def choose():
    global player2
    me.setText('Select the opponent')
    c=init1('Human','Easy Computer','AI')
    if c!=1:
        player2='Computer'
    entry()
    return c
       
def set1():
    c=choose()
    board(1)
    p1="Turn of "+player1+" O"
    p2="Turn of " + player2 +" X"
    p3=player1 +' Winner'
    p4=player2 +' Winner'
    a=[1]+[0]*9
    while True:
        chance(p1,'O','cyan',1,a)
        if winn(a,p3)==1:
            break
        if c==1:
            chance(p2,'X','red',2,a)
        elif c==2:
            chance(p2,'X','red',3,a)
        else:
            chance(p2,'X','red',4,a)
        if winn(a,p4)==1:
            break
    me.setText("Click Anywhere to Restart")
    win.getMouse()
    me.setText("O X")
    base.setFill('cyan')
    board(2)
    main()

def set2():
    me.setText('Click Anywhere to go back')
    c=Text(Point(100,100),'Suryaprakash Agarwal')
    c.setTextColor('orange')
    c.setSize(20)
    c.draw(win)
    win.getMouse()
    c.undraw()
    me.setText('O X')
    base.setFill('cyan')
    main()
    
def main():
    init()
    global player1
    global player2
    player1='player1'
    player2='player2'
    k=init1('START','CREDITS','EXIT')
    if k==1:
        set1()
    elif k==2:
        set2()
    else:
        win.close()

main()
