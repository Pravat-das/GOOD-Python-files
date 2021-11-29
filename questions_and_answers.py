# write a program to find sum of digits of a given number
"""input1=int(input("Enter the number"));
sum=0;
while(input1>0):
    sum=(sum+input1)%10
    input1=input1//10
print("sum of digits ",sum)"""
# wap to find the sum of square of digits of a gisven number
"""input1=int(input("Enter the number"))
sum=0;
while(input1>0):
    sum=sum+(input1%10)*(input1%10);
    input1=input1//10
print("sum of square of each digits ",sum)"""
# wap to find the sum of cubs of digits of a given number
"""input1=int(input("Enter the number"))
i=input1
sum=0
while(i>0):
    sum=sum+(i%10)*(i%10)*(i%10)
    i=i//10
print("sum of cube of the number is : ",sum)"""
# wap to check wheather a given number is armstrong or not
# armstrong==>add digits of a number with it's power to get the same number
"""input1=int(input("Enter the number"))
original=input1
sum=0
while(input1>0):
    sum=sum+(input1%10)*(input1%10)*(input1%10)
    input1=input1//10
if original==sum:
    print("number is armstrong")
else:
    print("number is not armstrong");"""
# wap to generate armstrong numbers between 100 to 1000
lowernumber=int(input("Enter the starting number"));
uppernumber=int(input("Enter the boundary limit"))
for i in range(lowernumber,uppernumber):
    sum=0
    temp=i
    while temp>0:
        digit=temp%10
        sum+=digit**3
        temp//=10
    if i==sum:
        print(i)
# 


