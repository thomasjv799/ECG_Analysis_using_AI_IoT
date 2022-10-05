from dash import Dash, dcc, html, Input, Output
import plotly.express as px
import pandas as pd

app = Dash(__name__)

app.layout = html.Div([
    html.H4('Simple stock plot with adjustable axis'),
    html.Button("Switch Axis", n_clicks=0, 
                id='button'),
    dcc.Graph(id="graph"),
])


@app.callback(
    Output("graph", "figure"), 
    Input("button", "n_clicks"))
def display_graph(n_clicks):
    df = pd.read_csv('analog-data2.csv')

    if n_clicks % 2 == 0:
        x, y = 'AAPL_x', 'AAPL_y'
    else:
        x, y = 'AAPL_y', 'AAPL_x' 

    fig = px.line(df,y="Value")    
    return fig


app.run_server(debug=True)