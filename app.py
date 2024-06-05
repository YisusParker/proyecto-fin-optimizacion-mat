import dash
from dash import dcc, html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import sys

# Verificar la ubicación del intérprete de Python
print("Python interpreter location:", sys.executable)

# Inicializar la aplicación de Dash
app = dash.Dash(
    __name__,
    external_stylesheets=[dbc.themes.BOOTSTRAP],  # Utilizar Bootstrap para los estilos externos
    suppress_callback_exceptions=True,  # Suprimir excepciones de callback para permitir callbacks en múltiples archivos
)
app.title = "GymBody"  # Establecer el título de la aplicación

# Configurar el servidor para la implementación
server = app.server

# Definir la estructura de la aplicación con la navegación
app.layout = html.Div(
    [
        dcc.Location(id="url", refresh=False),  # Componente para manejar la URL y la navegación
        html.Div(id="page-content")  # Div para mostrar el contenido de la página según la URL
    ]
)

# Callback para actualizar la página según la URL
@app.callback(Output("page-content", "children"), Input("url", "pathname"))
def display_page(pathname):
    # Importar y mostrar el layout de la página principal si la URL es '/main'
    if pathname == "/main":
        from pages import main
        return main.layout
    else:
        # Importar y mostrar el layout de la página de inicio para cualquier otra URL
        from pages import index
        return index.layout

# Ejecutar la aplicación
if __name__ == "__main__":
    app.run_server(debug=True)  # Ejecutar la aplicación en modo de depuración
