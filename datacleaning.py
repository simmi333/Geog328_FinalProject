# flake8: noqa

import pandas as pd
import geopandas as gpd

def geojson_to_file(df, output):
    df.to_file(output, driver = 'GeoJSON')
    print(f"Cleaned Data saved to: {output}")

def merge_clean(gdf, df, left, right, drops):
    merged_gdf = gdf.merge(df, left_on = left, right_on = right, how = "inner")
    merged_gdf = merged_gdf.drop(columns = drops)
    return merged_gdf

CountriesShape = gpd.read_file("countries.geo.json")
CountriesShape = CountriesShape.to_crs(epsg = 4326)
CountriesShape['Centroids'] = CountriesShape.geometry.centroid
CountriesPoint = CountriesShape[['id','name', 'Centroids']].set_geometry('Centroids')
emissions = pd.read_csv("CleanedData/EuropeCo2.csv")
density = pd.read_csv("CleanedData/EuropePopD.csv")

CountryEmissions = merge_clean(CountriesShape, emissions, "id", "Code", ["Entity", "Code"])
CountryEmissions = CountryEmissions.rename(columns = {'Annual CO₂ emissions (per capita)':'Emissions'})
CountryEmissions = CountryEmissions.drop(columns = ['Centroids'])

CountryDensity = merge_clean(CountriesPoint, density, "id", "Code", ["Entity", "Code"])
CountryDensity = CountryDensity.rename(columns = {'Population density':'PopDensity'})

geojson_to_file(CountryEmissions, "CleanedData/Emissions.geojson")
geojson_to_file(CountryDensity, "CleanedData/Density.geojson")