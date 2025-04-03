from dash import html, dcc
import dash_bootstrap_components as dbc
from components.graphs import get_sample_bar_chart
from data.constants import data_problem

explanations_content = html.Div(
    [
        html.P(" "),
        html.P(
            "Choose the objective function you want to improve in the solution.",
            className="description-text",
        ),
        dcc.Dropdown(
            id="objectives-dropdown",
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
            placeholder="Select an objective function",
        ),
        html.P(" "),
        html.P(
            [
                html.Span("Red", style={"color": "#C00000"}),
                " bars indicate objectives that negatively impact the selected objective, while ",
                html.Span("blue", style={"color": "blue"}),
                " bars indicate positive effects.",
            ],
            className="description-text",
        ),
        dcc.Graph(
            id="bar-chart",
            figure=get_sample_bar_chart(),
            style={
                "margin": "0",
                "padding": "0",
                "paddingTop": "1rem",
            },  # Remove margin and padding
        ),
        html.P(" "),
        dbc.Alert(
            [
                html.I(className="bi bi-lightbulb", style={"marginRight": "10px"}),
                "To improve the selected objective, consider impairing red-bar objectives or those with smaller blue bars.",
            ],
            color="warning",
            className="description-text",
        ),
    ]
)
