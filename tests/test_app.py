# Run the tests with: pytest tests/test_app.py
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import add_numbers

def test_add_numbers():
    assert 3 == add_numbers(1, 2)
