import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import plotly.express as px
import numpy as np
import pandas as pd


app = dash.Dash(__name__)

app.layout = html.Div([
    html.H4("Promjenom parametara a i b, mijenja se i funkcija aX+b"),
    html.Div([
        "parametar a: ",
        dcc.Input(id='my-input', value= 3, type='text', debounce = True)
    ]),
    html.Div([
        "parametar b: ",
        dcc.Input(id='my-input2', value= 1, type='text', debounce = True)
    ]),
    html.H4("Posle promjene parametara pritisnite Enter"),
    html.Br(),
    dcc.Graph(id='line-graph')

])


@app.callback(
    Output(component_id='line-graph', component_property='figure'),
    Input(component_id='my-input', component_property='value'),
    Input(component_id='my-input2', component_property='value'),    
)

def update_figure(input_value1, input_value2):
    
    x = np.arange(10)
    y = (int(float(input_value1))*x + int(float(input_value2)))
    df = pd.DataFrame(({'x':x, 'y':y}))
    
    fig = px.line(df, x="x", y="y")
    fig.update_layout(transition_duration=1000,
    xaxis_title ='x',
    yaxis_title = 'y',
    title = 'Prikaz aX+b za unesene parametre a i b')
    return fig


if __name__ == '__main__':
    app.run_server(debug=True)
