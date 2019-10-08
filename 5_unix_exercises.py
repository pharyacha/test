#!/usr/bin/env python
# coding: utf-8

# ### Excercise 1: reconstruct a file from segments.

# Each of the files F* is a short segment of the original text file.
# The fragments are non-overlapping: one segments starts where the previous one ends.
# 
# The format of the file is `(n1: 5 char int),(n2: 5 char int),string`
# The string represents the content of the file in the range `[n1:n2]`
# 
# Your task is to reconstruct the original file using unix commands only. There is a one line solution involving several unix commands connected by pipes "|".

# In[1]:


get_ipython().run_line_magic('cd', '~/Documents/DSE/dse200-notebooks/data/NLTK/Chopped/')
# Use DSE200 folder path instead of ~/DSE200
get_ipython().system('ls F*')
get_ipython().system("cat F* | sort -n F* | cut -c 11- | tr -d '\\n'> /Users/polinaharyacha/Documents/DSE/dse200-notebooks/day_1_python_and_unix/all.txt ")


# ### Excercise 2:

# In[2]:


#Issue a UNIX command to create a file called Caesar that contains the following lines (include the mistakes!!)

#Text = """Caesar, a great general, is petitioned by several citizens to show clemency to one of his enemies.
#He declines, pompously speaking of himself in the third person. The group of conspirators then proceeds to stab him.
#With his dying breath he gasps, "Et tu, Brute? ("And you, Brutus?") Thus falls Caesar." 
#The conspirators exult, and Shakespeare inserts a self-referential joke as Cassius says, 
#"How many ages hence shall this our lofty scene be acted over in states unborn and accents yet unknown!"
#"""

#Change the permissions of this file to 666
#Issue a UNIX command to determine the file type
#Isue a unix comannd to count the number of words in the above text that contains no vowels
#Replace the word Caesar wherever it is found in the entire text to Leonidas
#Make a copy of the above file without the first and last lines of the text and rename this file to Leonidas
get_ipython().run_line_magic('cd', '~/Documents/DSE/dse200-notebooks/day_1_python_and_unix/')
get_ipython().system('touch Caesar.txt')
get_ipython().system('echo $\'Caesar, a great general, is petitioned by several citizens to show clemency to one of his enemies.\\n He declines, pompously speaking of himself in the third person. The group of conspirators then proceeds to stab him.\\n With his dying breath he gasps, "Et tu, Brute? ("And you, Brutus?") Thus falls Caesar."\\n The conspirators exult, and Shakespeare inserts a self-referential joke as Cassius says,\\n "How many ages hence shall this our lofty scene be acted over in states unborn and accents yet unknown!"\'>> Caesar.txt')
get_ipython().system('chmod 666 Caesar.txt')
get_ipython().system('file Caesar.txt')
get_ipython().system("grep -civ '[aeiouy]' Caesar.txt")
get_ipython().system("sed -i '' 's/Caesar/Leonidas/g' Caesar.txt")
get_ipython().system('cp Caesar.txt Leonidas.txt')
get_ipython().system("sed -i '' '1d;$d' Leonidas.txt")


# ### Excercise 3:

# In[3]:


#What is the command to count lines,words and characters in a file and how do you make this comand display only linecount?
#Also write a single command that lists the files in the current directory that begin with upper case letters
#count lines,words and characters:
get_ipython().system('wc Caesar.txt')
#count lines only:
get_ipython().system('wc -l Caesar.txt')


# ### Excercise 4:

# In[4]:


#Combine the files Caesar and Leonidas and save the combined file as kings
get_ipython().system('cat Caesar.txt Leonidas.txt > kings.txt ')


# In[5]:


#Display the contents of this file using more command
#Sort this file in reverse alphabetic order and display it by piping it into more
get_ipython().system('cat Caesar.txt Leonidas.txt > kings.txt')
get_ipython().system('more kings.txt')
get_ipython().system('sort -r kings.txt | more')


# ### Excercise 5:

# In[6]:


#List all files in your current directory. Make a subDirectory and copy all these files in the subdirectory.
get_ipython().system('ls -a')
get_ipython().system('mkdir -p test')
get_ipython().system('mv * test')


# In[8]:


#Write Unix commands to rename all the files to the format - currentDate_originalname

for i in *.*
    do
    get_ipython().system('mv "$f" "$(date "$f"+%d-%m-%Y)"')
done


# ### Excercise 6:

# In[ ]:


