# tests/test_report_generator.py
import pytest
from io import StringIO
import json
from apollo11.report_generator import ReportGenerator

def test_generate_reports(tmp_path):
    report_generator = ReportGenerator()

    data = {'project1': [{'date': '210124120000', 'mission': 'ORBONE', 'device_type': 'device_1', 'device_status': 'excellent', 'hash': 'hash1'},
                            {'date': '210124121500', 'mission': 'ORBONE', 'device_type': 'device_2', 'device_status': 'good', 'hash': 'hash2'}]}

    report_generator.generate_reports(data)

    report_filename = f'APLSTATS-REPORT-210124120000.log'
    report_path = tmp_path / 'reports' / report_filename

    assert report_path.is_file()

    with open(report_path, 'r') as report_file:
        report_content = json.load(report_file)
        assert 'project1' in report_content
        assert 'excellent' in report_content['project1']
        assert report_content['project1']['excellent'] == 1
