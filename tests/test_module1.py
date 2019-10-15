import ast
import inspect

import astunparse
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


def test_split_line_with_space():
    calls = get_calls(main)
    message = "Are you calling `split()` of the line variable and pass in a space ' ' as the separator?"
    assert 'line:split: ' in calls, message


def test_get_last_element_in_splitted():
    assignments = get_assignments(main, return_type='list')

    # print(assignments)


def test_use_astunparse():
    inspected = inspect.getsource(main)
    parsed = ast.parse(inspected)
    unparsed = astunparse.unparse(parsed)

    print(type(inspected))  # 'str'
    print(type(parsed))
    print(type(unparsed))

    print(inspected)
    