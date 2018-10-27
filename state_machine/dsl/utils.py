from pathlib import Path


def load_module(module_path, globals_dict):
    """
    Load the python module stored at the given path.
    """

    code = compile(Path(module_path).read_text(), module_path, 'exec')
    exec(code, globals_dict, globals_dict)
