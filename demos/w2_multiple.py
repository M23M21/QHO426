age = int(input("Enter age: "))
ch = int(input("Enter number of children: "))

if age < 25 and ch > 0 :
  print("you are a young parent")
elif age > 55 and ch > 0:
  print("you will have some support in future")
elif age < 18 or ch == 0:
  print ("There is still time to have a child if you wish ")
else:
  print("you are not so young :(")