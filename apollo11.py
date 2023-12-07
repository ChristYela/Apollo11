import sys
import logging
from argparse import ArgumentParser
import yaml
from apollo11.simulator import Apolo11Simulator

def main():
    """
    Función principal para ejecutar el programa Apolo-11.
    """
    try:
        # Configuración de LOGGING
        logging.basicConfig(level=logging.INFO)

        # Configuración de argumentos de línea de comandos
        parser = ArgumentParser(description="Apolo-11 Simulation")
        parser.add_argument("--config", help="Path to the configuration YAML file", default="config/config.yml")
        args = parser.parse_args()

        # Cargar configuraciones desde el archivo YAML
        with open(args.config, "r") as config_file:
            config = yaml.load(config_file, Loader=yaml.FullLoader)

            # Configurar logging, etc. (si es necesario)
            
            # Crear instancia de Apolo11Simulator y ejecutar la simulación
            apollo_simulator = Apolo11Simulator(simulation_interval=config['intervalo_simulacion'])
            apollo_simulator.run_simulation()

    except Exception as e:
        # Manejo de excepciones y registro en LOGGING
        logging.error(f"Error en la ejecución principal: {e}")

if __name__ == "__main__":
    main()
