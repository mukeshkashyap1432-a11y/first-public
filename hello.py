"""Greeting helpers for the ADP manual tests (project s1)."""


def greet(name: str) -> str:
    """Return a friendly greeting for *name*."""
    return f"Hello, {name}!"


def shout(text: str) -> str:
    """Return *text* in uppercase with an exclamation mark."""
    return text.upper() + "!"


def wave(name: str) -> str:
    """Return a wave greeting for *name*."""
    return f"Wave, {name}!"
