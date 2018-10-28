from contextlib import contextmanager
from dataclasses import dataclass, field
from pathlib import Path
from types import MethodType
from typing import List


def create_html_element_function(element_name):
    @contextmanager
    def element_function(builder, **kwargs):
        params = [f"{key}={str(value)}" for key, value in kwargs.items()]
        builder.build_context.append(f"<{' '.join([element_name] + params)}>")
        try:
            yield None
        finally:
            builder.build_context.append(f"</{element_name}>")

    return element_function


@dataclass
class HtmlBuilder:
    build_context: List = field(default_factory=list)

    @contextmanager
    def body(self):
        self.build_context.append("<body>")
        try:
            yield
        finally:
            self.build_context.append("</body>")

    def __getattr__(self, item):
        return MethodType(create_html_element_function(item), self)

    def __add__(self, other):
        self.build_context.append(str(other))

    def __repr__(self):
        return "\n".join(self.build_context)


h = HtmlBuilder()

with h.html():
    with h.body():
        for i in range(5):
            with h.h1():
                h + "Hello PyCon!"
            with h.h3():
                h + "Hello PyCon!"

        with h.img(src="/Users/sitalov/Dropbox/SoftwareEngineering/Experiments/Python/dsl/pyconie/media/python.gif"):
            h + "whee!"

Path('/tmp/pycon.html').write_text(str(h))
