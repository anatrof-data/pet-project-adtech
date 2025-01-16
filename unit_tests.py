"""
Unit tests for the auction model.
"""

import unittest
from model import model


class TestAuctionModel(unittest.TestCase):
    """Test cases for auction model."""

    def test_model_structure(self):
        """Test model structure."""
        self.assertEqual(len(model.layers), 3)
        self.assertEqual(model.layers[0].units, 128)
        self.assertEqual(model.layers[1].units, 64)
        self.assertEqual(model.layers[2].units, 1)


if __name__ == '__main__':
    unittest.main()
