from state_machine.dsl.context_manager import EventsContext
from state_machine.dsl.utils import load_module


def load_machine(path):
    module_dict = dict(globals())
    module_dict['events'] = EventsContext(module_dict)

    load_module(path, module_dict)


load_machine(
    '/Users/sitalov/Dropbox/SoftwareEngineering/Experiments/Python/dsl/pyconie/state_machine/example_context_manager.py')
