#!/usr/bin/env python
# coding: utf-8

# Q.1. What are keywords in python? Using the keyword library, print all the python keywords.
# 
# 
# : Keywords are the reserved keywords in python that has their own meaning and we can't use them as a variable or as a identifier. 

# In[5]:


import keyword

print(keyword.kwlist)


# Q.2. What are the rules to create variables in python?
# 
# : There are some rules as the coding principles that we have to follow while creating variables in python.
# variable name should be in capital letters and it should start with letter or underscore. 
# 
# should not contain any special characters.
# 
# should be keep in mind they are case sensitive, so if you are using that in capital letters then it should be followed throughout the program.
# 
# no reserved keywords can be used as a variable name.
# 

# Q.3. What are the standards and conventions followed for the nomenclature of variables in
# python to improve code readability and maintainability?
# 
# : variable name should be descriptive and meaningful that add more meaning or infromation to the reader.
# 
# should use underscore if there are two separate words in the varible name.
# 
# should not use reserved keywords.
# 
# constants should be used in all capital letters.
# 
# use clear names not anything.

# Q.4. What will happen if a keyword is used as a variable name?
# 
# : Possibilities of two thing 1) Either the menaing of variable will change and it will affect the output or value.
# it will throw error for many reasons, like it will not take value assignement most of the time.

# Q.5. For what purpose def keyword is used?
# 
# : It is used to define a function without def keyword we can't define a function.

# Q.6. What is the operation of this special character ‘\’?
# 
# it is normal used to escape sequence like for new line. e.g. "hello\world".
# like that it will allow characters to include in a string that is not allowed otherwise.
# for example escaping double quotes. "hello\"world\"".
# print('It\'s Python!')  # Escapes single quote
# 
# total = 10 + 20 + \
#         30 + 40
# print(total)  # Output: 100 (to continue code in the next line)

# Q.7. Give an example of the following conditions:
# (i) Homogeneous list
# (ii) Heterogeneous set
# (iii) Homogeneous tuple
# 
# :A homogeneous list contains elements of the same data type, such as [10, 20, 30, 40], where all elements are integers. A heterogeneous set includes elements of different data types, for example {25, "Python", 3.14, True} which combines an integer, string, float, and boolean. A homogeneous tuple holds elements of the same type, like ("apple", "banana", "cherry"), where all items are strings.

# Q.8. Explain the mutable and immutable data types with proper explanation & examples.
# 
# :In Python, mutable data types are those whose values can be changed after creation, such as lists, dictionaries, and sets. For example, you can modify a list like `[1, 2, 3]` by changing an element or adding new ones. On the other hand, immutable data types cannot be altered once created; any change results in a new object. Examples include strings, integers, floats, and tuples. For instance, modifying a string like `"Python"` by adding `"3"` creates a new string `"Python3"`, leaving the original unchanged.

# Q.9. Write a code to create the given structure using only for loop.
# *
# ***
# *****
# *******
# *********

# In[32]:


rows = 6
for i in range(rows):
    stars = 2*i +1

    print("*"*stars)


# Q.10. Write a code to create the given structure using while loop.

# In[3]:


rows = 9 
while rows >0:
    print("|"*rows)
    rows-=2
  

