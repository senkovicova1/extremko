import unittest

def setUp(file):
    with open(file, "r") as txt:
        whole = txt.read().split("\n")
        arr = []
        for i in whole:
            arr.append(i.split(";"))
        print(arr)
        return arr

data = setUp("suborDat.txt")

class TestStringMethods(unittest.TestCase):


    valid_chars = ['0', '1', '2', '3', '4', '5', '6', '7', '9']
    valid_chars2 = ['0', '1', '2', '3', '4', '9']
    valid_chars3 = ['0', '1', '2', '3', '4', '5', '9']

    def test_empty(self):
        self.assertFalse(not data)

    def test_q1_to_q9(self):
        for x in range(1, len(data)-1):
            with self.subTest(x=x):
                for y in range(1,10):
                    with self.subTest(y=y):
                        try:
                            self.assertTrue(data[x][y] in self.__class__.valid_chars, msg="Dotazník {0}, otázka {1}: hodnota {2} je mimo povolený rozsah".format(x, y, data[x][y]))
                        except IndexError:
                            self.fail("V dotazníku {0} chýbajú údaje".format(x))

    def test_q10_to_q20(self):
        for x in range(1, len(data)-1):
            with self.subTest(x=x):
                for y in range(10,21):
                    with self.subTest(y=y):
                        try:
                            self.assertTrue(data[x][y] in self.__class__.valid_chars2, msg="Dotazník {0}, otázka {1}: hodnota {2} je mimo povolený rozsah".format(x, y, data[x][y]))
                        except IndexError:
                            self.fail("V dotazníku {0} chýbajú údaje".format(x))

    def test_q22(self):
        for x in range(1, len(data)-1):
            with self.subTest(x=x):
                try:
                    self.assertTrue(data[x][22] in self.__class__.valid_chars3, msg="Dotazník {0}, otázka {1}: hodnota {2} je mimo povolený rozsah".format(x, 22, data[x][22]))
                except IndexError:
                    self.fail("V dotazníku {0} chýbajú údaje".format(x))

    def test_q13_to_q27(self):
        for x in range(1, len(data)-1):
            with self.subTest(x=x):
                for y in range(23,28):
                    with self.subTest(y=y):
                        try:
                            self.assertTrue(data[x][y] in self.__class__.valid_chars2, msg="Dotazník {0}, otázka {1}: hodnota {2} je mimo povolený rozsah".format(x, y, data[x][y]))
                        except IndexError:
                            self.fail("V dotazníku {0} chýbajú údaje".format(x))

    def test_q28_to_q36(self):
        for x in range(1, len(data)-1):
            with self.subTest(x=x):
                for y in range(28,37):
                    with self.subTest(y=y):
                        try:
                            self.assertTrue(data[x][y] in self.__class__.valid_chars, msg="Dotazník {0}, otázka {1}: hodnota {2} je mimo povolený rozsah".format(x, y, data[x][y]))
                        except IndexError:
                            self.fail("V dotazníku {0} chýbajú údaje".format(x))

if __name__ == '__main__':
    unittest.main()