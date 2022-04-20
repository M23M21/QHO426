import triangle

print(f"Area of triangle is {triangle .calc_area(19, 19)}")


import triangle as t

print(f"Area of triangle is {t .calc_area(19, 19)}")


from triangle import calc_area
print(f"Area of triangle is {calc_area(8, 10)}")

from triangle import calc_area as tri
print(f"Area of triangle is {tri(8, 15)}")



from demos.x.triangle import *
print(f"Area of triangle is {calc_area(8, 20)}")
run()