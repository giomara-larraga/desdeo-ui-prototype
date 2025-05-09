from dash import State, no_update
import shap
from app import app  # Import app instance
from dash.dependencies import Input, Output
from data.constants import data_problem
from desdeo_tools.scalarization import (
    SimpleASF,
    DiscreteScalarizer,
    StomASF,
    PointMethodASF,
)
from shapley_values.utilities import (
    generate_black_box,
    Normalizer,
    generate_missing_data,
)
from desdeo_problem.problem import DiscreteDataProblem
import pandas as pd
import numpy as np
from components.graphs import (
    build_pcp,
    get_sample_bar_chart,
    get_sample_pcp,
    build_bar_chart,
    build_heatmap,
)
from components.solutions_table import create_table


# Callback to store the slider values in a new store
@app.callback(
    Output("opt1-preferences-store", "data"),  # Update this store with slider values
    [
        Input(f"{objective}-slider", "value")
        for objective in data_problem[0]["objective_names"]  # Input for each slider
    ],
    prevent_initial_call=True,
)
def update_slider_values(*slider_values):
    # The `slider_values` argument is a tuple of all the slider values
    objective_data = dict(
        zip(data_problem[0]["objective_names"], slider_values)
    )  # Create a dictionary with objective names and their values

    # Return the updated data to the store
    return objective_data


@app.callback(
    [
        Output("opt1-current-solution-store", "data"),
        Output("opt1-shap-values-store", "data"),
        Output("click-store", "data"),
    ],
    [Input("iterate-btn", "n_clicks"), Input("opt1-preferences-store", "data")],
    State("click-store", "data"),
    prevent_initial_call=True,
)
def load_data(n_clicks, preferences, click_data):
    if n_clicks > click_data["n_clicks"]:
        if preferences != None:
            n_objectives = data_problem[0]["n_objectives"]
            ideal = np.array(data_problem[0]["ideal"])
            nadir = np.array(data_problem[0]["nadir"])
            objective_names = data_problem[0]["objective_names"]
            # Load and setup problem
            df = pd.read_csv("data/river_pollution_10178.csv")
            pareto_front = df.to_numpy()
            asf = StomASF(ideal)
            problem = DiscreteDataProblem(
                df, ["x_1", "x_2"], objective_names, nadir, ideal
            )

            missing_data = generate_missing_data(200, ideal, nadir)
            bb = generate_black_box(problem, asf)
            explainer = shap.KernelExplainer(bb, missing_data)

            # normalizer = Normalizer(ideal, nadir)
            reference_point = list(preferences.values())
            result = bb(np.atleast_2d(np.array(reference_point)))
            shap_values = np.array(explainer.shap_values(np.array(reference_point)))
            return result, shap_values, {"n_clicks": n_clicks}
        else:
            return None, None, click_data
    return None, None, click_data


# Update chart ONLY when the iterate button is clicked
@app.callback(
    [
        Output("pcp-chart", "figure"),
        Output("solutions-table", "figure"),
        Output("heatmap", "figure"),
    ],
    [
        Input("opt1-current-solution-store", "data"),
        Input("opt1-shap-values-store", "data"),
        Input("heatmap-scale-store", "data")
    ],
    [State("opt1-preferences-store", "data")],  # Use State instead of Input
)
def update_chart(solution, shap_values, scale,preferences):
    if solution is None:
        return no_update  # Prevent update if solution is not ready

    # Generate the updated graph (replace with actual plotting code)
    return (
        build_pcp(solution, preferences),
        create_table(solution, preferences),
        build_heatmap(shap_values,scale),
    )


# Update chart ONLY when the iterate button is clicked
@app.callback(
    Output("bar-chart", "figure"),
    [Input("opt1-selected-objective-store", "data"), Input("barchart-scale-store", "data")],
    [State("opt1-shap-values-store", "data")],  # Use State instead of Input
)
def update_bar_chart(selected_objective, scale, shap_values):
    if shap_values is None:
        print("shap is none")
        return no_update  # Prevent update if solution is not ready

    if selected_objective is None:
        print("selected is none")
        return get_sample_bar_chart()
    # Generate the updated graph (replace with actual plotting code)
    return build_bar_chart(shap_values, selected_objective, scale)


@app.callback(
    Output("opt1-selected-objective-store", "data"),
    Input("objectives-dropdown", "value"),
)
def update_output(value):
    print("selected ", value)
    return value


@app.callback(
    Output("barchart-scale-store", "data"),
    Input("radio-scale", "value"),
)
def update_scale(value):
    print("Scale ", value)
    return value


@app.callback(
    Output("heatmap-scale-store", "data"),
    Input("radio-scale-heatmap", "value"),
)
def update_scale_heatmap(value):
    print("Scale ", value)
    return value
    