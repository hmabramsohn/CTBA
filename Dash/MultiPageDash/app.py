# This app runs the website and connects all the components.

# Catch all needed dash exceptions
import dash
# Remove dash. prefix requirement for these three
from dash import dcc,html,Dash
import dash_bootstrap_components as dbc

# With dbc, you can call themes from dbc themes found online by 'inspect element'

# Initialize app with; 
# use_pages to use subpages (in folder pages)
# suppress_callback_exceptions to reduce errors while developing
app = Dash(__name__, use_pages=True, suppress_callback_exceptions=True, title="Multi-Page App")
# Set server for deployment
server = app.server

# Hub layout; NavLink to home page 
app.layout = html.Div([
    dbc.NavbarSimple([
        dbc.NavLink("home", href="/", active="exact"),
        dbc.NavLink("Page 1", href="/page1", active="exact"),
        dbc.NavLink("Page 2", href="/page2", active="exact"),
        dbc.NavLink("Page 3", href="/page3", active="exact")
    ], brand = "Multi-Page App"),
    dash.page_container
])

if __name__ == '__main__':
    app.run(debug=True)