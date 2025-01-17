"""
Unit tests
"""
import unittest
import os
import tempfile
from src.utils import ensure_directory_exists


class TestEnsureDirectoryExists(unittest.TestCase):
    def test_directory_already_exists(self):
        """
        Test that the function does nothing if the directory already exists.
        """
        with tempfile.TemporaryDirectory() as temp_dir:
            # Ensure the directory exists before calling the function
            self.assertTrue(os.path.exists(temp_dir))

            # Call the function and verify the directory still exists
            ensure_directory_exists(temp_dir)
            self.assertTrue(os.path.exists(temp_dir))

    def test_directory_does_not_exist(self):
        """
        Test that the function creates the directory if it does not exist.
        """
        with tempfile.TemporaryDirectory() as temp_dir:
            # Create a non-existing subdirectory path
            new_dir = os.path.join(temp_dir, "new_subdirectory")
            self.assertFalse(os.path.exists(new_dir))

            # Call the function and verify the directory is created
            ensure_directory_exists(new_dir)
            self.assertTrue(os.path.exists(new_dir))


if __name__ == "__main__":
    unittest.main()
