import pymysql
import json

# Configuración de la conexión a la base de datos
host = "127.0.0.1"
user = "root"
password = "fernando"
db = "tta039"

# Crear una conexión a la base de datos
conexion = pymysql.connect(host=host, user=user, password=password, db=db)

try:
    # Consulta SQL para Unidades de Aprendizaje
    with conexion.cursor() as cursor_ua:
        sql_ua = """
        SELECT 
            ua_id,
            area_id,
            ua_des,
            ua_horast
        FROM 
            UnidadAprendizaje;
        """
        
        cursor_ua.execute(sql_ua)
        
        # Obtener los resultados para Unidades de Aprendizaje
        resultados_ua = cursor_ua.fetchall()
        
        # Convertir los resultados a la estructura JSON deseada para Unidades de Aprendizaje
        unidades = {"unidades_aprendizaje": {}}
        for i, fila in enumerate(resultados_ua):
            unidad_key = f"unidad{i+1}"
            unidades["unidades_aprendizaje"][unidad_key] = {
                "ua_id": fila[0],
                "area_id": fila[1],
                "ua_des": fila[2],
                "ua_horat": fila[3]
            }

        # Convertir el diccionario a una cadena JSON y guardar en un archivo para Unidades de Aprendizaje
        with open("UA.json", "w", encoding="utf-8") as file_ua:
            json.dump(unidades, file_ua, indent=4, ensure_ascii=False)

    # Consulta SQL para Docentes
    with conexion.cursor() as cursor_docentes:
        sql_docentes = """
        SELECT 
            Profesor.profesor_id,
            Profesor_hrs.profesor_hrs_bas,
            Profesor.area
        FROM 
            Profesor
        INNER JOIN 
            Profesor_hrs ON Profesor.profesor_hrs_id = Profesor_hrs.profesor_hrs_id;
        """
        
        cursor_docentes.execute(sql_docentes)
        
        # Obtener los resultados para Docentes
        resultados_docentes = cursor_docentes.fetchall()
        
        # Convertir los resultados a la estructura JSON deseada para Docentes
        docentes = {"docentes": {}}
        for i, fila in enumerate(resultados_docentes):
            docente_key = f"docente{i+1}"
            docentes["docentes"][docente_key] = {
                "profesor_id": fila[0],
                "profesor_hrs_bas": fila[1],
                "area": fila[2]
            }

        # Convertir el diccionario a una cadena JSON y guardar en un archivo para Docentes
        with open("docentes.json", "w", encoding="utf-8") as file_docentes:
            json.dump(docentes, file_docentes, indent=4, ensure_ascii=False)

finally:
    # Cerrar la conexión a la base de datos
    conexion.close()
