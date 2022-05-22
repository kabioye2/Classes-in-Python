# week8.py

# function types
# 3 types of functions/methods

'''
Terminology:
    Functions not associated with specific type: abs,mas,len-do not have calling objects
    methods are functions defined inside a class: list.append, str.upper
1. function/methods that modifies/sets something. Does not return anything
    cannot use in assignment statement
    print
    list.append
    list.sort
2. function/method that returns/gets something
    can be used in assignement statement
    abs,max,len
    str.upper
    sorted

*pop does both: modifies list and returns item removed
'''

# Object-oriented programming

'''
    data/attributes-underlying data representing the object
    methods-code used to access/manipulate the attributes
'''
# Point class

'''
two versions:
    v1-all methods are explicit
    v2-adds magic/dunder methods that are called automatically
'''

#v1
class Point:

    # p.setx(4) -> Point.setx(p,4)
    def setx(self,xcoord): # self and p are the same. p is name outside class, self is name insode class
        self.x=xcoord

    def sety(self,ycoord):
        self.y=ycoord

    #p.get() -> Point.get(p)
    def get(self): #self is a convention
        return (self.x,self.y)

    def move(self,deltax,deltay):
        self.x=self.x+deltax
        self.y=self.y+deltay

#v2 - with magic/dunder (double underline)
# dunder methods run automatically
class Point:
    
    # p=Point() -> Point.__init__(p)
    def __init__(self,xcoord=0,ycoord=0):
        # initialize self!
        self.x=xcoord
        self.y=ycoord

    # __repr is called automatically when a str representation is needed
    def __repr__(self): # string representation
        return f"Point({self.x},{self.y})"
        #return "Point({},{})".format(self.x,self.y)

    # p==q -> Point.__eq__(p,q)
    def __eq__(self,other): # compares Xs and Ys boolean. Checks memory if not used
        if self.x==other.x and self.y==other.y: # two points are equal when underlying numerical data is the same
            return True
        else:
            return False
        # or
        #return self.x==other.x and self.y==other.y
    
    # p.setx(4) -> Point.setx(p,4)
    def setx(self,xcoord): # self and p are the same. p is name outside class, self is name insode class
        self.x=xcoord
        # if i needed to keep positive
##        if xcoord>0:
##            self.x=xcoord
##        else:
##            self.x=0

    def sety(self,ycoord):
        self.y=ycoord

    #p.get() -> Point.get(p)
    def get(self): #self is a convention. Can use anything but self is the convention. Better to be consiatant in all methods
        return (self.x,self.y)

    def move(self,deltax,deltay):
        self.x=self.x+deltax
        self.y=self.y+deltay

# client

def movePointAround():
    x,y=eval(input('Enter a point: '))
    pt=Point(x,y) # construct a point (initialize a point), calls __init__
    while True:
        ans=input('Move it how? ') # can't eval empty string
        if ans == '':
            break
        else: # adjust the point
            dx,dy=eval(ans)
            pt.move(dx,dy)
            print(pt) # calls __repr__
    return pt
