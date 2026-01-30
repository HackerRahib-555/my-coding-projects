import matplotlib.pyplot as plt
x = [1, 2, 3, 4, 5, 6, 7, 8]
y = [12, 6.7, 2, 5, 8, 6.66, 1, 29]
a = [1, 2, 3, 4, 5, 6, 7, 8]
b = [13, 7, 5, 8, 19.67, 4, 6.7, 9.99]
plt.plot(x, y, marker='^', color="green", label="Numbers Number")
plt.plot(a, b, marker='x', color="purple", label="Decimated Number")
plt.title("random numbers")
plt.xlabel("NPC numbers")
plt.ylabel("Kooler numbers")
plt.legend()
plt.show()

