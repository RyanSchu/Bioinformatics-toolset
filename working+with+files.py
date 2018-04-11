
# coding: utf-8

# In[21]:


#get your current working directoy, by importing os
import os
os.getcwd()
#set your cwd as a string variable for later use
mydir = os.getcwd()
#now create a variable that contains the adress of the actual file you wish to read
infile = mydir + "\\filename.txt"
#open a readable version of the file
f = open(infile, 'r')
#initialize an empty array to store the lines 
lines = []
for line in f:
    #store all the lines in the array
    lines.append(line)
#now create an output textfile
f = open('output.txt', 'w')
#now check the index of each line
#remember that arrays begin at 0
#therefore write and print out any odd index of the array
for i in range(len(lines)):
    if i% 2 != 0:
        f.write(str(lines[i]) +'\n')
        print(lines[i])

