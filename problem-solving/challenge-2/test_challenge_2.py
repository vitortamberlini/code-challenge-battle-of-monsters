from unittest import TestCase

from challenge2 import dice_faces_calculator


class Challenge2(TestCase):
    def test_Case_1(self):
        value = dice_faces_calculator(6, 6, 6)

        self.assertEqual(value, 18)

    def test_Case_2(self):
        value = dice_faces_calculator(5, 5, 5)

        self.assertEqual(value, 15)

    def test_Case_3(self):
        value = dice_faces_calculator(1, 2, 3)

        self.assertEqual(value, 3)

    def test_Case_4(self):
        value = dice_faces_calculator(1, 1, 3)

        self.assertEqual(value, 2)

    def test_Case_5(self):
        value = dice_faces_calculator(5, 3, 3)

        self.assertEqual(value, 6)

    def test_Case_6(self):
        value = dice_faces_calculator(3, 5, 3)

        self.assertEqual(value, 6)

    def test_Case_7(self):
        value = dice_faces_calculator(4, 5, 6)

        self.assertEqual(value, 6)

    def test_Case_8(self):
        with self.assertRaises(Exception) as exec_info:
            dice_faces_calculator(7, 6, 5)

        self.assertEqual(str(exec_info.exception), "Dice out of number range")

    def test_Case_9(self):
        with self.assertRaises(Exception) as exec_info:
            dice_faces_calculator(0, 6, 5)

        self.assertEqual(str(exec_info.exception), "Dice out of number range")

    def test_Case_10(self):
        with self.assertRaises(Exception) as exec_info:
            dice_faces_calculator(-1, 2, 3)

        self.assertEqual(str(exec_info.exception), "Dice out of number range")
