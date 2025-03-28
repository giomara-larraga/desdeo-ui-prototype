from dash import html, dcc
from components.graphs import get_bar_chart
from data.constants import data_problem

sidebar_explanations_option1 = html.Div(
    [
        html.H5("Explanations"),
        html.Ol(
            [
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
            value=0,  # Default selection (first objective)
            placeholder="Select an objective function to improve",
        ),
        dcc.Graph(
            id="line-chart",
            figure=get_bar_chart(),
            style={
                "margin": "0",
                "padding": "0",
                "padding-top": "1rem",
            },  # Remove margin and padding
        ),
    ],
    className="sidebar-explanations",
)
