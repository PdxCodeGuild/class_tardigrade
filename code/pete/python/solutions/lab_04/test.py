import pytest
# import pytest_repeat
from num_to_phrase import translator
from num2words import num2words


i = -1

@pytest.mark.repeat(1000)
def test():
    global i
    i += 1
    assert translator(i) == num2words(i).replace(' and ', ' ')

