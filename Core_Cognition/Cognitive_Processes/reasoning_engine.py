import logging

logger = logging.getLogger(__name__)

class ReasoningEngine:
    def __init__(self, working_memory, long_term_memory):
        self.working_memory = working_memory
        self.long_term_memory = long_term_memory

    def reason(self):
        """Esegue ragionamento logico-analitico."""
        contents = self.working_memory.get_contents()
        if contents:
            reasoning_result = f"Risultato del ragionamento basato su {contents}"
            logger.info(f"Risultato del ragionamento: {reasoning_result}")
            return reasoning_result
        else:
            logger.warning("Nessun contenuto nella memoria operativa per eseguire il ragionamento.")
            return None
            
