from dash import html, dcc
import dash_bootstrap_components as dbc
from components.graphs import get_sample_pcp

import pandas as pd

df = pd.DataFrame(
    {
        "First Name": ["Arthur", "Ford", "Zaphod", "Trillian"],
        "Last Name": ["Dent", "Prefect", "Beeblebrox", "Astra"],
    }
)

table = dbc.Table.from_dataframe(df, striped=True, bordered=True, hover=True)

card = dbc.Card(
    dbc.CardBody(
        html.Div(
            [
                html.H6("Visualization", className="card-title"),
                dcc.Graph(
                    id="pcp-chart",
                    figure=get_sample_pcp(),
                    style={"margin": "0", "padding": "0"},  # Remove margin and padding
                ),
            ]
        )
    ),
    style={"width": "100%", "margin-bottom": "1rem"},
)

card_table = dbc.Card(
    dbc.CardBody(
        [
            html.H6("Numerical results", className="card-title"),
            table,
        ]
    ),
    style={"width": "100%"},
)

solutions_panel = html.Div(
    children=[
        html.H5("Obtained solutions"),
        card,
        card_table,
    ],
    className="solutions-panel",
)
