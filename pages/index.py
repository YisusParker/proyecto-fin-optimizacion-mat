from dash import dcc, html

# Definir el diseño de la página utilizando html.Div con varias propiedades de estilo y contenido
layout = html.Div(
    style={
        "fontFamily": "Kanit, sans-serif",  # Establece la familia de fuentes para todo el contenido
        "backgroundColor": "#EFEFEF",  # Establece el color de fondo
        "paddingLeft": "40px",  # Añade padding a la izquierda
        "paddingTop": "40px",  # Añade padding en la parte superior
        "minHeight": "100vh",  # Establece la altura mínima al 100% del viewport
        "display": "flex",  # Utiliza flexbox para el diseño
        "flexDirection": "column",  # Establece la dirección de los elementos flex en columna
        "justifyContent": "space-between",  # Distribuye el espacio de manera uniforme entre los elementos
    },
    children=[
        html.Div(
            style={"flex": "1"},  # Hace que el div de contenido ocupe el espacio restante
            children=[
                html.Div(
                    className="caja1",
                    children=[
                        html.Div(
                            "Welcome to GymBody: Your Ultimate Fitness Companion",
                            className="titulo",
                            style={
                                "fontWeight": "bold",  # Establece el peso de la fuente a negrita
                                "fontSize": "48px",  # Establece el tamaño de la fuente
                                "color": "#274c77",  # Establece el color del texto
                            },
                        ),
                        html.Div(
                            className="texto1",
                            children=[
                                html.P(
                                    "At GymBody, we are dedicated to making exercise easier and more accessible for everyone. "
                                    "Whether you're a seasoned athlete or just beginning your fitness journey, GymBody is here "
                                    "to support and guide you every step of the way.",
                                    style={"fontSize": "20px", "marginTop": "20px"},  # Establece el tamaño de la fuente y el margen superior
                                )
                            ],
                        ),
                    ],
                ),
                html.Div(
                    className="caja15",
                    style={
                        "display": "flex",  # Utiliza flexbox para el diseño
                        "alignItems": "center",  # Centra los elementos a lo largo del eje transversal
                        "marginTop": "40px",  # Añade margen en la parte superior
                    },
                    children=[
                        html.A(
                            "Start Your Fitness Journey Today",
                            href="/main",  # Enlace a la página principal
                            className="callto",
                            style={
                                "fontWeight": "450",  # Establece el peso de la fuente
                                "fontSize": "39px",  # Establece el tamaño de la fuente
                                "backgroundColor": "#274c77",  # Establece el color de fondo
                                "color": "#efefef",  # Establece el color del texto
                                "padding": "20px",  # Añade padding
                                "borderRadius": "15.31px",  # Establece el radio de las esquinas
                                "textDecoration": "none",  # Elimina la subrayado del texto del enlace
                            },
                        ),
                        html.Div(
                            className="imagen1",
                            style={"marginLeft": "20px", "paddingLeft": "340px"},  # Añade margen a la izquierda y padding a la izquierda
                            children=[
                                html.Img(
                                    src="/assets/imgs/gymmode.png",  # Ruta de la imagen
                                    alt="ej1",  # Texto alternativo para la imagen
                                    style={
                                        "maxWidth": "100%",  # Establece el ancho máximo al 100%
                                        "height": "auto",  # Ajusta la altura automáticamente
                                        "borderRadius": "15.31px",  # Establece el radio de las esquinas
                                    },
                                )
                            ],
                        ),
                    ],
                ),
                html.Div(
                    className="caja2",
                    style={"paddingTop": "80px"},  # Añade padding en la parte superior
                    children=[
                        html.Div(
                            className="texto2",
                            children=[
                                html.P(
                                    "Ready to transform your fitness routine? Sign up now and discover how GymBody can make "
                                    "exercising easier and more enjoyable. Join our community and take the first step towards "
                                    "a healthier, happier you.",
                                    style={"fontSize": "20px", "marginBottom": "20px"},  # Establece el tamaño de la fuente y el margen inferior
                                )
                            ],
                        ),
                        html.Div(
                            className="sign",
                            children=[
                                html.A(
                                    "Sign Up Now",
                                    href="#",  # Enlace (actualmente vacío)
                                    style={
                                        "fontWeight": "500",  # Establece el peso de la fuente
                                        "fontSize": "medium",  # Establece el tamaño de la fuente
                                        "color": "#274c77",  # Establece el color del texto
                                        "textDecoration": "none",  # Elimina el subrayado del texto del enlace
                                    },
                                ),
                                " | ",
                                html.A(
                                    "Learn More",
                                    href="#",  # Enlace (actualmente vacío)
                                    style={
                                        "fontWeight": "500",  # Establece el peso de la fuente
                                        "fontSize": "medium",  # Establece el tamaño de la fuente
                                        "color": "#274c77",  # Establece el color del texto
                                        "textDecoration": "none",  # Elimina el subrayado del texto del enlace
                                    },
                                ),
                            ],
                        ),
                    ],
                ),
                html.Div(
                    className="corner-image",
                    style={
                        "position": "absolute",  # Posiciona el div de forma absoluta
                        "bottom": "0",  # Lo coloca en la parte inferior
                        "right": "0",  # Lo coloca en la parte derecha
                        "margin": "20px",  # Añade margen
                    },
                    children=[
                        html.Img(
                            src="/assets/imgs/muscle 1.png",  # Ruta de la imagen
                            alt="Corner Image",  # Texto alternativo para la imagen
                            style={"maxWidth": "150px", "height": "auto"},  # Establece el ancho máximo y ajusta la altura automáticamente
                        )
                    ],
                ),
            ],
        ),
        html.Footer(
            style={"backgroundColor": "#EFEFEF"},  # Establece el color de fondo del pie de página
        ),
    ],
)
