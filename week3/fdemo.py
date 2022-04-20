
def Rectangle(width, height):
   #calculate the area
   Area = width * height
   Perimeter = 2 * (width + height)
  #calculate the Perimeter
   print("\n Area is : %.2f" %Area)
   print("Perimeter is : %.2f" %Perimeter)

width = float(input("Enter the width: "))   
height = float(input("Enter the lenght: "))

Rectangle(width, height)
  