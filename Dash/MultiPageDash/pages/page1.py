# Libraries
import dash
from dash import html

# Register page
dash.register_page(__name__, path="/page1", name="Page 1")
# Layout; app is called in app.py, so you don't need full app.layout call
layout = html.Div([
    # Top row
    html.Div("Top (1st Row)", className="block block-top"),
    # Middle row; 2 columns
    html.Div([
        html.Div("Middle Left", className="block"),
        html.Div("Middle Right", className="block")
    ],
        className = "row-2"
    ),
    html.Div("Footer", className="block block-footer")
], className= "page1-grid"
)