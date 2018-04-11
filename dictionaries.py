
# coding: utf-8

# In[7]:


#initialize s with string and an empty dictionary
s = ""
d = {}
#split the string at whitespaces with the .split() method produces a list
for i in s.split():
    #iterate through the list, if the word is in d already increase the value by 1
    if i in d:
        d[i] += 1
    #otherwise add the word to the dictionary with a value of 1
    else:
        d[i] = 1
#finally print the key value pairs nicely, casting the values to string
for key in d:
    print(key + " " + str(d[key]))


# In[ ]:


s = ""

