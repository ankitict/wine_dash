import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc 
import pandas as pd
import plotly.graph_objs as go
from dash.dependencies import Input, Output
import dash_table
from app import app
from database import transforms

df = transforms.df

layout = html.Div(
            id='table-paging-with-graph-container',
            className="five columns"
        )

@app.callback(Output('table-paging-with-graph-container', "children"),
[Input('rating-95', 'value')
, Input('Alcohol-slider', 'value')
])

def update_graph(ratingcheck, prices):
    dff = df

    low = prices[0]
    high = prices[1]

    dff = dff.loc[(dff['Alcohol'] >= low) & (dff['Alcohol'] <= high)]
    
    if ratingcheck == ['Y']:
       dff = dff.loc[dff['Malic.acid'] >= 95]
    else:
        dff

    trace1 = go.Scattergl(x = dff['Malic.acid']
                        , y = dff['Alcohol']
                        , mode='markers'
                        , opacity=0.7
                        , marker={
                                'size': 8
                                , 'line': {'width': 0.5, 'color': 'white'}
                                }
                        , name='Malic.acid v Alchohol'
                    )
    return html.Div([
        dcc.Graph(
            id='rating-Alcohol'
            , figure={
                'data': [trace1
                    # dict(
                    #     x=df['Alcohol'],
                    #     y=df['rating'],
                    #     #text=df[df['continent'] == i]['country'],
                    #     mode='markers',
                    #     opacity=0.7,
                    #     marker={
                    #         'size': 8,
                    #         'line': {'width': 0.5, 'color': 'white'}
                    #     },
                    #     name='Price v Rating'
                    #) 
                ],
                'layout': dict(
                    xaxis={'type': 'log', 'title': 'Rating'},
                    yaxis={'title': 'Price'},
                    margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
                    legend={'x': 0, 'y': 1},
                    hovermode='closest'
                )
            }
        )
    ])