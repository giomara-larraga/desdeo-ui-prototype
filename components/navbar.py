from dash import html
import dash_bootstrap_components as dbc

navbar = dbc.NavbarSimple(
    brand="DESDEO | R - XIMO",
    brand_href="/",
    color="#092C4C",
    dark=True,
    className="custom-navbar",  # Apply custom CSS class here
    fluid=True,
)
