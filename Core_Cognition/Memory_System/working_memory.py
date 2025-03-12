import logging

logger = logging.getLogger(__name__)

class WorkingMemory:
    def __init__(self, capacity=7):
        self.capacity = capacity
        self.contents = []

    def add_item(self, item):
        """Aggiunge un elemento alla memoria operativa."""
        if not isinstance(item, str):  # Controllo tipo input
            raise ValueError("L'elemento deve essere una stringa.")
        if len(self.contents) >= self.capacity:
            logger.warning("Memoria operativa piena. Non posso aggiungere ulteriori elementi.")
            return False
        self.contents.append(item)
        logger.info(f"Elemento aggiunto alla memoria operativa: {item}")
        return True

    def remove_item(self, item):
        """Rimuove un elemento dalla memoria operativa."""
        if item in self.contents:
            self.contents.remove(item)
            logger.info(f"Elemento rimosso dalla memoria operativa: {item}")
            return True
        logger.warning(f"Elemento non trovato nella memoria operativa: {item}")
        return False

    def get_contents(self):
        """Restituisce il contenuto della memoria operativa."""
        return self.contents

    def clear_contents(self):
        """Pulisce il contenuto della memoria operativa."""
        self.contents.clear()
        logger.info("Contenuto della memoria operativa pulito.")
