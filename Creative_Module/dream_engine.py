import random
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)

class DreamEngine:
    def __init__(self, long_term_memory, max_memories=3, max_random_elements=2):
        self.long_term_memory = long_term_memory
        self.max_memories = max_memories
        self.max_random_elements = max_random_elements

    def generate_dream(self):
        """Genera un sogno combinando ricordi e elementi casuali."""
        memories = self.long_term_memory.get_storage()

        if not memories:
            logger.warning("Memoria a lungo termine vuota. Generazione di un sogno casuale.")
            dream_elements = self._random_imagery(5)  # Use more random elements
            dream = " - ".join(dream_elements)
            logger.info(f"Sogno generato: {dream}")
            return dream

        selected_memories = random.sample(list(memories.values()), min(self.max_memories, len(memories)))
        dream_elements = list(set(selected_memories + self._random_imagery(self.max_random_elements)))

        dream = " - ".join(dream_elements)
        logger.info(f"Memorie selezionate per il sogno: {selected_memories}")
        logger.info(f"Elementi casuali aggiunti: {self._random_imagery(self.max_random_elements)}")
        logger.info(f"Sogno generato: {dream}")
        return dream

    def _random_imagery(self, count=2):
        """Genera elementi casuali per arricchire il sogno."""
        random_elements = [
            "un cielo viola", "un labirinto infinito", "una foresta incantata",
            "un fiume che scorre al contrario", "un uccello parlante"
        ]
        return random.sample(random_elements, min(count, len(random_elements)))