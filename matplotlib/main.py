import matplotlib.pyplot as plt
import numpy as np

y_points1 = np.array([1, 5, 8, 16])
y_points2 = np.array([1, 10, 4, 20])

plt.plot(y_points1, marker='*')
plt.plot(y_points2, marker='*')

plt.title("Sports Watch Data")
plt.xlabel("Average Pulse")
plt.ylabel("Calorie Burnage")

# Show gird
plt.grid(axis = 'x')

plt.show()
