from dash import dcc, html, callback, Output, Input
import dash_bootstrap_components as dbc
from pulp import LpMaximize, LpProblem, LpVariable, lpSum, value

# Definir la función de optimización para planificar entrenamientos
def plan_entrenamiento(num_dias):
    # Crear el problema de maximización
    problem = LpProblem("Maximizar_Hipertrofia", LpMaximize)

    # Definir variables de decisión para cada grupo muscular y cada día
    grupos = ['pecho', 'espalda', 'piernas', 'brazos']
    dias = range(1, num_dias + 1)
    series = LpVariable.dicts("Series", [(grupo, dia) for grupo in grupos for dia in dias], lowBound=0, upBound=6, cat='Integer')

    # Variables binarias auxiliares para determinar si un grupo muscular es entrenado en un día específico
    entrenado = LpVariable.dicts("Entrenado", [(grupo, dia) for grupo in grupos for dia in dias], cat='Binary')

    # Función objetivo: maximizar el total de series en la semana
    problem += lpSum(series[(grupo, dia)] for grupo in grupos for dia in dias), "Total de Series"

    # Restricción: no más de 12 series por sesión diaria
    for dia in dias:
        problem += lpSum(series[(grupo, dia)] for grupo in grupos) <= 12, f"MaxSeriesDia{dia}"

    # Restricción: descanso entre entrenamientos para evitar entrenar el mismo grupo en días consecutivos
    for grupo in grupos:
        for dia in range(1, num_dias):  # hasta el penúltimo día para evitar índice fuera de rango
            problem += series[(grupo, dia)] + series[(grupo, dia + 1)] <= 6, f"Descanso_{grupo}_Dia{dia}"

    # Restricción: no más de tres grupos musculares en una misma sesión
    for dia in dias:
        problem += lpSum(entrenado[(grupo, dia)] for grupo in grupos) <= 3, f"MaxGruposDia{dia}"

    # Restricción: entrenar al menos dos grupos musculares diferentes en cada sesión
    for dia in dias:
        problem += lpSum(entrenado[(grupo, dia)] for grupo in grupos) >= 2, f"MinGruposDia{dia}"

    # Restricción: definir la relación entre series y entrenado
    for grupo in grupos:
        for dia in dias:
            problem += series[(grupo, dia)] >= 1 * entrenado[(grupo, dia)]
            problem += series[(grupo, dia)] <= 6 * entrenado[(grupo, dia)]

    # Resolver el problema
    problem.solve()

    # Crear y mostrar el plan semanal
    plan_semanal = {dia: {grupo: value(series[(grupo, dia)]) for grupo in grupos} for dia in dias}

    # Formatear el resultado para mostrarlo en la interfaz
    resultado = f"Plan Semanal para {num_dias} días:<br>"
    for dia, entrenamientos in plan_semanal.items():
        resultado += f"Día {dia}:<br>"
        for grupo, num_series in entrenamientos.items():
            resultado += f"  {grupo}: {num_series} series<br>"
        resultado += "<br>"

    resultado += f"Valor Óptimo de la Función Objetivo: {value(problem.objective)}<br>"

    for grupo in grupos:
        total_series = sum(plan_semanal[dia][grupo] for dia in dias)
        resultado += f"Total de series para {grupo}: {total_series}<br>"

    return resultado

# Definir el layout de la aplicación con estilos y componentes
layout = html.Div(
    style={'fontFamily': 'Kanit, sans-serif', 'backgroundColor': '#EFEFEF', 'padding': '40px', 'minHeight': '100vh', 'display': 'flex', 'flexDirection': 'column', 'justifyContent': 'space-between'},
    children=[
        html.Div(
            className='proceso',
            style={'flex': '1', 'display': 'flex', 'flexDirection': 'row', 'alignItems': 'flex-start'},
            children=[
                html.Div(
                    style={'flex': '3'},
                    children=[
                        html.Div(
                            'Para comenzar ingrese el número de días disponibles para entrenar (mínimo 3, máximo 7):',
                            className='titulomain', style={'fontWeight': 'bold', 'fontSize': '48px', 'color': '#274c77'}
                        ),
                        html.Div(
                            className='pregunta',
                            style={'paddingTop': '20px'},  # Reduce padding para ahorrar espacio
                            children=[
                                dcc.Textarea(id='dias', name='dias', rows='1', cols='50')  # Campo de texto para ingresar los días
                            ]
                        ),
                        html.Button(
                            'Enviar', id='submit-button', n_clicks=0, 
                            style={'borderRadius': '15px', 'backgroundColor': '#274C77', 'color': 'white', 'marginTop': '5px', 'padding': '0 50px'}
                        ),  # Botón para enviar los datos
                        html.Div(
                            id='resultado', className='resultado',
                            style={'width': '600px', 'height': '300px', 'marginTop': '20px', 'marginBottom': '10px', 'padding': '20px', 'backgroundColor': '#a3cef1a6', 'boxShadow': '0 0 10px rgba(0, 0, 0, 0.1)', 'color': '#274C77', 'overflow': 'auto'}
                        ),  # Div para mostrar el resultado
                        html.A(
                            'Volver', href='/', className='back',
                            style={'backgroundColor': '#274C77', 'borderRadius': '15px', 'paddingLeft': '20px', 'paddingRight': '20px', 'color': 'white', 'textDecoration': 'none', 'marginTop': '20px'}
                        )  # Enlace para volver a la página principal
                    ]
                ),
                html.Div(
                    className='imagen2',
                    style={'flex': '1', 'display': 'flex', 'justifyContent': 'flex-end', 'alignItems': 'flex-start', 'paddingTop': '20px', 'marginRight': '50px'},  # Ajusta la imagen a la derecha
                    children=[
                        html.Img(src='/assets/imgs/muscle 2.png', alt='ej2', style={'maxWidth': '400px', 'height': 'auto'})  # Imagen decorativa
                    ]
                )
            ]
        ),
    ]
)

# Definir la función callback para manejar el evento del botón
@callback(
    Output('resultado', 'children'),
    Input('submit-button', 'n_clicks'),
    Input('dias', 'value')
)
def handleButtonClick(n_clicks, dias):
    print(f"Callback ejecutado con n_clicks={n_clicks} y dias={dias}")  # Log para depuración
    if n_clicks > 0 and dias:
        try:
            num_dias = int(dias)
            if num_dias >= 3 and num_dias <= 7:
                resultado = plan_entrenamiento(num_dias)
                print(f"Resultado generado: {resultado}")  # Log para depuración
                return resultado.replace("\n", "<br>")  # Reemplazar saltos de línea por <br>
            else:
                return "El número mínimo de días para entrenar es 3 y el máximo es 7."
        except ValueError:
            return "Por favor, ingrese un número válido."
    return "Ingrese el número de días y presione Enviar."
