from dash import html, dcc
from dash.dependencies import Input, Output
from data.constants import data_problem
from dash_bootstrap_components import Button
import numpy as np
from data.constants import data_problem

colors = data_problem[0]["colors"]


# This function generates the sidebar content dynamically
def create_sidebar_preferences():
    objective_names = data_problem[0]["objective_names"]
    # objective_max_multipliers = np.array(data_problem[0]["multipliers"])
    ideal = np.array(data_problem[0]["ideal"])
    nadir = np.array(data_problem[0]["nadir"])
    # Create a list of sliders dynamically for each objective
    sliders = [
        html.Div(
            children=[
                html.Label(
                    [
                        html.Span(
                            style={
                                "display": "inline-block",
                                "width": "12px",
                                "height": "12px",
                                "backgroundColor": colors[index],
                                "marginRight": "8px",
                                "borderRadius": "3px",
                            }
                        ),
                        f"{objective} (min)",
                    ]
                ),
                dcc.Slider(
                    id=f"{objective}-slider",
                    min=ideal[index],
                    max=nadir[index],
                    step=(np.abs(nadir[index] - ideal[index]) / 100),
                    value=nadir[index],
                    marks={
                        nadir[index]: str(
                            round(nadir[index], data_problem[0]["decimal_places"])
                        ),
                        ideal[index]: str(
                            round(ideal[index], data_problem[0]["decimal_places"])
                        ),
                    },
                ),
            ]
        )
        for index, objective in enumerate(objective_names)
    ]
    # Here we can dynamically generate the content based on `explainer_data`
    return html.Div(
        children=[
            html.H5("Preference Information"),
            html.P(
                "Provide your preferences by either clicking on the bars. You must give a preference for each objective.",
                className="description-text",
            ),
            *sliders,
            Button(
                "Iterate",
                id="iterate-btn",
                color="primary",
                className="me-1",
                n_clicks=0,
            ),
        ],
        className="sidebar-preferences",
    )
