# Build an interactive dashboard displaying data and summary statistics for weather from open-meteo API
# Include a city selection dropdown, current and future temperature readings and graph, and summary statistics

# Libraries for API
import requests

# Libraries for data wrangling
import pandas as pd
from datetime import datetime as dt

# Libraries for visualization (dash)
from dash import Dash, html, dcc, Input, Output
import dash_bootstrap_components as dbc
import plotly.express as px

# City coordinates
CITY_COORDS = {
    "Williamsburg": (37.2707, -76.7075),
    "Richmond": (37.5407, -77.4360),
    "Virginia Beach": (36.8529, -75.9780),
    "Roanoke": (37.27097, -79.94143),
    "Charlottesville": (38.0293, -78.4767)
}

# Function for api
def fetch_hourly_temp(lat: float, long: float) -> pd.DataFrame:

