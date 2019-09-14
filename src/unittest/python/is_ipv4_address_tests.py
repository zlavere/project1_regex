import unittest
from ipv4_matchers import *

# sample test class
class TestIsIPv4Address(unittest.TestCase):

    def testPassValidIPv4Address(self):
        self.assertTrue(isIpv4Address('160.010.025.006'))

    def testInvalidAllOctetsTooHighIPv4Address(self):
        self.assertFalse(isIpv4Address('988.988.988.988'))

    def testInvalidNoneAsAddressParameterIPv4Address(self):
        self.assertFalse(isIpv4Address(None))

    def testInvalidTooShortOneMissingOctetIPv4Address(self):
        self.assertFalse(isIpv4Address('168.168.168'))

    def testValidAllTwoDigitOctetsIPv4Address(self):
        self.assertTrue(isIpv4Address('12.12.12.12'))

    def testValidAllLeadingZeroTwoDigitOctetsIPv4Address(self):
        self.assertTrue(isIpv4Address('01.01.01.01'))

    def testValidTwoLeadingZeroOctetsIPv4Address(self):
        self.assertTrue('001.001.001.001')

    def testSingleNonZeroDigitOctetIPv4Address(self):
        self.assertTrue('1.1.1.1')

    def testInvalidTooLongOneExtraOctetIPv4Address(self):
        self.assertFalse(isIpv4Address('168.168.168.168.168'))

    def testValidAllTwoFiveFiveOctetIPv4Address(self):
        self.assertTrue(isIpv4Address('255.255.255.255'))

    def testValidAllZeroOctetIPv4Address(self):
        self.assertTrue(isIpv4Address('0.0.0.0'))

    def testInvalidOneOctetTooLongIPv4Address(self):
        self.assertFalse(isIpv4Address('123.123.1234.123'))

    def testInvalidOneOctetHasNoValueIPv4Address(self):
        self.assertFalse(isIpv4Address('123.123..123'))
