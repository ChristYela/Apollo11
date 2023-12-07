import os
import logging
from datetime import datetime
from typing import Dict, List

class ReportGenerator:
    def generate_reports(self, data: Dict[str, List[Dict[str, str]]]):
        report_filename = f'APLSTATS-REPORT-{datetime.now().strftime("%d%m%y%H%M%S")}.log'
        report_path = os.path.join('reports', report_filename)

        with open(report_path, 'w') as report_file:
            report_file.write("Reporte de Estadísticas\n\n")

            for mission, device_states in self.mission_device_states.items():
                report_file.write(f"\nMisión: {mission}\n")
                for state, count in device_states.items():
                    report_file.write(f"{state}: {count} eventos\n")

            report_file.write("\nGestión de Desconexiones\n")
            for mission in self.mission_device_states.keys():
                unknown_count = self.mission_device_states[mission]['unknown']
                report_file.write(f"Misión {mission}: {unknown_count} desconexiones\n")

            report_file.write("\nConsolidación de Misiones\n")
            total_faulty_devices = sum(self.mission_device_states[mission]['faulty'] for mission in self.mission_device_states)
            report_file.write(f"Total de dispositivos inoperables: {total_faulty_devices}\n")

            report_file.write("\nCálculo de Porcentajes\n")
            for mission in self.mission_device_states.keys():
                total_devices = sum(self.mission_device_states[mission][state] for state in self.DEVICE_STATES)
                for state in self.DEVICE_STATES:
                    state_count = self.mission_device_states[mission][state]
                    percentage = (state_count / total_devices) * 100 if total_devices > 0 else 0
                    report_file.write(f"{mission} - {state}: {percentage:.2f}%\n")

        logging.info(f"Reporte generado: {report_filename}")