# # create a dictionary and display it's keys alphabetically
# dict = {
#     "name": "pravat",
#     "age": "20",
#     "gender": "male"
# }

# # 2) calculate multiplication and division of 2 numbers


# def mult_div(a, b):
#     product = a*b
#     if product <= 1000:
#         return product
#     else:
#         return a+b


# result1 = mult_div(20, 30)
# result2 = mult_div(40, 30)
# print("result is : ", result1)
# print("result is : ", result2)

# """ wap to iterate 1st 10 numbers and in each iteration print the sum of current
#  and previous number"""
# previous = 0
# for i in range(1, 11):
#     sum = previous+i
#     print("current number : ", i, "previous no : ", previous, "sum : ", sum)
#     previous = i
# """wap to accept a string from a user and display characters which are
# present at even index number"""
# userinput = input("Enter a word : ")
# x = list(userinput)   # converted to a list first
# for i in x[::2]:
#     print(i)
# """wap to remove characters from a string starting from 0 upto n
# and return a new string"""
# word="pravat";
# x=word[3:];
# print(x);
"""wap that returns true if the first and last number of a given list
is same otherwise returns false"""
# def firstlastsame(numlist):
#     firstnum=numlist[0];
#     lastnum=numlist[-1];
#     if firstnum==lastnum:
#         return True
#     else:
#         return False
# samenumbers=[10,20,30,40,50,10];
# print("result is : ",firstlastsame(samenumbers));
# differentnums=[10,20,30,40,50,6]
# print("result is : ",firstlastsame(differentnums));
"""wap to create a new list which contains odd numbers for 1st list
and even numbers for 2nd list"""
# def lists(list1, list2):
#     resultlist = []

#     for i in list1:
#         if i % 2 != 0:
#             resultlist.append(i)
#     for j in list2:
#         if j % 2 == 0:
#             resultlist.append(j)
#     return resultlist
# list1 = [10, 20, 25, 30, 35]
# list2 = [40, 45, 60, 75, 90]
# print("result is : ", lists(list1, list2))
"""print multiplication table"""
# for i in range(1,11):
#     for j in range(1,11):
#         print(i*j,end=" ");
#         print("\t\t");
"""print half pyramid pattern with asterisk downward"""
# for i in range(6,0,-1):
#     for j in range(0,i,-1):
#         print("*",end=" ");
#         print(" ");
"""wap to extract each digit from an integer in an reverse order"""
# num=1205;
# while num>0:
#     digit=num%10
#     num=num//10
#     print(digit,end=" ");
"""wap to demonstrate palindrome of the string"""
def palindrome(a):
    mid=(len(a)-1)//2;
    last=len(a)-1
    start=0
    flag=0
    while(start<mid):
        if(a[start]==a[last]):
            start+=1
            last-=1;
        else:
            flag=1
            break
        if flag==0:
            print("palindrome string");
        else:
            print("not palindrome");
palindrome(121)



