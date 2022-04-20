#Declare an empty list
bleh = []
meh = list()
#Declare non-empty list
yummy = ["Pizza", "Lasagna", "Spaghetti Bolognese"]
#Print entire list
print(yummy)
#Print single item
print(yummy[2])
#Printing some elements
print(yummy[:2])
#Add elements to our list (expand it) - adding elements at the end
print(bleh)
bleh.append("Fish")
bleh.append("Coconut")
bleh.append("Onion")
bleh.append("Chocolate")
print(bleh)
#Add multiple items  to the list, based on user input
n = int(input("How many items to add?"))
for i in range(n):
    yummy.append(input("Enter a new yummy food: "))
print(yummy)
#Adding data at any point inside of a list
print(bleh)
bleh.insert(1,"Mashed Potatoes")
print(bleh)
bleh.insert(3, "Cabbage")
print(bleh)
#Remove an item from list
if "Frankfurters" in bleh:
    bleh.remove("Frankfurters")
if "Coconut" in bleh:
    bleh.remove("Coconut")  
print(bleh)
#Remove item via index
x = bleh.pop(2)
print(bleh)
print(x)
#Alternative way of deliting via index
del bleh[1]
print(bleh)
#Extending a list
print(yummy)
yummy.extend(["Fish", "Bacon", "Ketchup"])
print(yummy)
#Checking for particular data type
lista = ["Fred", True, 6, 8, -7.88, False, "Lalala", 55]
total = 0
for item in lista:
    if isinstance(item, int):
        total += item
print(total)
