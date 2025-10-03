import numpy as np
from pyswarms.single import GlobalBestPSO

class PSOOptimizer:
    def __init__(self, evaluator, crop, land_id, min_bounds, max_bounds):
        self.evaluator = evaluator
        self.crop = crop
        self.land_id = land_id
        self.min_bounds = min_bounds
        self.max_bounds = max_bounds

    def objective(self, params):
        """
        Defines objective function to be optimized with PSO.
        introduces parameters to evaluate
        Appends compatibilidad to results
        """
        results = []
        for p in params:
            compatibilidad = -self.evaluator.evaluate(p[0], p[1], p[2], p[3])
            results.append(compatibilidad)
        return np.array(results)

    def optimize(self):
        """
        Apply PSO to find the optimal conditions for maximum compatibility.
        """
        bounds = (self.min_bounds, self.max_bounds)
        options = {'c1': 0.5, 'c2': 0.3, 'w': 0.9}
        n_particles = 10 #particles that are going to look for an optimal solution
        dimensions = 4 #same number of parameters to analyze
        options = options
        bounds = bounds #upper and lower bounds determined
        optimizer = GlobalBestPSO(n_particles, dimensions, options=options, bounds=bounds)
        best_cost, best_pos = optimizer.optimize(self.objective, iters=50)
        return best_pos, -best_cost
