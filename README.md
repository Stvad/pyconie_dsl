# Domain specific languages in Python. The Why and How. 

    🙂                  🙂          🙂🙂🙂😛🙂🙂
    🙂                  🙂                😛
    🙂                  🙂                😛
    🙂                  🙂                😛
    🙂                  🙂                😛
    🙂                  🙂                😛
    🙂                  🙂                😛
    🙂                  🙂                😛
    🙂                  🙂                😛
    🙂                  🙂                😛
    🙂                  🙂                😛
    🦄🦄🦄🦄🦄🦄🦄🦄🦄🙂                😛
    🙂                  🙂                😛
    🙂                  🙂                😛
    🙂                  🙂                😛
    🙂                  🙂                😛
    🙂                  🙂                😛
    🙂                  🙂                😛
    🙂                  🙂                😛
    🙂                  🙂                😛
    🙂                  🙂                😛
    🙂                  🙂           🙂🙂🙂🙂🙂🙂

> created via [Character Canvas DSL](examples/magic_overloading.py)

---

This repo contains materials and examples for the PyconIE 2018 talk: **Domain specific languages in Python. The Why and How**

You can find the presentation [here](pycon_ie_presentation.key) [pdf version](pycon_ie_presentation.pdf).

Video from the conference was lost to history, but you can listen to [pre-conference recording](media/pre-conference-recording.m4a) & read it's [transcript](media/pre-conference-recording-transcript.txt)
## Examples

1. State Machine/Home automation DSL. The example is inspired by the "Gothic security system" from [DSL book by Martin Fowler](#references) 
    * [State Machine Model](state_machine/model.py)
    * Various ways of initializing the state machine:
        * [Imperative Initialization](state_machine/example_cqi.py)
        * [YAML DSL](state_machine/example.yaml)
        * [External DSL](state_machine/example.machine)
        * [Fluent interface init](state_machine/example_fluid.py)
        * [Internal DSL](state_machine/example_context_manager.py)
    * DSL code:
        * [Fluid interface definition](state_machine/model_fluid.py)
        * [DSL from the introduction](state_machine/dsl) - combines a variety of techniques.
1. [Character Canvas/Drawing Board/Turtle DSL 🦄](examples/magic_overloading.py). An example DSL to demonstrate the utility of operators/magic method overloading.
1. [Fabric-inspired contexts + dynamic field generation](examples/fabric_contexts.py)
1. HTML
    * [Simple context manager-based HTML builder](examples/context_manager.py) 
    * [HTML builder that uses dynamic class property generation](examples/dynamic_generatioin.py)
    * [A more extensive HTML builder DSL example, that combines a variety of techniques](html/html_builder.py)
1. Defining global executing context: [runner](examples/global_context_manipulation.py), [dsl-file](examples/global_context_manipulation_dsl.py)
1. Defining local execution context: [Implicit 'self' emulation](examples/implicit_self.py)
1. [Elixir-style pipes usage example](examples/elixir_pipes.py). Demonstrates one of the applications of import time AST manipulation.

## References


1. [Domain-Specific Languages](https://www.goodreads.com/book/show/8082269) by Martin Fowler
1. [The library that implements Elixir style pipes](https://github.com/robinhilliard/pipes)
1. [Macropy](https://macropy3.readthedocs.io/) A framework to help you with import time AST manipulation.
1. [SSM Document Generator (the accidental DSL)](https://github.com/awslabs/aws-systems-manager-document-generator)
1. DSLs mentioned in the talk:
    * [Attrs](https://attrs.org/)
    * [ANTLR](https://antlr.org/)
    * [Scons](https://scons.org/)
    * [Rake](https://github.com/ruby/rake)
    * [GraphViz](https://www.graphviz.org/)
    * RegEx
    * CSS
    
1. Various other resources I found useful while doing research for the talk:
    * https://orbifold.xyz/python-dsl.html
    * https://nvbn.github.io/2015/04/04/python-html-dsl/
    * https://rszalski.github.io/magicmethods  
    * https://play.kotlinlang.org/byExample/09_Kotlin_JS/06_HtmlBuilder
    
---

![Python is Dynamic!](media/python.gif)

