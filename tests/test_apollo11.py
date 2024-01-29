# tests/test_apollo11.py
import pytest
from io import StringIO
from apollo11 import main

@pytest.mark.parametrize("args, expected_output", [
    (["--config", "config/config.yml", "--project", "ORBONE"], "Ciclo completado. Esperando el próximo ciclo..."),
    # Agrega más combinaciones de argumentos y salidas esperadas según sea necesario
])
def test_main(args, expected_output, monkeypatch, capsys):
    monkeypatch.setattr("sys.argv", ["apollo11.py"] + args)

    with pytest.raises(SystemExit) as context:
        main()

    assert context.value.code == 0
    captured = capsys.readouterr()
    assert expected_output in captured.out

