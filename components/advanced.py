from dash import html, dcc
from components.graphs import build_heatmap
from data.constants import data_problem
import dash_bootstrap_components as dbc


advanced_content = html.Div(
    [
        html.P(" "),
        html.P(
            [
            "The following heatmap summarizes the trade-offs and synergies between different objectives. Each row represents the effects of improving the objective on that row, while the columns show how the other objectives are affected. ",
            html.Span("Blue", style={"color": "blue"}),
            " cells indicate synergies (both objectives improve together). ",
            html.Span("Red", style={"color": "#C00000"}),
            " cells indicate trade-offs (improving one objective worsens the other).",
            ],
            className="description-text",

        ),
        dcc.RadioItems(
        id="radio-scale-heatmap",
        options={
                'ABS': 'Normalized',
                'REL': 'Raw data'        },
        value='REL',
        inline=True,
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
