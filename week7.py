# clean

##def clean(sentence):
##    start=0
##    end=-1
##    while sentence[start]in " \t\n":
##        start+=1
##    while sentence[end]in " \t\n":
##        end-=1
##    end+=1
##    return sentence[start:end]



def clean(sentence):
    while sentence[0] in (" ","\t","\n"):
        sentence=sentence[1:]
    while sentence[-1] in (" ","\t","\n"):
        sentence=sentence[:-1]
    return sentence

        
#v3 - correct
def pigLatin(word):
    # move consonant if there is one
    while word[0] not in 'aeiou':
        # move consonant to the end
        word=word[1:] + word[0] 
    return word + 'ay'

        
###########################################################
# week 7.py

'''make this work
>>> frequencies([5,8,5,8,7])
{5:2.8:2,7:1}
'''

def frequencies(iterable):
    '''return a dictionary with frquency counts of items in a list'''
    counts={}
    for item in iterable:
        #if item is new, add key
        if item not in counts:
            counts[item]=1
        # otherwise, update count
        else:
            counts[item]+= 1
    return counts


'''
make this work
rolls: 3 3,5 5, 2 1
>>> diceTotal() # for above rolls
19
'''

import random
#acculator, while
def diceTotal():
    pips=0
    die1=random.randrange(1,7)
    die2=random.randrange(1,7)
    #print(die1,die2)
    pips +=die1+die2
    
    while die1==die2:
        die1=random.randrange(1,7)
        die2=random.randrange(1,7)
        #print(die1,die2)
        pips +=die1+die2
    return pips


'''
make this work
>>> d={'a':'k','b':'g'}
>>> encode('bat',d)
'gkt'
'''

def encode(phrase,d):
    #accumulate a str
    ans=""
    #iterate over the phrase
    for char in phrase:
        # if letter in dictionary
        #replace it with value
        if char in d:
            ans+=d[char]
        #if not, leave it alone
        else:
            ans +=char
    return ans
        
# substitution cipher
'''
>>> alphabet="abcdefghijklmnopqrstuvwxyz"
>>> alpha2=list(alphabet)
>>> alpha2
['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
>>> import random
>>> random.shuffle(alpha2)
>>> alpha2
['i', 'y', 'b', 'j', 'n', 't', 'q', 'd', 'f', 'c', 'g', 'a', 'l', 'r', 'u', 'e', 'p', 's', 'm', 'k', 'z', 'x', 'v', 'w', 'o', 'h']
>>> alphabet=list(alphabet)
>>> zip(alphabet,alpha2)
<zip object at 0x00000160FAF73FC0>
>>> list(zip(alphabet,alpha2))
[('a', 'i'), ('b', 'y'), ('c', 'b'), ('d', 'j'), ('e', 'n'), ('f', 't'), ('g', 'q'), ('h', 'd'), ('i', 'f'), ('j', 'c'), ('k', 'g'), ('l', 'a'), ('m', 'l'), ('n', 'r'), ('o', 'u'), ('p', 'e'), ('q', 'p'), ('r', 's'), ('s', 'm'), ('t', 'k'), ('u', 'z'), ('v', 'x'), ('w', 'v'), ('x', 'w'), ('y', 'o'), ('z', 'h')]
>>> dict(zip(alphabet,alpha2))
{'a': 'i', 'b': 'y', 'c': 'b', 'd': 'j', 'e': 'n', 'f': 't', 'g': 'q', 'h': 'd', 'i': 'f', 'j': 'c', 'k': 'g', 'l': 'a', 'm': 'l', 'n': 'r', 'o': 'u', 'p': 'e', 'q': 'p', 'r': 's', 's': 'm', 't': 'k', 'u': 'z', 'v': 'x', 'w': 'v', 'x': 'w', 'y': 'o', 'z': 'h'}
>>> cipher=dict(zip(alphabet,alpha2))
>>> encode('the quick red fox jumped over the laazy dog',cipher)
'kdn pzfbg snj tuw czlenj uxns kdn aiiho juq'
'''

msg = '''
>>> aitmjx xwan
Xwl Flc mo Texwmc, qe Xai Tlxljn
Qlksxaosu an qlxxlj xwkc srue.
Lztuayax an qlxxlj xwkc aituayax.
Naitul an qlxxlj xwkc ymitulz.
Ymitulz an qlxxlj xwkc ymituaykxlh.
Oukx an qlxxlj xwkc clnxlh.
Ntkjnl an qlxxlj xwkc hlcnl.
Jlkhkqauaxe ymscxn.
Ntlyaku yknln kjlc'x ntlyaku lcmsrw xm qjlkb xwl jsuln.
Kuxwmsrw tjkyxaykuaxe qlkxn tsjaxe.
Ljjmjn nwmsuh cldlj tknn naulcxue.
Sculnn lztuayaxue naulcylh.
Ac xwl okyl mo kiqarsaxe, jlosnl xwl xlitxkxamc xm rslnn.
Xwljl nwmsuh ql mcl-- kch tjloljkque mcue mcl --mqdamsn vke xm hm ax.
Kuxwmsrw xwkx vke ike cmx ql mqdamsn kx oajnx sculnn ems'jl Hsxyw.
Cmv an qlxxlj xwkc cldlj.
Kuxwmsrw cldlj an moxlc qlxxlj xwkc *jarwx* cmv.
Ao xwl aitulilcxkxamc an wkjh xm lztukac, ax'n k qkh ahlk.
Ao xwl aitulilcxkxamc an lkne xm lztukac, ax ike ql k rmmh ahlk.
Ckilntkyln kjl mcl wmcbacr rjlkx ahlk -- ulx'n hm imjl mo xwmnl!'''

