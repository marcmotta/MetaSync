# test_metasync.py
"""
Tests for MetaSync module.
"""

import unittest
from metasync import MetaSync

class TestMetaSync(unittest.TestCase):
    """Test cases for MetaSync class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = MetaSync()
        self.assertIsInstance(instance, MetaSync)
        
    def test_run_method(self):
        """Test the run method."""
        instance = MetaSync()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
