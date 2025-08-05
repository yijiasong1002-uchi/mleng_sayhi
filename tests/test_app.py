# Run the tests with: pytest tests/test_app.py
import sys
import os

# Add the parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import add_numbers  # pylint: disable=wrong-import-position


def test_add_numbers():
    """Test the add_numbers function."""
    assert add_numbers(1, 2) == 3
