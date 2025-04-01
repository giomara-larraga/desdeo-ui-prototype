from dash import html, dcc
from components.graphs import build_heatmap
from data.constants import data_problem
import dash_bootstrap_components as dbc


advanced_content = html.Div(
    [
        html.P(" "),
        html.P(
            "Summary of impairing and improving effects of the components of the reference point on the values of the obtained solution for each objective function",
            className="description-text",
        ),
        dcc.Graph(
            id="heatmap",
            figure=build_heatmap(None),
            style={
                "margin": "0",
                "padding": "0",
                "padding-top": "1rem",
            },  # Remove margin and padding
        ),
    ]
)
