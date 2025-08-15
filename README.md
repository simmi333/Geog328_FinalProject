# Tracking Carbon Emissions in Europe

## Project Description
This project aims to create an interactive web map that visualizes carbon emissions across European countries on a per capita basis. The map highlights countries with both high and low carbon emissions, allowing users to explore trends, compare data, and understand the factors influencing emissions. The goal is to provide a tool for policymakers, environmental organizations, and the general public to better understand carbon emissions and identify strategies for reducing them.

## Project Goal
The primary goal of this project is to deliver a clear and interactive visualization of carbon emissions in Europe, emphasizing the importance of per capita measurements to ensure fair comparisons between countries of different sizes. By highlighting both high and low emissions countries, the project aims to:
- Raise awareness about the impact of population growth and energy consumption on carbon emissions.
- Encourage discussions on effective strategies for reducing carbon footprints.
- Provide a resource for policymakers, educators, and the public to explore and compare emissions data.

## Application URL
https://jordanchiang627.github.io/Geog328_FinalProject/

## Screenshots
![1950 Carbon Emissions in Europe](images/screenshot1950.png)
Europe Carbon Emission (1950)
![2023 Carbon Emissions in Europe](images/screenshot2023.png)
Europe Carbon Emissions (2023)

## Main Functions
- **Interactive Map**: Visualize carbon emissions per capita and total CO₂ emissions for European countries.
- **Color Gradient**: Use a color gradient to represent emissions per capita (green for low, yellow for medium, red for high).
- **Circle Size**: Represent total CO₂ emissions using circle size.
- **Time Slider**: Allows users to explore data from 1950 to 2023.
- **Popup Information**: Displays detailed information (population density and emissions per capita) when hovering over a country.
- **Play Button**: Animates the time slider, progressing through the years from 1950 to 2023. The button can be pressed again to pause. The button will automatically loop.

## Data Sources
- **Per Capita Emissions**: [Our World in Data](https://ourworldindata.org/grapher/co-emissions-per-capita)
- **Population Density**: [Our World in Data](https://ourworldindata.org/grapher/population-density)

## Applied Libraries and Web Services
- **GitHub**: For hosting the repository and deploying the web application.
- **Excel**: For initial data cleaning and preparation.
- **HTML/CSS/JavaScript**: For building the front-end interface.
- **Turf.js**: For geospatial analysis (e.g., calculating centroids).
