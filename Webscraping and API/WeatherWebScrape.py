# Assisted by Professor Schlosser
# Call public weather API for multiple Virginia cities.
# Output clean, comparable table of current conditions.
# Use Open-Meteo API to request city latitudes and longitudes.
# Find weather at each coordinate, retrieve, parse, and extract weather details, and display as a table with pandas.

import pandas as pd
import requests

# Sample cities; hardcoded coordinates
cities_va = {
    "Williamsburg": (37.2707, -76.7075),
    "Richmond": (37.5407, -77.4360),
    "Virginia Beach": (36.8529, -75.9780),
    "Roanoke": (37.27097, -79.94143),
    "Charlottesville": (38.0293, -78.4767)
}

url = "https://api.open-meteo.com/v1/forecast"

results = []

# Call .items() in for loop in order to call key:value pairs
for city, (lat, lon) in cities_va.items():
    
    # Set parameters for GET request
    params = {
        "latitude": lat,
        "longitude": lon,
        "current_weather": True
    }
    
    # Save responses with params
    response = requests.get(url, params=params)
    # Convert response to python dictionary
    data = response.json()
    
    # Check for existing data and append to results if existing
    if "current_weather" in data:
        weather = data["current_weather"]
        results.append({
            "City": city,
            "Temperature (C)": weather["temperature"],
            "Wind Speed (m/s)": weather["windspeed"],
            "Time": weather["time"]
        })
    # Post None if no data exists for location
    else:
        results.append({"City": city,
                        "Temperature (C)": None,
                        "Wind Speed (m/s)": None,
                        "Time": None})
        
# Fit to pandas DataFrame
df = pd.DataFrame(results)
print(df)