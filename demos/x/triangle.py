import random 


#Defined a function - I specified what it is ,what it does and what name is attacehed to it
#Parameter - data given into the function
#Default parameters - some data that woud be used ,if not given an argument
def calc_area(h = 4, b = 6):
    # h = float(input("Enter height: "))
    # b = float(input("Enter base: "))
    area = h*b*0.5
    # print(area)
    return area
def run():
  
    print(calc_area(random.randint(1, 10), 5))
    a1 = calc_area(15, 8)
    a2 = calc_area(6, 9)
    if a1>a2:
      print("Area 1 was larger")
    print(calc_area(100))
    calc_area(b=20)
    calc_area()

run()