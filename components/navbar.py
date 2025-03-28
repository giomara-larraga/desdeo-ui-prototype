from dash import html
import dash_bootstrap_components as dbc

navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Home", href="/")),
        dbc.NavItem(dbc.NavLink("Option 1", href="/option_1")),
        dbc.NavItem(dbc.NavLink("Option 2", href="/option_2")),
    ],
    brand="Explainable Reference Point Method",
    brand_href="/",
    color="primary",
    dark=True,
    className="custom-navbar",  # Apply custom CSS class here
    fluid=True,
)
