import rockpaperscissors
from unittest import TestCase
from unittest import mock
from unittest.mock import patch

class TestrockpaperscissorsGame(TestCase):

    def test_get_computer_pick(self):
        '''This insures that the random function returns 1, 2, or 3'''

        outcome = rockpaperscissors.get_computer_pick()
        self.assertIn((outcome), (1, 2, 3))

        for x in range(1,4):
            with patch('rockpaperscissors.get_computer_pick', side_effect=[x]):

                outcome = rockpaperscissors.get_computer_pick()
                self.assertIn((outcome),(1,2,3))
                self.assertNotIn((outcome),(4,5,6))

            with patch('random.randint', return_value=[x]):
                self.assertTrue(x, rockpaperscissors.get_computer_pick())
                
    @patch('rockpaperscissors.get_computer_pick', side_effect=[2])
    @patch('builtins.input', side_effect=['1', 'q'])
    @patch('builtins.print')            

    def test_winner_pick(self):
        '''This verifies win/loss combinations'''
        
        outcome = rockpaperscissors.winner_pick(player, computer)
        self.assertEqual(outcome, 'tie')

        outcome = rockpaperscissors.winner_pick('Paper','rock')
        self.assertEqual(outcome, 'computer wins - paper beats rock')
        
        outcome = rockpaperscissors.winner_pick('rock', 'Scissors')
        self.assertEqual(outcome, 'player wins - rock beats scissors')

        outcome = rockpaperscissors.winner_pick('Paper', 'rock')
        self.assertEqual(outcome, 'player wins - paper beats rock')

        outcome = rockpaperscissors.winner_pick('Scissors', 'rock')
        self.assertEqual(outcome, 'computer wins - rock beats scissors')
