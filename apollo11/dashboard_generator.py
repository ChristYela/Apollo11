# apollo11/dashboard_generator.py

import os
import logging
import json
import pandas as pd
from datetime import datetime
from typing import Dict, List


class DashboardGenerator:
    def __init__(self):
        # Inicializa el atributo mission_device_states como un diccionario vacío
        self.mission_device_states: Dict[str, Dict[str, int]] = {}

    def generate_dashboard(self, start: str, end: str):

        def dashboard_data_update(self, data_dash: dict, data_add: dict):
            """
            Esta funcion sumara los nuevos reportes a un diccionario global
            """
            for key, value in data_add.items():

                if type(value) == dict:
                    for keys, values in value.items():
                        if keys != 'percentages':
                            val1 = data_dash[key][keys]
                            val2 = data_add[key][keys]
                            data_dash[key][keys] = val1 + val2
                        else:
                            continue
                else:
                    val1 = data_dash[key]
                    val2 = data_add[key]
                    data_dash[key] = val1 + val2
            with open(dashboard_path, 'w') as report_file:
                report_file.write(json.dumps(data_dash, indent=4))

        def dashboard_data_clean(self,):
            """
            Se usa para limpiar el historial de las misiones

            """
            with open(dashboard_path, 'r') as report_file:
                dashboard_dict = json.load(report_file)
            misions = ["ORBONE", "CLNM", "TMRS", "GALXONE", "UNKN"]
            for mision in misions:
                for key, value in dashboard_dict[mision].items():
                    dashboard_dict[mision][key] = 0
                with open(dashboard_path, 'w') as report_file:
                    report_file.write(json.dumps(dashboard_dict, indent=4))

        def print_dashboard():
            filas = []
            columnas = []
            with open(dashboard_path, 'r') as report_file:
                dashboard_dict = json.load(report_file)
            for key, value in dashboard_dict.items():
                if dashboard_dict[key]['total_devices'] != 0:

                    for keys, values in value.items():
                        percentage = round(
                            100*value[keys]/dashboard_dict[key]['total_devices'], 2)
                        value[keys] = f'{values}-{percentage}%'
                else:
                    continue
                filas.append(key)
                columnas.append(value)
            db = pd.DataFrame(columnas, index=filas)
            print(db)
            logging.debug(
                f"Tablero de control actualizado: {dashboard_filename}")

        # Nombre y ruta del archivo de tablero de control
        dashboard_filename = f'dashboard.json'
        dashboard_path = os.path.join('dashboard', dashboard_filename)
        # Llamar los archivos
        # Crear un diccionario en blanco
        with open(dashboard_path, 'r') as report_file:
            dashboard_dict = json.load(report_file)
        # Llamar los reportes acumulados
        content = os.listdir('./reports')
        for report_file in content:
            filename = report_file
            path_file = os.path.join('reports', filename)
            with open(path_file, "r") as fl:
                act_report_file = json.load(fl)
            dashboard_data_update(self, dashboard_dict, act_report_file)
            logging.debug(
                f"Se esta agregando el archivo {report_file} al dashboard")
        print_dashboard()
        dashboard_data_clean(self)
        logging.debug(
            f"Se limpiaron lo registros de dashboard.json")
        time = datetime.now().strftime('%Y%m%d%H%M%S')
        logging.info(f'Ultima actualización {time}')

        # Estructura de datos del tablero de control

        # Agregar información de dispositivos por misión al tablero de control

        # Escribir el tablero de control en un archivo JSON

        # Registrar en el registro que el tablero de control ha sido actualizado
