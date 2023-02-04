import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [n**3 for n in x]

fig, ax = plt.subplots()

ax.set_title(" Cubic numbers", fontsize=20)
ax.set_xlabel("numbers", fontsize=12)
ax.set_ylabel("cubes", fontsize=12)

ax.scatter(x, y)
plt.show()
