import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget, QTextEdit
from Core_Cognition.Memory_System.sensory_memory import SensoryMemory
from Core_Cognition.Memory_System.working_memory import WorkingMemory
from Core_Cognition.Memory_System.long_term_memory import LongTermMemory
from Core_Cognition.Cognitive_Processes.decision_core import DecisionMaker

class UserInterface(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.init_memory_system()
        self.init_cognition_system()

    def init_ui(self):
        self.setWindowTitle("SHintilla - AI Interface")
        self.setGeometry(100, 100, 600, 400)

        # Layout principale
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout()

        # Titolo
        self.label = QLabel("Sistema Cognitivo Attivo", self)
        layout.addWidget(self.label)

        # Log output
        self.log_output = QTextEdit(self)
        self.log_output.setReadOnly(True)
        layout.addWidget(self.log_output)

        # Pulsanti di controllo
        self.start_button = QPushButton("Avvia Processo Cognitivo", self)
        self.start_button.clicked.connect(self.start_cognition)
        layout.addWidget(self.start_button)

        self.memory_status_button = QPushButton("Stato della Memoria", self)
        self.memory_status_button.clicked.connect(self.show_memory_status)
        layout.addWidget(self.memory_status_button)

        central_widget.setLayout(layout)

    def init_memory_system(self):
        """Inizializza le componenti della memoria"""
        self.sensory_memory = SensoryMemory()
        self.working_memory = WorkingMemory()
        self.long_term_memory = LongTermMemory()

    def init_cognition_system(self):
        """Inizializza i processi cognitivi"""
        self.decision_core = DecisionMaker()

    def start_cognition(self):
        """Simula un processo cognitivo e mostra i log"""
        self.log_output.append("Avvio processo decisionale...")
        decision = self.decision_core.make_decision("Esempio di input")
        self.log_output.append(f" Decisione presa: {decision}")

    def show_memory_status(self):
        """Mostra lo stato attuale delle memorie"""
        self.log_output.append("Stato della Memoria:")
        self.log_output.append(f"Sensory Memory: {self.sensory_memory.get_data()}")
        self.log_output.append(f"Working Memory: {self.working_memory.get_contents()}")
        self.log_output.append(f"Long-Term Memory: {self.long_term_memory.retrieve_data()}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = UserInterface()
    main_window.show()
    sys.exit(app.exec_())
