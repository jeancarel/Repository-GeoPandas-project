import geopandas as gpd
import matplotlib.pyplot as plt
import os

def poly(agri, qualite):
    # Fusionner les GeoDataFrames en une seule géométrie unifiée
    union_agri = agri.unary_union
    union_qualite = qualite.unary_union
    
    # Fusionner les deux géométries unifiées en une seule
    fusion = union_agri.union(union_qualite)
    
    # Créer un GeoDataFrame contenant le polygone fusionné
    polygone = gpd.GeoDataFrame(geometry=[fusion], crs=agri.crs)
    
    return polygone

# Chemins vers les fichiers shp
chemin_agri = r"C:\Users\boaca\OneDrive\Bureau\Projet GeoPandas M1\Zada\Zada\agri.shp"
chemin_qualite = r"C:\Users\boaca\OneDrive\Bureau\Projet GeoPandas M1\Zada\Zada\qualite.shp"
fusion_agri_qualite = r"C:\Users\boaca\OneDrive\Bureau\Projet GeoPandas M1\Zada\Zada\qualite_et_agri.shp"

#  les fichiers shapefiles en GeoDataFrames
agri = gpd.read_file(chemin_agri)
qualite = gpd.read_file(chemin_qualite)
fusion_agri_qualite = gpd.read_file(fusion_agri_qualite)
#pour gerer les geo vides*
agri = agri[~agri.is_empty]
qualite = qualite[~qualite.is_empty]
# Calculer l'intersection entre les deux fichiers
agri_x_quali = gpd.overlay(agri, qualite, how='intersection', keep_geom_type= False)

# Nombre de géométries résultantes après l'intersection
nb_geometries_agri_qualite = len(agri_x_quali)



# Appeler la fonction 
polygone = poly(agri, qualite)

# Extraire la géométrie fusionnée du GeoDataFrame de référence
reference_fusion = fusion_agri_qualite.geometry.unary_union

# Comparer les géométries
is_equal = polygone.iloc[0].geometry.equals(reference_fusion)
print(f"Les géométries sont-elles égales? {is_equal}")

# Afficher les premières lignes du résultat
print("Agri:")
print(agri.head())
print("Qualité:")
print(qualite.head())
print("Fusion de référence:")
print(fusion_agri_qualite.head())
print("ma fusion")
print(polygone.head())
print("Intersection calculée:")
print(agri_x_quali)
print("Nombre de géométries après intersection:", nb_geometries_agri_qualite)
# Afficher le polygone avec matplotlib
#fig, ax = plt.subplots()
#polygone.plot(ax=ax)
#plt.show()

# Afficher les premières lignes des GeoDataFrames d'origine
#print(agri.head())
#print(qualite.head())
#print("la fusion:", fusion_agri_qualite.head())
# Afficher les géométries fusionnées pour visualisation

chemin_sortie = r"C:\Users\boaca\OneDrive\Bureau\Projet GeoPandas M1\Zada\Zada\polygone_fusionne.shp"
polygone.to_file(chemin_sortie, driver='ESRI Shapefile')
# Afficher le polygone avec matplotlib
fig, ax = plt.subplots()
polygone.plot(ax=ax, color='blue', alpha=0.5, label='Fusion Calculée')
gpd.GeoSeries(reference_fusion).plot(ax=ax, color='red', alpha=0.5, label='Fusion de Référence')
plt.legend()
plt.show()
