import inspect
from contextlib import contextmanager
from itertools import groupby

from pipeop import pipes

"""
Context managers can execute some code before and after supplied block of code and hence can serve as a good way to 
represent hierarchical structure.
"""


@contextmanager
def tag(tag_name):
    print(f'<{tag_name}>')
    try:
        yield
    finally:
        print(f'</{tag_name}>')


with tag("html"):
    with tag("body"):
        with tag("h1"):
            print("Whee")

# -----

"""
Elixir style pipes in Python.
"""


def group_to_dict(group_by_object):
    return {key: list(value) for key, value in group_by_object}


def group_by_character_set(input_string):
    print(group_to_dict(
        groupby(map(lambda x: x.lower(),
                    input_string.split()
                    ),
                lambda x: frozenset(x))
    ))


@pipes
def piped_group_by_character_set(input_string):
    input_string.split() << \
    map(lambda x: x.lower()) >> \
    groupby(lambda x: frozenset(x)) >> \
    group_to_dict >> print


group_by_character_set("abc bca cbd")
piped_group_by_character_set("abc bca cbd")

# ----

"""
Implicit self emulation in Python using context managers, inspection and locals manipulation.
"""


def is_public(field_name: str):
    return False if field_name.startswith('__') else True


@contextmanager
def in_context(context_object):
    caller_locals = inspect.currentframe().f_back.f_back.f_locals
    # on frame for `in_context` and one for decorator
    # horrible things, I know :p

    locals_snapshot = caller_locals.copy()
    for field in dir(context_object):
        if is_public(field):
            caller_locals[field] = getattr(context_object, field)
    try:
        yield
    finally:
        caller_locals.clear()
        caller_locals.update(locals_snapshot)


test_list = []
with in_context(test_list):
    append(3)
    extend([1, 7, 2])
    sort()

print(test_list)
