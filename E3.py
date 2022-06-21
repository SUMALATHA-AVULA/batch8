"""Exercise 3: Print characters from a string that are present at an even index number
Write a program to accept a string from the user and display characters that are present at an even index number.
For example, str = "pynative" so you should display ‘p’, ‘n’, ‘t’, ‘v’.

Expected Output:

Orginal String is  pynative
Printing only even index chars
p
n
t
v
"""


str=input("sample string: ")
print("Original String is ", str)
print("Printing only even index chars")
count=0
for i in str:
        if(count%2==0):
            print(i,"\n")
        count=count+1
        
