# Default; stacking components from the top-down
# You can reprogram dashboards to follow different structures, such as horizontal
# dcc Bootstrap; A popular front-end web development framework
# Easy rows and columns
# dbc.x :
## .Container; responsive grid container
## .Row; Horizontal row
## .Col; Vertical column inside row
## .Button; Styled clickable button
## .Alert; Message box with colors for different conditions
## .Card; Container with header, body, and footer
## .Navbar; Responsive navigational bar
## .Modal; Popup dialog box
## .Spinner; Animated loading indicator

### import dash_bootstrap_components as dbc
### dbc.Row([dbc.Col(), dbc.Col()]) - A row with two columns

# Import modules
from dash import Dash, html
import dash_bootstrap_components as dbc

# Initialize with external CSS and define a style
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
app.title = "Multi Layout App"
box_style = {
    "border": "2px solid black",
    "border-radius": "5px",
    "padding": "20px",
    "margin": "5px",
    "backgroundColor": "lightgray"
}

# Layout
app.layout = dbc.Container([
    dbc.Row(
        dbc.Col(
            html.Div("Top Row(Full Width)", style=box_style),
            width = 12
            )
        ),
    dbc.Row([
        dbc.Col(
            html.Div("Left Column", style=box_style)
        ),
        dbc.Col(
            html.Div("Right Column", style=box_style)
        )
    ]),
    dbc.Row(
        dbc.Col(
            html.Div("Footer (Full Width)", style=box_style),
            width = 12
        )
    )
], fluid=True)    

# Run 
if __name__ == "__main__":
    app.run(debug=True)