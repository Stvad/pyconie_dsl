from pathlib import Path


def achieve_zen():
    import this


the_answer = 42

namespace = dict(achieve_zen=achieve_zen,
                 the_answer=42)

source = Path('global_context_manipulation_dsl.py').read_text()
exec(source, namespace)

print(namespace['random_string'])
