from dash import dcc, html, Input, Output, callback, register_page
import pandas as pd
import plotly.express as px
# Helper library to get .csv from /data
from pathlib import Path

register_page(__name__, path="/page3", name="Electricity")

# Access .csv
# Doesn't work with Anaconda, but for example:
# DATA_PATH = Path(__file__).resolve().parent
df = pd.read_csv(r"C:\Users\harri\Desktop\CTBA\Dash\MultiPageDash\data\electricity_prices.csv")
print(df)

df["year"] = pd.to_numeric(df["year"]).astype(int)

layout = html.Div(style={"backgroundColor":"#29381","padding":"20px"},
    children=[
    html.H1("Electricity Prices by US State", style={"textAlign":"center"}),
    dcc.Slider(
        id="year-slider",
        min=df["year"].min(),
        max=df["year"].max(),
        value=df['year'].min(),
        marks={str(y): str(y) for y in sorted(df["year"].unique())},
        step=None,
        tooltip = {"placement":"bottom", "always_visible":True}
    ),
    html.Br(),
    dcc.Graph(id="choropleth-map")
])

@callback(
    Output("choropleth-map", "figure"),
    Input("year-slider", "value")
)
def update_map(selected_year):
    d = df[df["year"] == selected_year]
    fig = px.choropleth(
        d,
        locations="state",
        locationmode="USA-states",
        color="price",
        scope="usa",
        color_continuous_scale="Reds",
        labels={
            "price":"Price (cents/kWh)"
        },
        title=f"Residential Electricity Prices - {selected_year}"
    )
    fig.update_layout(
        geo=dict(bgcolor = "orange"),
        paper_bgcolor="#32453c",
        font_color="white",
        # l for left, etc.
        margin=dict(l=10, r=10, t=50, b=10)
    )
    return fig