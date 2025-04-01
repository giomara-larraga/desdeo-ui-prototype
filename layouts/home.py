from dash import html
from components.sidebar_preferences import create_sidebar_preferences
from components.solutions_panel import solutions_panel
from components.sidebar_explanations import sidebar_explanations

sidebar_preferences = create_sidebar_preferences()

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
