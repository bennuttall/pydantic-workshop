# Pydantic workshop

Pydantic workshop given at PyCon UK 2025

## What is Pydantic?

- Pydantic is a Python library for data validation and settings management
- It uses Python type hints to define data models
- Pydantic makes working with structured, validated data in Python simple, safe, and efficient

## What can we use it for?

- Data modelling
- Data validation
- Schema definitions
- Consuming web APIs
- Serving web APIs
- Settings & configuration management

## Workshop prerequisites

- You have installed Python
- Have a suitable IDE (e.g. vscode)
  - an IDE which shows inferred types on hover and has autocomplete for inferred types would be most
    useful
- You can run a Python program in the terminal or your IDE
- You have a mechanism for creating virtual environments - and knowing how to activate and connect
  with your IDE
- Create a virtualenv and run `make develop` at the root of the repo, or run  `pip install -e .`
  from the `lib` directory

## vscode

This repo includes vscode settings for automatically formatting your code with Black. This is a
personal preference so you may wish to enable it (ensure you have the relevant extensions
installed), disable it, or change the settings in [.vscode/settings.json](.vscode/settings.json).

## Pydantic V1 vs V2

This workshop is strictly based on Pydantic V2.

If you previously learned Pydantic V2, there are a few differences but it's easy to learn V2 and
fairly easy to migrate. See the migration guide:
[https://docs.pydantic.dev/latest/migration/](https://docs.pydantic.dev/latest/migration/)

Please be aware that due to the nature of ChatGPT training, it may provide responses with Pydantic
V1 syntax, so it's usually a good idea to specify Pydantic V2 when asking for code snippets.

## Workshop

1. [Simple Pydantic model example](workshop/01.md)
2. [Collections](workshop/02.md)
3. [Consuming a JSON web API](workshop/03.md)
4. [Field validation](workshop/04.md)
5. [Model validation](workshop/05.md)
6. [pydantic-settings](workshop/06.md)
7. [Serialization](workshop/07.md)
8. [FastAPI server](workshop/08.md)
9. [FastAPI client](workshop/09.md)
10. [Typer](workshop/10.md)

## Licence

These workshop materials are copyright 2025 Ben Nuttall, licensed under [Creative Commons
Attribution-ShareAlike 4.0 International (CC BY-SA
4.0)](https://creativecommons.org/licenses/by-sa/4.0/)