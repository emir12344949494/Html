# src/generate_report.py


def generar_informe(nombre_archivo, contenido):
    try:
        with open(nombre_archivo, 'w') as archivo:
            archivo.write(contenido)
        print(f"Informe generado exitosamente en {nombre_archivo}")
    except Exception as e:
        print(f"Error al generar el informe: {e}")

if __name__ == "__main__":
    # Ejemplo de contenido para el informe
    contenido_informe = """
    Informe de Proyecto de IA en Ciberseguridad

    Resumen:
    - Datos procesados: Se han procesado y limpiado datos para el modelado.
    - Modelo entrenado: Se ha entrenado un modelo de IA utilizando Random Forest.

    Métricas de Rendimiento:
    - Precisión: 0.85
    - Recall: 0.78
    - F1-score: 0.81
    - ROC AUC Score: 0.91

    Conclusiones:
    - El modelo muestra un buen rendimiento en la clasificación de amenazas cibernéticas.
    - Se recomienda explorar modelos adicionales y ajustar hiperparámetros para mejorar aún más la precisión.

    """

    # Nombre del archivo donde se guardará el informe
    nombre_archivo = 'reports/informe_proyecto_ia.txt'

    # Generar el informe
    generar_informe(nombre_archivo, contenido_informe)
