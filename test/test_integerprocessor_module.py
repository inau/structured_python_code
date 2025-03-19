import pytest

import sys
import os

# Add the 'modules' directory to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'modules')))

from myinteger import myint

class TestMyIntegerProcessor:
    
    @pytest.mark.parametrize("ctor_value, input_value, expected_result", [
        (5, 5, 10),    #  ok, 5 +5 = 10
        (5, -5, 0),    #  ok, 5 + -5 = 0
        (2, 5, -3),    # !ok, 2 + 5 = -3
    ])
    def test_get_modified_constant(self, ctor_value, input_value, expected_result):
        processor = myint.IntegerWrapper(ctor_value)
        assert processor.get_modified_value(input_value) == expected_result