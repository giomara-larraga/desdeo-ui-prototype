from dash import html, dcc
from dash.dependencies import Input, Output
from server import app  # Import app from server.py
from components.navbar import navbar
from layouts import home, main_layout
from utils.RXIMO import get_problem_data
from components.sidebar_preferences import create_sidebar_preferences
from components.solutions_panel import solutions_panel

problem_data = get_problem_data()
sidebar_preferences = create_sidebar_preferences()


app_layout = html.Div(
    [
        dcc.Store(id="opt1-preferences-store", storage_type="session", data=None),
        dcc.Store(id="opt1-current-solution-store", storage_type="session", data=None),
        dcc.Store(
            id="opt1-problem-data-store", storage_type="session", data=problem_data
        ),
        dcc.Store(id="opt1-shap-values-store", storage_type="session", data=None),
        dcc.Store(
            id="opt1-selected-objective-store", storage_type="session", data=None
        ),
        dcc.Store(id="click-store", data={"n_clicks": 0}),
        dcc.Store(id="barchart-scale-store", data="REL"),
        dcc.Store(id="heatmap-scale-store", data="ABS"),
        dcc.Location(id="url", refresh=False),
        navbar,
        home.layout,
    ]
)


""" @app.callback(Output("page-content", "children"), Input("url", "pathname"))
def display_page(pathname):
    if pathname == "/option_1":
        return main_layout.create_layout(
            sidebar_preferences, solutions_panel, sidebar_explanations_option1
        )
    elif pathname == "/option_2":
        return main_layout.create_layout(
            sidebar_preferences, solutions_panel, sidebar_explanations_option2
        )
    else:
        return home.layout """


# Import the callbacks after the layout definition to avoid circular import
import pages.callbacks
