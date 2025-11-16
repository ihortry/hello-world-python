"""
A simple example module for demonstrating CI pipelines.
"""

def hello() -> str:
    """Return a greeting string."""
    return "Hello, CI World!"


def add(a: int, b: int) -> int:
    """Return the sum of two integers."""
    return a + b


if __name__ == "__main__":
    print(hello())
    print(f"1 + 2 = {add(1, 2)}")
