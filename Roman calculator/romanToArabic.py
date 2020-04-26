import unittest
import re

def convertToInt(romanNumber, letters ="IVXLCDM"):
    spolu = 0
    i = 0
    rad = 1000
    if badLetters(letters) or romanNumber == "":
        return -9999
    for r in romanNumber:
        if r.upper() not in letters:
            return -9999
    while i < (len(romanNumber)):
        number1, rad1 = getBase(romanNumber[i].upper(), letters)
        number2, rad2 = getBase(romanNumber[i + 1].upper(), letters) if i + 1 < len(romanNumber) else (0, 0)
        number3, rad3 = getBase(romanNumber[i + 2].upper(), letters) if i + 2 < len(romanNumber) else (0, 0)
        number4, rad4 = getBase(romanNumber[i + 3].upper(), letters) if i + 3 < len(romanNumber) else (0, 0)

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

def badLetters(romanLetters):
    badCharInLetters = not all(c.isupper() for c in romanLetters)
    duplicatesInLetters = len(romanLetters)!=(len(set(romanLetters)))
    if (romanLetters == "") or (badCharInLetters) or (duplicatesInLetters):
        return True    
    return False

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


def getBase(char, letters):
    charInLetters = letters.find(char)
    rad = int(charInLetters / 2)
    if (charInLetters % 2) == 0:
        number = 1
    else:
        number = 5
    number = number * pow(10, rad)
    return (number, rad+1)


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
        if 1 <= result <= 3999:
            return intToRoman(result)
        else:
            return "Číslo mimo"
    else:
        return "Zlý vstup"

def maxNumber(romanLetters):
    if badLetters(romanLetters):
        return -9999
    length = len(romanLetters)
    result = "3"
    if (length % 2 == 0):
        result = "8"
    rest = '9'*((length-1)//2)
    return int(result + rest)

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

    def test_upper45(self):
        self.assertEqual(49, convertToInt('XLIX'))

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

    def test_upper46(self):
        self.assertEqual("I", rimskaKalkulacka("L-XLIX"))

    def test_upper47(self):
        self.assertEqual("XCIX", rimskaKalkulacka("L+XLIX"))

    def test_upper48(self):
        self.assertEqual("V", rimskaKalkulacka("XX/IV"))

    def test_upper49(self):
        self.assertEqual("MMMCMXCVIII", rimskaKalkulacka("MMMCMXCIX-I"))

    def test_upper50(self):
        self.assertEqual("Číslo mimo", rimskaKalkulacka("MMMCMXCIX+I"))

    def test_upper51(self):
        self.assertEqual("MMMCMXCIX", rimskaKalkulacka("MMMCMXCIX*I"))

    def test_upper52(self):
        self.assertEqual("MMMCMXCIX", rimskaKalkulacka("MMMCMXCIX/I"))

    def test_upper53(self):
        self.assertEqual("Číslo mimo", rimskaKalkulacka("MLC/C"))

    def test_upper54(self):
        self.assertEqual("Číslo mimo", rimskaKalkulacka("M-M"))

    def test_upper55(self):
        self.assertEqual("I", rimskaKalkulacka("M-CMXCIX"))

    def test_upper56(self):
        self.assertEqual("Zlý vstup", rimskaKalkulacka("XX//IV"))

    def test_upper57(self):
        self.assertEqual("Zlý vstup", rimskaKalkulacka("-XX/IV"))

    def test_upper58(self):
        self.assertEqual(convertToInt("VIII", "IV"), 8)

    def test_upper59(self):
        self.assertEqual(convertToInt("AAA", "A"), 3)

    def test_upper60(self):
        self.assertEqual(convertToInt("IV","I"), -9999)

    def test_upper61(self):
        self.assertEqual(convertToInt("LXXXIX", "IVXL"), 89)

    def test_upper62(self):
        self.assertEqual(convertToInt("QVA", "IAVXLCQDM"), 1015)

    def test_upper63(self):
        self.assertEqual(convertToInt("SSS", "IVXLCDMPQRS"), 300000)

    def test_upper64(self):
        self.assertEqual(convertToInt("IV", ""), -9999)

    def test_upper65(self):
        self.assertEqual(convertToInt("IV", "IVXLX"), -9999)

    def test_upper66(self):
        self.assertEqual(convertToInt("IV", "IVXLX"), -9999)
        
    def test_upper67(self):
        self.assertEqual(convertToInt("OOP", "-POKL"), -9999)
        
    def test_upper68(self):
        self.assertEqual(convertToInt("DS", "ASDA"), -9999)
        
    def test_upper69(self):
        self.assertEqual(convertToInt("DS", "ASD"), 15)
        
    def test_upper70(self):
        self.assertEqual(convertToInt("MM", "IVXlCDM"), -9999)
        
    def test_upper71(self):
        self.assertEqual(convertToInt("", "IVXL"), -9999)
        
    def test_upper72(self):
        self.assertEqual(convertToInt("IV", ""), -9999)
        
    def test_upper73(self):
        self.assertEqual(convertToInt("IV", "789LK"), -9999)
        
    def test_upper74(self):
        self.assertEqual(convertToInt("-IV", "IVXL"), -9999)
        
    def test_upper75(self):
        self.assertEqual(convertToInt("AAAS", "ASDFG"), -9999)

    def test_upper76(self):
        self.assertEqual(maxNumber("I"),3)

    def test_upper77(self):
        self.assertEqual(maxNumber("IV"), 8)
        
    def test_upper78(self):
        self.assertEqual(maxNumber("IVX"), 39)
        
    def test_upper79(self):
        self.assertEqual(maxNumber("ASDF"), 89)
        
    def test_upper80(self):
        self.assertEqual(maxNumber("WERTA"), 399)
        
    def test_upper81(self):
        self.assertEqual(maxNumber("BARLEY"), 899)
        
    def test_upper82(self):
        self.assertEqual(maxNumber("VERITAS"), 3999)
        
    def test_upper83(self):
        self.assertEqual(maxNumber("GRAFICKY"), 8999)
        
    def test_upper84(self):
        self.assertEqual(maxNumber("POILKJHRT"), 39999)
        
    def test_upper85(self):
        self.assertEqual(maxNumber("QWERTZUIOP"), 89999)
        
    def test_upper86(self):
        self.assertEqual(maxNumber("ASDFGHJKLMN"), 399999)
        
    def test_upper87(self):
        self.assertEqual(maxNumber("YXCVBNMLKJHG"), 899999)
        
    def test_upper88(self):
        self.assertEqual(maxNumber("WERTAA"), -9999)
        
    def test_upper89(self):
        self.assertEqual(maxNumber(""), -9999)
        
    def test_upper90(self):
        self.assertEqual(maxNumber("12"), -9999)
        
    def test_upper91(self):
        self.assertEqual(maxNumber("AA"), -9999)
        
    def test_upper92(self):
        self.assertEqual(maxNumber("asdERT"), -9999)
        
    def test_upper93(self):
        self.assertEqual(maxNumber("ASDFGHJKLMND"), -9999)
        
    def test_upper94(self):
        self.assertEqual(maxNumber("ASDFGHaJKLMN"), -9999)
        
    def test_upper95(self):
        self.assertEqual(maxNumber("YXCVBNMLKJHGi"), -9999)

    def test_upper96(self):
        self.assertEqual(maxNumber("H A"), -9999)

    def test_upper97(self):
        self.assertEqual(maxNumber("."), -9999)


if __name__ == '__main__':
    unittest.main()
