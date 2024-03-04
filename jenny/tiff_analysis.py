import rasterio
from rasterio.plot import show
import matplotlib.pyplot as plt
import numpy as np

# Step 1: Read the dataset into a Python variable using Rasterio
dataset_path = 'dataset.tiff'
dataset = rasterio.open(dataset_path)

# Step 2: Extract metadata using Rasterio
resolution = dataset.res
crs = dataset.crs
extent = dataset.bounds
num_bands = dataset.count

print("Resolution:", resolution)
print("CRS:", crs)
print("Extent:", extent)
print("Number of bands:", num_bands)

# Step 3: Display the dataset using Matplotlib
fig, ax = plt.subplots(figsize=(10, 10))
show(dataset, ax=ax)
plt.show()

# Step 4: Perform histogram analysis or basic statistical/numerical analysis
# Read all bands into a NumPy array
bands_data = dataset.read()

# Flatten the data for histogram analysis
flat_data = bands_data.flatten()

# Plot histogram
plt.figure(figsize=(10, 6))
plt.hist(flat_data, bins=50, color='blue', alpha=0.7)
plt.xlabel('Pixel Value')
plt.ylabel('Frequency')
plt.title('Histogram of Pixel Values')
plt.grid(True)
plt.show()

# Basic statistical analysis
print("Basic statistical analysis:")
print("Min value:", np.min(flat_data))
print("Max value:", np.max(flat_data))
print("Mean value:", np.mean(flat_data))
print("Standard deviation:", np.std(flat_data))
