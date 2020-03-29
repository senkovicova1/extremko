import unittest
import re


def convertToInt(roman):
    pole = ["I", "V", "X", "L", "C", "D", "M"]
    spolu = 0
    i = 0
    rad = 1000
    if (roman == ""):
        return -9999
    for r in roman:
        if r.upper() not in pole:
            return -9999
    while i < (len(roman)):

        number1, rad1 = getBase(roman[i].upper())
        number2, rad2 = getBase(roman[i + 1].upper()) if i + 1 < len(roman) else (0, 0)
        number3, rad3 = getBase(roman[i + 2].upper()) if i + 2 < len(roman) else (0, 0)
        number4, rad4 = getBase(roman[i + 3].upper()) if i + 3 < len(roman) else (0, 0)

        if number1 == number2 == number3 == number4:
            return -9999

        if number1 < number2:
            if pole.index(roman[i + 1].upper()) - pole.index(roman[i].upper()) > 2:
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


def intToRoman(integer):
    cislo = ""
    rad = 1
    integ = integer

    while integ != 0:
        c = integ % 10
        while (c == 0):
            integ = integ // 10
            rad += 1
            c = integ % 10
        typ = getTyp(c)
        if rad == 1:
            cislo = typ + cislo
        else:
            cislo = getCislo(typ, rad) + cislo

        integ = integ // 10
        rad += 1
    return cislo


def getBase(r):
    if (r == "M"):
        return (1000, 4)
    if (r == "D"):
        return (500, 3)
    if (r == "C"):
        return (100, 3)
    if (r == "L"):
        return (50, 2)
    elif (r == "X"):
        return (10, 2)
    elif (r == "V"):
        return (5, 1)
    elif (r == "I"):
        return (1, 1)


def getCislo(typ, rad):
    pole = ["X", "L", "C", "D", "M"]
    cislo = ""
    choices = []
    if (rad == 2):
        choices = ["X", "L", "C"]
    elif (rad == 3):
        choices = ["C", "D", "M"]
    else:
        choices = ["M"]

    for i in typ:
        if i == "I":
            cislo += choices[0]
        if i == "V":
            cislo += choices[1]
        if i == "X":
            cislo += choices[2]

    return cislo


def getTyp(cislo):
    if (cislo == 1):
        return "I"
    if (cislo == 2):
        return "II"
    if (cislo == 3):
        return "III"
    elif (cislo == 4):
        return "IV"
    elif (cislo == 5):
        return "V"
    elif (cislo == 6):
        return "VI"
    elif (cislo == 7):
        return "VII"
    elif (cislo == 8):
        return "VIII"
    elif (cislo == 9):
        return "IX"


def rimskaKalkulacka(str):
    global result
    str = str.replace(" ", "")
    operation = "".join(re.findall('[+\-/*]', str))
    numArray = re.split('[+\-/*]', str)
    if len(numArray) == 2 and len(operation) == 1:
        num1 = convertToInt(numArray[0])
        num2 = convertToInt(numArray[1])
        if operation == '-':
            result = num1 - num2
        elif operation == '+':
            result = num1 + num2
        elif operation == '/':
            result = num1 / num2
            if not result.is_integer():
                result = 9999
        elif operation == '*':
            result = num1 * num2
        if 1 < result < 3999:
            return intToRoman(result)
        else:
            return "Číslo mimo"
    else:
        return "Zlý vstup"


