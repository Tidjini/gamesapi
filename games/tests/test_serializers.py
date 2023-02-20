from unittest import TestCase

from games.serializers import GameSerializer


class GameSeriliazerTest(TestCase):

    def test_validate(self):
        serializer = GameSerializer()
        data = serializer.validate({
            'name': 'God of War'
        })

        self.assertEqual(data, {
            'name': 'God of War',
            'slug':'god-of-war'
        })
