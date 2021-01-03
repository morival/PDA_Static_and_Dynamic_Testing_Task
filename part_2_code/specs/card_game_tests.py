import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):
    
    def setUp(self):
        
        # Cards
        self.eight = Card("Eight", 8)
        self.five = Card("Five", 5)
        self.ace = Card("Ace", 1)

        self.cards = [self.eight, self.five, self.ace]

    def test_check_for_ace(self):
        check_if_ace = CardGame.check_for_ace(self, self.ace)
        self.assertEqual(True, check_if_ace)

    def test_highest_card(self):
        highest_card = CardGame.highest_card(self, self.eight, self.five)
        self.assertEqual("Eight", highest_card.suit)

    def test_cards_total(self):
        cards_total = CardGame.cards_total(self, self.cards)
        self.assertEqual("You have a total of 14", cards_total)