import re

ipv4Regex = re.compile(r'''(
(^|(?=\s))                                  # start anchors
([01]?[0-9][0-9]?|2[0-4][0-9]|25[0-5]?)\.   # first Octet
([01]?[0-9][0-9]?|2[0-4][0-9]|25[0-5]?)\.   # second Octet
([01]?[0-9][0-9]?|2[0-4][0-9]|25[0-5]?)\.   # third Octet
([01]?[0-9][0-9]?|2[0-4][0-9]|25[0-5]?)     # last Octet
($|\s)                                      # end anchors
)''', re.VERBOSE | re.MULTILINE)


def isIpv4Address(address):
    """Determines if a string is a valid IPv4 address

    Args:
        address: String to validate as IPv4 address
    Returns:
        True if address is a valid IPv4 address, otherwise False
    """
    if address is None:
        return False

    searchResult = ipv4Regex.search(address)

    if searchResult is not None:
        return True

    return False


def extractIpv4AddressesFrom(text):
    """Extracts valid IPv4 addresses from argument string.

    Args:
        text: Text from which all valid IPv4 Addresses will be extracted.
    Returns:
        A list of all extracted IPv4 Addresses.
    """
    if text is None:
        return None

    addresses = ipv4Regex.finditer(str(text))
    results = []

    for current in addresses:
        results.append(current.group())

    if not results:
        results = None

    return results


netmaskRegex = re.compile(r'''(
# start anchors
(^|(?=\s))
# first octet
(255|254|252|248|240|224|192|128|0{1,3})\.
# second octet
((?<=255\.)255|(?<=255\.)254|
(?<=255\.)252|(?<=255\.)248|
(?<=255\.)240|(?<=255\.)224|
(?<=255\.)192|(?<=255\.)128|0{1,3})\.
# third octet
((?<=255\.)255|(?<=255\.)254|
(?<=255\.)252|(?<=255\.)248|
(?<=255\.)240|(?<=255\.)224|
(?<=255\.)192|(?<=255\.)128|0{1,3})\.
# last octet
((?<=255\.)255|(?<=255\.)254|
(?<=255\.)252|(?<=255\.)248|
(?<=255\.)240|(?<=255\.)224|
(?<=255\.)192|(?<=255\.)128|0{1,3})
# end anchors
($|\s)
)''', re.VERBOSE | re.MULTILINE)


def isNetMask(address):
    """Determines if a string is a valid Subnet mask.

    Args:
        address: String to validate as Subnet mask.
    Returns:
        True if address is a valid Subnet mask, otherwise False.
    """
    if address is None:
        return False

    searchResult = netmaskRegex.search(address)

    if searchResult is not None:
        return True

    return False


def getAdapterSettingsFrom(text):
    if text is None:
        return None

    lines = text.splitlines()
    pairs = {}

    for line in lines:
        pair = extractAdapterSetting(line)
        if pair is not None:
            pairs.update(pair)

    return pairs


# TODO: write distinct tests for getAdapterSettingsFrom() and extractAdapterSetting()
#       after extracting deeply nested conditions from getAdapterSettingsFrom()
def extractAdapterSetting(line):
    splitLine = line.split(',')
    pair = {}
    if len(splitLine) >= 2:
        if isIpv4Address(splitLine[0]) and isNetMask(splitLine[1]):
            pair[splitLine[0]] = splitLine[1]

    return pair
