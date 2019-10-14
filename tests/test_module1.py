import pytest

from src import main

def test_import_builtin_libraries_module1():
    assert 'os' in dir(main), 'Have you imported the built-in `os` library?'