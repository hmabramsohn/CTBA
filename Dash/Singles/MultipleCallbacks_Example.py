# Using multiple callbacks; Updating several components in response to input event

# Required modules from dash
from dash import Dash, html, dcc, Input, Output, callback

# Generate local instance of app
app = Dash(__name__)

# Create app layout
app.layout = html.Div([
    # Three inputs in html.Div([]), which are dash core components
    dcc.Input(id='input1', type='number', placeholder='Enter a number'),
    dcc.Input(id='input2', type='number', placeholder='Enter another number'),
    dcc.Input(id='input3', type='text', placeholder='Enter some text'),
    
    # Outputs in divs
    html.Div(id="output1", style={"margin-top":"20px"}),
    html.Div(id="output2"),
    html.Div(id="output3")
])

# Set up callbacks - output = children, implied in app.layout, input = value, as input is a value
@app.callback(
    Output("output1","children"),
    Output("output2","children"),
    Output("output3","children"),
    Input("input1","value"),
    Input("input2","value"),
    Input("input3","value")
)
def update_outputs(num1, num2, text):
    # Handle Nones
    num1 = num1 or 0
    num2 = num2 or 0
    text = text or ""
    # Perform operations
    result1 = f"The sum of the first 2 numbers is: {num1 + num2}"
    result2 = f"The product of the first 2 numbers is: {num1 * num2}"
    result3 = f"The reversed text of the third celll is: {text[::-1]}"
    # Return results
    return result1, result2, result3

# Run app
if __name__ == "__main__":
    app.run(debug=True)