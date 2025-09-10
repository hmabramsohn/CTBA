# Libraries
import dash
import requests
from dash import html, dcc, callback, Output, Input

# Register page
dash.register_page(__name__, path="/page2", name="Page 2")
# Layout; app is called in app.py, so you don't need full app.layout call
layout = html.Div([
    html.H2("Page 2", className="page-title"),
    html.P("Click to fetch a random cat fact from a public API", className="page-subtitle"),
    html.Button("Get Cat Fact", id = "btn-cat", n_clicks=0),
    dcc.Loading(
        html.Div(id="cat-fact"))
], className="page2-wrap")

@callback(
    Output("cat-fact", "children"),
    Input("btn-cat", "n_clicks")
)
def get_cat_fact(n):
    # Error handling
    try:
        # API with timeout 
        r = requests.get("https://catfact.ninja/fact", timeout=5)
        r.raise_for_status
        # Parse JSON and get fact
        fact = r.json().get("fact", "No Fact Found")
        return html.Div(fact)
    except requests.RequestException as e:
        return html.Div(f"Error Contacting API: {e}")