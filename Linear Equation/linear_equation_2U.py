from __future__ import division
import sys
#equation 1

x1,y1,c1=raw_input("Enter the co-eff x1 y1 c1..").split()
x1=float(x1)
y1=float(y1)
c1=float(c1)
eqn1=[x1,y1,c1]
#print eqn1

#equation 2


x2,y2,c2=raw_input("Enter the co-eff x2 y2 c2..").split()
x2=float(x2)
y2=float(y2)
c2=float(c2)
eqn2=[x2,y2,c2]

count = 0

if x1==0 or x2==0 or y1==0 or y2==0:

    if x1==0:
        y=eqn1[2]/eqn1[1]
        x=eqn2[2]-y
        
    elif x2==0:
        y=eqn2[2]/eqn2[1]
        x=eqn1[2]-y

    elif y1==0:
        x=eqn1[2]/eqn1[0]
        y=eqn2[2]-x
    else:
        x=eqn2[2]/eqn2[0]
        y=eqn1[2]-x

elif ((x1%x2==0 and y1%y2==0) or (x2%x1==0 and y2%y1==0)):
    slope1= -eqn1[0]/eqn1[1]
    slope2= -eqn2[0]/eqn2[1]
    
    if (x1/x2 == c1/c2 and y1/y2 == c1/c2):
      print "this problem has infinite solution"
      count=1

    elif slope1 != slope2:
    #solve x to get y
        eqn1= [i*x2 for i in eqn1]
        eqn2= [i*-x1 for i in eqn2]
        #print eqn1
        #print eqn2

        y=int(eqn1[1]+eqn2[1])
        c=int(eqn1[2]+eqn2[2])
        #print "value of y  & C ",y,c

        #finding the value of y
        y=c/y

        #finding the value of x
        x=(eqn1[2]-(eqn1[1]*y))/eqn1[0]

    else:
      print "this problem has no solution \n given equation is inconsistant"
      count=1

else:
    #solve x to get y
    eqn1= [i*x2 for i in eqn1]
    eqn2= [i*-x1 for i in eqn2]
    #print eqn1
    #print eqn2

    y=int(eqn1[1]+eqn2[1])
    c=int(eqn1[2]+eqn2[2])
    #print "value of y  & C ",y,c

    #finding the value of y
    y=c/y

    #finding the value of x
    x=(eqn1[2]-(eqn1[1]*y))/eqn1[0]

#result
if count == 0:
    print "The value of x and y are..",x,y
    
