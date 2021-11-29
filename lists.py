from typing import Reversible


print("python lists... Part1");
# lists in python are ordered and changeable and allows duplicates
mylist1=["apple","banana",100,10.52,"orange"];
print(mylist1);
print(len(mylist1));
for i in mylist1:
    print(i)
# change a list item
mylist1[2]=2000;
print(mylist1);
# insert item into the list
mylist1.insert(2,"watermelon");
print(mylist1)
# add item at last using append() function
mylist1.append("pinaapple");
print(mylist1);

print("Python lists===========Part 2");
# add another list's item to an existing list using extend() function
firstlist=[10,20,30,40,50,60];
secondlist=["pravat","das","gopal"]
firstlist.extend(secondlist);
print(firstlist);
# pop() method removes the last item with no index mentioned
firstlist.pop();
print(firstlist);
# pop() with given index removes that item
firstlist.pop(1);
print(firstlist);
print(len(firstlist));
for items in firstlist:
    print(items,end=" ");
# ====================================================================
# list sorting using sort() function in ascending order

print("\n");
mylist=["apple","butter","grape","bhindi"];
mylist.sort();
print(mylist);
# sort() a list in decending order alphabetically by using
#  "reverse=True" method
mylist.sort(reverse=True);
print(mylist);
# sort() the list in reverse manner without alphabetically
mylist2=[10,50,45,21,65]
mylist2.reverse()
print(mylist2);
# copy list items
copy_of_mylist2=mylist2.copy()
print(copy_of_mylist2);
copy_of_mylist2.sort();
copy_of_mylist2.sort(reverse=True);
print(copy_of_mylist2);
# another exmaple
marks=[100,45,90,60,50];
marks.reverse();
marks.sort(reverse=True);
marks.sort();
print(marks);


"""write a program to take input of 5 fruits from user and store it 
    in a list """
i = 5
a = []
while i>0:
  print ("Enter fruit name")
  fru = str(input())
  a.append(fru)
  i = i-1;
print (a);



