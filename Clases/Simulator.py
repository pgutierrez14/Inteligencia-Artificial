import simpy

"""
Simulator Class: Simulates the compatibility evaluation over a year using SimPy.
"""
class Simulator:
    def __init__(self, env, lands, crops, evaluator):
        self.env = env
        self.lands = lands
        self.crops = crops
        self.evaluator = evaluator
        self.results = []

    def simulate_year(self):
        """
        Simulate 365 days of compatibility evaluation.
        """
        for day in range(1, 366):
            for land in self.lands:
                land.update_conditions()
                for crop in self.crops:
                    compatibility = self.evaluator.evaluate(
                        land.ph, land.sun_hours, land.humidity, land.mineral_richness
                    )
                    self.results.append({
                        'day': day,
                        'land': land.id,
                        'crop': crop.name,
                        'ph': land.ph,
                        'sun': land.sun_hours,
                        'humidity': land.humidity,
                        'richness': land.mineral_richness,
                        'compatibility': compatibility
                    })
            yield self.env.timeout(1)