# **Proyecto de Optimización Matemática: Maximización de Resultados de Entrenamiento**

## **Descripción**
Este proyecto se enmarca en el ejercicio académico realizado en la materia de Optimización Matemática, con el objetivo de diseñar un programa de entrenamiento personalizado que maximice la hipertrofia muscular. Usando técnicas de programación lineal, el proyecto busca optimizar la distribución de series de ejercicios por grupo muscular y por día, teniendo en cuenta diversas restricciones operativas y preferencias del cliente.

## **Problema**
Un gimnasio ofrece a sus miembros un programa personalizado de entrenamiento para maximizar la hipertrofia muscular. La hipertrofia se optimiza realizando entre 10 y 20 series por grupo muscular por semana. Se propone enfocarse en cuatro grupos musculares principales: pecho, espalda, piernas y brazos. El cliente dispone de 5 días a la semana para entrenar, con un máximo de 2 horas por sesión de entrenamiento.

## **Objetivo**
Determinar el número óptimo de series por grupo muscular y por día para maximizar la hipertrofia, considerando las siguientes restricciones:

- Cada grupo muscular debe descansar al menos 1 día entre entrenamientos.
- No se deben superar las 6 series por grupo muscular en una sola sesión de entrenamiento.
- El cliente prefiere no entrenar más de 3 grupos musculares por sesión.

## **Metodología**
El problema se aborda mediante un modelo de programación lineal, donde se definirán variables para el número de series dedicadas a cada grupo muscular por día. La función objetivo será maximizar el volumen total de entrenamiento, sujeto a las restricciones mencionadas.

## **Contextualización y Terminología**
En un gimnasio, se ha propuesto un desafío interesante: diseñar un programa de entrenamiento que maximice la hipertrofia muscular, es decir, el aumento en el tamaño de los músculos. Para lograr esto, es importante planificar cuidadosamente cuántas series de ejercicios debe realizar una persona por grupo muscular y por día a lo largo de una semana.

### **¿Qué es una serie?**
Una "serie" es un conjunto de repeticiones de un ejercicio específico realizado sin descansar. Por ejemplo, hacer 10 levantamientos de pesas seguidos constituye una serie.

### **Los Grupos Musculares Involucrados**
El programa se enfoca en cuatro grupos musculares principales: pecho, espalda, piernas y brazos. El desafío es determinar cuántas series dedicar a cada uno de estos grupos para obtener los mejores resultados.

### **Planificación Semanal**
Cada persona tiene cinco días a la semana para entrenar, con un máximo de dos horas disponibles por sesión. Hay reglas específicas que deben seguirse para evitar el sobreentrenamiento y promover la recuperación muscular efectiva:

- **Descanso entre entrenamientos:** Cada grupo muscular necesita descansar al menos un día después de ser entrenado, antes de ser trabajado nuevamente.
- **Límite de series por sesión:** No se pueden realizar más de 6 series para un mismo grupo muscular en un solo día.
- **Diversidad de entrenamiento diario:** Se prefiere no entrenar más de tres grupos musculares en una misma sesión.

## **Estructura del Proyecto**

El proyecto está compuesto por varios archivos clave que incluyen:

- `app.py`: Contiene la lógica principal de la aplicación web Flask, gestionando las rutas y funciones para manejar las solicitudes y optimizar el plan de entrenamiento.
- `optimizer.py`: Incluye la función de optimización que utiliza PuLP para planificar los entrenamientos según las restricciones y la función objetivo.
- `index.html`: Define la estructura de la página de inicio, con una llamada a la acción para comenzar el viaje de fitness.
- `main.html`: Define la estructura de la página principal donde los usuarios pueden ingresar el número de días disponibles para entrenar y ver los resultados de la optimización.
- `styles.css`: Contiene los estilos para las páginas HTML, asegurando un diseño visual consistente y atractivo.

## **Resultados Clave**

El proyecto ha demostrado que es posible generar planes de entrenamiento personalizados que maximicen la hipertrofia muscular utilizando técnicas de programación lineal. Los resultados clave incluyen:

