from datetime import date
from django.test import TestCase

from games.models import Game

class GameTestCase(TestCase):

    def setUp(self):

        self.game = Game.objects.create(
            name='Half Life',
            release_date=date(1995, 1, 1),
            category='Multiplayer - FPS',
        )
        self.game_created_at = self.game.created_at
        
        
    def test_game_basic(self):
        self.assertEqual(self.game.name, 'Half Life')
        self.assertEqual(self.game.release_date, date(1995, 1, 1))
        self.assertEqual(self.game.category, 'Multiplayer - FPS')
        self.assertEqual(self.game.played, False)
        self.assertEqual(self.game.created_at, self.game_created_at)