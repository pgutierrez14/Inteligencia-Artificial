import numpy as np

"""
Land Class: Represents a land with environmental conditions that vary daily.
"""
class Land:
    def __init__(self, id):
        self.id = id
        self.ph = np.random.uniform(5.5, 8.5)
        self.sun_hours = np.random.uniform(5, 12)
        self.humidity = np.random.uniform(10, 90)
        self.mineral_richness = np.random.uniform(0, 100)

    def update_conditions(self):
        """
        Updates the environmental conditions daily.
        """
        self.ph = np.random.uniform(5.5, 8.5)
        self.sun_hours = np.random.uniform(5, 12)
        self.humidity = np.random.uniform(10, 90)
        self.mineral_richness = np.random.uniform(0, 100)