cipher={'Z':'x','T':'p','U':'l','O':'f','E':'y','Y':'c','S':'u','R':'g','N':'s','A':'i','M':'o','D':'b','L':'e','X':'t','J':'r','Q':'b','W':'h','K':'a','C':'n','B':'k'}
msg=msg.upper()
print(encode(msg,cipher))

'''
>>> #dict
>>> phonenums={'frank':111,'sue':222,'sally',333}
SyntaxError: invalid syntax
>>> phonenums={'frank':111,'sue':222,'sally':333}
>>> phonenums={'sue'}
>>> phonenums={'frank':111,'sue':222,'sally':333}
>>> phonenums{'sue'}
SyntaxError: invalid syntax
>>> phonenums['sue']
222
>>> hash('frank')
-9003768856554657743
>>> hash('sue')
8265846667445526663
>>> hash('suE')
-7226080549308248200
>>> phonenums['sally']
333
>>> # can also assign
>>> phonenums['fred']=444
>>> phonenums
{'frank': 111, 'sue': 222, 'sally': 333, 'fred': 444}
>>> # can change a value
>>> phonenums['sue']=777
>>> phonenums
{'frank': 111, 'sue': 777, 'sally': 333, 'fred': 444}
>>> # can I change a key?
>>> # no!
>>> # but can remove
>>> phonenums.pop('sue')
777
>>> phonenums
{'frank': 111, 'sally': 333, 'fred': 444}
>>> phonenums['Sue']=777
>>> phonenums
{'frank': 111, 'sally': 333, 'fred': 444, 'Sue': 777}
>>> phonenums['abc']=None
>>> phonenums
{'frank': 111, 'sally': 333, 'fred': 444, 'Sue': 777, 'abc': None}
>>> # set is dictionaty without values
>>> # just the keys
>>> # == order doesn't matter
>>> {'a':1,'b':2}=={'b':2,'a':a}
Traceback (most recent call last):
  File "<pyshell#131>", line 1, in <module>
    {'a':1,'b':2}=={'b':2,'a':a}
NameError: name 'a' is not defined
>>> {'a':1,'b':2}=={'b':2,'a':1}
True
>>> 'frank' in phonenums
True
>>> 111 in phonenums
False
>>> # iterate
>>> for key in phonenums:
	print(key,phonenums[key])

	
frank 111
sally 333
fred 444
Sue 777
abc None
>>> # sorted version
>>> for key in sorted(phonenums):
	print(key,phonenums[key])

	
Sue 777
abc None
frank 111
fred 444
sally 333
>>> phonenums[['Curie','Marie']]=888
Traceback (most recent call last):
  File "<pyshell#142>", line 1, in <module>
    phonenums[['Curie','Marie']]=888
TypeError: unhashable type: 'list'
>>> # because lists are immutable the key can be changed
>>> # problem!
>>> phonenums[('Curie','Marie')]=888
>>> # use tuple
>>> # tuples are NOT immutable
>>> phonenums
{'frank': 111, 'sally': 333, 'fred': 444, 'Sue': 777, 'abc': None, ('Curie', 'Marie'): 888}
>>> #CORRECTION! Lists are mutable. Tuples are immutable
>>> # dictionaries are mutable keys are immutable
>>> 
=========== RESTART: C:\Users\taiwo\OneDrive\Desktop\CSC401\week7.py ===========
>>> frequencies([5,8,5,8,7])
{5: 2, 8: 2, 7: 1}
>>> frequencies('abracadabra')
{'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1}
>>> frequencies([5,8,5,8,7,"apple",[1,2]])
Traceback (most recent call last):
  File "<pyshell#153>", line 1, in <module>
    frequencies([5,8,5,8,7,"apple",[1,2]])
  File "C:\Users\taiwo\OneDrive\Desktop\CSC401\week7.py", line 40, in frequencies
    if item not in counts:
TypeError: unhashable type: 'list'
>>> frequencies([5,8,5,8,7,"apple",(1,2)])
{5: 2, 8: 2, 7: 1, 'apple': 1, (1, 2): 1}
>>> 
>>> 
>>> # tuples are useful for assignment
>>> x,y=2,3
>>> x
2
>>> y
3
>>> x,y
(2, 3)
>>> x,y=y,x
>>> x,y
(3, 2)
>>> t= (3,2,5)
>>> t.sort()
Traceback (most recent call last):
  File "<pyshell#165>", line 1, in <module>
    t.sort()
AttributeError: 'tuple' object has no attribute 'sort'
>>> # sort is a modifier
>>> sorted(t)
[2, 3, 5]
>>> t
(3, 2, 5)
>>> x=7
>>> # is x one of 2,3, or 5
>>> x==2 or x==3 or x==5
False
>>> x in (2,3,5)
False
>>> x,y
(7, 2)
>>> x=y
>>> x,y
(2, 2)
>>> 
>>> 
>>> # list comprehensions
>>> # [0,1,4,9,16,...,100] # squares
>>> squares = []
>>> for i in range(11):
	squares.append(i*i)

	
>>> 
>>> squares
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
>>> # same thing with a list comprehension
>>> [i*i for i in range(11)]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
>>> [i*i for i in range(11) if i%3!=0]
[1, 4, 16, 25, 49, 64, 100]
>>> 
>>> # build combinations with nested comp
>>> [(p1,p2) for p1 in 'RPS' for p2 in 'RPS']
[('R', 'R'), ('R', 'P'), ('R', 'S'), ('P', 'R'), ('P', 'P'), ('P', 'S'), ('S', 'R'), ('S', 'P'), ('S', 'S')]
>>> 
'''
