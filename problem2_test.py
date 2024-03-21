import unittest
from problem2_code import determine_board_state


class TestDetermineBoardState(unittest.TestCase):
    def test_valid_input_player1_win(self):
        input_list = [[1, 1, 1],
                      [0, 2, 0],
                      [2, 0, 2]]
        self.assertTrue(determine_board_state(input_list))

    def test_valid_input_player2_win(self):
        input_list = [[1, 0, 1],
                      [0, 2, 2],
                      [2, 2, 2]]
        self.assertTrue(determine_board_state(input_list))

    def test_valid_input_no_winner(self):
        input_list = [[1, 2, 1],
                      [2, 1, 2],
                      [2, 1, 2]]
        self.assertFalse(determine_board_state(input_list))

    def test_invalid_input_wrong_type(self):
        input_list = "invalid"
        with self.assertRaises(Exception):
            determine_board_state(input_list)

    def test_invalid_input_wrong_inner_list_length(self):
        input_list = [[1, 2],
                      [0, 1, 2],
                      [2, 1, 0]]
        with self.assertRaises(Exception):
            determine_board_state(input_list)

    def test_invalid_input_wrong_inner_list_value(self):
        input_list = [[1, 2, "a"],
                      [0, 1, 2],
                      [2, 1, 0]]
        with self.assertRaises(Exception):
            determine_board_state(input_list)

if __name__ == '__main__':
    unittest.main()
