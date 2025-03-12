import logging

logger = logging.getLogger(__name__)

class MetaCognition:
    def __init__(self, working_memory, long_term_memory):
        self.working_memory = working_memory
        self.long_term_memory = long_term_memory

    def self_reflection(self):
        """Esegue riflessioni interne sulla propria performance."""
        contents = self.working_memory.get_contents()
        reflection = f"Riflessione sulla performance basata su {contents}"
        logger.info(f"Riflessione: {reflection}")
        return reflection

    def learning_evaluation(self):
        """Valuta continuamente il processo di apprendimento."""
        evaluation = "Valutazione del processo di apprendimento"
        logger.info(f"Valutazione: {evaluation}")
        return evaluation
