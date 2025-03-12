import unittest
import logging
from Core_Cognition.Memory_System.working_memory import WorkingMemory
from Core_Cognition.Memory_System.long_term_memory import LongTermMemory
from Core_Cognition.Cognitive_Processes.decision_core import DecisionMaker
from Learning_Engine.reinforcement_learning_core import ReinforcementLearning
from Core_Cognition.Emotional_Engine.emotion_simulator_core import EmotionSimulator
from Creative_Module.dream_engine import DreamEngine


class TestWorkingMemory(unittest.TestCase):
    def setUp(self):
        self.memory = WorkingMemory()

    def test_add_valid_data(self):
        self.memory.add_item("dato1")
        self.assertEqual(self.memory.get_contents(), ["dato1"])

    def test_add_multiple_data(self):
        inputs = ["dato1", "dato2", "dato3"]
        for data in inputs:
            self.memory.add_item(data)
        self.assertEqual(self.memory.get_contents(), inputs)

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            self.memory.add_item(123)

    def test_clear_buffer(self):
        self.memory.add_item("dato1")
        self.memory.clear_contents()
        self.assertEqual(self.memory.get_contents(), [])

    def test_logging_on_add(self):
        with self.assertLogs('Core_Cognition.Memory_System.working_memory', level='INFO') as log:
            self.memory.add_item("dato1")
            self.assertIn("Elemento aggiunto alla memoria operativa: dato1", log.output[0])


class TestLongTermMemory(unittest.TestCase):
    def setUp(self):
        self.memory = LongTermMemory()

    def test_store_and_retrieve(self):
        self.memory.store_information("chiave", "valore")
        self.assertEqual(self.memory.retrieve_information("chiave"), "valore")

    def test_retrieve_nonexistent_key(self):
        self.assertIsNone(self.memory.retrieve_information("chiave_non_esistente"))

    def test_logging_on_store(self):
        with self.assertLogs('Core_Cognition.Memory_System.long_term_memory', level='INFO') as log:
            self.memory.store_information("chiave", "valore")
            self.assertIn("Informazioni archiviate con chiave 'chiave': valore", log.output[0])


class TestDecisionCore(unittest.TestCase):
    def setUp(self):
        self.working_memory = WorkingMemory()
        self.long_term_memory = LongTermMemory()
        self.decision_maker = DecisionMaker(self.working_memory, self.long_term_memory)

    def test_make_decision(self):
        # Assicurati che `make_decision()` accetti effettivamente una lista di opzioni.
        result = self.decision_maker.make_decision(["opzione1", "opzione2"])
        self.assertIn(result, ["opzione1", "opzione2"])


class TestReinforcementLearning(unittest.TestCase):
    def setUp(self):
        self.working_memory = WorkingMemory()
        self.long_term_memory = LongTermMemory()
        self.rl = ReinforcementLearning(self.working_memory, self.long_term_memory)

    def test_reward_increases_value(self):
        # Verifica se il metodo corretto esiste in `ReinforcementLearning`
        self.rl.apply_reward("azione")
        self.assertGreater(self.rl.get_value("azione"), 0)

    def test_punishment_decreases_value(self):
        # Verifica se il metodo corretto esiste in `ReinforcementLearning`
        self.rl.apply_punishment("azione")
        self.assertLess(self.rl.get_value("azione"), 0)


class TestEmotionSimulator(unittest.TestCase):
    def setUp(self):
        self.working_memory = WorkingMemory()
        self.long_term_memory = LongTermMemory()
        self.emotion = EmotionSimulator(self.working_memory, self.long_term_memory)

    def test_emotional_response(self):
        # Verifica il nome corretto del metodo in `EmotionSimulator`
        response = self.emotion.react("evento felice")
        self.assertIn(response, ["felice", "euforico"])


class TestDreamEngine(unittest.TestCase):
    def setUp(self):
        self.long_term_memory = LongTermMemory()
        self.dream = DreamEngine(self.long_term_memory)

    def test_generate_dream(self):
        # Verifica il metodo corretto in `DreamEngine`
        dream = self.dream.generate_dream()
        self.assertIsInstance(dream, str)
        self.assertGreater(len(dream), 0)

    def test_generate_dream_empty_memory(self):
        # Verifica il comportamento con memoria vuota
        empty_memory = LongTermMemory()
        dream_engine = DreamEngine(empty_memory)
        dream = dream_engine.generate_dream()
        self.assertEqual(dream, "Sogno vuoto... ")


if __name__ == '__main__':
    unittest.main()
