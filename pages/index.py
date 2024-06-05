from dash import dcc, html

layout = html.Div(
    style={
        "fontFamily": "Kanit, sans-serif",
        "backgroundColor": "#EFEFEF",
        "paddingLeft": "40px",
        "paddingTop": "40px",
        "minHeight": "100vh",
        "display": "flex",
        "flexDirection": "column",
        "justifyContent": "space-between",
    },
    children=[
        html.Div(
            style={"flex": "1"},  # This makes the content div take the remaining space
            children=[
                html.Div(
                    className="caja1",
                    children=[
                        html.Div(
                            "Welcome to GymBody: Your Ultimate Fitness Companion",
                            className="titulo",
                            style={
                                "fontWeight": "bold",
                                "fontSize": "48px",
                                "color": "#274c77",
                            },
                        ),
                        html.Div(
                            className="texto1",
                            children=[
                                html.P(
                                    "At GymBody, we are dedicated to making exercise easier and more accessible for everyone. "
                                    "Whether you're a seasoned athlete or just beginning your fitness journey, GymBody is here "
                                    "to support and guide you every step of the way.",
                                    style={"fontSize": "20px", "marginTop": "20px"},
                                )
                            ],
                        ),
                    ],
                ),
                html.Div(
                    className="caja15",
                    style={
                        "display": "flex",
                        "alignItems": "center",
                        "marginTop": "40px",
                    },
                    children=[
                        html.A(
                            "Start Your Fitness Journey Today",
                            href="/main",
                            className="callto",
                            style={
                                "fontWeight": "450",
                                "fontSize": "39px",
                                "backgroundColor": "#274c77",
                                "color": "#efefef",
                                "padding": "20px",
                                "borderRadius": "15.31px",
                                "textDecoration": "none",
                            },
                        ),
                        html.Div(
                            className="imagen1",
                            style={"marginLeft": "20px", "paddingLeft": "340px"},
                            children=[
                                html.Img(
                                    src="/assets/imgs/gymmode.png",
                                    alt="ej1",
                                    style={
                                        "maxWidth": "100%",
                                        "height": "auto",
                                        "borderRadius": "15.31px",
                                    },
                                )
                            ],
                        ),
                    ],
                ),
                html.Div(
                    className="caja2",
                    style={"paddingTop": "80px"},
                    children=[
                        html.Div(
                            className="texto2",
                            children=[
                                html.P(
                                    "Ready to transform your fitness routine? Sign up now and discover how GymBody can make "
                                    "exercising easier and more enjoyable. Join our community and take the first step towards "
                                    "a healthier, happier you.",
                                    style={"fontSize": "20px", "marginBottom": "20px"},
                                )
                            ],
                        ),
                        html.Div(
                            className="sign",
                            children=[
                                html.A(
                                    "Sign Up Now",
                                    href="#",
                                    style={
                                        "fontWeight": "500",
                                        "fontSize": "medium",
                                        "color": "#274c77",
                                        "textDecoration": "none",
                                    },
                                ),
                                " | ",
                                html.A(
                                    "Learn More",
                                    href="#",
                                    style={
                                        "fontWeight": "500",
                                        "fontSize": "medium",
                                        "color": "#274c77",
                                        "textDecoration": "none",
                                    },
                                ),
                            ],
                        ),
                    ],
                ),
                html.Div(
                    className="corner-image",
                    style={
                        "position": "absolute",
                        "bottom": "0",
                        "right": "0",
                        "margin": "20px",
                    },
                    children=[
                        html.Img(
                            src="/assets/imgs/muscle 1.png",
                            alt="Corner Image",
                            style={"maxWidth": "150px", "height": "auto"},
                        )
                    ],
                ),
            ],
        ),
        html.Footer(
            style={"backgroundColor": "#EFEFEF"},
        ),
    ],
)
