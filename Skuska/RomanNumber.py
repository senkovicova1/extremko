import unittest


class RomanNumber():
    value = 3999
    letters = ""

    def __init__(self, romanLetters=""):
        if not self.badLetters(romanLetters):
            self.letters = romanLetters
            self.value = 0

    def badLetters(self, romanLetters):
        badCharInLetters = not all((c.isalpha() or c.isdigit()) for c in romanLetters)
        duplicatesInLetters = len(romanLetters) != (len(set(romanLetters)))
        if (romanLetters == "") or badCharInLetters or duplicatesInLetters:
            return True
        return False

    def maximum(self):
        if self.letters == "":
            return self.value
        length = len(self.letters)
        result = "3"
        if (length % 2 == 0):
            result = "8"
        rest = '9' * ((length - 1) // 2)
        return int(result + rest)

    def minimum(self):
        if self.letters == "":
            return 0
        return 1

    def setValue(self, nValue):
        if self.minimum() <= nValue <= self.maximum():
            self.value = nValue

    def getValue(self):
        return self.value

    def setRomanNumber(self, romanNumber, letters="IVXLCDM"):
        spolu = 0
        i = 0
        rad = 1000
        if self.badLetters(letters) or romanNumber == "":
            return -9999
        for r in romanNumber:
            if r.upper() not in letters:
                return -9999
        while i < (len(romanNumber)):
            number1, rad1 = self.getBase(romanNumber[i].upper(), letters)
            number2, rad2 = self.getBase(romanNumber[i + 1].upper(), letters) if i + 1 < len(romanNumber) else (0, 0)
            number3, rad3 = self.getBase(romanNumber[i + 2].upper(), letters) if i + 2 < len(romanNumber) else (0, 0)
            number4, rad4 = self.getBase(romanNumber[i + 3].upper(), letters) if i + 3 < len(romanNumber) else (0, 0)

            if number1 == number2 == number3 == number4:
                return -9999

            if number1 < number2:
                if letters.index(romanNumber[i + 1].upper()) - letters.index(romanNumber[i].upper()) > 2:
                    return -9999
                if number3 == number1:
                    return -9999
                if number1 * 2 == number2:
                    return -9999

            if number1 == number2:
                if number1 / 5 in [1, 10, 100, 1000]:
                    return -9999
                if number2 == number3 and number4 > number3:
                    return -9999

            if number1 < number2:
                spolu += number2 - number1
                rad = number1
                i += 2
            else:
                if (rad1 > rad):
                    return -9999
                spolu += number1
                rad = number1
                i += 1

        return spolu

    def getBase(self, char, letters):
        charInLetters = letters.find(char)
        rad = int(charInLetters / 2)
        if (charInLetters % 2) == 0:
            number = 1
        else:
            number = 5
        number = number * pow(10, rad)
        return (number, rad + 1)

class RomanNumberWithZero(RomanNumber):

    def __init__(self, romanLetters="OIVXLCDM"):
        super(RomanNumberWithZero, self).__init__(romanLetters)


class TestStringMethods(unittest.TestCase):

    def test1_ZlaAbeceda(self):
        roman = RomanNumber("IVXLCDMSAC")
        self.assertEqual(roman.maximum(), 3999)

    def test1_maxZlychPismeniek(self):
        roman = RomanNumber("IVXLCI")
        self.assertEqual(roman.maximum(), 3999)

    def test1_prazdnyMax(self):
        roman = RomanNumber(" ")
        self.assertEqual(roman.maximum(), 3999)

    # Maximum
    def test1_max_I(self):
        roman = RomanNumber("I")
        self.assertEqual(roman.maximum(), 3)

    def test1_max_V(self):
        roman = RomanNumber("V")
        self.assertEqual(roman.maximum(), 3)

    def test1_max_IV(self):
        roman = RomanNumber("IV")
        self.assertEqual(roman.maximum(), 8)

    def test1_max_IVX(self):
        roman = RomanNumber("IVX")
        self.assertEqual(roman.maximum(), 39)

    def test1_max_IVXL(self):
        roman = RomanNumber("IVXL")
        self.assertEqual(roman.maximum(), 89)

    def test1_max_IVXLC(self):
        roman = RomanNumber("IVXLC")
        self.assertEqual(roman.maximum(), 399)

    def test1_max_IVXLCD(self):
        roman = RomanNumber("IVx8CD")
        self.assertEqual(roman.maximum(), 899)

    def test1_max_IVXLCDM(self):
        roman = RomanNumber("IVXLCDM")
        self.assertEqual(roman.maximum(), 3999)

    def test1_max_IVXLCDMQF(self):
        roman = RomanNumber("123LCDMQF")
        self.assertEqual(roman.maximum(), 39999)

    ##    def test1_max_ABCDEFGHIJKLMNOPQRST():
    ##        roman = RomanNumber(er roman("ABCDEFGHIJKLMNOPQRST")
    ##        self.assertEqual(roman.maximum(), 410065407)

    # set, get int
    def test1_I_I_3(self):
        roman = RomanNumber("I")
        roman.setValue(3)
        self.assertEqual(roman.getValue(), 3)

    def test1_IVXLCDM_3894(self):
        roman = RomanNumber()
        roman.setValue(3894)
        self.assertEqual(roman.getValue(), 3894)

    def test1_IVX_10(self):
        roman = RomanNumber("IVX")
        roman.setValue(10)
        self.assertEqual(roman.getValue(), 10)

    def test1_IVX_39(self):
        roman = RomanNumber("IVX")
        roman.setValue(39)
        self.assertEqual(roman.getValue(), 39)

    def test1_IVX_40(self):
        roman = RomanNumber("IVX")
        roman.setValue(40)
        self.assertEqual(roman.getValue(), 0)

    def test1_IVXLCDMPQRSTUWY_16353046(self):
        roman = RomanNumber("IVXLCDMPQRSTUWY")
        roman.setValue(16353046)
        self.assertEqual(roman.getValue(), 16353046)

    def test1_ABCD_80(self):
        roman = RomanNumber("ABCD")
        roman.setValue(80)
        self.assertEqual(roman.getValue(), 80)

    def test1_IVxL(self):
        roman = RomanNumber("IVxL")
        self.assertEqual(roman.maximum(), 89)

    def test1_p1234(self):
        roman = RomanNumber("1234")
        self.assertEqual(roman.maximum(), 89)
        self.assertEqual(roman.minimum(), 1)

    def test1_IVbodkaL(self):
        roman = RomanNumber("IV.L")
        self.assertEqual(roman.maximum(), 3999)

    def test1_xXYy(self):
        roman = RomanNumber("xXYy")
        self.assertEqual(roman.maximum(), 89)


if __name__ == '__main__':
    unittest.main()