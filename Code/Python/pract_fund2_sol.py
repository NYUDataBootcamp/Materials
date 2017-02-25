"""
Practice problems, Python fundamentals 2 -- Solutions

@author: Balint Szoke
@date: 14/02/2017
"""


#===========================================================
# 1) Solution
numbs = {1: 'one', 2: 'two', 3: 'three'}
numbs[2]




#===========================================================
# 2) Solution
l1 = [1, 2, 3]
l2 = ['one', 'two', 'three']
#(a)
list(zip(l1, l2))       # or  [i for i in zip(l1, l2)]
#(b)
dict(zip(l1, l2))




#===========================================================
# 3) Solution
name1 = 'Dave'
name2 = 'Glenn'

if name1 > name2:
    print(name2)
elif name1 == name2:
    pass 
else:
    print(name1)

# Function
def alphabetical(name1, name2):
    if name1 > name2:
        print(name2)
    else:
        print(name1)
# Test
alphabetical('Chase', 'Glenn')
alphabetical('Chase', 'Anne')




#===========================================================
# 4) Solution
stuff = ['cat', 3.7, 5, 'dog']
#(a)    
for item in stuff:
    print('The type of', item, 'is', type(item))    
#(b)    
for item in stuff:
    if type(item) == str:
        print(item, 'is a string')    

def myfunc(s):
    x = []
    for item in s:
        x.append('The type of {a} is {b}'.format(a=item, b=type(item)))
    return x
    

        
#===========================================================
# 5) Solution
a, b = 6, 4
six = a==6 or b==6 or a+b==6 or abs(a-b)==6

# Function
def love6(a, b, love=6):
    return a==love or b==love or a+b==love or abs(a-b)==love    

#Test
love6(6, 4)
love6(4, 5)
love6(1, 5)




#===========================================================
# 6) Solution

summ = a + b
if summ >= 10 and summ <= 20:
    summ = 20
print(summ)    
    
# Function
def cond_sum(a, b, lb=10, ub=19):
    """
    Returns the sum of a and b given that it is in [lb, ub]
    
    lb : lower bound (included) of the interval when it returns 20
    ub : upper bound (included) of the interval when it returns 20

    """
    summ = a + b
    if summ >= lb and summ <= ub:
        return 20
    else:
        return summ
    
#Test
cond_sum(3, 4)
cond_sum(9, 4)
cond_sum(10, 11)




#===========================================================
# 7) Solution 
   
bond_yields = [.01, .02, .03]    

yields = []

for bond in bond_yields:
    yields.append(100*bond)

print(yields)
    
# List comprehension
print([100*bond for bond in bond_yields])    
# Function
def yield_percent(bond_yields):
    return [100*bond for bond in bond_yields]
    

    
    
#===========================================================
# 8) Solution
#(a) from 0 to n
n = 5
print([i for i in range(n+1)])

# (b) from n1 to n2
n1, n2 = 4, 8
print([i for i in range(n1, n2+1)])

# Function
def linspace(n2, n1=0):
    return [i for i in range(n1, n2+1)]

# Test
linspace(5)
linspace(8, 4)



#%%


#===========================================================
# 9) Solution
x = [1, 4, 5, 6, 4, 2, 7, 12, 4, 23, 4]

indices = []
for i in range(len(x)):
    if x[i] == 4:
        indices.append(i)
print(indices)

#or 
[i for i in range(len(x)) if x[i]==4]

# Function
def index_of_value(x, value):
    """
    Takes the list x and returns a list of indices where it takes value
    """
    indices = [i for i in range(len(x)) if x[i]==value]
    if indices == []:
        print("There is no item=={v} in the list".format(v=value))
    else:
        return indices 

#Test
index_of_value(x, 4)
index_of_value(x, 10)


#===========================================================
# 10) Solution
s1 = "abc def ghi"
s2 = "def ghi abc"

# (a) contain exactly the same characters?
sorted(list(s1)) == sorted(list(s2)) 
# or (what is a set?)
set(list(s1)) == set(list(s2)) 

# (b) contain the same words?
sorted(s1.split(' ')) == sorted(s2.split(' '))
set(s1.split(' ')) == set(s2.split(' '))

