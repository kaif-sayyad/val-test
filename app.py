"""Tiny placeholder app. The point of this repo is its pinned dependencies."""


def greet(name):
    return f"Hello, {name}!"


if __name__ == "__main__":
    assert greet("test") == "Hello, test!"
    print("ok")
