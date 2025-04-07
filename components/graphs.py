import plotly.express as px
import plotly.graph_objects as go
from data.constants import data_problem
import pandas as pd
import numpy as np


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

    line1 = solution[0]
    line2 = list(preferences.values())
    # Combine both lines into a single dataset
    values = np.array([line1, line2])

    # Assign a categorical index for coloring
    color_values = [0, 1]  # 0 for Red, 1 for Yellow

    # Create the Parallel Coordinate Plot
    fig = go.Figure(
        go.Parcoords(
            line=dict(
                color=color_values,  # Assign colors
                colorscale=[
                    [0, "blue"],
                    [1, "black"],
                ],  # Red for first, Yellow for second
            ),
            dimensions=[
                {
                    "label": dimensions[i],
                    "values": values[:, i],
                    "range": [ideal[i], nadir[i]],  # Range should be [min, max]
                }  # Assign values for each dimension
                for i in range(values.shape[1])
            ],
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


def build_pcp2(solution, preferences):
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


def get_sample_bar_chart():
    objectives = data_problem[0]["objective_names"]
    values = [0, 0, 0, 0, 0]  # Example values

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
            showlegend=False,  # Hide this trace from the legend
            text="test",
            # marker_color="crimson",
        )
    )
    # Dummy Scatter Traces for Legend
    fig.add_trace(
        go.Scatter(
            x=[None],  # Empty x value, just for legend
            y=[None],  # Empty y value, just for legend
            mode="markers",
            marker=dict(size=12, color="#C00000"),  # Red marker
            showlegend=False,
        )
    )

    fig.add_trace(
        go.Scatter(
            x=[None],  # Empty x value
            y=[None],  # Empty y value
            mode="markers",
            marker=dict(size=12, color="blue"),  # Blue marker
            showlegend=False,
            # name="Improving effect",
        )
    )
    fig.update_layout(
        height=250,  # Set the height (in pixels)
        margin=dict(l=1, r=0, t=0, b=10),  # Remove left, right, top, and bottom margins
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
    )

    return fig


def build_bar_chart(values, selected_objective, scale="REL"):
    values_to_plot = values[selected_objective]
    values_to_plot[selected_objective] = 0

        
        
    norm_v = np.linalg.norm(values_to_plot, keepdims=True)
    values_to_plot = values_to_plot/norm_v

    objectives = data_problem[0]["objective_names"]

    # Assign colors based on value (red if >0, blue if <0)
    colors = ["#C00000" if v > 0 else "blue" for v in values_to_plot]
    colored_labels = [
        f"<span style='color:{c}; font-size:20px'>&#9632;</span> {obj}"
        for obj, c in zip(objectives, data_problem[0]["colors"])
    ]

    fig = go.Figure()
    fig.add_trace(
        go.Bar(
            x=colored_labels,
            y=values_to_plot,
            marker=dict(color=colors),  # Set color dynamically
            showlegend=False,  # Hide this trace from the legend
        )
    )

    # Dummy Scatter Traces for Legend
    fig.add_trace(
        go.Scatter(
            x=[None],  # Empty x value, just for legend
            y=[None],  # Empty y value, just for legend
            mode="markers",
            marker=dict(size=12, color="#C00000"),  # Red marker
            showlegend=False,
        )
    )

    fig.add_trace(
        go.Scatter(
            x=[None],  # Empty x value
            y=[None],  # Empty y value
            mode="markers",
            marker=dict(size=12, color="blue"),  # Blue marker
            showlegend=False,
        )
    )

    fig.update_layout(
        height=250,  # Set the height (in pixels)
        margin=dict(l=1, r=0, t=0, b=10),  # Remove left, right, top, and bottom margins
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
    )

    if (scale =="ABS"):
        min_value = min([min(element) for element in values])
        max_value = max([max(element) for element in values])
        fig.update_yaxes(range=[min_value,max_value])


    return fig


def build_heatmap(values, scale="ABS"):


    objectives = data_problem[0]["objective_names"]  # Get row/column names
    print(values)
    # Check if values is None or empty
    if values is None or len(values) == 0:
        # Return an empty figure
        fig = go.Figure()
        fig.update_layout(
            title="No Data Available", height=250, margin=dict(l=1, r=0, t=50, b=10)
        )
        return fig

    

    # Convert values to a NumPy array for safety
    values = np.array(values)

    # Ensure it's an N × N matrix
    if values.shape[0] != values.shape[1]:
        raise ValueError("Input matrix must be square (N × N).")

    np.fill_diagonal(values, 0)

    if (scale =="ABS"):
        x_norm = np.linalg.norm(values, axis=1, keepdims=True)
        values = values/x_norm
        #df_norm_row = df.apply(lambda x: (x-np.mean(x))/np.std(x), axis = 1)

    fig = go.Figure(
        data=go.Heatmap(
            z=values,  # Data matrix
            x=objectives,  # Column names
            y=objectives,  # Row names
            colorscale="RdBu_r",  # Red for negative, blue for positive
            zmid=0,  # Center scale at 0
            showscale=False,  # Hide the color bar
        )
    )

    fig.update_layout(
        height=250,
        margin=dict(l=1, r=0, t=5, b=10),
    )

    #fig.update_xaxes(side="top")


    return fig
