# tests/test_data_generator.py
import pytest
from io import StringIO
from apollo11.data_generator import DataGenerator

def test_generate_data():
    data_generator = DataGenerator()
    max_files = 10
    min_files = 5

    data = data_generator.generate_data(max_files, min_files)

    assert data  # Verificar que los datos generados no están vacíos
    assert all(isinstance(value, list) for value in data.values())  # Verificar que los valores son listas
    assert all(len(value) >= min_files and len(value) <= max_files for value in data.values())  # Verificar la cantidad de archivos generados
    # Puedes agregar más aserciones según sea necesario
