from pathlib import Path
from tempfile import TemporaryDirectory
import cards
import pytest


class TestClassThree:
    def test_zero(self,cards_db):
        count = cards_db.count()
        assert count == 0
    