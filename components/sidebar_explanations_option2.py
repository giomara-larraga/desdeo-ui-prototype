from dash import html, dcc
from components.graphs import get_bar_chart

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
            ["NYC", "MTL", "SF"],
            "NYC",
            id="demo-dropdown",
            placeholder="Select an objective function to improve",
        ),
        html.P("     "),
        html.H6(
            "Effects of the values of the reference point on the obtained solution"
        ),
    ],
    className="sidebar-explanations",
)
