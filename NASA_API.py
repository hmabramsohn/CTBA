# Harrison Abramsohn
# Dash app that connects to NASA's APOD API to pick a date and see posted image/video of the day

from dash import Dash, html, Input, Output, dcc
from datetime import datetime as dt
import requests

# Define today and url for easier syntax
today = dt.today().strftime("%Y-%m-%d")
url = f"https://api.nasa.gov/planetary/apod?api_key=8Dj7olElsXvPyNSNSedPC5zF8vTuClDsyMH99XBr&date={today}"

# Request APOD as JSON
get = requests.get(url).json()

# Define JSON elements for easier Dash building
title = get['title']
date = get['date']
descr = get['explanation']
img = get['hdurl']

app = Dash(__name__)
app.title = "APOD Example"

app.layout = html.Div(
    [html.H1(f'NASA APOD: {title}'),
    html.H2(f'{date}'),
    html.Img(src=img, style={"max-width":"50%","height":"auto"}),
    html.P(f'{descr}', style = {"text-align":"justify", "margin":"50px 250px"})],
    style = {"text-align":"center"}
)

if __name__ == '__main__':
    app.run(debug=True)