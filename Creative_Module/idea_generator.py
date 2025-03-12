import random
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)

class IdeaGenerator:
    def __init__(self, long_term_memory):
        self.long_term_memory = long_term_memory

    def generate_idea(self, topic=None):
        """Genera un'idea creativa basata su un argomento o elementi casuali."""
        memories = self.long_term_memory.get_storage()

        if not memories:
            logger.warning("Memoria a lungo termine vuota. Nessuna idea generata.")
            return "Nessuna idea disponibile 🤔"

        if topic:
            relevant_memories = [v for k, v in memories.items() if topic.lower() in k.lower()]
            if not relevant_memories:
                logger.info(f"Nessun ricordo trovato per il tema '{topic}'.")
                relevant_memories = list(memories.values())
        else:
            relevant_memories = list(memories.values())

        selected = random.sample(relevant_memories, min(2, len(relevant_memories)))
        twist = self._random_twist()

        idea = f"Combina {selected[0]} con {selected[1]} in un contesto {twist}."
        logger.info(f"Idea generata: {idea}")
        return idea

    def _random_twist(self):
        """Aggiunge un tocco creativo all'idea."""
        twists = [
            "futuristico", "distopico", "magico", "minimalista", "post-apocalittico",
            "iper-realistico", "astratto", "comico", "surreale"
        ]
        return random.choice(twists)
