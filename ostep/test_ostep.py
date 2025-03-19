import pytest


@pytest.mark.parametrize(
    "expected",
    [
        63,
        52,
        25,
    ],
)
def test_template(expected: int):

    actual = expected

    print(f"expected: {expected}")
    print(f"actual: {actual}")

    assert actual == expected, f"Expected {expected}, but got {actual}"
