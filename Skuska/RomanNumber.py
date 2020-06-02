import math

class RomanNumber():
    value = 3999
    letters = ""

    def __init__(self, romanLetters="IVXLCDM"):
        romanLetters = romanLetters.replace(" ", "")
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
        length = self.lengthLetters()
        result = "3"
        if (length % 2 == 0):
            result = "8"
        rest = '9' * ((length - 1) // 2)
        return int(result + rest)

    def lengthLetters(self):
        return len(self.letters)

    def minimum(self):
        return 1

    def setValue(self, nValue):
        if self.minimum() <= nValue <= self.maximum():
            self.value = nValue
            return True
        self.value = 0
        return False

    def getValue(self):
        return self.value

    def setRomanNumber(self, romanNumber):
        number = self.romanToInt(romanNumber)
        if number == -9999:
            self.value = 0
            return False
        self.value = number
        return True

    def getRomanNumber(self):
        if self.value == 0:
            return "NO_NUMBER"
        return self.intToRoman(self.value)

    def romanToInt(self, nRomanNumber):
        romanNumber = nRomanNumber.replace(" ", "")
        spolu = 0
        i = 0
        rad = 1000
        if self.letters == "" or romanNumber == "":
            return -9999
        for r in romanNumber:
            if r not in self.letters:
                return -9999
        while i < (len(romanNumber)):
            number1, rad1 = self.getBase(romanNumber[i])
            number2, rad2 = self.getBase(romanNumber[i + 1]) if i + 1 < len(romanNumber) else (0, 0)
            number3, rad3 = self.getBase(romanNumber[i + 2]) if i + 2 < len(romanNumber) else (0, 0)
            number4, rad4 = self.getBase(romanNumber[i + 3]) if i + 3 < len(romanNumber) else (0, 0)

            if number1 == number2 == number3 == number4:
                return -9999

            if number1 < number2:
                if self.letters.index(romanNumber[i + 1]) - self.letters.index(romanNumber[i]) > 2:
                    return -9999
                if number3 == number1:
                    return -9999
                if number1 * 2 == number2:
                    return -9999
                if number3 < number2 and number3 != 0 and rad1 == rad3 and rad1 == 1:
                    return -9999
                if number2 == number3:
                    if number2 / 5 in [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000]:
                        return -9999

            if number1 == number2:
                if number1 / 5 in [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000, 1000000000]:
                    return -9999
                if number2 == number3 and number4 > number3:
                    return -9999
                if rad1 == 1 and rad3 == 2:
                    return -9999
                if rad1 == rad3 and number1 != number3:
                    return -9999

            if number1 == number3:
                if rad1 == rad2 and rad2 == rad3 and number1 / 5 in [1, 10, 100, 1000, 10000, 100000, 1000000, 10000000,
                                                                     100000000, 1000000000]:
                    return -9999

            if number1 < number2:
                spolu += number2 - number1
                rad = number1
                i += 2
            else:
                if (rad1 > rad):
                    return -9999
                spolu += number1
                rad = rad1
                i += 1

        return spolu

    def intToRoman(self, integer):
        cislo = ""
        rad = 1

        while integer != 0:
            c = integer % 10
            while (c == 0):
                integer = integer // 10
                rad += 1
                c = integer % 10
            typ = self.getTyp(c)
            if rad == 1:
                cislo = typ + cislo
            else:
                cislo = self.getCislo(typ, rad) + cislo

            integer = integer // 10
            rad += 1
        return cislo

    def getBase(self, char):
        charInLetters = self.letters.find(char)
        rad = int(charInLetters / 2)
        if (charInLetters % 2) == 0:
            number = 1
        else:
            number = 5
        number = number * pow(10, rad)
        return (number, rad + 1)

    def getCislo(self, typ, rad):
        pole = list(self.letters[2:])
        cislo = ""
        choices = pole[:3]
        pole.pop(0)
        pole.pop(0)
        r = rad - 2
        while r > 0:
            choices = pole[:3]
            if len(pole) > 0:
                pole.pop(0)
            if len(pole) > 0:
                pole.pop(0)
            r -= 1

        for i in typ:
            if i == self.letters[0]:
                cislo += choices[0]
            if i == self.letters[1]:
                cislo += choices[1]
            if i == self.letters[2]:
                cislo += choices[2]

        return cislo

    def getTyp(self, cislo):
        if (cislo == 1):
            return self.letters[0]
        if (cislo == 2):
            return self.letters[0] * 2
        if (cislo == 3):
            return self.letters[0] * 3
        elif (cislo == 4):
            return self.letters[0] + self.letters[1]
        elif (cislo == 5):
            return self.letters[1]
        elif (cislo == 6):
            return self.letters[1] + self.letters[0]
        elif (cislo == 7):
            return self.letters[1] + self.letters[0] + self.letters[0]
        elif (cislo == 8):
            return self.letters[1] + self.letters[0] + self.letters[0] + self.letters[0]
        elif (cislo == 9):
            return self.letters[0] + self.letters[2]

    def isPowerOf10(self, number):
        n = round(number)
        while n > 1:
            if (n % 10 != 0):
                return False
            n /= 10
        return True

class RomanNumberWithZero(RomanNumber):

    allLetters = ""

    def __init__(self, romanLetters="OIVXLCDM"):
        super(RomanNumberWithZero, self).__init__(romanLetters)

    def minimum(self):
        return -RomanNumber.maximum(self)

    def lengthLetters(self):
        length = len(self.letters)
        return length-1

    def getBase(self, char):
        charInLetters = self.letters.find(char)
        if charInLetters == 0:
            return (0, 0)
        else:
            #aby sedeli rady v getBase
            self.saveAllLetters()
            base = RomanNumber.getBase(self, char)
            self.restoreAllLetters()
            return base

    def setRomanNumber(self, romanNumber):
        if romanNumber[0] == "-":
            RomanNumber.setRomanNumber(self, romanNumber[1:])
            self.value = -self.value
        else:
            RomanNumber.setRomanNumber(self, romanNumber)

    def getRomanNumber(self):
        if self.value == 0:
            romanNumber = self.letters[0]
        else:
            self.saveAllLetters()
            if self.value < 0:
                value = self.value
                self.value = -self.value
                romanNumber = RomanNumber.getRomanNumber(self)
                romanNumber = "-"+romanNumber
                self.value = value
            else:
                romanNumber = RomanNumber.getRomanNumber(self)
            self.restoreAllLetters()
        return romanNumber

    def saveAllLetters(self):
        self.allLetters = self.letters
        self.letters = self.letters[1:]

    def restoreAllLetters(self):
        self.letters = self.allLetters

    def calculator(self, expr):
        if len(expr) < 3:
            return False

        op1 = ""
        i = 0
        if expr[i] == "-":
            op1 += "-"
            i += 1
        while expr[i] not in "/*-+":
            op1 += expr[i]
            i += 1
            if i == len(expr):
                return False

        operator = expr[i]
        
        if i+1 == len(expr):
            return False
        
        op2 = expr[i+1:]

        intOp1 = self.romanToInt(op1)
        intOp2 = self.romanToInt(op2)

        if intOp1 == -9999 or intOp2 == -9999:
            print("here", intOp1, intOp2)
            return False

        if operator == "+":
            self.value = intOp1 + intOp2
            return True
        if operator == "-":
            self.value = intOp1 - intOp2
            return True
        if operator == "*":
            self.value = intOp1 * intOp2
            return True
        if operator == "/":
            if intOp2 == 0:
                return False
            self.value = math.floor(intOp1 / intOp2)
            return True
        return False













            
