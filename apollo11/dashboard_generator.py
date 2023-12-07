import os
import logging
import json
from datetime import datetime
from typing import Dict, List

class DashboardGenerator:
    def generate_dashboard(self, data: Dict[str, List[Dict[str, str]]]):
        dashboard_filename = 'dashboard.json'
        dashboard_path = os.path.join('reports', dashboard_filename)
        dashboard_data = {
            'last_update': datetime.now().strftime('%d%m%y%H%M%S'),
            'missions': {}
        }

        for mission, device_states in self.mission_device_states.items():
            dashboard_data['missions'][mission] = {
                'total_devices': sum(device_states.values())
            }

        with open(dashboard_path, 'w') as dashboard_file:
            # Ajustar el formato y contenido del archivo JSON según las necesidades específicas
            dashboard_file.write(json.dumps(dashboard_data, indent=2))

        logging.info(f"Tablero de control actualizado: {dashboard_filename}")


