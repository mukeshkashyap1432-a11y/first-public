"""Greeting helpers for the ADP manual tests (project s1)."""


def greet(name: str) -> str:
    """Return a friendly greeting for *name*."""
    return f"Hello, {name}!"


def shout(text: str) -> str:
    """Return *text* in uppercase with an exclamation mark."""
    return text.upper() + "!"


def summit(name: str) -> str:
    """Return a summit greeting for *name*."""
    return f"Summit, {name}!"
