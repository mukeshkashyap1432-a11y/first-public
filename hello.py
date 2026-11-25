"""Greeting helpers for the ADP manual tests (project s1)."""


def greet(name: str) -> str:
    """Return a friendly greeting for *name*."""
    return f"Hello, {name}!"


def shout(text: str) -> str:
    """Return *text* in uppercase with an exclamation mark."""
    return text.upper() + "!"


def beam(name: str) -> str:
    """Return a friendly beam greeting for *name*."""
    return f"Beam, {name}!"
