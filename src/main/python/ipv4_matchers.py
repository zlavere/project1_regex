import re

ipv4Regex = re.compile(r'''(
(^|(?=\s))                                  # start anchors
([01]?[0-9][0-9]?|2[0-4][0-9]|25[0-5]?)\.   # first Octet
([01]?[0-9][0-9]?|2[0-4][0-9]|25[0-5]?)\.   # second Octet
([01]?[0-9][0-9]?|2[0-4][0-9]|25[0-5]?)\.   # third Octet
([01]?[0-9][0-9]?|2[0-4][0-9]|25[0-5]?)     # last Octet
($|\s)                                      # end anchors
)''',re.VERBOSE | re.MULTILINE)


def isIpv4Address(address):
    """Determines if a string is a valid IPv4 address

    Args:
        address: String to validate as IPv4 address
    Returns:
        True if address is a valid IPv4 address, otherwise False
    """
    if address == None:
        return False

    searchResult = ipv4Regex.search(address)

    if searchResult != None:
        return True

    return False

def extractIpv4AddressesFrom(text):
    """Extracts valid IPv4 addresses from argument string.

    Args:
        text: Text from which all valid IPv4 Addresses will be extracted.
    Returns:
        A list of all extracted IPv4 Addresses.
    """
    if text == None:
        return None

    addresses = ipv4Regex.finditer(str(text))
    results = []

    for current in addresses:
        results.append(current.group())

    if not results:
        results = None

    return results

netmaskRegex = re.compile(r'''(
(^|(?=\s))                                  # start anchors
([01]?[0-9][0-9]?|2[0-4][0-9]|25[0-5]?)\.   # first Octet
([01]?[0-9][0-9]?|2[0-4][0-9]|25[0-5]?)\.   # second Octet
([01]?[0-9][0-9]?|2[0-4][0-9]|25[0-5]?)\.   # third Octet
([01]?[0-9][0-9]?|2[0-4][0-9]|25[0-5]?)     # last Octet
($|\s)                                      # end anchors
)''',re.VERBOSE | re.MULTILINE)
