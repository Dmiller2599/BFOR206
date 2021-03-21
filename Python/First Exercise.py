# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a block comment.
I can type whatever I desire here.

This script will demonstarte basic variables,
if statements, and for loops with Python.

"""
# this is a normal comment.

"""
The comment below defines a chunck that spyder can
use to separate parts of code into small blocks.
This makes it easy to run just a small part of your code.

The syntax is 
#%%
If you want to name a chunk

#%% chunk name
"""

#%% define vars

# To run a single line press, f9
my_str = "this is a string"
print(my_str)

my_num = 123.456789
my_int = 123

print(my_num, my_int)

# to run entire chunk
# Ctrl + Enter (Cmd + Enter on Mac)

# to run the entire chunk and go to the next chunk
# Shift + Enter

#%% if statements
a = 0
b = 1


print("the value of a is:", a)

if a > b:
    # Everything indented is part of the if statement
	print("a is greater than b. Wow!")
elif a < b:
    print("a is less than b. Weak!")

else:
    	print("a and b are the same, eh?")

print("Done with if statements.")

#%% for loops

for i in range(10):
    print("the number i is", i)


#%% nested statements

for i in range(5, 10):
    print("i is ", i)
    # indents are important!
    for j in range(3):
        print("j is ", j)
print("done with nested loops")


#%% lab
"""
Fix this code below to complete the lab
"""
my_list = ['Hello', 'BFOR', 206, None, 'Bye!']

for item in my_list:    
    if item is None:
        print("Found item with value of None!")   
    else:
        print("The item is", item)
