class RewardSystem:
    def __init__(self):
        self.reward_values = {}

    def apply_reward(self, action):
        """Aumenta il valore associato a un'azione per incentivarla."""
        if action not in self.reward_values:
            self.reward_values[action] = 0
        self.reward_values[action] += 1  # Ricompensa l'azione

    def get_reward_value(self, action):
        """Restituisce il valore positivo associato a un'azione."""
        return self.reward_values.get(action, 0)
