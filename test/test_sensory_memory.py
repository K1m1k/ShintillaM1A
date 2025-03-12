import unittest
import logging
from Core_Cognition.Memory_System.sensory_memory import SensoryMemory

class TestSensoryMemory(unittest.TestCase):
    def setUp(self):
        self.sensory_memory = SensoryMemory()

    def test_add_valid_input(self):
        self.sensory_memory.add_sensory_input("Vedo un albero")
        self.assertEqual(self.sensory_memory.get_buffer(), ["Vedo un albero"])

    def test_add_multiple_inputs(self):
        inputs = ["Vedo un albero", "Sento un suono", "Percepisco calore"]
        for data in inputs:
            self.sensory_memory.add_sensory_input(data)
        self.assertEqual(self.sensory_memory.get_buffer(), inputs)

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            self.sensory_memory.add_sensory_input(123)  # Non una stringa

    def test_clear_buffer(self):
        self.sensory_memory.add_sensory_input("Vedo un albero")
        self.sensory_memory.clear_buffer()
        self.assertEqual(self.sensory_memory.get_buffer(), [])

    def test_logging_on_add(self):
        with self.assertLogs('Core_Cognition.Memory_System.sensory_memory', level='INFO') as log:
            self.sensory_memory.add_sensory_input("Vedo un albero")
            self.assertIn("Input sensoriale aggiunto: Vedo un albero", log.output[0])

if __name__ == '__main__':
    unittest.main()
