#!/usr/bin/env python
# coding: utf-8

# **[Slide No.- 35]**
# 
# 1. Create a empty list and check its Data type 

# In[ ]:


list1 = []
type(list1)


# In[ ]:





# 

# In[ ]:





# **[Slide No.- 35]**
# 
# 2. Create a list in which at even places string are present and at odd places integervalue is present and the length of the string is 6.

# In[ ]:



random = ['abc',1,'def',3,'ghi',5]


# **[Slide No. - 36]**
# 
# 3. Create a lsit which has 6 elements and print last three elements from the list 

# In[ ]:



random1 = ['q',5,-3,8.5,'erfev',98]
random1[-3:]


# **[Slide No. - 36 ]**
# 
# 4. What is the output :
#  list = [1,2,3,4,5,6,7] 
#  
#  list[:]=?

# In[ ]:


[1,2,3,4,5,6,7]


# **[Slide No. - 36]**
# 
# 5. What is the output : list = [1,2,3,4,5,6,7]
# 
# Print the even places items from the list.

# In[ ]:


list2 = [1,2,3,4,5,6,7]
list2[::2]


# **[Slide No. - 36]**
# 
# 6. What is the output : list = [1,2,3,4,10,11,7]
# 
# print 10 and 11 item from the list .

# In[ ]:


list3 = [1,2,3,4,10,11,7]
list3[-3:-1]


# In[ ]:





# **[Slide No. -38]**
# 
# 7.  Delete the 3 index value from the list and the print the list.
# 
# list = [1, 2, 3, 4, 5, 6]    
# 
# print(list)    
#     
#  

# In[ ]:


list4 = [1,2,3,4,5,6]
list4.pop(3)
print(list4)


# In[ ]:





# [Slide No. - 37]
# 8. list = [1, "a", 3, 4, 5, 6] 
# 
# replace "a" by 2 in the list
# 
# What is the new list?

# In[ ]:


list5 = [1,"a",3,4,5,6]
list5[1] = 2
print(list5)


# In[ ]:





# **[Slide No - 37]**
# 
# 9. list = [1, 2, 3, 4, 5, 6] 
# 
# by using neagtive indexing replace 5 by 'e' in the list 
# 
# print(list)

# In[ ]:


list6 = [1,2,3,4,5,6]
list6[-2] = 'e'
print(list6)


# **[Slide No. - 37]**
# 
# 10. list = [1, 2, 3, 4, 5, 6] 
# 
# replace 1st and 2nd index value by (89,78)
# 
# print(list) 

# In[ ]:


list7 = [1,2,3,4,5,6]
list7[1:3]=89,78

print(list7)


# **[Slide No. -38]**
# 
# 11. Create a list and delete 2 to 4 index value  from list ?

# In[ ]:


list8 = [1,2,3,4,5,6]
rem = [2,2,2]
for l in rem:
    list8.pop(l)
print(list8)


# **[Slide No.- 39]**
# 
# 12. Rermove Science  item from the list.
# 
# Subject =['math', 'science', 'hindi', 'SST', 'Sanskrit']
# 

# In[ ]:


list9 = ['math', 'science', 'hindi', 'SST', 'Sanskrit']
list9.remove('science')
print(list9)


# In[ ]:





# In[ ]:




