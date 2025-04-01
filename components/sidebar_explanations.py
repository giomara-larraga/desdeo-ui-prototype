from dash import html, dcc
from components.graphs import get_sample_bar_chart
from data.constants import data_problem
import dash_bootstrap_components as dbc
from components.comparison import comparison_content as tab1_content
from components.explanations import explanations_content as tab2_content
from components.advanced import advanced_content as tab3_content


sidebar_explanations = html.Div(
    [
        dbc.Tabs(
            [
                dbc.Tab(tab2_content, label="Explanations"),
                dbc.Tab(tab3_content, label="Advanced"),
                dbc.Tab(tab1_content, label="Details"),
            ]
        ),
    ],
    className="sidebar-explanations",
)
