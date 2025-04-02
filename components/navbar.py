from dash import html
import dash_bootstrap_components as dbc

navbar = dbc.NavbarSimple(
    brand=html.Div(
        [
            html.Img(src="/assets/logo.png", height="20px"),  # Adjust path and height
            html.Span(
                "DESDEO | R - XIMO",
                style={"marginLeft": "10px"},
            ),
        ],
        style={"display": "flex", "alignItems": "center"},
    ),  # Align image and text
    brand_href="/",
    dark=False,
    className="custom-navbar",  # Apply custom CSS class here
    fluid=True,
)
