import unittest

class RomanNumber():
    value = 0
    letters = ""

    def __init__(romanLetters):
        self.value = 0
        if not self.badLetters(romanLetters):
            self.letters = romanLetters

    def badLetters(romanLetters):
        badCharInLetters = not all(c.isupper() for c in romanLetters)
        duplicatesInLetters = len(romanLetters)!=(len(set(romanLetters)))
        if (romanLetters == "") or (badCharInLetters) or (duplicatesInLetters):
            return True    
        return False

    def maximum():
        if self.letters == "":
            return -9999
        length = len(self.letters)
        result = "3"
        if (length % 2 == 0):
            result = "8"
        rest = '9'*((length-1)//2)
        return int(result + rest)
