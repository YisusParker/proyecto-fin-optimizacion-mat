import dash
from dash import dcc, html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import sys

# Verificar el entorno de Python
print("Python interpreter location:", sys.executable)

# Inicializar la aplicación de Dash
app = dash.Dash(
    __name__,
    external_stylesheets=[dbc.themes.BOOTSTRAP],
    suppress_callback_exceptions=True,
)
app.title = "GymBody"

# Configurar el servidor para la implementación
server = app.server

# Definir la estructura de la aplicación con la navegación
app.layout = html.Div(
    [dcc.Location(id="url", refresh=False), html.Div(id="page-content")]
)


# Callback para actualizar la página según la URL
@app.callback(Output("page-content", "children"), Input("url", "pathname"))
def display_page(pathname):
    if pathname == "/main":
        from pages import main

        return main.layout
    else:
        from pages import index

        return index.layout


# Ejecutar la aplicación
if __name__ == "__main__":
    app.run_server(debug=True)
