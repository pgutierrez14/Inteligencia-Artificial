import simpy
import pandas as pd
from Clases.Land import Land
from Clases.Crop import Crop
from Clases.FuzzyEvaluator import FuzzyEvaluator
from Clases.Simulator import Simulator
from Clases.PSOOptimizer import PSOOptimizer

class SimulationController:
    def __init__(self, lands, crops, evaluator):
        self.lands = lands
        self.crops = crops
        self.evaluator = evaluator
        self.env = simpy.Environment()

    def run_simulation(self):
        """
        Executes the simulation process for 365 days and stores results in a CSV file.
        """
        simulator = Simulator(self.env, self.lands, self.crops, self.evaluator)
        print("Starting Simulation...")
        self.env.process(simulator.simulate_year())
        self.env.run()
        print("Simulation completed.\n")

        # Save results
        df = pd.DataFrame(simulator.results)
        df.to_csv("simulation_results.csv", index=False)
        print("Simulation results saved to simulation_results.csv")

    def run_optimization(self):
        """
        Executes the optimization process for each land and crop and searchs for an optimal combination.
        """
        all_results = []
        for land in self.lands:
            min_bounds, max_bounds= self.bound_determinator(land.id)
            for crop in self.crops:
                optimizer = PSOOptimizer(self.evaluator, crop, land.id, min_bounds, max_bounds)
                best_conditions = optimizer.optimize()
                all_results.append({
                    "Land": land.id,
                    "Crop": crop.name,
                    "Optimal Conditions": best_conditions
                })

        # Save optimization results
        df = pd.DataFrame(all_results)
        df.to_csv("optimization_results.csv", index=False)
        print("Optimization results saved to optimization_results.csv")


    def bound_determinator(self, land_id):
        """
        Reads minimum and maximum values of condiitons from the previous file simulation_results.csv.
        """
        #Uploads previos csv file
        data = pd.read_csv("simulation_results.csv")

        #Filters for the land_id passed by param
        land_data = data[data['land'] == land_id]

        # Checks data in file
        if land_data.empty:
            print(f"No hay datos para el land_id {land_id}")
            return None, None

        # Gets minimum and maximum values for each condition
        min_values = land_data[['ph', 'sun', 'humidity', 'richness']].min().values
        max_values = land_data[['ph', 'sun', 'humidity', 'richness']].max().values

        return min_values, max_values