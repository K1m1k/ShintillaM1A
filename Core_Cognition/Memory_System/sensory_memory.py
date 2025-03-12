import logging

logger = logging.getLogger(__name__)

class SensoryMemory:
    def __init__(self):
        self.buffer = []

    def add_sensory_input(self, data):
        """Aggiunge un input sensoriale al buffer."""
        if not isinstance(data, str):
            raise ValueError("L'input sensoriale deve essere una stringa.")
        self.buffer.append(data)
        logger.info(f"Input sensoriale aggiunto: {data}")

    def get_buffer(self):
        """Restituisce il contenuto del buffer."""
        return self.buffer

    def clear_buffer(self):
        """Pulisce il buffer."""
        self.buffer.clear()
        logger.info("Buffer della memoria sensoriale pulito.")
