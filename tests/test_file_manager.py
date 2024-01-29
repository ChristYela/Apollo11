# tests/test_file_manager.py
import pytest
from io import StringIO
import json
import os
from apollo11.file_manager import FileManager

def test_manage_files(tmp_path):
    file_manager = FileManager()

    data = {'project1': [{'date': '210124120000', 'mission': 'ORBONE', 'device_type': 'device_1', 'device_status': 'excellent', 'hash': 'hash1'},
                            {'date': '210124121500', 'mission': 'ORBONE', 'device_type': 'device_2', 'device_status': 'good', 'hash': 'hash2'}]}

    file_manager.manage_files(data)

    project_folder = tmp_path / 'devices' / 'project1'
    assert project_folder.is_dir()

    for file_data in data['project1']:
        file_name = f"APL{file_data['mission']}-{len(data['project1'])}.log"
        file_path = project_folder / file_name

        assert file_path.is_file()
        with open(file_path, 'r') as file:
            file_content = json.load(file)
            assert file_content == {'project1': [file_data]}
