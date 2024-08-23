import unittest
from src.design_feedback import DesignFeedbackSystem

class TestDesignFeedbackSystem(unittest.TestCase):
    def test_analyze_design(self):
        system = DesignFeedbackSystem()
        feedback = system.analyze_design('data/sample_designs/design1.json')
        self.assertIn('performance', feedback)
        self.assertIn('safety', feedback)
        self.assertIn('efficiency', feedback)
        self.assertIn('simulation_results', feedback)

if __name__ == '__main__':
    unittest.main()
