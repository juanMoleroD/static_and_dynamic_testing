import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):
    
    def setUp(self):
        self.card1 = Card("Spades", 1)
        self.card2 = Card("Hearts", 10)
        self.card3 = Card("Diamonds", 7)
        self.cardgame = CardGame()
    
    def test_check_ace_and_returns_true(self):
        self.assertTrue(self.cardgame.check_for_ace(self.card1))

    def test_check_ace_returns_false(self):
        self.assertFalse(self.cardgame.check_for_ace(self.card2))

    def test_highest_card(self):
        self.assertEqual(self.card2, self.cardgame.highest_card(self.card2, self.card3))

    def test_cards_total(self):
        self.assertEqual("You have a total of 17", self.cardgame.cards_total([self.card2, self.card3]) )

