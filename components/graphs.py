import plotly.express as px
import plotly.graph_objects as go
from data.constants import data_problem
import pandas as pd


def get_sample_pcp():
    ideal = data_problem[0]["ideal"]
    nadir = data_problem[0]["nadir"]
    dimensions = data_problem[0]["objective_names"]

    df = pd.DataFrame([ideal, nadir], columns=dimensions)

    # Define Categories and Colors
    categories = ["Ideal", "Nadir"]
    colors = {"Ideal": "blue", "Nadir": "red"}

    # Create Figure Using Graph Objects (for Custom Colors)
    fig = go.Figure()

    # Define dimensions once (we don't need to do this for each line)
    dimensions_dict = [{"label": dim, "values": df[dim]} for dim in dimensions]

    # Add Each Line with Custom Colors
    for category, values in zip(categories, [ideal, nadir]):
        fig.add_trace(
            go.Parcoords(
                line=dict(color=colors[category]),  # Assign specific color
                dimensions=dimensions_dict,
                name=category,  # Legend Name (not displayed in Parcoords directly)
            )
        )

    annotations = []
    axis_colors = data_problem[0]["colors"]

    # Adding annotations for each axis
    for i, dim in enumerate(dimensions):
        annotations.append(
            dict(
                x=0.25 * (i),  # Position of the colored square (adjust as needed)
                y=1.1,  # Position above the plot
                xref="paper",
                yref="paper",  # Reference to paper (the entire plotting area)
                text="",  # Axis label
                showarrow=False,  # No arrow
                font=dict(size=12, color="black"),  # Label text style
                bgcolor=axis_colors[i],  # Background color (square color)
                width=10,  # Size of the colored square
                height=10,  # Size of the colored square
                align="center",  # Center the text inside the square
            )
        )

    # Update Layout: Add Annotations and Adjust Plot Layout
    fig.update_layout(
        height=300,  # Set the height (in pixels)
        margin=dict(
            l=10, r=10, t=50, b=10
        ),  # Remove left, right, top, and bottom margins
        annotations=annotations,  # Add annotations for the axes
    )
    return fig


def build_pcp(solution, preferences):
    ideal = data_problem[0]["ideal"]
    nadir = data_problem[0]["nadir"]
    dimensions = data_problem[0]["objective_names"]
    # ranges = pd.DataFrame([ideal, nadir], columns=dimensions)

    solution_df = pd.DataFrame([solution[0]], columns=dimensions)
    reference_point_df = pd.DataFrame([list(preferences.values())], columns=dimensions)

    # Add a 'category' column to distinguish between Solution and Reference Point
    solution_df["category"] = "Solution"
    reference_point_df["category"] = "Reference Point"

    combined_df = pd.concat([solution_df, reference_point_df], ignore_index=True)

    # Create the figure for the parallel coordinates plot
    fig = go.Figure()

    # Define the dimensions (each dimension is represented as a dictionary)
    combined_dimensions = [
        {
            "label": dim,
            "values": combined_df[dim],
            "range": [ideal[i], nadir[i]],  # Range should be [min, max]
        }
        for i, dim in enumerate(dimensions)
    ]

    # Define a color map for each category
    color_map = {
        "Solution": "#C00000",
        "Reference Point": "#0000FF",
    }  # Red for Solution, Blue for Reference Point

    # Create the 'line_color' array based on the 'category' column
    combined_df["line_color"] = combined_df["category"].map(color_map)

    # Add the parallel coordinates trace with custom colors
    fig.add_trace(
        go.Parcoords(
            dimensions=combined_dimensions,
            line_color=combined_df.index,  # Color lines by their index
        )
    )

    # Adding annotations for axis labels (colored squares)
    annotations = []
    axis_colors = data_problem[0]["colors"]

    for i, dim in enumerate(dimensions):
        annotations.append(
            dict(
                x=0.25 * (i),  # Position of the colored square (adjust as needed)
                y=1.1,  # Position above the plot
                xref="paper",
                yref="paper",  # Reference to paper (the entire plotting area)
                text="",  # No axis label text here
                showarrow=False,  # No arrow
                font=dict(size=12, color="black"),
                bgcolor=axis_colors[i],  # Background color (square color)
                width=10,  # Size of the colored square
                height=10,  # Size of the colored square
                align="center",  # Center the text inside the square
            )
        )

    # Update layout with annotations and adjust plot layout
    fig.update_layout(
        height=300,  # Set the height (in pixels)
        margin=dict(l=10, r=10, t=50, b=10),  # Set margins
        annotations=annotations,  # Add annotations for the axes
    )
    return fig


def get_bar_chart():
    objectives = data_problem[0]["objective_names"]
    values = [500, -600, 700, 500, -55]  # Example values

    # Assign colors based on value (red if >0, blue if <0)
    colors = ["#C00000" if v > 0 else "blue" for v in values]
    colored_labels = [
        f"<span style='color:{c}; font-size:20px'>&#9632;</span> {obj}"
        for obj, c in zip(objectives, data_problem[0]["colors"])
    ]

    fig = go.Figure()
    fig.add_trace(
        go.Bar(
            x=colored_labels,
            y=values,
            marker=dict(color=colors),  # Set color dynamically
            # marker_color="crimson",
            name="expenses",
        )
    )
    fig.update_layout(
        height=200,  # Set the height (in pixels)
        margin=dict(l=1, r=0, t=0, b=0),  # Remove left, right, top, and bottom margins
        plot_bgcolor="white",
        xaxis=dict(
            layer="above traces",  # Ensures x-axis is on top
            tickmode="array",
            tickvals=[
                i for i in range(len(objectives))
            ],  # Ensure the tick positions correspond to bars
            ticktext=colored_labels,
            showline=True,
            linewidth=1,
            linecolor="black",
            mirror=True,
            ticks="outside",  # Ensures the ticks appear outside the axis
            tickangle=0,  # Ensures the ticks are horizontal
        ),
        yaxis=dict(
            layer="above traces",  # Ensures x-axis is on top
            showticklabels=False,
            showline=True,
            linewidth=1,
            linecolor="black",
            mirror=True,
            zeroline=True,  # Draw zero line
            zerolinecolor="black",  # Make it more visible
        ),
        annotations=[
            dict(
                x=0.25,
                y=1.15,
                xref="paper",
                yref="paper",
                text="<span style='color:#C00000; font-size:16px'>&#9632;</span> Increase",
                showarrow=False,
                font=dict(size=14),
            ),
            dict(
                x=0.75,
                y=1.15,
                xref="paper",
                yref="paper",
                text="<span style='color:blue; font-size:16px'>&#9632;</span> Decrease",
                showarrow=False,
                font=dict(size=14),
            ),
        ],
    )

    return fig
