from dash import html, dcc
from components.sidebar_preferences import create_sidebar_preferences
from dash.dependencies import Input, Output


def create_layout(sidebar_preferences, solutions_panel, sidebar_explanations):
    layout = html.Div(
        [
            html.Div(
                [sidebar_preferences], style={"width": "25%", "float": "left"}
            ),  # Left Sidebar (Dashboard-specific)
            html.Div(
                [solutions_panel],
                style={"width": "50%", "float": "left"},
            ),  # Main Content
            html.Div(
                [sidebar_explanations], style={"width": "25%", "float": "right"}
            ),  # Right Sidebar (Dashboard-specific)
        ]
    )
    return layout
