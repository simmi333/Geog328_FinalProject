# flake8: noqa

import pandas as pd
import geopandas as gpd

def clean_save(input, output, subset_col, filter_col, filter_value):
    df = pd.read_csv(input)
    df = df[df["Year"] >= 1950]
    df = df.dropna(subset = [subset_col])
    df = df[df[filter_col] != filter_value]
    df.to_csv(output, index = False)
    print(f"Cleaned Data saved to: {output}")

def geojson_to_file(df, output):
    df.to_file(output, driver = 'GeoJSON')
    print(f"Cleaned Data saved to: {output}")

def merge_clean(gdf, df, left, right, drops):
    merged_gdf = gdf.merge(df, left_on = left, right_on = right, how = "inner")
    merged_gdf = merged_gdf.drop(columns = drops)
    return merged_gdf

clean_save("CO2PerCapita.csv", "CleanedData/EmissionsR1Clean.csv", "Code", "Entity", "World")
clean_save("PopDensity.csv", "CleanedData/DensityR1Clean.csv", "Code", "Entity", "World")

CountriesShape = gpd.read_file("countries.geo.json")
CountriesShape = CountriesShape.to_crs(epsg = 4326)
CountriesShape['Centroids'] = CountriesShape.geometry.centroid
CountriesPoint = CountriesShape[['id','name', 'Centroids']].set_geometry('Centroids')
emissions = pd.read_csv("CleanedData/EmissionsR1Clean.csv")
density = pd.read_csv("CleanedData/DensityR1Clean.csv")

CountryEmissions = merge_clean(CountriesShape, emissions, "id", "Code", ["Entity", "Code"])
CountryEmissions = CountryEmissions.rename(columns = {'Annual CO₂ emissions (per capita)':'Emissions'})
CountryEmissions = CountryEmissions.drop(columns = ['Centroids'])

CountryDensity = merge_clean(CountriesPoint, density, "id", "Code", ["Entity", "Code"])
CountryDensity = CountryDensity.rename(columns = {'Population density':'PopDensity'})

geojson_to_file(CountryEmissions, "CleanedData/Emissions.geojson")
geojson_to_file(CountryDensity, "CleanedData/Density.geojson")