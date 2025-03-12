class GoalSetting:
    """Gestisce la definizione e il monitoraggio degli obiettivi."""
    def __init__(self):
        self.goals = []

    def add_goal(self, goal):
        """Aggiunge un nuovo obiettivo."""
        self.goals.append(goal)

    def list_goals(self):
        """Restituisce tutti gli obiettivi."""
        return self.goals