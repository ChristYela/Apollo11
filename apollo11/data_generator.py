# apollo11/data_generator.py
import os
import random
import hashlib
from datetime import datetime
from typing import Dict, List

class DataGenerator:
    MISSIONS = ["ORBONE", "CLNM", "TMRS", "GALXONE", "UNKN"]
    DEVICE_STATES = ["excellent", "good", "warning", "faulty", "killed", "unknown"]

    def generate_data(self, max_files: int, project: str) -> Dict[str, List[Dict[str, str]]]:
        data = {}

        for _ in range(random.randint(1, max_files)):
            mission = project if project in self.MISSIONS else "UNKN"
            device_type = f'device_{random.randint(1, 10)}'
            device_status = random.choice(self.DEVICE_STATES)

            hash_value = self.generate_hash(mission, device_type, device_status)

            file_content = {
                "date": datetime.now().strftime("%d%m%y%H%M%S"),
                "mission": mission,
                "device_type": device_type,
                "device_status": device_status,
                "hash": hash_value[:32]  # Tomar solo los primeros 32 caracteres del hash
            }

            if project not in data:
                data[project] = []

            data[project].append(file_content)

        return data

    def generate_hash(self, mission: str, device_type: str, device_status: str) -> str:
        # Generar hash solo si la misión no es "unknown"
        if mission == "UNKN":
            return "unknown"

        data_to_hash = f"{datetime.now().strftime('%d%m%y%H%M%S')}{mission}{device_type}{device_status}"
        hash_value = hashlib.sha256(data_to_hash.encode()).hexdigest()
        return hash_value
