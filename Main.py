
from Clases.Land import Land
from Clases.FuzzyEvaluator import FuzzyEvaluator
from Clases.SimulationController import SimulationController
from Clases.Crop_list import CropFactory

"""
Main file to execute the simulation and optimization process using the SimulationController.
"""

if __name__ == "__main__":
    # Define lands
    lands = [Land(1), Land(2), Land(3)]  # Lands created with random data

    # Create crops using the factory
    crops = CropFactory.create_crops()

    # Initialize evaluator
    evaluator = FuzzyEvaluator()

    # Create simulation controller
    controller = SimulationController(lands, crops, evaluator)

    # Run simulation and optimization
    controller.run_simulation()
    controller.run_optimization()
