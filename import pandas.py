import geopandas as gpd

def poly(agri, qualite):
    fusion = agri.unary_union(qualite.geometry)
    
    # Créer un GeoDataFrame contenant le polygone résultant
    polygone_resultant = gpd.GeoDataFrame(geometry=[fusion], crs=agri.crs)
    
    return polygone_resultant


# Chemins vers les fichiers shapefiles
chemin_agri = r"C:\Users\boaca\OneDrive\Bureau\Projet GeoPandas M1\Zada\Zada\agri.shp"
chemin_qualite = r"C:\Users\boaca\OneDrive\Bureau\Projet GeoPandas M1\Zada\Zada\qualite.shp"
fusion_agri_qualite = r"C:\Users\boaca\OneDrive\Bureau\Projet GeoPandas M1\Zada\Zada\qualite_et_agri.shp"
#  les fichiers shapefiles en GeoDataFrames
agri = gpd.read_file(chemin_agri)
qualite = gpd.read_file(chemin_qualite)
fusion_agri_qualite = gpd.read_file(fusion_agri_qualite)
# essaie d'intersection entre les deux fichiers 

agri_x_quali = gpd.overlay(agri, qualite, how = 'intersection')

nb_geometries_agri_qualite = len(agri_x_quali)
polygone= agri.unary_union.union(qualite.unary_union)
test = poly(agri, qualite)

# Afficher les premières lignes du résultat
print(agri.head())
print(qualite.head())
print("la fusion:", fusion_agri_qualite.head())
print("ma fusion:", agri_x_quali  )
print("- Nombre de géométries :", nb_geometries_agri_qualite)
test.plot()




