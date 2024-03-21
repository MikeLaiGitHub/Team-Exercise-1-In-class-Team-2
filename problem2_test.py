import unittest
from problem2_code import determine_board_state


class TestTicTacToe(unittest.TestCase):
    def test_row_win(self):
        # Test row win condition
        self.assertTrue(determine_board_state([[1, 1, 1], [0, 2, 0], [0, 0, 2]]))

    def test_column_win(self):
        # Test column win condition
        self.assertTrue(determine_board_state([[1, 0, 2], [1, 0, 2], [1, 0, 0]]))

    def test_diagonal_win(self):
        # Test diagonal win condition
        self.assertTrue(determine_board_state([[2, 0, 1], [0, 2, 1], [1, 0, 2]]))

    def test_no_win(self):
        # Test no win condition
        self.assertFalse(determine_board_state([[1, 2, 1], [2, 1, 2], [2, 1, 2]]))

    def test_invalid_input_type(self):
        # Test invalid input type
        with self.assertRaises(Exception):
            determine_board_state("not a valid board")


if __name__ == '__main__':
    unittest.main()

