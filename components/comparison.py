from dash import html, dcc
from components.graphs import get_sample_bar_chart
from data.constants import data_problem
import dash_bootstrap_components as dbc


comparison_content = html.Div(
    [
        html.P(" "),
        html.P(
            "Comparison between the desirable values and the obtained solution",
            className="description-text",
        ),
    ]
)
