import unittest
from ipv4_matchers import *

class TestIsSubnetAddress(unittest.TestCase):

    def testValidAllTwoFiveFiveOctetsAddress(self):
        address = '255.255.255.255'
        self.assertTrue(isNetMask(address))

    def testValidFirstOctetLessThanTwoFiveFive(self):
        address = '192.0.0.0'
        self.assertTrue(isNetMask(address))

    def testValidSecondOctetLessThanTwoFiveFive(self):
        address = '255.192.0.0'
        self.assertTrue(isNetMask(address))

    def testValidThirdOctetLessThanTwoFiveFive(self):
        address = '255.255.192.0'
        self.assertTrue(isNetMask(address))

    def testValidLastOctetLessThanTwoFiveFive(self):
        address = '255.255.255.192'
        self.assertTrue(isNetMask(address))

    def testValidSubnetMaskWithLeadingZeroes(self):
        address = '00.00.00.00'
        self.assertTrue(isNetMask(address))

    def testValidSubnetMaskWithTwoLeadingZeroes(self):
        address = '000.000.000.000'
        self.assertTrue(isNetMask(address))

    def testValidSubnetMaskWithLeadingZeroInLastOctet(self):
        address = '255.255.192.00'
        self.assertTrue(isNetMask(address))

    def testInvalidAllOnesNetmask(self):
        address = '1.1.1.1'
        self.assertFalse(isNetMask(address))

    def testInvalidTwoNonTwoFiveFiveOctets(self):
        address = '255.192.128.0'
        self.assertFalse(isNetMask(address))

    def testInvalidLessThanTwoFiveFiveBeforeTwoFiveFive(self):
        address = '192.255.255.255'
        self.assertFalse(isNetMask(address))

    def testInvalidZeroInFirstOctetFollowedByNonZeroes(self):
        address = '0.255.255.255'
        self.assertFalse(isNetMask(address))

    def testInvalidZeroInFirstOctetNonZeroInSecond(self):
        address = '0.255.0.0'
        self.assertFalse(isNetMask(address))

    def testInvalidSecondOctet(self):
        address = '255.42.0.0'
        self.assertFalse(isNetMask(address))

    def testNoneAsParameterReturnsFalse(self):
        address = None
        self.assertFalse(isNetMask(address))
