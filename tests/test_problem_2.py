import pytest
import logging
from src.main import problem_2

logging.basicConfig(level=logging.INFO)
mylogger = logging.getLogger()


def test_2_a():
    problem = problem_2('inputs/input2.txt')
    result = problem.solve()
    mylogger.info(len(result))


def test_2_b():
    problem = problem_2('inputs/input2.txt', False)
    result = problem.solve()
    mylogger.info(len(result))


def test_2_missing_file():
    with pytest.raises(Exception) as exception:
        problem_2('inputs/aaaa.txt').solve()

    assert str(exception.value) == "file does not exist"


def test_2_file_type():
    with pytest.raises(Exception) as exception:
        problem_2('inputs/input1.json').solve()

    assert str(exception.value) == "invalid file type"
