from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import List, Dict


@dataclass
class HtmlBuilder:
    element_name: str = 'html'
    build_context: List = field(default_factory=list)
    parent: HtmlBuilder = None
    params: Dict = field(default_factory=dict)

    def __getattr__(self, item):
        return HtmlBuilder(item, self.build_context)

    def __add__(self, other):
        self.build_context.append(str(other))

    def __repr__(self):
        return "\n".join(self.build_context)

    def __enter__(self, **kwargs):
        self.build_context.append(f"<{' '.join([self.element_name] + self.param_string())}>")

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.build_context.append(f"</{self.element_name}>")
        if self.parent:
            self.parent.build_context.extend(self.build_context)

    def param_string(self):
        return [f"{key}={str(value)}" for key, value in self.params.items()]

    def __call__(self, **kwargs):
        self.params = kwargs
        return self


h = HtmlBuilder()

with h.body:
    for i in range(5):
        with h.h1:
            h + "Hello PyCon!"
        with h.h3():
            h + "Hello PyCon!"

    with h.img(src="/Users/sitalov/Dropbox/SoftwareEngineering/Experiments/Python/dsl/pyconie/media/python.gif"):
        h + "whee!"

Path('/tmp/pycon.html').write_text(str(h))

print(str(h))
