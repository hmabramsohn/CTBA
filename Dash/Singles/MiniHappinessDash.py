# Import modules
from dash import Dash, html

# Initialize
app = Dash(__name__)

# Layout
app.layout = html.Div([
    html.H1("World Happiness Dashboard"),
    html.P("This dashboard will visualize the World Happiness score."),
    html.Br(),
    html.A("World Happiness Report",href="https://worldhappiness.report",target="_blank",style={'color':'#6065a3'})
])

# Run app
if __name__ == "__main__":
    app.run(debug=True)