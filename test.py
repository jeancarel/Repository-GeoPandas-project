import os
import geopandas as gpd
import pandas as pd

rencontre = pd.read_json("dataset arretBus", orient='index')


print(rencontre)