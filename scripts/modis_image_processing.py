import pandas as pd
import geemap
import ee
import os
import datetime
import numpy as np

ee.Authenticate()
ee.Initialize(project='###')


start_date = pd.to_datetime('2000-01-01')
end_date = pd.to_datetime('2023-08-01')
dates_list = pd.date_range(start='2000-08-01', freq='YS-AUG', periods=24)

lat, lon = 22.833, 32.500
point = ee.Geometry.Point([lon, lat]).buffer(distance=5000)

# Preparing the list of images

image_collection = []
for date in dates_list:
    bands = ['sur_refl_b02', 'sur_refl_b04', 'sur_refl_b03']  
    MOD = ee.ImageCollection("MODIS/061/MOD09GA")\
            .filterDate(start=date)\
            .filterBounds(point)
    image_collection.append(ee.Image(MOD.first()))

map = geemap.Map(center=[lat, lon], zoom=8)

roi = ee.Geometry.Rectangle([32.3, 22.7, 32.7, 22.9]) 

# Defining visualization parameters for the images
visual_params = {
    'min': -100.0,
    'max': 8000.0
}

map.add_ee_layer(image_collection[0].select(bands).clip(roi), visual_params)


# Converting the list of images into a time series
col = geemap.create_timeseries(
    ee.ImageCollection(image_collection),
    start_date='2000-01-01',
    end_date='2023-08-01',
    region=roi,
    bands=bands
)

# Modifying images using visualization parameters
col = col.select(bands).map(
    lambda img: img.visualize(**visual_params).set({
        "system:time_start": img.get("system:time_start"),
        "system:date": img.get("system:date"),
    })
)

# Video settings
video_args = {
    "dimensions": 768,
    "region": roi
}


out_dir = ''
count = col.size().getInfo()
basename = 'MOD'
names = [
    os.path.join(out_dir, f"{basename}_{str(i + 1).zfill(len(str(count)))}.jpg")
    for i in range(count)
]

geemap.get_image_collection_thumbnails(
    col,
    './MOD',
    vis_params={"min": 0, "max": 255, "bands": video_args["bands"]},
    dimensions=768,
    names=names
)

# Creating GIF
geemap.make_gif(
    ['./MOD/' + x for x in names],
    'MOD.gif',
    fps=2,
    mp4=False,
    clean_up=True
)

# GIF with date
geemap.add_text_to_gif(
    'MOD.gif',
    'MOD.gif',
    text_sequence=[x.strftime('%Y-%m-%d') for x in dates_list],
    font_size=24,
    font_color='white',
    duration=1000 / 3,
    font_type=None  
)

# Final video settings
video_args["framesPerSecond"] = 30
video_args["crs"] = "EPSG:3857"
video_args["min"] = 0
video_args["max"] = 255
video_args["bands"] = ["vis-red", "vis-green", "vis-blue"]
