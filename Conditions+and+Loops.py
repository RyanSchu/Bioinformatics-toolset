
# coding: utf-8

# In[15]:


#initialize variables
a = 100
b = 200
#initialize sum holder
sum = 0
#for the range of values from a to b, inclusive repeat the following
for i in range(a,b+1):
    #check if the number is odd with the modulo operator and add to sum if true
    if i % 2 == 1:
        sum = sum + i      
print(sum)

