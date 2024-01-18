# apollo11/file_manager.py
import os
import shutil
import logging
from typing import Dict, List

class FileManager:
    def __init__(self):
        os.makedirs('backups', exist_ok=True)  # Asegura que la carpeta 'backups' exista

    def manage_files(self, data: Dict[str, List[Dict[str, str]]]):
        os.makedirs('devices', exist_ok=True)  # Asegura que la carpeta 'devices' exista

        for project, files in data.items():
            file_content = files[0]  # Tomar solo el primer archivo para simplificar la lógica
            file_name = f"APL{project}-{len(files)}"
            file_path = os.path.join('devices', file_name + '.log')
            with open(file_path, 'w') as file:
                file.write(f"Date: {file_content['date']}\nMission: {file_content['mission']}\n"
                            f"Device Type: {file_content['device_type']}\nDevice Status: {file_content['device_status']}\n"
                            f"Hash: {file_content['hash']}\n")
                logging.info(f"File {file_name} generated for project {project}")

    def move_processed_files(self):
        backup_folder = 'backups'
        os.makedirs(backup_folder, exist_ok=True)
        # Mover solo el último archivo procesado para cumplir con el formato requerido
        latest_file = max(os.listdir('devices'), key=lambda x: os.path.getmtime(os.path.join('devices', x)))
        source_path = os.path.join('devices', latest_file)
        destination_path = os.path.join(backup_folder, latest_file)
        shutil.move(source_path, destination_path)

        logging.info("Processed file moved to the backups folder.")
