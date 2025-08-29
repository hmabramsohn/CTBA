# Dash generates websites through Python. HTML and CSS are interposed through the Python interpreter.
# Dash is built on top of Plotly, Flask, and React - built by Plotly.
# Basic visualization library for data scientists.
# Dash has Dcc (Dash core components) and HTML (Dash HTML components).
# Dash is for building full web apps and dashboards.
# Dash handles both static and dynamic content by building pages at runtime from API callbacks, database queries, and live data streams. 

from dash import Dash, html

# Initialize web application
app = Dash(__name__)

from flask.helpers import get_root_path
print(get_root_path(__name__))

# Define website layout; name Div as "My Dashboard", specify H1 and P elements
app.layout = html.Div([
    html.H1("Hello Dash!", style={'color' : "#410606",
                                  'fontSize' : "20px",
                                  }),
    html.P("This is a simple dashboard.", style={'border':'1px solid black',
                                                 'padding':'20px',
                                                 'margin':'50px'}),
    html.Br(),
    html.A("Click Here", href="https://example.com")
])

# Dash allows inline styles, links to external CSS, and styling through a Python dictionary
# Python automatically flags styles in an assets folder under the project folder; external CSS can be placed here

# Run web app on port 8050
# debug = True forces reloads; use_reloader = False prevents infinite reloading on local machine
if __name__ == "__main__":
    app.run(port=8050, debug=True, use_reloader=False)
    
