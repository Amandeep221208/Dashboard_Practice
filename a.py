#pip install dash
import dash                              # pip install dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Output, Input

from dash_extensions import Lottie       # pip install dash-extensions
import dash_bootstrap_components as dbc  # pip install dash-bootstrap-components
import plotly.express as px              # pip install plotly
import pandas as pd                      # pip install pandas
from datetime import date
import calendar
from wordcloud import WordCloud          # pip install wordcloud


# Bootstrap themes: https://hellodash.pythonanywhere.com/theme_explorer
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.DARKLY])

# if Jupyter Notebook/Colab
# app = JupyterDash(__name__, external_stylesheets=[dbc.themes.LUX])
sidebar = html.Div(
    [
        html.H2("Navigation", className="display-7"),
        html.Hr(),
        html.P("Choose a section:", className="lead"),
        dbc.Nav(
            [
                dbc.NavLink("Home", href="#", active="exact"),
                dbc.NavLink("Profile", href="#", active="exact"),
                dbc.NavLink("Messages", href="#", active="exact"),
                dbc.NavLink("Settings", href="#", active="exact"),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    style={
        "position": "fixed",
        "top": 0,
        "left": 0,
        "bottom": 0,
        "width": "13rem",
        "padding": "2rem 1rem",
        "backgroundColor": "#0077B5",
        "color": "black",
    },
)

"""
dbc stands for Dash Bootstrap Components
 
- For professional, responsive dashboards.
- If you want cleaner, reusable, and maintainable code.
- When using Bootstrap themes for styling.
"""


content = dbc.Container([
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardImg(src='/assets/linkedin.png', top=True)
            ],className='mb-2'), 
            # margin bottom 2 space,  0.5rem (8px) margin
            # link: https://hackerthemes.com/bootstrap-cheatsheet/
            # dbc.card: https://dash-bootstrap-components.opensource.faculty.ai/docs/components/card/
            dbc.Card([  
                dbc.CardBody([ 
                ])
            ]),
        ], width=2),
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    dbc.CardImg(src='/assets/young.png', top=True) 
                ])
            ]),
        ], style = {"marginTop": "4rem", "padding": "2rem 1rem"},  width=4),
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                     html.H3("Sign in", className="text-center mb-4", style={"color": "#0077B5"}),
                     html.Div([
                        dbc.Label("Email or Phone", className="mb-2"),
                        dbc.Input(type="email", placeholder="Enter your email or phone"),
                    ], className="mb-3"),
                    html.Div(
                        [
                            dbc.Label("Password", className="mb-2"),
                            dbc.Input(type="password", placeholder="Enter your password"),
                        ],
                        className="mb-3"
                    ),
                    dbc.Button("Sign in", color="primary", style={"backgroundColor": "#0077B5"}),
                     ])
            ]),
        ], width=4),
    ],className='mb-2 mt-2'), # or: my-2
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    
                ])
            ]),
        ], width=2),
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                ])
            ]),
        ], width=2),
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                ])
            ]),
        ], width=2),
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                ])
            ]),
        ], width=2),
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                ])
            ]),
        ], width=2),
    ],className='mb-2'),
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                ])
            ]),
        ], width=6),
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                ])
            ]),
        ], width=4),
    ],className='mb-2'),
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                ])
            ]),
        ], width=3),
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                ])
            ]),
        ], width=3),
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                ])
            ]),
        ], width=4),
    ],className='mb-2'),
     dbc.Row(
        dbc.Col(html.Div("© 2024 LinkedIn Clone. All rights reserved.", style={"textAlign": "center", "color": "gray"})),
        className="mt-4"
    )
], fluid=True, style={"marginLeft": "13rem", "padding": "2rem 1rem"})  # Added marginLeft to accommodate the sidebar

app.layout = html.Div([sidebar, content])




# It is used to ensure that certain parts of the code are executed 
# only when the script is run directly, and not when it is imported as a module in another script.

if __name__=='__main__':
# you can change the port number here
    app.run_server(debug=False, port=8001)  # Starts the server only if run directly.
    
    
# if jupyter notebook/colab
# app.run_server(mode='jupyterlab', port=8001)