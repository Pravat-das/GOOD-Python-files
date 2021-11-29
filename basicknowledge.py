# python is an interpreted language this means whwe we write .py files
# in the text editor and put those files into pthon interpreter
# to be executed
print("hello world . i am a python programmmer")

# i am a single line comment
"""i 
 am 
 a 
 multiline 
 comment """

#  variables
x = 5
y = "pravat"
print(x, y)
# type casting is used to convert a datatype to another datatype
num1 = 5.0
print(type(num1))
x1 = int(num1)   # convert it to integer type
print(type(x1))

# unpacking a collection in python
# unpacking is done for exact elements
fruits = ["apple", "grapes", "pineapple", "starwberry"]
f1, f2, f3, f4 = fruits
print(f1)
print(f2)
print(f3)
print(f4)

# + operator is used for adding both text and variable
x = "good language"
print("python is a "+x)
# global variables are created outside of a function
# lobal variables can be used in both inside and outside of
# a function.
number = 100
def function1():
    print("number is", number)
function1()
