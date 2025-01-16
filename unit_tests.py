"""
Unit tests for the auction model.
"""

import unittest
from model import model

class TestAuctionModel(unittest.TestCase):
    """Test cases for auction model."""

    def test_model_structure(self):
        """Test model structure."""
        self.assertEqual(len(model.layers), 3)  # Number of layers
        self.assertEqual(model.layers[0].units, 128)  # Number of neurons in the first layer
        self.assertEqual(model.layers[1].units, 64)  # Number of neurons in the second layer
        self.assertEqual(model.layers[2].units, 1)  # Number of neurons in the output layer

if __name__ == '__main__':
    unittest.main()
