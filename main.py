import logging
import threading
import random
import time
import wikipedia

# Importazioni dei moduli interni
from Core_Cognition.Memory_System.sensory_memory import SensoryMemory
from Core_Cognition.Memory_System.working_memory import WorkingMemory
from Core_Cognition.Memory_System.long_term_memory import LongTermMemory
from Core_Cognition.Memory_System.subconscious_core import SubconsciousLoop

from Core_Cognition.Cognitive_Processes.decision_core import DecisionMaker
from Core_Cognition.Cognitive_Processes.reasoning_engine import ReasoningEngine
from Core_Cognition.Cognitive_Processes.meta_cognition_core import MetaCognition

from Core_Cognition.Emotional_Engine.emotion_simulator_core import EmotionSimulator
from Core_Cognition.Emotional_Engine.mood_tracker_core import MoodTracker

from Learning_Engine.reinforcement_learning_core import ReinforcementLearning
from Learning_Engine.pattern_recognition_core import PatternRecognition

# Configurazione del logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Funzione per cercare informazioni su Wikipedia
def search_wikipedia(query):
    try:
        summary = wikipedia.summary(query, sentences=2)
        logging.info(f"Ricerca Wikipedia per '{query}': {summary}")
        return summary
    except wikipedia.exceptions.PageError:
        logging.error(f"Nessuna pagina trovata per la query: {query}")
        return None
    except wikipedia.exceptions.DisambiguationError as e:
        logging.warning(f"Ambiguità nella query '{query}': {e.options}")
        return None
    except Exception as e:
        logging.error(f"Errore nella ricerca Wikipedia: {e}")
        return None

# Funzione per aggiornare la memoria con ricerche online
def dynamic_online_search(sensory_memory, working_memory, long_term_memory, query):
    wiki_info = search_wikipedia(query)

    if wiki_info:
        sensory_memory.add_sensory_input(wiki_info)
        working_memory.add_item(wiki_info)
        long_term_memory.store_information(query, wiki_info)
        logging.info(f"Memoria aggiornata con risultati Wikipedia per: {query}")
    else:
        logging.warning(f"Nessuna informazione valida trovata per la query: {query}")

    logging.info(f"Contenuti della memoria operativa: {working_memory.get_contents()}")

# Avvia ricerca automatica periodica
def start_online_search(sensory_memory, working_memory, long_term_memory, stop_event):
    def search_loop():
        queries = {
            "Artificial Intelligence": [
                "Applications of AI in Robotics",
                "Ethical Challenges of AI",
                "Future of AI in Education"
            ],
            "Latest Technological News": [
                "Top Emerging Technologies 2023",
                "AI and Automation Trends",
                "Quantum Computing Breakthroughs"
            ],
            "Scientific Discoveries": [
                "Recent Advances in Space Exploration",
                "Breakthroughs in Genetic Engineering",
                "New Discoveries in Neuroscience"
            ],
            "Philosophy": [
                "Philosophy of Consciousness",
                "Ethics in Modern Technology",
                "Existentialism in the Digital Age"
            ],
            "Modern Art": [
                "Digital Art Movements",
                "Impact of AI on Art Creation",
                "Postmodernism in Contemporary Art"
            ]
        }

        while not stop_event.is_set():
            main_query = random.choice(list(queries.keys()))
            sub_queries = queries[main_query]
            query = random.choice([main_query] + sub_queries)  # Sceglie tra la query principale o una delle sue sottocategorie
            dynamic_online_search(sensory_memory, working_memory, long_term_memory, query)
            time.sleep(30)

    search_thread = threading.Thread(target=search_loop)
    search_thread.daemon = True
    search_thread.start()
    logging.info("Ricerca web automatica avviata.")

# Funzione per simulare immissione sensoriali
def simulate_sensory_inputs(sensory_memory, working_memory, long_term_memory):
    """Simula immissione sensoriali variabili e li trasferisce alle memorie."""
    visual_inputs = ["Vedo un gatto", "Vedo un cane che corre", "Vedo una macchina rossa"]
    auditory_inputs = ["Sento un rumore", "Sento il rumore della pioggia", "Sento una sirena"]
    tactile_inputs = ["Sento qualcosa di ruvido", "Sento una superficie liscia"]
    olfactory_inputs = ["Sento odore di fumo", "Sento odore di caffè"]
    gustatory_inputs = ["Sento il sapore dolce di una mela", "Sento il sapore amaro del caffè"]

    all_inputs = [
        random.choice(visual_inputs),
        random.choice(auditory_inputs),
        random.choice(tactile_inputs),
        random.choice(olfactory_inputs),
        random.choice(gustatory_inputs)
    ]

    for input_data in all_inputs:
        sensory_memory.add_sensory_input(input_data)
        if hasattr(working_memory, 'add_item'):
            working_memory.add_item(input_data)
            long_term_memory.store_information("Input sensoriale", input_data)
        else:
            logging.error("La memoria operativa non ha il metodo 'add_item'.")

    logging.info("Input sensoriali variabili simulati e trasferiti alla memoria operativa.")
    logging.info(f"Contenuti della memoria operativa: {working_memory.get_contents()}")

