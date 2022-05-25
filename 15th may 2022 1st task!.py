#!/usr/bin/env python
# coding: utf-8

# In[2]:


# 1 . Try to extract data from index one to index 300 with a jump of 3 

s = "this is My First Python programming class and i am learNING python string and its function"
s[0:300:3]


# In[3]:


# 2. Try to reverse a string without using reverse function 
s[::-1]


# In[4]:


# 3. Try to split a string after conversion of entire string in uppercase 
s1=s.upper()


# In[5]:


s1


# In[6]:


s1.split()


# In[7]:


#4 4. try to convert the whole string into lower case 
s1.lower()


# In[8]:


# 5 . Try to capitalize the whole string 
s1.upper()


# In[9]:


# 6 . Write a diference between isalnum() and isalpha()
# ANS- isalnum checkes weather the strings contains numaric values or not in a string, if numbers are present it returns "True" otherwise "False", if the string has combination of numbers and alphabets it returns "False" ex:s="gty675539jk"
# ANS- isalpha checkes weather the strings contains alphabets or not in a string, if alphabets are present it returns "True" otherwise "False",if the string has combination of alphabets and numbers it returns "False" ex:g="hgyug7649273ohyu"


# In[10]:


#7. Try to give an example of expand tab
s2=("Hare\t Krishna\t Hare\t Rama")
s2.expandtabs()


# In[13]:


# 8 . Give an example of strip , lstrip and rstrip 
s3="     harekrishna        "
s3.strip()


# In[14]:


s3.lstrip()


# In[15]:


s3.rstrip()


# In[16]:


# 9.  Replace a string charecter by another charector by taking your own example "sudhanshu" 

a="sudhanshu"
a.replace('s','z')


# In[18]:


# 10 . Try  to give a defination of string center function with and exmple 
#ANS- srting center function makes the string to appeare in the middel with respective number of spaces that you give to the string
b = " Hare Krishna "
b.center(50,"$")

# here "50" is the string length or size "$" is the notation that will appere on bothe sizes of the string


# In[19]:


# 11 . Write your own definition of compiler and interpretor without copy paste form internet in your own language
#COMPILER- converts code into object code like.exe file and data is taken to that .exe file and run the program "Real Life EX"- watching a movie with english subtiles which means its already compiled and read to see.
#Interpreter - check line by line and convert into object code and run the program, "Real Life EX"-Translator with translate the message line by line, in this case if we speack the translater would be translate.


# In[20]:


# 12 . Python is a interpreted of compiled language give a clear ans with your understanding 
# in my understanding python is both compiler and interpreter

#Ex:-python is a platform independence, python compile its self and give us bite code, that bite code can run on pvm(python virtual machine)


# In[ ]:


#13 . Try to write a usecase of python with your understanding .

# Python can be used in developing Web applications. Ex:-Netflex,google,uber
# Python programming language are  used  Software development.
# Python language is used  Data science.
#Python is used  AI applications. Ex:lenskart
#Python used for developing Game. Ex:-Battlefield 2,World of Tanks.

