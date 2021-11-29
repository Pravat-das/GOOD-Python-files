# to use a file 1st use the open() function
# open function takes two parameters filename and mode
"""some modes are :
1)"r" -read - opens a file for reading.throws error if the file doesnot exist
2)"a" - Append - Opens a file for appending at the end, creates the file if it does not exist
3)"w" - Write - Opens a file for writing or overwriting, creates the file if it does not exist
4)"x" - Create - Creates the specified file, returns an error if the file exists
5)"t" - Text - Default value. Text mode
6)"b" - Binary - Binary mode (e.g. images)"""
# read() function reads current file

""" f=open("file.txt","r");
 print(f.read());
 print(f.read(10))    # read some parts of a file
 print(f.readline());   #  read a line of a file
 print(f.readline());"""
#  looping through a file to get all content
"""for words in f:
    print(words)
f.close();"""

# =================================================================

# python file appending() . using this function multiple times
# will append the file many times
"""f=open("file.txt","a");
f.write(("\n i like python language"))
f.close();
f=open("file.txt","r");
print(f.read())"""

# overwrite content to the file using "w" or write mode

"""f=open("file.txt","w")
f.write("i have successfully written a line\n")
f.write("i have successfully written another line\n")
f.close
f=open("file.txt","r")
print(f.read())"""

# create a file in python using "x" mode
'''but create file once. ok'''
#  newfile=open("newfile.txt","x")
"""newfile=open("newfile.txt","w")
newfile.write("this is a new file");
newfile.close();"""

# check if a file exist in the directory use os module
"""import os
if os.path.exists("newfile.txt"):
    print("file exists bro!!!");
else:
    pass"""

# remove a file from the directory
# newfile1=open("anotherfile.txt","x");
"""import os
if os.path.exists("anotherfile.txt"):
    os.remove("anotherfile.txt")
else:
    print("file doesnot exist")"""

# creating a folder in python and adding a file into it 
# then writing some content to it
# to crete a file inside the folder give path name followed by dot (.)
# then u r done ok.

"""
import os
folder=os.makedirs("./pythonfolder/");
fileinfolder=open("C:\Web Development\python practice\pythonfolder\data.txt","x");
insidefolder=open("./pythonfolder/data.txt","w");
insidefolder=open("./pythonfolder/data.txt","r");
"""

"""insidefolder.write("i am firstline file inside of another folder\n")
insidefolder.write("i am second line of file inside of another folder\n")
"""

"""for data in insidefolder:
    print(data)
insidefolder.close()"""

# creating a folder an deleting it
import os
# folder2=os.makedirs("./temporaryfolder")
if os.path.exists("temporaryfolder"):
    os.rmdir("temporaryfolder");
    print("folder deleted successfully")
else:
    print("folder doesnot exist")
