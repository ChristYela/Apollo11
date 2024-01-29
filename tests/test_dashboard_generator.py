# tests/test_dashboard_generator.py
import pytest
from io import StringIO
import json
from apollo11.dashboard_generator import DashboardGenerator

def test_dashboard_data_clean(tmp_path):
    dashboard_generator = DashboardGenerator()

    dashboard_path = tmp_path / 'dashboard.json'
    with open(dashboard_path, 'w') as report_file:
        dashboard_data = {'mission1': {'excellent': 5, 'good': 3}, 'mission2': {'excellent': 10, 'good': 8}}
        report_file.write(json.dumps(dashboard_data, indent=4))

    dashboard_generator.dashboard_data_clean()

    with open(dashboard_path, 'r') as report_file:
        cleaned_data = json.load(report_file)
        for mission_data in cleaned_data.values():
            for value in mission_data.values():
                assert value == 0

def test_print_dashboard(capsys, tmp_path):
    dashboard_generator = DashboardGenerator()

    dashboard_path = tmp_path / 'dashboard.json'
    with open(dashboard_path, 'w') as report_file:
        dashboard_data = {'mission1': {'excellent': 5, 'good': 3}, 'mission2': {'excellent': 10, 'good': 8}}
        report_file.write(json.dumps(dashboard_data, indent=4))

    dashboard_generator.print_dashboard()

    captured = capsys.readouterr()
    assert "mission1" in captured.out
    assert "mission2" in captured.out
    assert "5(60.0%)" in captured.out
    assert "10(80.0%)" in captured.out
