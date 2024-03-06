import rasterio as rio
from rasterio.plot import show


# unpack a tiff for overlay
def unpack_tiff(fpath):

    # unpack the tiff file
    with rio.open(fpath) as src:
        return {
            'data': src.read(),
            'transform': src.transform,
            'crs': src.crs,
            'bounds': src.bounds,
            'meta': src.meta
        }
