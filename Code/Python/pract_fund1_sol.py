"""
Practice problems, Python fundamentals 1 -- Solutions

@authors: Balint Szoke, Daniel Csaba
@date: 06/02/2017
"""

#-------------------------------------------------------  
# 1) Solution
good_string = "Sarah's code"
#or 
good_string = """Sarah's code"""
 
#-------------------------------------------------------  
# 2) Solution
i = 1234
list(str(i))

#-------------------------------------------------------  
# 3) Solution
year = '2016'
next_year = str(int(year) + 1)

#-------------------------------------------------------  
# 4) Solution
x, y = 3, 'hello'
print(x, y)
z = x
x = y
y = z
print(x, y)

#-------------------------------------------------------  
# 5) Solution
name = 'Jones'
print(name.upper())

#-------------------------------------------------------  
# 6) Solution
name = 'Ulysses'
print(name.count('s'))

#-------------------------------------------------------  
# 7) Solution
long_string = 'salamandroid'
long_string = long_string.replace('a', '*')
print(long_string)

#-------------------------------------------------------  
# 8) Solution
ll = [1, 2, 3, 4, 5]

ll.reverse()
print(ll)
#ll.pop(1) 
# or better
ll.pop(ll.index(4))
print(ll)
ll.append(1.5)
print(ll)
ll.sort()
print(ll)

#%% #-------------------------------------------------------  
# 9) Solution
number = "32,054.23"
number_no_comma = number.replace(',', '')
number_float = float(number_no_comma)
print(number_float)

#or
print(float(number.replace(',', '')))

#-------------------------------------------------------  
# 10) Solution
firstname_lastname = 'john_doe'
firstname, lastname = firstname_lastname.split('_')
Firstname = firstname.capitalize()
Lastname = lastname.capitalize()
print(Firstname, Lastname)
#-------------------------------------------------------  
# 11-12) Solution
l = [0, 1, 2, 4, 5]
index = l.index(4)
l.insert(index, 3)
print(l)

#-------------------------------------------------------  
# 13) Solution
s = 'www.example.com'
s = s.lstrip('w.')
s = s.rstrip('.c')

# or in a single line
(s.lstrip('w.')).rstrip('.com')

#-------------------------------------------------------  
# 14) Solution
link = 'https://play.spotify.com/collection/albums'
splitted_link = link.rsplit('/', 1)
print(splitted_link[0]) 
#or
link.rsplit('/', 1)[0]

#-------------------------------------------------------  
# 15) Solution
amount = "32.054,23"
ms = amount.maketrans(',.', '.,')
amount = amount.translate(ms)
print(amount)
