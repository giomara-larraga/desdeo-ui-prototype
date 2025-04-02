from dash import Dash
import dash_bootstrap_components as dbc

# Initialize Dash app
app = Dash(
    __name__,
    suppress_callback_exceptions=True,
    external_stylesheets=[
        dbc.themes.BOOTSTRAP,
        dbc.icons.BOOTSTRAP,
    ],
)
server = app.server  # Expose server for deployment
