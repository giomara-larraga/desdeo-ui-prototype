from data.constants import data_problem
import pandas as pd
import dash_bootstrap_components as dbc
import plotly.graph_objects as go


def create_table(solution, reference_point):
    # Assuming `data_problem` contains the objective names
    header = data_problem[0]["objective_names"]
    num_objectives = data_problem[0]["n_objectives"]
    # Check if reference_point or solution are None/Empty
    if not reference_point and not solution:
        # Create an empty table
        fig = go.Figure(
            data=[
                go.Table(
                    header=dict(
                        values=["Type"] + header,
                    ),
                    cells=dict(
                        values=[["No Data"]]
                        + [[""] * 1] * num_objectives,  # Empty cells
                    ),
                )
            ]
        )
    else:
        # Convert inputs to lists (or use "-" if missing)
        reference_row = (
            [
                round(num, 3) if isinstance(num, (int, float)) else "-"
                for num in reference_point.values()
            ]
            if reference_point.values()
            else ["-"] * len(header)
        )
        solution_row = (
            [
                round(num, 3) if isinstance(num, (int, float)) else "-"
                for num in solution[0]
            ]
            if solution[0]
            else ["-"] * len(header)
        )

        # Convert to column-wise format for Plotly
        column_data = list(map(list, zip(reference_row, solution_row)))

        fig = go.Figure(
            data=[
                go.Table(
                    header=dict(
                        values=["Type"] + header,
                    ),
                    cells=dict(
                        values=[
                            ["Reference point", "Solution"],  # Row labels
                        ]
                        + column_data,  # Feature values
                    ),
                )
            ]
        )

    fig.update_layout(
        margin=dict(l=0, r=0, t=0, b=0),  # Set margins
    )
    return fig