class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual(convertToInt("I"), 1)

    def test_upper1(self):
        self.assertEqual(convertToInt("II"), 2)

    def test_upper2(self):
        self.assertEqual(convertToInt("III"), 3)

    def test_upper3(self):
        self.assertEqual(convertToInt("IV"), 4)

    def test_upper4(self):
        self.assertEqual(convertToInt("X"), 10)

    def test_upper5(self):
        self.assertEqual(convertToInt("x"), 10)

    def test_upper6(self):
        self.assertEqual(convertToInt("L"), 50)

    def test_upper7(self):
        self.assertEqual(convertToInt("C"), 100)

    def test_upper8(self):
        self.assertEqual(convertToInt("D"), 500)

    def test_upper9(self):
        self.assertEqual(convertToInt("M"), 1000)

    def test_upper10(self):
        self.assertEqual(convertToInt("IXIX"), -9999)

    def test_upper11(self):
        self.assertEqual(convertToInt("MMMCMXCIX"), 3999)

    def test_upper12(self):
        self.assertEqual(convertToInt("IIII"), -9999)

    def test_upper13(self):
        self.assertEqual(convertToInt("IIIX"), -9999)

    def test_upper14(self):
        self.assertEqual(convertToInt(""), -9999)

    def test_upper15(self):
        self.assertEqual(convertToInt("a"), -9999)

    def test_upper16(self):
        self.assertEqual(convertToInt("Ia"), -9999)

    def test_upper17(self):
        self.assertEqual(convertToInt("MCMXXXVIII"), 1938)

    def test_upper18(self):
        self.assertEqual(convertToInt("MCMXLXXL"), -9999)

    def test_upper19(self):
        self.assertEqual(convertToInt("MCMLXXXVIII"), 1988)

    def test_upper20(self):
        self.assertEqual(convertToInt("MMXXXVIII"), 2038)

    def test_upper21(self):
        self.assertEqual(convertToInt("CCCLXXX"), 380)

    def test_upper22(self):
        self.assertEqual(convertToInt("CCCXXX"), 330)

    def test_upper23(self):
        self.assertEqual(convertToInt("MLC"), -9999)

    def test_upper24(self):
        self.assertEqual(convertToInt("IL"), -9999)

    def test_upper25(self):
        self.assertEqual(convertToInt("CL"), 150)

    def test_upper26(self):
        self.assertEqual(-9999, convertToInt('CDC'))

    def test_upper27(self):
        self.assertEqual(convertToInt('XXXIXX'), -9999)

    def test_upper28(self):
        self.assertEqual(-9999, convertToInt('DDD'))

    def test_upper29(self):
        self.assertEqual(-9999, convertToInt('MVV'))

    def test_upper30(self):
        self.assertEqual(-9999, convertToInt('MLL'))

    def test_upper31(self):
        self.assertEqual(41, convertToInt('XLI'))

    def test_upper32(self):
        self.assertEqual(-9999, convertToInt('VIIII'))

    def test_upper33(self):
        self.assertEqual("XV", rimskaKalkulacka("XX-V"))

    def test_upper34(self):
        self.assertEqual("XX", rimskaKalkulacka("X*II"))

    def test_upper35(self):
        self.assertEqual("X", rimskaKalkulacka("XX/II"))

    def test_upper36(self):
        self.assertEqual("XXV", rimskaKalkulacka("XX+V"))

    def test_upper37(self):
        self.assertEqual("Zlý vstup", rimskaKalkulacka("XX--V"))

    def test_upper38(self):
        self.assertEqual("XX", rimskaKalkulacka(" XI + I X "))

    def test_upper39(self):
        self.assertEqual("Zlý vstup", rimskaKalkulacka(" MD "))

    def test_upper40(self):
        self.assertEqual("Zlý vstup", rimskaKalkulacka("MM @ I"))

    def test_upper41(self):
        self.assertEqual("Číslo mimo", rimskaKalkulacka("MCDXLIV / MCDXLV"))

    def test_upper42(self):
        self.assertEqual("Číslo mimo", rimskaKalkulacka("MMM + M"))

    def test_upper43(self):
        self.assertEqual("Číslo mimo", rimskaKalkulacka("V/IV"))

    def test_upper44(self):
        self.assertEqual("Zlý vstup", rimskaKalkulacka("X/V/II"))


if __name__ == '__main__':
    unittest.main()
