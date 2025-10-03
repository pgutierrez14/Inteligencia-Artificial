import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

"""
FuzzyEvaluator Class: Evaluates compatibility using fuzzy logic based on the conditions we choosed.
"""
class FuzzyEvaluator:
    def __init__(self):
        self.ph = ctrl.Antecedent(np.arange(5.5, 8.5, 0.1), 'ph')
        self.sun = ctrl.Antecedent(np.arange(5, 12, 0.1), 'sun')
        self.humidity = ctrl.Antecedent(np.arange(10, 90, 1), 'humidity')
        self.richness = ctrl.Antecedent(np.arange(0, 100, 1), 'richness')
        self.compatibility = ctrl.Consequent(np.arange(0, 101, 1), 'compatibility')

        # Membership Functions (We consider antecedents correctly trimmed by 3)
        #Compatibility needs to be trimmed manually because compatibility lower than 50 has to be low
        self.ph.automf(3)
        self.sun.automf(3)
        self.humidity.automf(3)
        self.richness.automf(3)
        self.compatibility['low'] = fuzz.trimf(self.compatibility.universe, [0, 0, 50])
        self.compatibility['medium'] = fuzz.trimf(self.compatibility.universe, [0, 50, 100])
        self.compatibility['high'] = fuzz.trimf(self.compatibility.universe, [50, 100, 100])

        # Fuzzy Rules
        self.rules = [
            ctrl.Rule(self.ph['good'] & self.sun['good'] & self.humidity['good'] & self.richness['good'], self.compatibility['high']),
            ctrl.Rule(self.ph['average'] | self.sun['average'] | self.humidity['average'] | self.richness['average'], self.compatibility['medium']),
            ctrl.Rule(self.ph['poor'] | self.sun['poor'] | self.humidity['poor'] | self.richness['poor'], self.compatibility['low'])
        ]
        self.system = ctrl.ControlSystem(self.rules)

    def evaluate(self, ph, sun, humidity, richness):
        """
        Sets the control system to evalutate compatibility.
        """
        simulation = ctrl.ControlSystemSimulation(self.system)
        simulation.input['ph'] = ph
        simulation.input['sun'] = sun
        simulation.input['humidity'] = humidity
        simulation.input['richness'] = richness
        simulation.compute()
        return simulation.output['compatibility']