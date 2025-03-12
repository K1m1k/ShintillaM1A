
import sqlite3
import logging

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)  # Abilita il logging DEBUG

class LongTermMemory:
    def __init__(self, db_path='long_term_memory.db'):
        self.db_path = db_path
        self._initialize_db()

    def _initialize_db(self):
        """Inizializza il database se non esiste già."""
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    CREATE TABLE IF NOT EXISTS memory (
                        key TEXT PRIMARY KEY,
                        value TEXT
                    )
                ''')
                conn.commit()
            logger.info("Database della memoria a lungo termine inizializzato.")
        except sqlite3.Error as e:
            logger.error(f"Errore durante l'inizializzazione del database: {e}")

    def store_information(self, key, data):
        """Archivia informazioni nella memoria a lungo termine."""
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    INSERT OR REPLACE INTO memory (key, value) VALUES (?, ?)
                ''', (key, data))
                conn.commit()
            logger.info(f"Informazioni archiviate con chiave '{key}': {data}")
        except sqlite3.Error as e:
            logger.error(f"Errore durante l'archiviazione: {e}")

    def retrieve_information(self, key):
        """Recupera informazioni dalla memoria a lungo termine."""
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    SELECT value FROM memory WHERE key = ?
                ''', (key,))
                result = cursor.fetchone()
                if result:
                    logger.info(f"Informazioni recuperate con chiave '{key}': {result[0]}")
                    return result[0]
                else:
                    logger.warning(f"Nessuna informazione trovata con chiave '{key}'.")
                    return None
        except sqlite3.Error as e:
            logger.error(f"Errore durante il recupero: {e}")
            return None

    def delete_information(self, key):
        """Elimina informazioni dalla memoria a lungo termine."""
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute('''
                    DELETE FROM memory WHERE key = ?
                ''', (key,))
                conn.commit()
            logger.info(f"Informazioni con chiave '{key}' rimosse dalla memoria.")
        except sqlite3.Error as e:
            logger.error(f"Errore durante l'eliminazione: {e}")

    def get_storage(self):
        """Restituisce tutto il contenuto della memoria come dizionario."""
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute('SELECT key, value FROM memory')
                storage = cursor.fetchall()
                storage_dict = dict(storage) if storage else {}  # Se vuoto, restituisce {}
                logger.debug(f"Contenuto attuale della memoria a lungo termine: {storage_dict}")
                return storage_dict
        except sqlite3.Error as e:
            logger.error(f"Errore durante la lettura della memoria: {e}")
            return {}

    def load_long_term_to_working_memory(self, working_memory):
        """Carica i dati dal DB nella memoria operativa."""
        stored_data = self.get_storage()
        for key, value in stored_data.items():
            working_memory.add_item(f"{key}: {value}")
            logger.info(f"Caricato in memoria operativa: {key} → {value}")
