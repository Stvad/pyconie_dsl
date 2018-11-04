from dataclasses import dataclass


@dataclass
class XmlBuilder:
    tag_name: str = "html"

    def __enter__(self):
        print(f'<{self.tag_name}>')

    def __exit__(self, *args):
        print(f'</{self.tag_name}>')

    def __getattr__(self, item):
        return XmlBuilder(item)


t = XmlBuilder()

with t:
    with t.body:
        with t.h1:
            print("Whee")
