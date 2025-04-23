import pytest
import cards


class TestClassOne:
    def test_zero(self,cards_db):
        count = cards_db.count()
        assert count == 0
    def test_two(self,cards_db):
        cards_db.add_card(cards.Card("first"))
        cards_db.add_card(cards.Card("second"))
        assert cards_db.count() == 2
    def test_three(self,cards_db):
        cards_db.add_card(cards.Card("first"))
        cards_db.add_card(cards.Card("second"))
        cards_db.add_card(cards.Card("third"))
        assert cards_db.count() == 3 


class TestClassTwo:
    def test_zero(self,cards_db):
        count = cards_db.count()
        assert count == 0
    def test_two(self,cards_db):
        cards_db.add_card(cards.Card("first"))
        cards_db.add_card(cards.Card("second"))
        assert cards_db.count() == 2
    def test_three(self,cards_db):
        cards_db.add_card(cards.Card("first"))
        cards_db.add_card(cards.Card("second"))
        cards_db.add_card(cards.Card("third"))
        assert cards_db.count() == 3 
