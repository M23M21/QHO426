#Initialise empty set
s = set()
s1 = {"Garry", "Harry"}
#print(type(s1))
#Initialise non-empty set
colours = {"blue", "orange", "yellow", "purple", "black"}
print(colours)
#Add elements to set
colours.add("white")
colours.add("red")
colours.add("green")
print(colours)
colours.add("orange")
colours.add("black")
print(colours)
#Remove items from set
if "red" in colours:
    colours.remove("red")
if "Yellow" in colours:
    colours.remove("Yellow")
print(colours)
#Checking membership
col = input("Enter a colour: ")
if col in colours:
    print("Yay - my favourite colour!")
else:
    print("My colour is not there")
x = {"cyan", "purple", "burgundy", "white", "green"}
#Union - joining two sets together, not keeping duplicates
c2 = colours.union(x)
print(c2)
print(x)
print(colours)
#Intersection - looking at common elements
c3 = colours.intersection(x)
print(c3)
#Difference =- keep only elements of one set, but NOT the other
c4 = colours.difference(x)
c5 = x.difference(colours)
print(c4)
print(c5)