from person import Person
from database import Database 

db = Database("Piotr")
print(f"Welcome to {db.name}")

while True:
    print('''
        \nChoose an option:
          1-Add a new member
          2-Remove a member
          3-Display all members
          4-Exit        
          ''')
    opt = int(input("Enter choice: "))
    if opt == 1:
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        p = Person(name, age)
        db.add_person(p)
    elif opt == 2:
        name = input("Enter name of person to be removed: ")
        for person in db.people:
            if person.name == name:
                db.remove_person(person)
    elif opt == 3:
        db.display_all()
    elif opt == 4:
        break