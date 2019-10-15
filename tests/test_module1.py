import pytest

from src import main
from .utils import get_assignments, get_calls, get_for_loops


def test_get_call_with_open_module1():
    assert 'open:input.txt' in get_calls(
        main), 'Are you calling `open()` and pass in the `input.txt` file?'
