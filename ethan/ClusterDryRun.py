import rasterio
from matplotlib import pyplot as plt
import numpy as np
from sklearn.cluster import KMeans
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

image_path = '.tiff image'

#Open the raster dataset
dataset = rasterio.open(image_path)

#Read the single band
band_data = dataset.read(1)

#Histogram Analysis
fig, ax = plt.subplots(figsize=(8, 5))

#Exclude zero value from histogram
non_zero_values = band_data[band_data != 0].flatten()
hist_values, bin_edges, _ = ax.hist(non_zero_values, bins=50, color='blue', alpha=0.7)
ax.set_title('Histogram (Excluding Zero)')
ax.set_xlabel('Pixel Value')
ax.set_ylabel('Frequency')

plt.tight_layout()
plt.show()

# Convert histogram values to a scatter plot
fig, ax = plt.subplots(figsize=(8, 5))

# Use bin centers as x-values
bin_centers = (bin_edges[:-1] + bin_edges[1:]) / 2

# Plot scatter plot
ax.scatter(bin_centers, hist_values, color='red', marker='.')
ax.set_title('Scatter Plot of Pixel Values (Excluding Zero)')
ax.set_xlabel('Pixel Value')
ax.set_ylabel('Frequency')

# Prepare data for clustering
data_stack = np.column_stack((bin_centers, hist_values))

# Normalize data using MinMaxScaler
scaler = MinMaxScaler()
scaled_data = scaler.fit_transform(data_stack)

# Perform K-Means clustering with different values of K
k_rng = range(1, 40)
sse = []  # Sum of Squared Errors
for k in k_rng:
    km = KMeans(n_clusters=k)
    km.fit(scaled_data)
    sse.append(km.inertia_)

# Plot the Elbow Curve to See Optimal K-value
fig, ax = plt.subplots(figsize=(8, 5))
ax.plot(k_rng, sse, marker='o')
ax.set_title('Elbow Method for Optimal K')
ax.set_xlabel('Number of Clusters (K)')
ax.set_ylabel('Sum of Squared Errors (SSE)')

plt.tight_layout()
plt.show()


#Elbow method shows that K should equal 3 based off range
km = KMeans(n_clusters=3)
km.fit(scaled_data)

# Get cluster labels
cluster_labels = km.labels_

# Plot scatter plot with cluster assignments
fig, ax = plt.subplots(figsize=(8, 5))
scatter = ax.scatter(bin_centers, hist_values, c=cluster_labels, cmap='viridis', marker='.')
ax.set_title('Scatter Plot of Pixel Values with 3 Clusters')
ax.set_xlabel('Pixel Value')
ax.set_ylabel('Frequency')
plt.colorbar(scatter, label='Cluster')
plt.tight_layout()
plt.show()





