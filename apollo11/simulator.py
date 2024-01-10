# apollo11/simulator.py
from typing import Dict, List
from datetime import datetime
import logging
import time
from apollo11.data_generator import DataGenerator
from apollo11.file_manager import FileManager
from apollo11.report_generator import ReportGenerator
from apollo11.dashboard_generator import DashboardGenerator

class Apolo11Simulator:
    def __init__(self, simulation_interval: int, max_files: int, project: str):
        self.simulation_interval = simulation_interval
        self.max_files = max_files
        self.project = project
        self.data_generator = DataGenerator()
        self.file_manager = FileManager()
        self.report_generator = ReportGenerator()
        self.dashboard_generator = DashboardGenerator()

    def run_simulation(self, num_cycles: int):
        for _ in range(num_cycles):
            data = self.data_generator.generate_data(self.max_files, self.project)
            self.file_manager.manage_files(data)
            self.report_generator.generate_reports(data)
            self.file_manager.move_processed_files()
            self.dashboard_generator.generate_dashboard(data)
            logging.info("Ciclo completado. Esperando el próximo ciclo...")

            # Agregar lógica para esperar el intervalo de simulación.
            time.sleep(self.simulation_interval)
