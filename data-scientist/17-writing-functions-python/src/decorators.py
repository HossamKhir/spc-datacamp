#! /usr/bin/python3
"""
:file:

practising decorators
"""
# Import the function you need to fix the problem
from functools import wraps


def print_before_and_after(func):
    def wrapper(*args):
        print('Before {}'.format(func.__name__))
        # Call the function being decorated with *args
        func(*args)
        print('After {}'.format(func.__name__))
    # Return the nested function
    return wrapper


@print_before_and_after
def multiply(a, b):
    print(a * b)


def print_return_type(func):
    # Define wrapper(), the decorated function
    def wrapper(*args, **kwargs):
        # Call the function being decorated
        result = func(*args, **kwargs)
        print('{}() returned type {}'.format(
            func.__name__, type(result)
        ))
        return result
    # Return the decorated function
    return wrapper


def counter(func):
    def wrapper(*args, **kwargs):
        wrapper.count += 1
        # Call the function being decorated and return the result
        return func(*args, **kwargs)
    wrapper.count = 0
    # Return the new decorated function
    return wrapper


def add_hello(func):
    # Decorate wrapper() so that it keeps func()'s metadata
    @wraps(func)
    def wrapper(*args, **kwargs):
        """Print 'hello' and then call the decorated function.
        """
        print('Hello')
        return func(*args, **kwargs)
    return wrapper

# Decorate print_sum() with the add_hello() decorator


@add_hello
def print_sum(a, b):
    """Adds two numbers and prints the sum"""
    print(a + b)


def html(open_tag, close_tag):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            msg = func(*args, **kwargs)
            return '{}{}{}'.format(open_tag, msg, close_tag)
        # Return the decorated function
        return wrapper
    # Return the decorator
    return decorator

# Make hello() return bolded text


@html("<b>", "</b>")
def hello(name):
    return 'Hello {}!'.format(name)

# Make goodbye() return italicized text


@html("<i>", "</i>")
def goodbye(name):
    return 'Goodbye {}.'.format(name)

# Wrap the result of hello_goodbye() in <div> and </div>


@html("<div>", "</div>")
def hello_goodbye(name):
    return '\n{}\n{}\n'.format(hello(name), goodbye(name))


def tag(*tags):
    # Define a new decorator, named "decorator", to return
    def decorator(func):
        # Ensure the decorated function keeps its metadata
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Call the function being decorated and return the result
            return func(*args, **kwargs)
        wrapper.tags = tags
        return wrapper
    # Return the new decorator
    return decorator


def returns_dict(func):
    # Complete the returns_dict() decorator
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        assert(type(result) == dict)
        return result
    return wrapper


def returns(return_type):
    # Complete the returns() decorator
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            assert(type(result) == return_type)
            return result
        return wrapper
    return decorator


if __name__ == "__main__":
    multiply(5, 10)

    @print_return_type
    def foo(value):
        return value

    print(foo(42))
    print(foo([1, 2, 3]))
    print(foo({'a': 42}))

    # Decorate foo() with the counter() decorator
    @counter
    def foo():
        print('calling foo()')

    foo()
    foo()

    print('foo() was called {} times.'.format(foo.count))

    print_sum(10, 20)
    print(print_sum.__doc__)
    # Call the original function instead of the decorated one
    print_sum.__wrapped__(10, 20)

    print(hello('Alice'))

    print(goodbye('Alice'))

    print(hello_goodbye('Alice'))

    @tag('test', 'this is a tag')
    def foo():
        pass

    print(foo.tags)

    @returns_dict
    def foo(value):
        return value

    try:
        print(foo([1, 2, 3]))
    except AssertionError:
        print('foo() did not return a dict!')

    @returns(dict)
    def foo(value):
        return value

    try:
        print(foo([1, 2, 3]))
    except AssertionError:
        print('foo() did not return a dict!')
