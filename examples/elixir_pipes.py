from itertools import groupby

from pipeop import pipes

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
