"""Exercise 1: Calculate the multiplication and sum of two numbers

Given two integer numbers return their product only if the product is greater than 1000, else return their sum."""
val1=input("number1 =")
val2=input("number2 =")
product=int(val1)*int(val2)
add=int(val1)+int(val2)
if product<=1000:
    print("result is ", product)
else:
    print("result is", add)
