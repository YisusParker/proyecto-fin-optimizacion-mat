from pulp import LpProblem, LpMaximize, LpVariable, lpSum, value


# Definir la función de optimización para planificar entrenamientos
def plan_entrenamiento(num_dias):
    # Crear el problema de maximización con el nombre "Maximizar_Hipertrofia"
    problem = LpProblem("Maximizar_Hipertrofia", LpMaximize)

    # Definir los grupos musculares y el rango de días
    grupos = ["pecho", "espalda", "piernas", "brazos"]
    dias = range(1, num_dias + 1)

    # Definir variables de decisión para el número de series para cada grupo muscular y cada día
    # Las variables están limitadas entre 0 y 6 y son de tipo entero
    series = LpVariable.dicts(
        "Series",
        [(grupo, dia) for grupo in grupos for dia in dias],
        lowBound=0,
        upBound=6,
        cat="Integer",
    )

    # Definir variables binarias auxiliares para determinar si un grupo muscular es entrenado en un día específico
    entrenado = LpVariable.dicts(
        "Entrenado", [(grupo, dia) for grupo in grupos for dia in dias], cat="Binary"
    )

    # Función objetivo: maximizar el total de series en la semana
    problem += (
        lpSum(series[(grupo, dia)] for grupo in grupos for dia in dias),
        "Total de Series",
    )

    # Restricción: no más de 12 series por sesión diaria
    for dia in dias:
        problem += (
            lpSum(series[(grupo, dia)] for grupo in grupos) <= 12,
            f"MaxSeriesDia{dia}",
        )

    # Restricción: descanso entre entrenamientos para evitar entrenar el mismo grupo en días consecutivos
    for grupo in grupos:
        for dia in range(1, num_dias):
            problem += (
                series[(grupo, dia)] + series[(grupo, dia + 1)] <= 6,
                f"Descanso_{grupo}_Dia{dia}",
            )

    # Restricción: no más de tres grupos musculares en una misma sesión
    for dia in dias:
        problem += (
            lpSum(entrenado[(grupo, dia)] for grupo in grupos) <= 3,
            f"MaxGruposDia{dia}",
        )

    # Restricción: entrenar al menos dos grupos musculares diferentes en cada sesión
    for dia in dias:
        problem += (
            lpSum(entrenado[(grupo, dia)] for grupo in grupos) >= 2,
            f"MinGruposDia{dia}",
        )

    # Restricción: definir la relación entre series y entrenado
    for grupo in grupos:
        for dia in dias:
            problem += series[(grupo, dia)] >= 1 * entrenado[(grupo, dia)]
            problem += series[(grupo, dia)] <= 6 * entrenado[(grupo, dia)]

    # Resolver el problema de optimización
    problem.solve()

    # Crear y mostrar el plan semanal basado en la solución del problema
    plan_semanal = {
        dia: {grupo: value(series[(grupo, dia)]) for grupo in grupos} for dia in dias
    }

    # Formatear el resultado para mostrarlo en la interfaz
    resultado = f"Plan Semanal para {num_dias} días:<br>"
    for dia, entrenamientos in plan_semanal.items():
        resultado += f"Día {dia}:<br>"
        for grupo, num_series in entrenamientos.items():
            resultado += f"  {grupo}: {num_series} series<br>"
        resultado += "<br>"

    # Formatear el valor óptimo de la función objetivo para mostrarlo en la interfaz
    valor_optimo = (
        f"Valor Óptimo de la Función Objetivo: {value(problem.objective)}<br>"
    )
    for grupo in grupos:
        total_series = sum(plan_semanal[dia][grupo] for dia in dias)
        valor_optimo += f"Total de series para {grupo}: {total_series}<br>"

    return resultado, valor_optimo
