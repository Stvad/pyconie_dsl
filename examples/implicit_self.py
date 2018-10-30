import inspect
from contextlib import contextmanager

"""
Implicit self emulation in Python using context managers, inspection and locals manipulation.
"""


def is_public(field_name: str):
    return False if field_name.startswith('__') else True


@contextmanager
def in_context(context_object):
    decorator_frame = inspect.currentframe().f_back
    caller_frame = decorator_frame.f_back
    caller_locals = caller_frame.f_locals
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

# todo hierarchical example?
# add 'why' to techniques I'm describing

print(test_list)