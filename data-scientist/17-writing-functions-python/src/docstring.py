#! /usr/bin/python3
"""
:file: docstring.py

developing docstring in google-style format
"""
import inspect


def count_letter(content, letter):
    """Count the number of times `letter` appears in `content`.

    Args:
      content (str): The string to search.
      letter (str): The letter to search for.

    Returns:
      int

    # Add a section detailing what errors might be raised
    Raises:
      ValueError: If `letter` is not a one-character string.
    """
    if (not isinstance(letter, str)) or len(letter) != 1:
        raise ValueError('`letter` must be a single character string.')
    return len([char for char in content if char == letter])


def build_tooltip(function):
    """Create a tooltip for any function that shows the 
    function's docstring.

    Args:
      function (callable): The function we want a tooltip for.

    Returns:
      str
    """
    # Use 'inspect' to get the docstring
    docstring = inspect.getdoc(function)
    border = '#' * 28
    return '{}\n{}\n{}'.format(border, docstring, border)


if __name__ == "__main__":
    # Get the docstring with an attribute of count_letter()
    docstring = count_letter.__doc__

    border = '#' * 28
    print('{}\n{}\n{}'.format(border, docstring, border))

    # Get the docstring with a function from the inspect module
    docstring = inspect.getdoc(count_letter)

    # border = '#' * 28
    print('{}\n{}\n{}'.format(border, docstring, border))
    print(build_tooltip(count_letter))
    print(build_tooltip(range))
    print(build_tooltip(print))
