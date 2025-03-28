from dash import html, dcc
import dash_bootstrap_components as dbc
from dash_bootstrap_components import Button

from data.constants import data_problem
import numpy as np

list_sugestions = [
    dbc.ListGroupItem(
        [
            dbc.Card(
                [
                    dbc.CardBody(
                        [
                            html.H5(
                                "This item has a heading",
                                className="card-title",
                            ),
                            html.P(
                                "To be able to improve ROI you need to let WQCity impair. Do you agree?",
                                className="mb-1",
                            ),
                            html.Div(
                                [
                                    Button(
                                        "Yes",
                                        id="accept-btn",
                                        color="primary",
                                        className="me-1",
                                        n_clicks=0,
                                    ),
                                    Button(
                                        "No",
                                        id="decline-btn",
                                        color="primary",
                                        className="me-1",
                                        n_clicks=0,
                                    ),
                                ],
                                className="d-flex w-100 justify-content-center",
                            ),
                        ]
                    ),
                ]
            )
        ]
    )
    for index, objective in enumerate(data_problem[0]["objective_names"])
]

sidebar_explanations_option2 = html.Div(
    [
        html.H5("Explanations"),
        html.Ol(
            [
                html.Li("Select one of the solutions provided by the method."),
                html.Li(
                    "Choose an objective function value from that solution that you want to improve."
                ),
                html.Li(
                    "A list of possible changes to the reference point will then be suggested. "
                ),
            ],
            className="description-text",
        ),
        dcc.Dropdown(
            id="opt2-objectives-dropdown",
            options=[
                {
                    "label": html.Span(
                        [
                            html.Div(
                                style={
                                    "display": "inline-block",
                                    "width": "12px",
                                    "height": "12px",
                                    "backgroundColor": color,
                                    "marginRight": "8px",
                                }
                            ),  # Colored square
                            name,
                        ],
                        style={"display": "flex", "alignItems": "center"},
                    ),
                    "value": idx,
                }
                for idx, (name, color) in enumerate(
                    zip(data_problem[0]["objective_names"], data_problem[0]["colors"])
                )
            ],
            placeholder="Select an objective function to improve",
        ),
        html.P("     "),
        html.H6(
            "Effects of the components of the reference point on the obtained solution"
        ),
        dbc.ListGroup([dbc.ListGroupItem(list_sugestions)]),
    ],
    className="sidebar-explanations",
)
