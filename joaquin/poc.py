import rasterio as rio
import numpy as np
from dataset import unpack_tiff
from rasterio.plot import show

# impervious_labels_fp = 'nlcd-tahoe/NLCD_2021_Impervious_L48_20230630_841FlORuKKMs6XJoybmJ.tiff'
landcover_fp = 'nlcd-tahoe/NLCD_2021_Land_Cover_L48_20230630_841FlORuKKMs6XJoybmJ.tiff'
impervious_fp = 'nlcd-tahoe/NLCD_2021_Impervious_descriptor_L48_20230630_841FlORuKKMs6XJoybmJ.tiff'

# unpack the tiffs
landcover = unpack_tiff(landcover_fp)
impervious = unpack_tiff(impervious_fp)


with rio.open(landcover_fp) as src:
    landcover = src.read(1)

with rio.open(impervious_fp) as src:
    impervious = src.read(1)

# create an overlay where labels overlap with the descriptor
impervious_undeveloped = np.where((landcover == 21) & (impervious == 24), 1, 0)

# show the overlay
show(impervious_undeveloped, cmap='viridis', title='Impervious Overlay')