import os
import shutil
import logging
from typing import Dict, List

class FileManager:
    def manage_files(self, data: Dict[str, List[Dict[str, str]]]):
        for mission_code, files in data.items():
            for file_content in files:
                file_name = f"APL{mission_code}-{len(files)}"  # Ajustar la lógica según necesidades específicas
                file_path = os.path.join('devices', file_name + '.log')
                with open(file_path, 'w') as file:
                    # Ajustar el formato y contenido del archivo según las necesidades específicas
                    file.write(f"Date: {file_content['date']}\nMission: {file_content['mission']}\n"
                                f"Device Type: {file_content['device_type']}\nDevice Status: {file_content['device_status']}\n"
                                f"Hash: {file_content['hash']}\n")
                    logging.info(f"File {file_name} generated for mission {mission_code}")

    def move_processed_files(self):
        backup_folder = 'backups'
        os.makedirs(backup_folder, exist_ok=True)
        for file_name in os.listdir('devices'):
            source_path = os.path.join('devices', file_name)
            destination_path = os.path.join(backup_folder, file_name)
            shutil.move(source_path, destination_path)

        logging.info("Processed files moved to the backups folder.")