# Classe per la generazione dei sogni
class DreamEngine:
    def __init__(self, long_term_memory):
        self.long_term_memory = long_term_memory

    def generate_dream(self):
        """Genera un sogno combinando ricordi e elementi casuali."""
        memories = self.long_term_memory.get_storage()

        if not memories:
            logging.warning("Memoria a lungo termine vuota. Generazione di un sogno casuale.")
            return self._generate_random_dream()

        selected_memories = random.sample(list(memories.values()), min(3, len(memories)))
        dream_elements = selected_memories + self._random_imagery()

        dream = " - ".join(dream_elements)
        logging.info(f"Sogno generato: {dream}")
        return dream

    def _random_imagery(self):
        """Genera elementi casuali per arricchire il sogno."""
        random_elements = [
            "un cielo viola", "un labirinto infinito", "una foresta incantata",
            "un fiume che scorre al contrario", "un uccello parlante"
        ]
        return random.sample(random_elements, 2)

    def _generate_random_dream(self):
        """Genera un sogno completamente casuale."""
        random_elements = [
            "un mondo sottomarino", "una città fluttuante", "un deserto stellato",
            "un castello abbandonato", "un viaggio interstellare"
        ]
        dream = " - ".join(random.sample(random_elements, 3))
        logging.info(f"Sogno casuale generato: {dream}")
        return dream

# Classe principale per la gestione del sistema cognitivo
class CognitiveSystem:
    def __init__(self, working_memory, long_term_memory):
        self.decision_maker = DecisionMaker(working_memory, long_term_memory)
        self.reasoning_engine = ReasoningEngine(working_memory, long_term_memory)
        self.meta_cognition = MetaCognition(working_memory, long_term_memory)
        self.emotion_simulator = EmotionSimulator(working_memory, long_term_memory)
        self.mood_tracker = MoodTracker(working_memory, long_term_memory)
        self.reinforcement_learning = ReinforcementLearning(working_memory, long_term_memory)
        self.pattern_recognition = PatternRecognition(working_memory, long_term_memory)
        self.dream_engine = DreamEngine(long_term_memory)  # Aggiunto il motore dei sogni

    def process_thoughts(self):
        decision = self.decision_maker.make_decision()
        reasoning = self.reasoning_engine.reason()
        reflection = self.meta_cognition.self_reflection()
        emotion = self.emotion_simulator.simulate_emotion()
        mood = self.mood_tracker.track_mood()
        reward = self.reinforcement_learning.reward_system()
        pattern = self.pattern_recognition.feature_extraction()

        combined_thought = {
            "decision": decision,
            "reasoning": reasoning,
            "reflection": reflection,
            "emotion": emotion,
            "mood": mood,
            "reward": reward,
            "pattern": pattern
        }
        return combined_thought

# Funzione principale
def main():
    try:
        # Inizializza il sistema di memoria
        sensory_memory = SensoryMemory()
        working_memory = WorkingMemory()
        long_term_memory = LongTermMemory()

        # Popola la memoria a lungo termine con dati iniziali
        initial_queries = [
            "Artificial Intelligence",
            "Latest Technological News",
            "Scientific Discoveries",
            "Philosophy",
            "Modern Art"
        ]
        for query in initial_queries:
            wiki_info = search_wikipedia(query)
            if wiki_info:
                long_term_memory.store_information(query, wiki_info)
                logging.info(f"Memoria a lungo termine aggiornata con: {query}")
            else:
                logging.warning(f"Nessuna informazione valida trovata per la query: {query}")

        # Inizializza il sistema cognitivo
        cognitive_system = CognitiveSystem(working_memory, long_term_memory)

        # Inizializza il ciclo subconscio
        subconscious_loop = SubconsciousLoop(sensory_memory, working_memory, long_term_memory)

        def run_subconscious():
            try:
                subconscious_loop.run_background_tasks()
            except Exception as exc:
                logging.error(f"Errore nel ciclo subconscio: {exc}")

        subconscious_thread = threading.Thread(target=run_subconscious)
        subconscious_thread.daemon = True
        subconscious_thread.start()
        logging.info("Ciclo subconscio avviato.")

        # Avvia la ricerca web automatica
        stop_event = threading.Event()
        start_online_search(sensory_memory, working_memory, long_term_memory, stop_event)

        # Simula input sensoriali
        simulate_sensory_inputs(sensory_memory, working_memory, long_term_memory)

        # Elabora i pensieri
        combined_thought = cognitive_system.process_thoughts()
        logging.info(f"Pensiero combinato: {combined_thought}")

        # Simula un sogno
        dream = cognitive_system.dream_engine.generate_dream()
        logging.info(f"Sogno simulato: {dream}")

    except Exception as e:
        logging.error(f"Errore nel main: {e}")

if __name__ == "__main__":
    main()