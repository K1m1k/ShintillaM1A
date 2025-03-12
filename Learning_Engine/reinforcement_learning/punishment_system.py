class PunishmentSystem:
    def __init__(self):
        self.punishment_values = {}

    def apply_punishment(self, action):
        """Riduce il valore associato a un'azione per scoraggiarla."""
        if action not in self.punishment_values:
            self.punishment_values[action] = 0
        self.punishment_values[action] -= 1  # Penalizzazione dell'azione

    def get_punishment_value(self, action):
        """Restituisce il valore negativo associato a un'azione."""
        return self.punishment_values.get(action, 0)
