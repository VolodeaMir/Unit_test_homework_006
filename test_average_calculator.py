import pytest
# import pylint
# import coverage
from average_calculator import AverageCalculator


def test_compare_averages_first_greater():
    result = AverageCalculator.compare_averages([1, 2, 3], [1, 2, 2])
    assert result == "Первый список имеет большее среднее значение"

def test_compare_averages_second_greater():
    result = AverageCalculator.compare_averages([1, 2, 2], [1, 2, 3])
    assert result == "Второй список имеет большее среднее значение"

def test_compare_averages_equal():
    result = AverageCalculator.compare_averages([1, 2, 3], [3, 2, 1])
    assert result == "Средние значения равны"

def test_compare_averages_empty_lists():
    result = AverageCalculator.compare_averages([], [])
    assert result == "Средние значения равны"

def test_compare_averages_one_empty_list():
    result = AverageCalculator.compare_averages([], [1, 2, 3])
    assert result == "Второй список имеет большее среднее значение"



