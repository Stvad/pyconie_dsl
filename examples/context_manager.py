from contextlib import contextmanager

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
