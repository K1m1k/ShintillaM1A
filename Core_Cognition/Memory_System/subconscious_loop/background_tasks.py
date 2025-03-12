import unittest
from unittest.mock import patch
from Core_Cognition.Memory_System.subconscious_loop.background_tasks import TestBackgroundTasks
from Core_Cognition.Memory_System.sensory_memory import SensoryMemory
from Core_Cognition.Memory_System.working_memory import WorkingMemory
from Core_Cognition.Memory_System.long_term_memory import LongTermMemory


class TestBackgroundTasks(unittest.TestCase):

    def setUp(self):
        """Inizializza le memorie e l'istanza di BackgroundTasks prima di ogni test."""
        self.sensory_memory = SensoryMemory()
        self.working_memory = WorkingMemory()
        self.long_term_memory = LongTermMemory()
        self.background_tasks = TestBackgroundTasks(self.sensory_memory, self.working_memory, self.long_term_memory)

    def test_run_tasks(self):
        """Testa il metodo `run_tasks` per verificare che tutti i task vengano eseguiti."""
        with patch.object(self.background_tasks, 'process_sensory_data') as mock_process, \
             patch.object(self.background_tasks, 'perform_housekeeping') as mock_housekeeping, \
             patch.object(self.background_tasks, 'transfer_to_long_term_memory') as mock_transfer:
            self.background_tasks.run_tasks()
            mock_process.assert_called_once()
            mock_housekeeping.assert_called_once()
            mock_transfer.assert_called_once()

    def test_process_sensory_data(self):
        """Testa il metodo `process_sensory_data` per verificare che i dati sensoriali vengano elaborati correttamente."""
        self.sensory_memory.add_sensory_input("Vedo un gatto")
        with patch.object(self.working_memory, 'add_item', return_value=True) as mock_add_item:
            self.background_tasks.process_sensory_data()
            mock_add_item.assert_called_once_with("Vedo un gatto")

    def test_process_sensory_data_with_filter(self):
        """Testa il filtro dei dati irrilevanti nel metodo `process_sensory_data`."""
        self.sensory_memory.add_sensory_input("Informazione irrilevante")
        with patch.object(self.working_memory, 'add_item', return_value=False) as mock_add_item:
            self.background_tasks.process_sensory_data()
            mock_add_item.assert_not_called()

    def test_perform_housekeeping(self):
        """Testa il metodo `perform_housekeeping` per verificare che la memoria operativa venga pulita."""
        self.working_memory.add_item("Elemento 1")
        with patch.object(self.working_memory, 'clear_contents') as mock_clear_contents:
            self.background_tasks.perform_housekeeping()
            mock_clear_contents.assert_called_once()

    def test_transfer_to_long_term_memory(self):
        """Testa il metodo `transfer_to_long_term_memory` per verificare il trasferimento dei dati."""
        self.working_memory.add_item("Dati importanti")
        with patch.object(self.long_term_memory, 'store') as mock_store:
            self.background_tasks.transfer_to_long_term_memory()
            mock_store.assert_called_once_with("Dati importanti")


if __name__ == '__main__':
    unittest.main()