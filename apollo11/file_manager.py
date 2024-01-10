# apollo11/file_manager.py
import os
import shutil
import logging
from typing import Dict, List

class FileManager:
    def manage_files(self, data: Dict[str, List[Dict[str, str]]]):
        for project, files in data.items():
            for file_content in files:
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
        for file_name in os.listdir('devices'):
            source_path = os.path.join('devices', file_name)
            destination_path = os.path.join(backup_folder, file_name)
            shutil.move(source_path, destination_path)

        logging.info("Processed files moved to the backups folder.")
