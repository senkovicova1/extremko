import unittest
from nacitanie import setUp

data = setUp("suborDat.txt")

class TestStringMethods(unittest.TestCase):

    valid_chars = ['0', '1', '2', '3', '4', '5', '6', '7', '99']
    valid_chars2 = ['0', '1', '2', '3', '4', '99']
    valid_chars3 = ['0', '1', '2', '3', '4', '5', '99']

    def test_empty(self):
        self.assertFalse(not data, msg="Neboli vložené žiadne dáta")

    def test_missing_dot(self):
        for x in range(2, len(data)-1):
            with self.subTest(x=x):
                self.assertEqual(int(data[x][0]), int(data[x+1][0])-1, msg="Dotazník {0} neexistuje".format(int(data[x][0])+1))

    def test_wrong_number_of_entries(self):
        for x in range(1, len(data)):
            with self.subTest(x=x):
                self.assertEqual(len(data[x]), 37, msg="Dotazník {0} má nesprávny počet záznamov".format(data[x][0]))

    def test_q1_to_q9(self):
        for x in range(1, len(data)):
            with self.subTest(x=x):
                for y in range(1,10):
                    with self.subTest(y=y):
                        self.assertTrue(data[x][y] in self.__class__.valid_chars, msg="Dotazník {0}, otázka {1}: hodnota \"{2}\" nie je v zozname moznych odpovedi".format(data[x][0], y, data[x][y]))
                        

    def test_q10_to_q20(self):
        for x in range(1, len(data)-1):
            with self.subTest(x=x):
                for y in range(10,21):
                    with self.subTest(y=y):
                        self.assertTrue(data[x][y] in self.__class__.valid_chars2, msg="Dotazník {0}, otázka {1}: hodnota \"{2}\" nie je v zozname moznych odpovedi".format(data[x][0], y, data[x][y]))

    def test_q22(self):
        for x in range(1, len(data)-1):
            with self.subTest(x=x):
                self.assertTrue(data[x][22] in self.__class__.valid_chars3, msg="Dotazník {0}, otázka {1}: hodnota \"{2}\" nie je v zozname moznych odpovedi".format(data[x][0], 22, data[x][22]))

    def test_q13_to_q27(self):
        for x in range(1, len(data)-1):
            with self.subTest(x=x):
                for y in range(23,28):
                    with self.subTest(y=y):
                        self.assertTrue(data[x][y] in self.__class__.valid_chars2, msg="Dotazník {0}, otázka {1}: hodnota \"{2}\" nie je v zozname moznych odpovedi".format(data[x][0], y, data[x][y]))

    def test_q28_to_q36(self):
        for x in range(1, len(data)-1):
            with self.subTest(x=x):
                for y in range(28, len(data[x])):
                    with self.subTest(y=y):
                        self.assertTrue(data[x][y] in self.__class__.valid_chars, msg="Dotazník {0}, otázka {1}: hodnota \"{2}\" nie je v zozname moznych odpovedi".format(data[x][0], y, data[x][y]))

if __name__ == '__main__':    
    unittest.main()
