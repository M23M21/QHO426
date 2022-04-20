import matplotlib.pyplot as plt

x = [0,2,4,6,8,10]
y = [0,20,40,60,80,100]

plt.xlabel("x values")
plt.ylabel("y values")

xs = range(-100,100,10)
x2 = [x**2 for x in xs]
plt.plot(xs, x2)
plt.savefig("quad.png")
plt.show()