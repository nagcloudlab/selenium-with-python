"""
Test Cases
* `finish` from "todo", "in prog", and "done" states
* `finish` an invalid id
"""
import pytest
from cards import Card, InvalidCardId


@pytest.mark.parametrize("start_state", ("todo", "in prog", "done"))
def test_finish(cards_db, start_state):
    """
    End state should be "done"
    """
    c = Card("foo", state=start_state)
    i = cards_db.add_card(c)
    cards_db.finish(i)
    c = cards_db.get_card(i)
    assert c.state == "done"

