import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import random

# Example dataset (prices)
prices = [random.randint(0, 1000) for i in range(20)]
prices = np.array(prices).reshape(-1, 1)  # Reshape to be a 2D array for KMeans

# Create the initial plot
plt.ion()  # Turn on interactive mode
fig, ax = plt.subplots()
scatter = ax.scatter(prices, [0] * len(prices))  # Initial scatter plot
ax.set_xlabel('Prices')
ax.set_title('K-Means Clustering of Prices')

# Apply KMeans clustering (let's assume 3 clusters)
kmeans = KMeans(n_clusters=4, random_state=0)
kmeans.fit(prices)

# Predict cluster labels
labels = kmeans.labels_

# Update the plot with cluster labels
scatter.set_color(labels)  # Color points based on cluster labels
fig.canvas.draw()  # Update the canvas with the new plot
fig.canvas.flush_events()  # Ensure that the plot is redrawn

# Print the cluster centers
print("Cluster Centers:", kmeans.cluster_centers_)

# Keep the plot open to see the result
plt.ioff()  # Turn off interactive mode to stop updating the plot
plt.show()  # Show the final plot