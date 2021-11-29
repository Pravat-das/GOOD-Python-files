# strings in python are arrays of bytes representing unicode characters
from typing import Text


x="pravat is a good boy";
print(x[1]);
# looping through a string
for i in "python":
    print(i,end="");
# check for a character is present in a string or not
Text="i am a good boy";
print("good" in Text);
print("hello" in Text);
print("hello" not in Text);
#  string slicing in python
str1="python is a good language";
print(str1[0:6])
# replace a string with another string
print(str1.replace("python","java"));
# we can combine strings and methods by using format() method
age=20
txt="my age is {}";
print(txt.format(age));
# another example of string format
person1="ram";
person2="gopal";
text1="{} and {} are my friends";
print(text1.format(person1,person2));
# \b is also called as backspace character
# backspace character removes the previous character
paragraph="hello \b python bhai";
print(paragraph);


