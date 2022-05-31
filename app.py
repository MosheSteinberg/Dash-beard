from sre_parse import State
from dash import Dash
from dash.html import Div, Button
from dash_extensions import BeforeAfter
from dash.dependencies import Input, Output, State

app = Dash(__name__)
server = app.server
app.title = "Moshe's beard"
app.layout = Div([
    BeforeAfter(id='before-after', before="assets/before.jpg", after="assets/after.jpg", width=256, height=300, defaultProgress=0.1),
    Button('Switch order', id='button')
])

@app.callback(
    Output(component_id='before-after', component_property='before'),
    Output(component_id='before-after', component_property='after'),
    Input(component_id='button', component_property='n_clicks'),
    State(component_id='before-after', component_property='before'),
    State(component_id='before-after', component_property='after')
)
def switch_pics(button, before, after):
    return after, before


if __name__ == "__main__":
    app.run_server()