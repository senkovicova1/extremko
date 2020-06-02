import unittest
from RomanNumber import RomanNumber, RomanNumberWithZero

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

    ##Roman to integer
    ##Set Roman
    def test2_I_I_I(self):
        roman = RomanNumber("I")
        self.assertTrue(roman.setRomanNumber("I"))

    def test2_IVX_IX(self):
        roman = RomanNumber("IVX")
        self.assertEqual(roman.setRomanNumber("IX"), True)

    def test2_IAVXLCQDM_AQV(self):
        roman = RomanNumber("IAVXLCQDM")
        self.assertTrue(roman.setRomanNumber("QVA"))

    def test2_I_I_IIII(self):
        roman = RomanNumber("I")
        self.assertFalse(roman.setRomanNumber("IIII"))

    def test2_I_IV(self):
        roman = RomanNumber("I")
        self.assertEqual(roman.setRomanNumber("IV"), False)

    def test2_IV_Prazdne(self):
        roman = RomanNumber("IV")
        self.assertEqual(roman.setRomanNumber(""), False)

    def test2_IV_VV(self):
        roman = RomanNumber("IV")
        self.assertFalse(roman.setRomanNumber("VV"))

    def test2_IV_IIV(self):
        roman = RomanNumber("IV")
        self.assertEqual(roman.setRomanNumber("IIV"), False)

    def test2_IV_IVI(self):
        roman = RomanNumber("IV")
        self.assertEqual(roman.setRomanNumber("IVI"), False)

    def test2_IV_VIV(self):
        roman = RomanNumber("IV")
        self.assertEqual(roman.setRomanNumber("VIV"), False)

    def test2_IV_IVV(self):
        roman = RomanNumber("IV")
        self.assertFalse(roman.setRomanNumber("IVV"))

    def test2_IV_IX(self):
        roman = RomanNumber("IV")
        self.assertEqual(roman.setRomanNumber("IX"), False)

    def test2_IVX_VX(self):
        roman = RomanNumber("IVX")
        self.assertFalse(roman.setRomanNumber("VX"))

    def test2_IVX_IIX(self):
        roman = RomanNumber("IVX")
        self.assertEqual(roman.setRomanNumber("IIX"), False)

    def test2_IVXL_LC(self):
        roman = RomanNumber("IVXL")
        self.assertEqual(roman.setRomanNumber("LC"), False)

    def test2_IVX_LXXXIX(self):
        roman = RomanNumber("IVX")
        self.assertFalse(roman.setRomanNumber("LXXXIX"))

    def test2_I_MVA(self):
        roman = RomanNumber("I")
        self.assertEqual(roman.setRomanNumber("MVA"), False)

    def test2_IVXL_MQV(self):
        roman = RomanNumber("IVXL")
        self.assertEqual(roman.setRomanNumber("MQV"), False)

    def test2_IVXLCDMPQRSTUWYZEFGH_IXV(self):
        roman = RomanNumber("IVXLCDMPQRSTUWYZEFGH")
        self.assertFalse(roman.setRomanNumber("IXV"))

    def test2_IVXLCDMPQRS_RR(self):
        roman = RomanNumber("IVXLCDMPQRS")
        self.assertFalse(roman.setRomanNumber("RR"))

    def test2_IVXLCDM_I(self):
        roman = RomanNumber()
        roman.setRomanNumber("I")
        self.assertEqual(roman.getValue(), 1)

    def test2_IVXLCDM_MMMDCCCXCIV(self):
        roman = RomanNumber()
        roman.setRomanNumber("MMMDCCCXCIV")
        self.assertEqual(roman.getValue(), 3894)

    def test2_I_I_III(self):
        roman = RomanNumber("I")
        roman.setRomanNumber("III")
        self.assertEqual(roman.getValue(), 3)

    def test2_IVX_X(self):
        roman = RomanNumber("IVX")
        roman.setRomanNumber("X")
        self.assertEqual(roman.getValue(), 10)

    def test2_IVXLC_CCCLXXXIX(self):
        roman = RomanNumber("IVXLC")
        roman.setRomanNumber("CCLXXXIX")
        self.assertEqual(roman.getValue(), 289)

    def test2_IVXLCDMPQRS_SQQQVII(self):
        roman = RomanNumber("IVXLCDMPQRS")
        roman.setRomanNumber("SQQQVII")
        self.assertEqual(roman.getValue(), 130007)

    def test2_IVXLCDMPQRSTUWY_YWUSSSRMMMXLVI(self):
        roman = RomanNumber("IVXLCDMPQRSTUWY")
        roman.setRomanNumber("YWUSSSRMMMXLVI")
        self.assertEqual(roman.getValue(), 16353046)

    def test2_IVXLCDMPQRS_SSSRMMMXLVI(self):
        roman = RomanNumber("IVXLCDMPQRS")
        roman.setRomanNumber("SSSRMMMXLVI")
        self.assertEqual(roman.getValue(), 353046)

    def test2_IVXLCDM_MMM(self):
        roman = RomanNumber()
        roman.setRomanNumber("MMM")
        self.assertEqual(roman.getValue(), 3000)

    def test2_IV_IV(self):
        roman = RomanNumber("IV")
        roman.setRomanNumber("IV")
        self.assertEqual(roman.getValue(), 4)

    def test2_IV_VIII(self):
        roman = RomanNumber("IV")
        roman.setRomanNumber("VIII")
        self.assertEqual(roman.getValue(), 8)

    def test2_ABCD_DCCC(self):
        roman = RomanNumber("ABCD")
        roman.setRomanNumber("DCCC")
        self.assertEqual(roman.getValue(), 80)

    def test2_IVXL_LXXXIX(self):
        roman = RomanNumber("IVXL")
        roman.setRomanNumber("LXXXIX")
        self.assertEqual(roman.getValue(), 89)

    def test2_IVXLCDMPQRSTUWYZ_ZUUUTSSSRQMPCCCXIV(self):
        roman = RomanNumber("IVXLCDMPQRSTUWYZ")
        roman.setRomanNumber("ZUUUTSSSRQMPCCCXIV")
        self.assertEqual(roman.getValue(), 53864314)

    def test2_IVXLCD_DCCLXXX(self):
        roman = RomanNumber("IVXLCD")
        roman.setRomanNumber("DCCLXXX")
        self.assertEqual(roman.getValue(), 780)

    def test2_TestEfektivnostiPatiek(self):
        roman = RomanNumber("IVXLCDMPQRSTUW")
        for i in range(1000):
            roman.setRomanNumber("WUSSSRMMMXLVIII")
            if (roman.getValue() != 6353048):
                self.assertTrue(False)
        self.assertTrue(True)

    def test2_TestEfektivnosti(self):
        for i in range(1000):
            roman = RomanNumber("IVXLCDMPQRSTUWY")
            roman.setRomanNumber("YWUSSSRMMMXLVIII")
            if (roman.getValue() != 16353048):
                self.assertTrue(False)
        self.assertTrue(True)

    # Integer to roman
    def test2_IVXLCDM_1(self):
        roman = RomanNumber()
        roman.setValue(1)
        self.assertEqual(roman.getRomanNumber(), "I")

    def test2_IVXLCDM_3896(self):
        roman = RomanNumber()
        roman.setValue(3896)
        self.assertEqual(roman.getRomanNumber(), "MMMDCCCXCVI")

    def test2_I_3(self):
        roman = RomanNumber("I")
        roman.setValue(3)
        self.assertEqual(roman.getRomanNumber(), "III")

    def test2_IVXLCDM_0(self):
        roman = RomanNumber()
        self.assertFalse(roman.setValue(0))

    def test2_IVXLCDM_NO_NUMBER(self):
        roman = RomanNumber()
        self.assertFalse(roman.setValue(0))
        self.assertEqual(roman.getRomanNumber(), "NO_NUMBER")

    def test2_IVXLCDM_NO_NUMBER_MAX(self):
        roman = RomanNumber()
        self.assertFalse(roman.setValue(4000))
        self.assertEqual(roman.getRomanNumber(), "NO_NUMBER")

    def test2_IVXLCDMPQRSTUWYZ_53864324(self):
        roman = RomanNumber("IVXLCDMPQRSTUWYZ")
        roman.setValue(53864324)
        self.assertEqual(roman.getRomanNumber(), "ZUUUTSSSRQMPCCCXXIV")

    ##    def test2_123(self):
    ##        roman = RomanNumber("ABCDE")
    ##        roman.setValue(15)
    ##        self.assertEqual(roman.getRomanNumber(), "CB")

    def test3_ZlaAbeceda_Zero(self):
        roman = RomanNumberWithZero("OIVXLCDMSAC")
        self.assertEqual(roman.maximum(), 3999)

    def test3_maxZlychPismeniek_Zero(self):
        roman = RomanNumberWithZero("OIVXLCI")
        self.assertEqual(roman.maximum(), 3999)

    def test3_prazdnyMax_Zero(self):
        roman = RomanNumberWithZero("   ")
        self.assertEqual(roman.maximum(), 3999)

    # Maximum
    def test3_max_I_Zero(self):
        roman = RomanNumberWithZero("OI")
        self.assertEqual(roman.maximum(), 3)

    def test3_max_V_Zero(self):
        roman = RomanNumberWithZero("OV")
        self.assertEqual(roman.maximum(), 3)

    def test3_max_IV_Zero(self):
        roman = RomanNumberWithZero("OIV")
        self.assertEqual(roman.maximum(), 8)

    def test3_max_IVX_Zero(self):
        roman = RomanNumberWithZero("OIVX")
        self.assertEqual(roman.maximum(), 39)

    def test3_max_IVXL_Zero(self):
        roman = RomanNumberWithZero("OIVXL")
        self.assertEqual(roman.maximum(), 89)

    def test3_max_IVXLCD_Zero(self):
        roman = RomanNumberWithZero("OIVXLCD")
        self.assertEqual(roman.maximum(), 899)

    def test3_max_IVXLCDMQF_Zero(self):
        roman = RomanNumberWithZero("OIVXLCDMQF")
        self.assertEqual(roman.minimum(), -39999)

    def test3_OIVXLCD_0(self):
        roman = RomanNumberWithZero("OIVXLCD")
        self.assertTrue(roman.setValue(0))
        self.assertEqual(roman.getValue(), 0)

    def test3_OIVXLCD_minusMuch(self):
        roman = RomanNumberWithZero("OIVXLCD")
        self.assertFalse(roman.setValue(-5520))

    def test3_OIVXLCD_minus(self):
        roman = RomanNumberWithZero("OIVXLCD")
        self.assertTrue(roman.setValue(-520))
        self.assertEqual(roman.getValue(), -520)

    def test4_IVXLCDM_I_Zero(self):
        roman = RomanNumberWithZero()
        roman.setRomanNumber("I")
        self.assertEqual(roman.getValue(), 1)

    def test4_IVXLCDM_MMMDCCCXCIV_Zero(self):
        roman = RomanNumberWithZero()
        roman.setRomanNumber("MMMDCCCXCIV")
        self.assertEqual(roman.getValue(), 3894)

    def test4_I_I_III_Zero(self):
        roman = RomanNumberWithZero("OI")
        roman.setRomanNumber("III")
        self.assertEqual(roman.getValue(), 3)

    def test4_IVX_X_Zero(self):
        roman = RomanNumberWithZero("OIVX")
        roman.setRomanNumber("X")
        self.assertEqual(roman.getValue(), 10)

    def test4_IVXLC_CCCLXXXIX_Zero(self):
        roman = RomanNumberWithZero("OIVXLC")
        roman.setRomanNumber("CCLXXXIX")
        self.assertEqual(roman.getValue(), 289)

    def test4_IVXLCDMPQRS_SQQQVII_Zero(self):
        roman = RomanNumberWithZero("OIVXLCDMPQRS")
        roman.setRomanNumber("SQQQVII")
        self.assertEqual(roman.getValue(), 130007)

    def test4_IVXLCDMPQRSTUWY_YWUSSSRMMMXLVI_Zero(self):
        roman = RomanNumberWithZero("OIVXLCDMPQRSTUWY")
        roman.setRomanNumber("YWUSSSRMMMXLVI")
        self.assertEqual(roman.getValue(), 16353046)

    def test4_IVXLCDMPQRS_SSSRMMMXLVI_Zero(self):
        roman = RomanNumberWithZero("OIVXLCDMPQRS")
        roman.setRomanNumber("SSSRMMMXLVI")
        self.assertEqual(roman.getValue(), 353046)

    def test4_IVXLCDM_MMM_Zero(self):
        roman = RomanNumberWithZero()
        roman.setRomanNumber("MMM")
        self.assertEqual(roman.getValue(), 3000)

    def test4_IV_IV_Zero(self):
        roman = RomanNumberWithZero("OIV")
        roman.setRomanNumber("IV")
        self.assertEqual(roman.getValue(), 4)

    def test4_IV_OIV_Zero(self):
        roman = RomanNumberWithZero("OIV")
        self.assertFalse(roman.setRomanNumber("OIV"))
        self.assertEqual(roman.getValue(), 0)

    def test4_IV_VIII_Zero(self):
        roman = RomanNumberWithZero("OIV")
        roman.setRomanNumber("VIII")
        self.assertEqual(roman.getValue(), 8)

    def test4_ABCD_DCCC_Zero(self):
        roman = RomanNumberWithZero("QABCD")
        roman.setRomanNumber("DCCC")
        self.assertEqual(roman.getValue(), 80)

    def test4_IVXL_LXXXIX_Zero(self):
        roman = RomanNumberWithZero("OIVXL")
        roman.setRomanNumber("LXXXIX")
        self.assertEqual(roman.getValue(), 89)

    def test4_IVXLCDMPQRSTUWYZ_ZUUUTSSSRQMPCCCXIV_Zero(self):
        roman = RomanNumberWithZero("OIVXLCDMPQRSTuWYZ")
        roman.setRomanNumber("ZuuuTSSSRQMPCCCXIV")
        self.assertEqual(roman.getValue(), 53864314)

    # def test4_IVXLCDMPQRSTUWYZ_12345atd(self):
    #   roman = RomanNumberWithZero("01234567890abcdef")
    #   roman.setValue(53865267)
    #   self.assertEqual(roman.getRomanNumber(), "fcccbaaa0985543211")

    def test4_IVXLCD_DCCLXXX_Zero(self):
        roman = RomanNumberWithZero("OIVXLCD")
        roman.setRomanNumber("DCCLXXX")
        self.assertEqual(roman.getValue(), 780)

    def test4_TestEfektivnostiPatiek_Zero(self):
        roman = RomanNumberWithZero("OIVXLCDMPQRSTUW")
        for i in range(0, 1000):
            roman.setRomanNumber("WUSSSRMMMXLVIII")
            if roman.getValue() != 6353048:
                self.assertTrue(False)
        self.assertTrue(True)

    def test4_TestEfektivnosti_Zero(self):
        for i in range(0, 1000):
            roman = RomanNumberWithZero("OIVXLCDMPQRSTUWY")
            roman.setRomanNumber("YWUSSSRMMMXLVIII")
            if roman.getValue() != 16353048:
                self.assertTrue(False)
        self.assertTrue(True)

    def test4_IVXLCDM_1_Zero(self):
        roman = RomanNumberWithZero()
        roman.setValue(1)
        self.assertEqual(roman.getRomanNumber(), "I")


    def test4_IVXLCDM_3896_Zero(self):
        roman = RomanNumberWithZero()
        roman.setValue(3896)
        self.assertEqual(roman.getRomanNumber(), "MMMDCCCXCVI")


    def test4_I_I_3_Zero(self):
        roman = RomanNumberWithZero("OI")
        roman.setValue(3)
        self.assertEqual(roman.getRomanNumber(), "III")


    def test4_IVXLCDM_0_Zero(self):
        roman = RomanNumberWithZero()
        self.assertTrue(roman.setValue(0))


    def test4_IVXLCDM_NO_NUMBER_Zero(self):
        roman = RomanNumberWithZero()
        self.assertTrue(roman.setValue(0))
        self.assertEqual(roman.getRomanNumber(), "O")


    def test4_IVXLCDM_NO_NUMBER_MAX_Zero(self):
        roman = RomanNumberWithZero()
        self.assertFalse(roman.setValue(4000))
        self.assertEqual(roman.getRomanNumber(), "O")


    def test4_IVMcisla(self):
        roman = RomanNumberWithZero("OIVXL CDM1 2345 6789")
        roman.setValue(-59293105)
        self.assertEqual(roman.getRomanNumber(), "-9684424MMMCV")


    def test4_opak(self):
        roman = RomanNumberWithZero("OIVXL CDM1 2345 6789")
        roman.setRomanNumber("-9684424MMMCVII")
        self.assertEqual(roman.getRomanNumber(), "-9684424MMMCVII")


    def test4_naCislo(self):
        roman = RomanNumberWithZero("OIVXL CDM1 2345 6789")
        roman.setRomanNumber("-9684424MMMCVII")
        self.assertEqual(roman.getValue(), -59293107)

if __name__ == '__main__':
    unittest.main()
