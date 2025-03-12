import logging
import random
import time

logger = logging.getLogger(__name__)

class SubconsciousLoop:
    def __init__(self, sensory_memory, working_memory, long_term_memory):
        self.sensory_memory = sensory_memory
        self.working_memory = working_memory
        self.long_term_memory = long_term_memory
        self.dream_simulation = DreamSimulation(long_term_memory)
        self.background_tasks = BackgroundTasks(sensory_memory, working_memory, long_term_memory)

    def run_background_tasks(self):
        """Esegue attività in background."""
        logger.info("Avvio attività in background...")
        while True:
            self.background_tasks.run_tasks()
            self.dream_simulation.simulate_dream()
            time.sleep(5)  # Simula un intervallo di tempo


class DreamSimulation:
    def __init__(self, long_term_memory):
        self.long_term_memory = long_term_memory

    def simulate_dream(self):
        """Simula un sogno basato sulle informazioni della memoria a lungo termine."""
        storage = self.long_term_memory.get_storage()
        if storage:
            key = random.choice(list(storage.keys()))
            dream_content = storage[key]
            logger.info(f"Sogno simulato basato su '{key}': {dream_content}")
        else:
            logger.warning("Nessuna informazione nella memoria a lungo termine per simulare sogni.")


class BackgroundTasks:
    def __init__(self, sensory_memory, working_memory, long_term_memory):
        self.sensory_memory = sensory_memory
        self.working_memory = working_memory
        self.long_term_memory = long_term_memory

    def run_background_tasks(self):
        """Esegue attività in background."""
        logger.info("Avvio attività in background...")
        while True:
            try:
                # Recupera i dati dalla memoria a lungo termine
                long_term_data = self.long_term_memory.get_storage()

                # Verifica che i dati siano un dizionario
                if isinstance(long_term_data, dict):
                    for key in long_term_data.keys():
                        logger.info(f"Elaborazione della chiave: {key}")
                        # Esegui altre operazioni con i dati
                else:
                    logger.error("Il tipo di dati della memoria a lungo termine non è supportato.")

                # Pulizia della memoria operativa
                self.working_memory.clear_contents()
                logger.info("Memoria operativa pulita.")
            except Exception as e:
                logger.error(f"Errore durante l'esecuzione delle attività in background: {e}")

            time.sleep(5)  # Simula un intervallo di tempo

    def run_tasks(self):
        """Esegue attività in background."""
        logger.info("Esecuzione attività in background...")
        self.process_sensory_data()
        self.perform_housekeeping()

    def process_sensory_data(self):
        """Elabora i dati sensoriali."""
        buffer = self.sensory_memory.get_buffer()
        for data in buffer:
            if self.working_memory.add_item(data):
                self.sensory_memory.clear_buffer()
                logger.info(f"Dati sensoriali elaborati e spostati in memoria operativa: {data}")

    def perform_housekeeping(self):
        """Esegue attività di manutenzione."""
        logger.info("Esecuzione attività di manutenzione...")
        self.working_memory.clear_contents()
        logger.info("Memoria operativa pulita.")