- Optimización de la distribución de series por grupo muscular y por día.
- Adaptabilidad a diversas restricciones y preferencias del usuario.
- Mejora significativa en la eficiencia y efectividad de los entrenamientos.
- Minimización del riesgo de sobreentrenamiento mediante un adecuado equilibrio entre ejercicio y descanso.

## **Beneficios de la Aplicación**

- **Optimización del Tiempo de Entrenamiento:** Maximiza los resultados dentro del tiempo disponible, asegurando sesiones efectivas y eficientes.
- **Planes de Entrenamiento Personalizados:** Adaptados a las necesidades y objetivos específicos de cada usuario.
- **Mejora del Desempeño Físico:** Optimiza la distribución de ejercicios y el descanso entre grupos musculares.
- **Facilidad de Uso:** Interfaz intuitiva y fácil de usar para personas con cualquier nivel de experiencia en fitness.
- **Ahorro de Tiempo:** Automatiza la planificación de rutinas de entrenamiento, permitiendo más tiempo para el ejercicio efectivo.

## **Aplicaciones Potenciales**

- **Gimnasios y Centros de Fitness:** Ofrecer planes de entrenamiento personalizados a los miembros.
- **Entrenadores Personales:** Diseñar programas de entrenamiento óptimos para los clientes.
- **Atletas y Deportistas:** Optimizar entrenamientos y mejorar el rendimiento en competiciones.
- **Corporaciones y Empresas:** Promover el bienestar de los empleados mediante programas de bienestar corporativo.
- **Educación y Formación:** Utilizar como herramienta didáctica en instituciones educativas y programas de formación en ciencias del deporte.
- **Usuarios Individuales:** Ayudar a cualquier persona interesada en mejorar su condición física.

## **Conclusiones y Recomendaciones**

### **Resumen de Puntos Clave**

En este proyecto, hemos desarrollado una aplicación de optimización matemática para diseñar programas de entrenamiento personalizados que maximicen la hipertrofia muscular. La aplicación utiliza técnicas de programación lineal para optimizar la distribución de series de ejercicios por grupo muscular y por día, teniendo en cuenta diversas restricciones operativas y preferencias del cliente. Los resultados muestran que la aplicación puede generar planes de entrenamiento efectivos y eficientes, adaptados a las necesidades y objetivos específicos de cada usuario.

### **Recomendaciones**

- **Mejorar la Interfaz de Usuario:** Continuar mejorando la interfaz de usuario para hacerla aún más intuitiva y fácil de usar, incluyendo tutoriales y ayudas contextuales.
- **Incorporar Más Variables:** Incluir más variables y parámetros en el modelo de optimización, como el nivel de condición física del usuario, el tipo de ejercicios y las preferencias personales.
- **Desarrollar Funcionalidades Adicionales:** Desarrollar funcionalidades adicionales como la posibilidad de ajustar los planes de entrenamiento en tiempo real, integrar recordatorios y notificaciones, y ofrecer análisis detallados del progreso del usuario.
- **Expandir las Aplicaciones:** Explorar nuevas aplicaciones de la herramienta en otros contextos, como la rehabilitación física, el entrenamiento para deportes específicos y la promoción de la salud en entornos corporativos.
- **Realizar Pruebas y Validaciones:** Continuar realizando pruebas y validaciones con usuarios reales para mejorar la precisión y efectividad de los planes generados.

## **Bibliografía**

1. Schoenfeld, B. J. (2010). The mechanisms of muscle hypertrophy and their application to resistance training. *Global Fitness Services, Scarsdale, New York*.
2. Krzysztofik, M., Wilk, M., Wojdała, G., & Gołaś, A. (2019). Maximizing muscle hypertrophy: A systematic review of advanced resistance training techniques and methods. *International Journal of Environmental Research and Public Health, 16*(24), 4897. doi: 10.3390/ijerph16244897.
3. Bernárdez-Vázquez, R., Raya-González, J., Castillo, D., & Beato, M. (2022). Resistance training variables for optimization of muscle hypertrophy: An umbrella review. *Frontiers in Sports and Active Living, 4*, 949021. doi: 10.3389/fspor.2022.949021.

