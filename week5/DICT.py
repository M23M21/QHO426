
#Instantiate empty dictionary
dicto = {}
d = dict()
#Instantiate non-empty dictionary
phonebook = {"Thomas":"077023746374", "Aga":"077326352763", "Udoh": "077736543645"}
#Print full dictionary
print(phonebook)
#Print individual elements
print(f' Calling {phonebook["Udoh"]}')
#Zipping two lists together
names = ["Jagoda", "Frank", "Ludovico"]
ages = [19, 72, 33, 67]
people = dict(zip(names, ages))
print(people)
#Traverse dictionary
for i in people:
    print(i)
for i in people.values():
    print(i)
for i,j in people.items():
    print(f"Person {i} is {j} years old")