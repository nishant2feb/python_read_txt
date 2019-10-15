import pytest

from src import main
from .utils import get_assignments, get_calls, get_for_loops


def test_get_call_with_open_module1():
    calls = get_calls(main)
    message = 'Are you calling `open()` and pass in the `input.txt` file?'
    assert 'open:input.txt' in calls, message


def test_get_loop_for_each_line():
    loops = get_for_loops(main, 'dict')
    message = 'Do you have a `for` loop that loops through the `infile`?'
    assert len(loops) != 0, message

    target_id = loops[0]['target:id']
    iter_id = loops[0]['iter:id']
    assert target_id == 'line', 'Do you have a variable `line` in the loop?'
    assert iter_id == 'infile', 'Do you loop through the `infile`?'
