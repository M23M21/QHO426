from person import Person

class Database:

    def __init__(self, name):
        self.name = name + "'s database"
        self.people = []
        self.no_ppl = len(self.people)

    def add_person(self, p):
        self.people.append(p)
        self.no_ppl += 1

    def remove_person(self, p):
        if p in self.people:
            self.people.remove(p)
        else:
            print("Person was not on the list")
    
    def display_all(self):
        for person in self.people:
            print(person)

if __name__ == "__main__":
    db = Database("Piotr")
    p1 = Person("Tadek", job = "Chef")
    p2 = Person("Renata")
    db.add_person(p1)
    db.add_person(p2)
    db.display_all()
