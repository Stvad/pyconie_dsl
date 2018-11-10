import subprocess
from contextlib import contextmanager
from dataclasses import dataclass
from os import environ, chdir, getcwd

PREPEND_BEHAVIOUR = 'prepend'
PATH_VAR = "PATH"


@contextmanager
def path(path_to_add, behavior=PREPEND_BEHAVIOUR):
    path_copy = environ.get(PATH_VAR, "")

    if behavior == PREPEND_BEHAVIOUR:
        environ[PATH_VAR] = f"{path_to_add}:{path_copy}"
    try:
        yield
    finally:
        environ[PATH_VAR] = path_copy


class MetaPath(type):
    def __getattr__(cls, item):
        return cls(behavior=item)


class Path(metaclass=MetaPath):
    def __init__(self, path_to_add='', behavior=PREPEND_BEHAVIOUR):
        self.path_to_add = path_to_add
        self.behavior = behavior

    def __enter__(self):
        self.path_copy = environ.get(PATH_VAR, "")

        if self.behavior == PREPEND_BEHAVIOUR:
            environ[PATH_VAR] = f"{self.path_to_add}:{self.path_copy}"

    def __exit__(self, exc_type, exc_val, exc_tb):
        environ[PATH_VAR] = self.path_copy

    def __call__(self, path_to_add):
        self.path_to_add = path_to_add
        return self


with Path.prepend('whee'):
    print(environ[PATH_VAR])


@contextmanager
def cd(new_dir):
    current_dir = getcwd()
    chdir(new_dir)

    try:
        yield
    finally:
        chdir(current_dir)


def run(command):
    subprocess.call(command, shell=True)


@dataclass
class NamedRunner:
    prefix: str = ''

    def __getattr__(self, item):
        self.prefix = item
        return self

    def __call__(self, command):
        run(f'{self.prefix} {command}')


with path('/lang/of/magic/binaries',
          behavior=PREPEND_BEHAVIOUR):
    with cd('/tmp'):
        run('touch PyCon')

c = NamedRunner()

with Path.prepend('/lang/of/magic/binaries'):
    with cd('/tmp'):
        c.touch('PyCon')
