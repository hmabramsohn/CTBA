# Commonly used filename (alt: index) for homepage

# Libraries
import dash
from dash import html

# Register to hub; Root URL is represented as "/"
dash.register_page(__name__, path="/")
# Layout; app is called in app.py, so you don't need full app.layout call
layout = html.Div([
    html.H2("Welcome to my Home Page"),
])