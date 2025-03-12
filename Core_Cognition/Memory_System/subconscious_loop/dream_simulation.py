import logging
import random

logger = logging.getLogger(__name__)

class DreamSimulation:
    def __init__(self, long_term_memory):
        self.long_term_memory = long_term_memory

    def generate_dream(self):
        """Genera un sogno combinando ricordi casuali dalla memoria a lungo termine."""
        all_memories = self.long_term_memory.get_all_memories()
        
        if len(all_memories) < 3:
            logger.warning("Memoria a lungo termine insufficiente per generare un sogno significativo.")
            return "Sogno confuso e frammentato."
        
        dream_elements = random.sample(all_memories, min(5, len(all_memories)))
        dream = "...".join(dream_elements)  # Unisce i ricordi in una narrazione
        
        logger.info(f"Sogno generato: {dream}")
        return dream

    def simulate_dream(self):
        """Simula un sogno e lo memorizza nella memoria a lungo termine."""
        dream = self.generate_dream()
        self.long_term_memory.store_information("ultimo_sogno", dream)
        return dream

