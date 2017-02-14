"""
Python Fundamentals 2

@author: Balint Szoke
@date:   2/11/2017
"""

"""---------------------------------------------------
REVIEW
---------------------------------------------------"""

# Assignment
x = 3.14                

# Strings
s = 'this is a string'      
type(s)
len(s)

# Lists
l = [1, 'help', 12.14]
print('This is a', type(l), 'containing', len(l), 'items')

#change types with  str(), int(), float()

#Methods
's is {t} with {c} chars'.format(t=type(s), c=len(s))
l.append(x)
print(l)

# Tab completion!

#%%
"""---------------------------------------------------
OTHER NATIVE PYTHON DATA TYPES
---------------------------------------------------"""

#====================
# Dictionary
#====================

dict1 = {'first': 12, 'second': 20, 3: 'first'}
print(dict1)
type(dict1)

# Unordered, access values through keys 
dict1['first']
dict1[3]
# dict1[0]                    # indexing doesn't work

#Key must be unique (only keeps last one)
dict2 = {'first': 12, 'first': [4, 1]}
print(dict2)

# Key must be inmutable! What's the problem?
#dict3 = {[1, 2]: 4}

# Methods
dict1.keys()
dict1.values()

list(dict1)
list(dict1.values())

#==========================
# Boolean (comparisons)
#==========================

# Yes/no questions
4 < 5           # interpreted as: is 5 greater than 4?       
x > 5           # can involve variables
type(x > 5)
z = x > 5       # True/False value can be assigned

# Basic comparison operators
x == 3          # equal to?
5 >= 5          # greater than or equal to?
x != 3          # not equal to? 

# True == 1, False == 0
int(z)

# can reverse comparisons with "not"
not 3 > 5

# Use it the usual way
x, y = 4*2, 2**3
"x={x}, y={y}, so x>y is {s}".format(x=x, y=y, s=x>y)

type('Sarah') == str      # can involve "type checking"
len('Sarah') >= 3

# Tricky one
name1 = 'Chase'
name2 = 'Spencer'

name1 > name2
name1 < name2
# what's going on? try
'a' < 'b'

# Handy alternatives:  "is" and "is not" 
x is y            # "equal to"?    
x is not y

# Clear syntax
1 in [1, 4, 5]
3 not in [1, 4, 5] 

# Standard Boolean logic to combine comparisons
print(True and True, 
      True and False, 
      False and False) 

print(True or True, 
      True or False, 
      False or False) 

#%%
"""---------------------------------------------------
SLICING : access a range of items from a container
---------------------------------------------------"""

x = [4, 1, 5, 2, 10, 23]
x[3]                        # indexing        
x[:3]                       # everything to the left (3 NOT included)                      
x[3:]                       # everything to the right  (3 included)                       
x[1:4]        

"""
Rule:

x[n_start:n_end] gives 
    [x[n_start], x[n_start + 1], ..., x[n_end-1]]
"""

# Counting backward
x[-1]                       # last element
x[-2]                       # second to last
x[2:-2]                     # combined

# not only lists
name = 'python'
# how to get 'py' from name?
name[:2]

#%%
"""===================================================
FLOW CONTROL
    control which commands are executed and the
    order in which they are processed
==================================================="""

"""---------------------------------------------------
(1) CONDITIONALS (if and else)
    tell Python to do things depending on the 
    value of a Boolean
---------------------------------------------------"""

this = True
if this is True:            # don't forget the colon 
    print("hello")          # don't forget the indentation

that = False
#that = 5                   # careful with negation!
if that is not True:
    print("bye")

# Indentation inticates an "inner code"  
x = 2
if x > 0:
    x = x + 1
    x = x * 5
    print(x)
    
"""
Structure matters! different branches
"""
x = 2
if x > 0:
    # first branch starts here
    print(x)
    x = x + 1
    print(x)
    if x < 5:
        # conditional second branch starts here
        print(x)
        x = x * 5
        x = x**3
        # second branch ends here
    print(x)          # back to the first branch

# ELSE - what to do if the condition is false  
if this is True:
    print('this is true')
else:
    print('this is false')

# ELIF - add more branches to the decision tree
if x < 2:
    print("x < 2")
elif x == 2:
    print("x == 2")
else:
    print("x > 2")    
    

'''---------------------------------------------------
(2) Loops (over containers):
    do the same thing many times
---------------------------------------------------'''

# Print out list of names one at a time
namelist = ['Chase', 'Anne', 'Josh', 'Alberto']

for i in namelist:
    print(i)

"""
Iterables: 
   def:  An object capable of returning its members 
         one at a time.
   e.g.: list, str, tuple, dict
"""
for i in "hello":
    print(i)

    
'''
i is just a dummy! It can be anything, but be careful
with using already defined var names
''' 
x = 5
print('before the loop x is', x)
for x in '01234':
    print('in the loop, x is', int(x))
print('after the loop x is', x)

    
# Compute the sum of the elements of a list of nums
numlist = [-2, 3.1, 10, 23]    
summ = 0
for i in numlist:
    summ = summ + i
print(summ)


#=================================================
# Loops over counters
#    loop over something a fixed number of times
#=================================================
how_many = 10
for i in range(how_many):
    print("boring")

# or we can use the elements of range()
# range(n) gives all integers from 0 to n-1 
for i in range(5):
    print(i)

# different starting point
for i in range(2, 8):
    print(i)

# print the squares of integers up to 10
for number in range(10):
    square = number**2
    print('Number and its square:', number, square)
    
# combine loop with conditional
for num in range(10):
    if num > 5:
        print(num)

# we might want to break the loop if something happens
maxnum = 20

total = 0
for num in range(maxnum):
    total = total + num
    if total > 100:
        break               # exit loop
        
print('At num =', num, 'we had total =', total)


#==========================================
# List comprehensions = 
#       create list using implicit loops
#==========================================

# Compare
for item in namelist:
    print(item.upper())
#with
[item2.upper() for item2 in namelist]    
    
# list comprehension with condition
fruits = ['apple', 'banana', 'orange']
fruits6 = [i for i in fruits if len(i)>=6]
print(fruits6)



#%%
'''==================================================
DEFINING OUR OWN FUNCTIONS
=================================================='''

#--------------------------
# Function with no output
#--------------------------
def hello(firstname):
    print("Hello,", firstname)

hello('Balint')

def silly():
    print("the same")
    
#--------------------------------------------------------
# Function creates a new value that Python can work with
#        RETURN - sends output back to the main program
#--------------------------------------------------------
def square_me(number):
    """
    Takes numerical input and returns its square
    """
    square = number**2
    
    return square

#Test
square_me(7)


def nextyear(string_year):
    """
    Takes a string year and returns a string of next year
    """
    int_year = int(string_year)
    next_year = int_year + 1
    
    return str(next_year)

nextyear('2016')

# use it just like the built-in functions
for i in range(2010, 2016):
    year = str(i)
    next_year = nextyear(year)
    print('year is', year, 'Next year is', next_year)


