#Declare a tuple
p = ("Piotr", 88, False)
y = tuple([3, 6, 9])
#Print tuples
print(p)
print(y)
print(p[1])
print(y[0]*y[2])
#Cannot change values in a tuple => immutable
#y[1] = 7778
#y.append(8)

#Concatenate tuples
z = p + y
print(z)
print(p)
print(y)
#Using min/max functions
print(min(y))
print(max(y))