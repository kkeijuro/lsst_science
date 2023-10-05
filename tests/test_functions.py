import os
import sys

sys.path.append(os.path.join((os.path.dirname(__file__)), "../src"))

print(os.path.join(os.path.dirname(__file__), "../src"))
from lsst.science.utils import sandbox


def test_good() -> None:
    assert 5 == sandbox.add(2, 3)


def test_bad() -> None:
    assert 3 == sandbox.returns_3()
