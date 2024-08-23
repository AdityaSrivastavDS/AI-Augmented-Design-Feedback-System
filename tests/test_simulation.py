import unittest
from src.simulation import simulate_design

class TestSimulation(unittest.TestCase):
    def test_simulate_design(self):
        design = {
            "parameters": {
                "material": "steel",
                "dimensions": {"length": 10, "width": 5, "height": 2},
                "load": 1000
            }
        }
        results = simulate_design(design)
        self.assertIn("stress_analysis", results)
        self.assertIn("load_distribution", results)
        self.assertIn("thermal_analysis", results)
        self.assertEqual(results["stress_analysis"], "Pass")
        self.assertEqual(results["load_distribution"], "Optimal")
        self.assertEqual(results["thermal_analysis"], "Needs Improvement")

if __name__ == '__main__':
    unittest.main()
