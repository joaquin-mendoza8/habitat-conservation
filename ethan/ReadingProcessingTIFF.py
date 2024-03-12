#READING PROCESSING TIFF

import rasterio
from rasterio.plot import show
from matplotlib import pyplot as plt

#opening dataset
image = '.tiff image'
dataset = rasterio.open(image)

#displaying dataset
show(dataset)

#metadata extraction
resolution = dataset.res
crs = dataset.crs
extent=  dataset.bounds
bands = dataset.count

print("\nMetadata:")
print(f"Resolution: {resolution}")
print(f"CRS: {crs}")
print(f"Extent: {extent}")
print(f"Bands #: {bands}")

#performing histogram analysis
fig, ax = plt.subplots(figsize=(8, 5))

#because there is only one band in given dataset
band_data = dataset.read(1)

#flattening and plotting histogram
ax.hist(band_data.flatten(), bins=50, color='blue', alpha=0.7)
ax.set_title('Histogram')
ax.set_xlabel('Pixel Value')
ax.set_ylabel('Frequency')

plt.tight_layout()
plt.scatter()
plt.show()

# Basic statistical/numerical analysis
print("\nStatistics:")
print(f"  Minimum: {band_data.min()}")
print(f"  Maximum: {band_data.max()}")
print(f"  Mean: {band_data.mean()}")
print(f"  Standard Deviation: {band_data.std()}")