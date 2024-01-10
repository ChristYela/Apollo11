# apollo11/data_generator.py
from typing import Dict, List
import random
from datetime import datetime
import hashlib

class DataGenerator:
    def generate_data(self, max_files: int, project: str) -> Dict[str, List[Dict[str, str]]]:
        data = {}
        for _ in range(random.randint(1, max_files)):
            data.setdefault(project, []).append(self.generate_file_content(project))

        return data

    def generate_file_content(self, project: str) -> Dict:
        date = datetime.now().strftime('%d%m%y%H%M%S')
        device_type = f'device_{random.randint(1, 10)}'
        device_status = random.choice(['excellent', 'good', 'warning', 'faulty', 'killed', 'unknown'])

        if project == 'unknown':
            mission = 'unknown'
        else:
            mission = project

        hash_value = hashlib.md5(f"{date}-{mission}-{device_type}-{device_status}".encode()).hexdigest()

        return {
            'date': date,
            'mission': mission,
            'device_type': device_type,
            'device_status': device_status,
            'hash': hash_value
        }
