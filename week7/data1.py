import matplotlib.pyplot as plt

x = [0,2,4,6,8,10]
y = [0,20,40,60,80,100]

plt.xlabel("x values")
plt.ylabel("y values")

#plt.plot(x, y)
plt.plot(x, y, "o")
plt.step(x, y)
plt.bar(x, y)
plt.savefig("line.png")
plt.show()