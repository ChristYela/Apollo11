# apollo11/report_generator.py
import os
import logging
from datetime import datetime
from typing import Dict, List

class ReportGenerator:
    def __init__(self):
        # Inicializa el atributo project_device_states como un diccionario vacío
        self.project_device_states: Dict[str, Dict[str, int]] = {}

    def generate_reports(self, data: Dict[str, List[Dict[str, str]]]):
        # Inicializar el diccionario si aún no ha sido inicializado
        if not isinstance(self.project_device_states, dict):
            self.project_device_states = {}

        # Actualizar el diccionario con nuevos datos
        for project, files in data.items():
            project_states = {'excellent': 0, 'good': 0, 'warning': 0, 'faulty': 0, 'killed': 0, 'unknown': 0}
            for file_content in files:
                project_states[file_content['device_status']] += 1
            self.project_device_states[project] = project_states

        # Generar un único informe consolidado
        report_filename = f'APLSTATS-REPORT-{datetime.now().strftime("%d%m%y%H%M%S")}.log'
        report_path = os.path.join('reports', report_filename)

        with open(report_path, 'w', encoding='utf-8') as report_file:
            report_file.write("Reporte de Estadísticas\n\n")

            for project, device_states in self.project_device_states.items():
                report_file.write(f"\nMisión: {project}\n")
                for state, count in device_states.items():
                    report_file.write(f"{state}: {count} eventos\n")

                unknown_count = device_states['unknown']
                report_file.write(f"Gestión de Desconexiones en la Misión {project}: {unknown_count} desconexiones\n\n")

            report_file.write("Consolidación de Misiones\n")
            total_faulty_devices = sum(device_states['faulty'] for device_states in self.project_device_states.values())
            report_file.write(f"Total de dispositivos inoperables: {total_faulty_devices}\n\n")

            report_file.write("Cálculo de Porcentajes\n")
            for project in self.project_device_states.keys():
                total_devices = sum(device_states[state] for state in self.project_device_states[project])
                for state in self.project_device_states[project]:
                    state_count = self.project_device_states[project][state]
                    percentage = (state_count / total_devices) * 100 if total_devices > 0 else 0
                    report_file.write(f"{project} - {state}: {percentage:.2f}%\n")

            logging.info(f"Informe consolidado generado: {report_filename}")

    def get_current_timestamp(self):
        return datetime.now().strftime('%Y%m%d%H%M%S')
