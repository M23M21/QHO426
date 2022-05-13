#The class Person which will be a blueprint for my objects to store information about humans

class Person:

    #Class attribute -> constant, which is visible to all objects of this class
    MAX_W = 150

    #Static Method -> Utility function, which does not require an object of our class to be instantiated

    def is_mature(age):
        if age >= 18:
            return "Person is Mature"
        else:
            return "Person is a child"

    
    #Initialiser/Constructor -> function that is automatically called immediately when a object is created (magic method)
    #"DUNDER" -> Double underscore
    def __init__(self, name = "Bob", age = 0, job = "Unemployed", weight = 50):
        #These are instance attributes (features of any Person object)
        self.name = name
        self.age = age
        self.job = job
        self.weight = weight
    #Magic method str, which is invoked when object is passed into print() function. INFORMAL string representation (communicating with the user)
    def __str__(self):
        return f"Person named {self.name} is {self.age} years old and works as {self.job}. Their weight is {self.weight}kg"

        #Method - function attached to specific data type

        #Instance method to increase weight
    def eat(self, food, w):
        print(f"{self.name} have eaten {food}")
        self.weight += w
        if self.weight > Person.MAX_W:
            self.weight = Person.MAX_W
        print(f"They now weight {self.weight}kg")
    
    def exercise(self, burned):
        self.weight -= burned
        print(f"{self.name} has exercised and now weights {self.weight}kg")

if __name__ == "__main__":
    #Object instantiation
    p1 = Person("Tibi", 28, "Lawyer", 68)
    p2 = Person("Piotr", 7, "Lecturer", 74)
    
    print(p1)
    print(p2)
    p1.eat("Pizza", 1.4)
    p2.eat("Noodles", 0.25)
    print(p1)
    print(p2)
    p1.exercise(2)
    p1.exercise(1.2)
    Person.is_mature(62)
    print(f"{p2.name}"+ Person.is_mature(p2.age))