#Suppose we have a script that performs numerous efficiency tests. 
#The output from the script contains lots of information, but our purpose now is to extract information
#about the CPU time of each test and sort these CPU times. The output from the tests takes the following form:
output = """
f95 -c -O0  versions/main_wIO.f F77WAVE.f
f95 -o app  -static main_wIO.o F77WAVE.o   -lf2c
app < input > tmp.out
CPU-time: 255.97   f95 -O0 formatted I/O
f95 -c -O1  versions/main_wIO.f F77WAVE.f
f95 -o app  -static main_wIO.o F77WAVE.o   -lf2c
app < input > tmp.out
CPU-time: 252.47   f95 -O1 formatted I/O
f95 -c -O2  versions/main_wIO.f F77WAVE.f
f95 -o app  -static main_wIO.o F77WAVE.o   -lf2c
app < input > tmp.out
CPU-time: 252.40   f95 -O2 formatted I/O
f95 -c -O3  versions/main_wIO.f F77WAVE.f
f95 -o app  -static main_wIO.o F77WAVE.o   -lf2c
app < input > tmp.out
CPU-time: 255.28   f95 -O0 formatted I/O
f95 -c -O4  versions/main_wIO.f F77WAVE.f
f95 -o app  -static main_wIO.o F77WAVE.o   -lf2c
app < input > tmp.out
CPU-time: 251.43  f95 -O0 formatted I/O
f95 -c -O5  versions/main_wIO.f F77WAVE.f
f95 -o app  -static main_wIO.o F77WAVE.o   -lf2c
app < input > tmp.out
CPU-time: 255.90   f95 -O0 formatted I/O
f95 -c -O6  versions/main_wIO.f F77WAVE.f
f95 -o app  -static main_wIO.o F77WAVE.o   -lf2c
app < input > tmp.out
CPU-time: 252.15   f95 -O0 formatted I/O
"""

#First we need to extract the lines starting with CPU-time. 
#Then we need to sort the extracted lines with respect to the CPU time, which is the number appearing in the second column. 
#Write a script to accomplish this task. 

#Hint: Find the lines with CPU time results by using a string comparison of the first 7 characters 
#to detect the keyword CPU-time. Then write a tailored sort function for sorting two lines 
#(extract the CPU time from the second column in both lines and compare the CPU times as floating-point numbers). 
#A tailored sort function takes two arguments a and b, which hold two list elements. 
#The sort function returns -1 if a is less than b, 1 if a is greater than b, and 0 otherwise (a equals b).


# In[14]:


get_ipython().run_line_magic('cd', '~/Documents/DSE/dse200-notebooks/day_1_python_and_unix/test')
get_ipython().system('touch output.txt  ')
get_ipython().system("echo 'f95 -c -O0  versions/main_wIO.f F77WAVE.f \\nf95 -o app  -static main_wIO.o F77WAVE.o   -lf2c \\napp < input > tmp.out \\nCPU-time: 255.97   f95 -O0 formatted I/O \\nf95 -c -O1  versions/main_wIO.f F77WAVE.f \\nf95 -o app  -static main_wIO.o F77WAVE.o   -lf2c \\napp < input > tmp.out \\nCPU-time: 252.47   f95 -O1 formatted I/O \\nf95 -c -O2  versions/main_wIO.f F77WAVE.f \\nf95 -o app  -static main_wIO.o F77WAVE.o   -lf2c \\napp < input > tmp.out \\nCPU-time: 252.40   f95 -O2 formatted I/O \\nf95 -c -O3  versions/main_wIO.f F77WAVE.f \\nf95 -o app  -static main_wIO.o F77WAVE.o   -lf2c \\napp < input > tmp.out \\nCPU-time: 255.28   f95 -O0 formatted I/O \\nf95 -c -O4  versions/main_wIO.f F77WAVE.f \\nf95 -o app  -static main_wIO.o F77WAVE.o   -lf2c \\napp < input > tmp.out \\nCPU-time: 251.43  f95 -O0 formatted I/O \\nf95 -c -O5  versions/main_wIO.f F77WAVE.f \\nf95 -o app  -static main_wIO.o F77WAVE.o   -lf2c \\napp < input > tmp.out \\nCPU-time: 255.90   f95 -O0 formatted I/O \\nf95 -c -O6  versions/main_wIO.f F77WAVE.f \\nf95 -o app  -static main_wIO.o F77WAVE.o   -lf2c \\napp < input > tmp.out \\nCPU-time: 252.15   f95 -O0 formatted I/O' >> output.txt")
get_ipython().system("grep -w '^CPU-time' output.txt | awk '{ print $2 }' | sort")


# ### Excercise 7:

# In[ ]:


#Make a copy of your working directory along with its subdirectories and 
#write unix+python commands that traverses the copied working directory and its subdirectories (recursively) and returns a 
#list of all files that are larger than X Mb and that have not been accessed the last Y days, 
#where X and Y are passed as user inputs.
#Include an option in this function that moves the files to a subdirectory trash under /tmp 
#(you need to create trash if it does not exist).


# In[21]:


get_ipython().run_line_magic('cd', '~/Documents/')
get_ipython().system('cp -r DSE DSE_copy')


# In[70]:


get_ipython().system('find DSE_copy -type f -size +1M -atime -10 ')


# In[77]:


#!/bin/bash

get_ipython().set_next_input('echo what is max file size');get_ipython().run_line_magic('pinfo', 'size')

read size

find DSE_copy -type f -size +size

