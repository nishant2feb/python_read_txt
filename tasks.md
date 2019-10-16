## Purpose of the project
This project will provide you a step-by-step guide to create a Python program to extract the last integer of each line in a text file.


## Verify locally
To test this module locally:
* Open up a terminal at the project root
* Run command `pytest -k module1`


## Task 1: Open the `input.txt` file as `infile`
A sample input file named `input.txt` is provided as part of the project.
We need to open it to get a [file object](https://docs.python.org/3.7/glossary.html#term-file-object) using the [open() method](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files).

A preferred way to open a file with automatic resource cleanup is using the `with` statement, 
which is a control-flow structure with basic structure as:
```
with expression [as variable]:
    with-block
```

In above structure, use `open()` in the `expression`, and name the variable as `infile`.


## Task 2: Loop through each line in `infile`
With the `infile` variable, we can loop through it to get each line in the `input.txt` file.

A simple way is just loop through the `infile` file object.
The basic structure of a loop in Python is as such:
```
for variable in iterable:
    body
```

Add a line of `for`-loop where the varible is named `line` and the iterable is `infile`.

The following tasks will fill in the `body` part of the loop


## Task 3: Separate line into list
Note that the fields in each line is separated by a space (`' '`) in `input.txt`.
For example, the first line is:
```
answer 42
```

Using the [str.split()](https://docs.python.org/3.7/library/stdtypes.html#str.split) function, split the `line` into a variable named `splitted`, with separator of a space.


## Task 4: Get the last element in the splitted list
Once we get the `splitted` list, it's time to get the last element in it.

To get the element at a given `index` in a `list`, use the following syntax: `list`[`index`], then assign it to a variable named `last`.

The `index` for the last element is `-1`.

## Task 5

## Task 6


