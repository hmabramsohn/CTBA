# Libraries
import dash
from dash import html

# Register page
dash.register_page(__name__, path="/page2", name="Page 2")
# Layout; app is called in app.py, so you don't need full app.layout call
layout = html.Div([
    
])