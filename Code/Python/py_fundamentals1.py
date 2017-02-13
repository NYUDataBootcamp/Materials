"""
Python Fundamentals 1

@author: Balint Szoke
@date:   2/4/2017

"""



"""---------------------------------------------------
 Python is a calculator. 
 Try these commands one line at a time in the console
---------------------------------------------------"""
2*3
2 * 3                # white space around operators no issue
2/3
2^3                  # what do you see?  
log(3)               # what does the error message say?

# Basic arithmetic operations:
2 + 3
2 - 3
2 / 3
5 % 2               # modulo = remainder from a division

"""---------------------------------------------------
 Assign values to variables 
 variables are names for values stored in memory
---------------------------------------------------"""
x = 5               # bind x to integer 3
y = 3
x                   # query the value of x

z = x/y             # use previously defined variables
z


"""---------------------------------------------------
 Execution from right to left:
   (1) interpreter evaluates the expression on the right
   (2) store the value in memory
   (3) binds the identifier on the left to that value 
---------------------------------------------------"""
w = 5
w = w + 2           # why is this not a violation of math?


#%%
'''--------------------------------------------------
NATIVE PYTHON DATA TYPES
--------------------------------------------------'''

#====================
# (1) String
#====================
a = 'some'
b = 'thing'
number = '12'       # a number can be a string
'12'/3              # try to understand the error message

a + b               # some arithmetic operations have
a * 5               # type-dependent meaning
a**2                # but not all of them

# Be careful
300 + 'ccc'
'300' + 'ccc'

# Better-looking output
print(z)
print('the value of z is', z)
# ... or even better (why?)
message = 'the value of z is'
print(message, z)

"I don't know"      # how about 'I don't know'

#============================
# (2) Integer and float
#============================
x, y = 1, 2
z, v = 3.4, 10.0

# complex numbers
c = complex(2, 4)


#============================
# (3) List
#============================
numberlist = [2, 4, 1]
stringlist = ['I', 'am', "Balint"]
mixedlist = [1, "hello", 4.32]

# Combining lists by adding them
#    Note: similar to stings! ("sequence type/container")
numberlist + stringlist
[numberlist, stringlist]

# lists can be unpacked as 
integers = [10, 20, 30]
x, y, z = integers
print(x, y)

# Access elements via indexes (square bracket)
numberlist[0]
stringlist[2]
mixedlist[3]
stringlist[2][3]     # what do you see?

# modify certain elements
stringlist[2] = "Anna"
print(stringlist)
del stringlist[1]

#============================
# (4) Tuple = immutable list
#============================
numbertuple = (2, 4, 1)
stringtuple = ('I', 'am', "Balint")

# Trying to mutate them produces an error
numbertuple[1] = 3    


"""
Technical digression:
    
list is mutable = content can be altered without 
                  creating a new object
            
tuple is immutable = it cannot be altered without 
                     creating a new object                 
"""

#%% 
"""
BUILT-IN FUNCTIONS
     syntax : function(object)
"""
len('hello')             # string is a container
len([2, 4])              # list is a container
len(123)                 # integer is not a container
len(1.23)                # float is not a container
len('12.3 ')             # blank space and . count

type(1.2)
type('12')
type(numberlist)
type(numbertuple)

x = [20, 30, 50]
max(x)
sum(x)

# Changing types:
# str -> int
t = '12'
type(t)
t = int(t)
type(t)

# str -> float
a = float('12.4') 
b = float('12')
type(b)

int('12.4')            # sometimes it doesn't make sense

# numbers -> str
g = str(4)
type(g)
h = str(4.5)
type(h)

#string -> list
x = 'abc'
x = list(x)
type(x)

#%%
"""
METHODS 
   = functions linked to objects with diff syntax
   syntax : object.methodName(arguments)
"""
# available methods depend on the object...how to check?
#      -> TAB COMPLETION

numberlist.append(56)
numberlist.pop?
numberlist.pop(2)
numberlist

s = 'godzilla'
s.count('g')
s.startswith('go')
s.upper()

