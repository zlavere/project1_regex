import unittest
from ipv4_matchers import *

class TestGetAdapterSettingsFrom(unittest.TestCase):

    def testValidOneLinePair(self):
        text = '192.168.1.1,255.255.255.255'
        pairs = getAdapterSettingsFrom(text)
        self.assertEquals(pairs['192.168.1.1'], '255.255.255.255')


    def testValidTwoLinePair(self):
        text = '192.168.1.1,255.255.255.255\n192.42.42.42,255.255.128.0'
        pairs = getAdapterSettingsFrom(text)
        self.assertEquals(pairs['192.168.1.1'], '255.255.255.255')
        self.assertEquals(pairs['192.42.42.42'], '255.255.128.0')

    def testInvalidAndValidTwoLinesOnePairReturned(self):
        text = '192.168.1.1,255.255.255.255\nabc,255.255.128.0'
        pairs = getAdapterSettingsFrom(text)
        self.assertEquals(pairs['192.168.1.1'], '255.255.255.255')
        self.assertEquals(len(pairs), 1)

    def testOneInvalidLineWithNoPairReturnsNone(self):
        text = 'Luke Skywalker'
        pairs = getAdapterSettingsFrom(text)
        self.assertFalse(pairs)

    def testOneInvalidLineWithIpv4AddressNoNetMaskReturnsNone(self):
        text = '192.168.1.1'
        pairs = getAdapterSettingsFrom(text)
        self.assertFalse(pairs)

    def testOneInvalidLineWithInvalidIpv4AddressValidNetMaskReturnsNone(self):
        text = '192.abc.42.42,255.255.255.255'
        pairs = getAdapterSettingsFrom(text)
        self.assertFalse(pairs)

    def testOneInvalidLineWithInvalidNetMaskValidIpv4AddressReturnsNone(self):
        text = '192.168.1.1,0.255.255.255'
        pairs = getAdapterSettingsFrom(text)
        self.assertFalse(pairs)

    def testTwoValidLineOneInvalidLineIpv4AddressIsEmptyStringValidNetMask(self):
        text = '192.168.1.1,255.255.255.255\n192.168.2.2,255.255.255.192\n,255.255.192.0'
        pairs = getAdapterSettingsFrom(text)
        self.assertEquals(pairs['192.168.1.1'],'255.255.255.255')
        self.assertEquals(pairs['192.168.2.2'],'255.255.255.192')
        self.assertEquals(len(pairs), 2)
