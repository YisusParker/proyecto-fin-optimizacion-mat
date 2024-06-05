from flask import Flask, render_template, request, jsonify, send_from_directory
import os
import random
from pulp import LpProblem, LpMaximize, LpVariable, lpSum, value

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/main')
def main():
    return render_template('main.html')

@app.route('/optimize', methods=['POST'])
def optimize():
    dias = int(request.form['dias'])
    resultado, valor_optimo = plan_entrenamiento(dias)
    return jsonify({
        'resultado': resultado,
        'valor_optimo': valor_optimo
    })

@app.route('/download_pdf/<int:dias>', methods=['GET'])
def download_pdf(dias):
    if dias < 3 or dias > 7:
        return "Número de días inválido", 400

    pdf_directory = os.path.join(app.static_folder, 'pdfs', str(dias))
    if not os.path.exists(pdf_directory):
        return "No se encontraron PDFs para el número de días especificado", 404

    pdf_files = [f for f in os.listdir(pdf_directory) if f.endswith('.pdf')]
    if not pdf_files:
        return "No se encontraron PDFs en la carpeta especificada", 404

    random_pdf = random.choice(pdf_files)
    return send_from_directory(pdf_directory, random_pdf, as_attachment=True)

def plan_entrenamiento(num_dias):
    problem = LpProblem("Maximizar_Hipertrofia", LpMaximize)

    grupos = ['pecho', 'espalda', 'piernas', 'brazos']
    dias = range(1, num_dias + 1)
    series = LpVariable.dicts("Series", [(grupo, dia) for grupo in grupos for dia in dias], lowBound=0, upBound=6, cat='Integer')
    entrenado = LpVariable.dicts("Entrenado", [(grupo, dia) for grupo in grupos for dia in dias], cat='Binary')

    problem += lpSum(series[(grupo, dia)] for grupo in grupos for dia in dias), "Total de Series"

    for dia in dias:
        problem += lpSum(series[(grupo, dia)] for grupo in grupos) <= 12, f"MaxSeriesDia{dia}"

    for grupo in grupos:
        for dia in range(1, num_dias):
            problem += series[(grupo, dia)] + series[(grupo, dia + 1)] <= 6, f"Descanso_{grupo}_Dia{dia}"

    for dia in dias:
        problem += lpSum(entrenado[(grupo, dia)] for grupo in grupos) <= 3, f"MaxGruposDia{dia}"

    for dia in dias:
        problem += lpSum(entrenado[(grupo, dia)] for grupo in grupos) >= 2, f"MinGruposDia{dia}"

    for grupo in grupos:
        for dia in dias:
            problem += series[(grupo, dia)] >= 1 * entrenado[(grupo, dia)]
            problem += series[(grupo, dia)] <= 6 * entrenado[(grupo, dia)]

    problem.solve()

    plan_semanal = {dia: {grupo: value(series[(grupo, dia)]) for grupo in grupos} for dia in dias}

    resultado = f"Plan Semanal para {num_dias} días:<br>"
    for dia, entrenamientos in plan_semanal.items():
        resultado += f"Día {dia}:<br>"
        for grupo, num_series in entrenamientos.items():
            resultado += f"  {grupo}: {num_series} series<br>"
        resultado += "<br>"

    valor_optimo = f"Valor Óptimo de la Función Objetivo: {value(problem.objective)}<br>"
    for grupo in grupos:
        total_series = sum(plan_semanal[dia][grupo] for dia in dias)
        valor_optimo += f"Total de series para {grupo}: {total_series}<br>"

    return resultado, valor_optimo

if __name__ == '__main__':
    app.run()
