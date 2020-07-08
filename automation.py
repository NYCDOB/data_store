import pandas as pd
import numpy as np
from arcgis.features import SpatialDataFrame
import arcgis
from arcgis import GIS
from arcgis import gis
from arcgis.features import FeatureLayer


gis = GIS("https://nycdobenforce.maps.arcgis.com/home/index.html", username="TahAlam@DOB", password="bldgvis20@")

known_item = gis.content.get("a3648b4038f84c3f8dee86affd1b075e")

fl = known_item.tables[0]

print("Extracting Table...")

# Use the `from_layer` method of the Spatial DataFrame to create a new Spatial DataFrame
sdf = SpatialDataFrame.from_layer(fl)

df = sdf.copy()
df = df[df["site_status"]!="Closed"]
df["inspStart"] = pd.to_datetime(df["inspStart"])
df["inspStart"] = df["inspStart"].dt.strftime("%m/%d/%y %H:%M")
df = df.reset_index(drop=True)

## save the file to local directory
path = "C:\\Users\\tahsi\\uploadingFolder\\"
df.to_csv(path+'Phase_1_Site_Inspections_2.csv',index=False)

print("Done!!File saved.")
