"""Exercise 2: Print the sum of the current number and the previous number"""
print("Printing current and previous number sum in a range(10)")
per=0
for i in range(10):
        Xnum=i+per
        print(f'Current Number {i} Previous Number {per} Sum: {Xnum}')
        per=i
