# Callbacks; dynamic input which returns outputs
# Automatically called when input property changes, updating output component
# Input changes; Dash calls function; Function processes input value; Function returns output value; Dash updates output property with value
# dcc = Dash Core Components; module allowing interactive UI elements

# Syntax:
#
# from dash import Input, Output
#
# @app.callback(
#     Output(component_id, component_property - returns tuple/list with one value for each output in order declared)
#     Input(component_id, component_property - allows multiple)
# ) - this is a decorator
# def function_name(input_object)
#   body
#   return output_object 

# Example

from dash import Dash, html, dcc, Input, Output, callback

app = Dash(__name__)
app.title = "Callback Example"

# add callback
@callback(
    Output("text-out","children"),
    Input("text-in", "value")
)
def showtext(value): 
    return f"Text: {value or ''}"

app.layout = html.Div(
    style={"maxWidth": 900, "margin":"40px auto", "fontFamily": "Georgia, serif"},
    children=[
        html.H1("Callback Example"),
        html.Ul([
            html.Li(["Input box's ", html.Code("value"), " property updates output text"])
        ]),
        dcc.Input(
            id="text-in",
            type="text",
            placeholder="type here...",
            style={"width":"100%", "fontSize":"48px","padding":"8px"}),
        
        html.Div(id = "text-out", style={"fontSize":"64px", "marginTop":"20px"})
    ])

if __name__ == "__main__":
    app.run(debug=True)