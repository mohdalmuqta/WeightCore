# test_weightcorepro.py
"""
Tests for WeightCorePro module.
"""

import unittest
from weightcorepro import WeightCorePro

class TestWeightCorePro(unittest.TestCase):
    """Test cases for WeightCorePro class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = WeightCorePro()
        self.assertIsInstance(instance, WeightCorePro)
        
    def test_run_method(self):
        """Test the run method."""
        instance = WeightCorePro()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
