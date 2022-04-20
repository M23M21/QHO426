print("Please enter the first number: ")
n1 = int(input())
print("Please enter the second number: ")
n2 = int(input())
print("Please enter the third number: ")
n3 = int(input())
odd = 0
even = 0
if n1 % 2 == 0:
    even += 1
else:
    odd += 1
if n2 % 2 == 0:
    even += 1
else:
    odd += 1
if n3 % 2 == 0:
    even += 1
else:
    odd += 1

print("There were {} even numbers and {} odd numbers".format(even, odd))
