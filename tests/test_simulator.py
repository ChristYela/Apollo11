# tests/test_simulator.py
import pytest
from io import StringIO
import time
from apollo11.simulator import Apolo11Simulator

def test_run_simulation(monkeypatch, capsys):
    # Mockear time.sleep para evitar esperas largas durante las pruebas
    monkeypatch.setattr(time, 'sleep', lambda x: None)

    simulator = Apolo11Simulator(20, 10, 5, 'ORBONE')
    simulator.run_simulation(2)  # Ejecutar dos ciclos de simulación

    captured = capsys.readouterr()
    assert "Ciclo completado. Esperando el próximo ciclo..." in captured.out
