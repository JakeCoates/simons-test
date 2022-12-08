import logging

import pytest
from src.main import problem_1

logging.basicConfig(level=logging.INFO)
mylogger = logging.getLogger()


def test_1_a():
    problem = problem_1('inputs/input1.txt', 2, 2020)
    result = problem.solve()
    mylogger.info(result)
    assert len(result) > 0


def test_1_b():
    problem = problem_1('inputs/input1.txt', 3, 2020)
    result = problem.solve()
    mylogger.info(result)
    assert len(result) > 0


def test_1_failure():
    problem = problem_1('inputs/input1.txt', 2, 103)
    result = problem.solve()
    mylogger.info(result)
    assert len(result) == 0


def test_1_higher_complexity():
    problem = problem_1('inputs/input1.txt', 4, 2020)
    result = problem.solve()
    mylogger.info(result)
    assert len(result) > 0


def test_1_missing_file():
    with pytest.raises(Exception) as exception:
        problem_1('inputs/aaaa.txt', 2, 2020).solve()

    assert str(exception.value) == "file does not exist"


def test_2_file_type():
    with pytest.raises(Exception) as exception:
        problem_1('inputs/input1.json', 2, 2020).solve()

    assert str(exception.value) == "invalid file type"
