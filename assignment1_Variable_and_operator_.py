#!/usr/bin/env python
# coding: utf-8

# # Variable and Operator 

# **[Slide No.- 19]**
# 
# 1. Which one of the following is correct way of declaring and initialising a variable, x with value 5?
# 
# A. int x
#   
#     x=5
# 
# B. int x=5
# 
# C. x=5
# 
# D. declare x=5
# 
# 
# 
# 
# 

# In[2]:


# Check your Answer
x = 5
print(x)


# **[Slide No.-19]**
# 
# 2. Which of the following is not valid variable name in Python?
# 
# A. _var = 6
# 
# B. var_name = 6
# 
# C. var11 = 6
# 
# D. 11var = 6

# In[ ]:


#Check your Answer


# **[Slide No.- 19]**
# 
# 
# 3. Which of the following will give error?
# 
# A. a=b=c=1
# 
# B. a,b,c=1
# 
# C. a b c=1, 4, 1.5
# 
# D. None of the above

# In[2]:


#Check your Answer
a,b,c=1


# **[Slide No.- 21]**
# 
# 4. What is the output of the following code
# 
# x = 6
# 
# y = 2
# 
# a=print(x ** y)
# 
# b= print(x // y)

# In[3]:


#Check your Answer
x = 6

y = 2

a=print(x ** y)

b= print(x // y)


# In[5]:


x//y


# **[Slide No.-21]**
# 
# # find the value of this expression (v+w) * x/ y
# v = 4
# 
# w = 5
# 
# x = 8
# 
# 
# y = 2
# 
# z = 0

# In[7]:


# find the value of this expression (v+w) * x/ y
v = 4

w = 5

x = 8

y = 2

z = 0
(v+w)*x/y


# **[Slide No.- 21]**
# 
# 6. What is the output of print(10 - 4 * 2)

# In[8]:


#Check your Answer
10-4*2


# **[Slide No.-21]**
# 
# 7. What is the output of print(2 * 3 ** 3 * 4)

# In[9]:


#Check your Answer
2*3**3*4


# 8. What is the output of the expression  print(-18 // 4)

# In[11]:


print(-17 // 4)      #Floor division    -4.5  =-5


# In[ ]:


x=8
x -=8+x    # X+8+8       x += 8       # x-(8+x)=x-8-x
print(x)


# **[Slide No.- 21]**
# 
# 9. Write a program to check 5 is less then 10 or greater then 3.

# In[ ]:


a,b,c=5,10,3
if c>a or c>b:
  print('5 is less then 10 or greater then 3')
else:
  print("wrong ourput")


# In[ ]:


a=int(input('enter number'))    # usaed to take the input from the user
b=int(input('enter number'))
c=int(input('enter number'))
if a<b and a>c:
  print('true')
else:
  print('false')


# 10 . Write a program  by using 'and' ,'or' And 'not' operator ?

# In[ ]:


a=3
b=7
print(a==3 or b==8)
print(a!=3)


# In[ ]:


print (((10 > 2) or (2 < 5)) and (7 != 9))


# **[Slide No.- 27]**
# 
# 11. What is the output of the following assignment operator
# 
# y = 10
# 
# y += 2
# 
# print(y)

# In[27]:


y = 10

y += 2

print(y)


# **[Slide No.-27]**
# 
# 12. What is the output of the code .
# 
# x=5
# 
# x +=x+4
# 
# print(x)
# 

# In[28]:


x=5

x +=x+4

print(x)


# **[Slide No.-27]**
# 
# 13.  what is the output :
# 
# y=7
# 
# x  +=y+4
# 
# print(x)

# In[29]:


y=7

x +=y+4

print(x)


# In[ ]:


#x=x+y+4
y=7
p=6
p+=y+4

print(p)


# In[ ]:


x=6                #110
x=x|3              #011   
print(x)           #  010


# In[30]:


x=6
x=x>>2                 # 6 = 110 --> 011 --> 001 = 1 

print(x)


# In[26]:


s='hello how\nare you'

print(s+s)
s

