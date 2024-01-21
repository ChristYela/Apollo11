# apollo11/dashboard_generator.py

import os
import logging
import json
import pandas as pd
from datetime import datetime
from typing import Dict, List
from apollo11.report_generator import ReportGenerator as rg


class DashboardGenerator:
    def __init__(self):
        # Inicializa el atributo mission_device_states como un diccionario vacío
        self.mission_device_states: Dict[str, Dict[str, int]] = {}

    def generate_dashboard(self, data: Dict[str, List[Dict[str, str]]]):
        # Nombre y ruta del archivo de tablero de control
        dashboard_filename = 'dashboard.json'
        dashboard_path = os.path.join('reports', dashboard_filename)
        report_filename = f'APLSTATS-REPORT-{datetime.now().strftime("%d%m%y%H%M%S")}.log'
        report_path = os.path.join('reports', report_filename)

        # Estructura de datos del tablero de control
        dashboard_data = {
            'last_update': datetime.now().strftime('%d%m%y%H%M%S'),

        }

        # Agregar información de dispositivos por misión al tablero de control
        for mission, device_states in self.mission_device_states.items():
            dashboard_data['missions'][mission] = {
                'total_devices': sum(device_states.values())
            }

        # Escribir el tablero de control en un archivo JSON
        with open(dashboard_path, 'w') as dashboard_file:
            dashboard_file.write(json.dumps(dashboard_data, indent=2))

        # Registrar en el registro que el tablero de control ha sido actualizado
        logging.info(f"Tablero de control actualizado: {dashboard_filename}")
