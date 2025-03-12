import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)  # Per mostrare i log a livello DEBUG

class DecisionMaker:
    def __init__(self, working_memory, long_term_memory):
        self.working_memory = working_memory
        self.long_term_memory = long_term_memory

    def make_decision(self):
        """Prende una decisione basata su input e stato interno."""
        if not hasattr(self.working_memory, 'get_contents'):
            logger.error("L'oggetto working_memory non ha il metodo get_contents().")
            return None

        contents = self.working_memory.get_contents()
        logger.debug(f"Contenuti della memoria operativa: {contents}")

        if contents:
            decision = f"Decisione basata su {contents}"
            logger.info(f"Decisione presa: {decision}")
            return decision
        else:
            logger.warning("Nessun contenuto nella memoria operativa per prendere una decisione.")
            return None
