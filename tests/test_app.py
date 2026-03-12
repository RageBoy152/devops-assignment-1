import pytest
from app import (
    main_conversion_function,
)

# Example cases for conversion functions
def test_kg_to_grams():
    # test that 1 kg is equal to 1000 grams
    # if this test fails, the function kg_to_grams is incorrect
    assert main_conversion_function(1, 'kg', 'grams') == 1000

def test_grams_to_kg():
    # test that 1000 grams is equal to 1 kg
    # if this test fails, the function grams_to_kg is incorrect
    assert main_conversion_function(1000, 'grams', 'kg') == 1

def test_kg_to_pounds():
    # test that 1 kg is equal to 2.20462 pounds
    # if this test fails, the function kg_to_pounds is incorrect
    assert pytest.approx(main_conversion_function(1, 'kg', 'pounds'), rel=0.01) == 2.20462

def test_pounds_to_kg():
    # test that 2.20462 pounds is equal to 1 kg
    # if this test fails, the function pounds_to_kg is incorrect
    assert pytest.approx(main_conversion_function(2.20462, 'pounds', 'kg'), rel=1e-5) == 1

def test_grams_to_pounds():
    # test that 1000 grams is equal to 2.20462 pounds
    # if this test fails, the function grams_to_pounds is incorrect
    assert pytest.approx(main_conversion_function(1000, 'grams', 'pounds'), rel=1e-5) == 2.20462

