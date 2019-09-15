import re

# todo: complete this regex
ipv4Regex = r'(^|(?=\s))([01]?[0-9][0-9]?|2[0-4][0-9]|25[0-5]?)\.([01]?[0-9][0-9]?|2[0-4][0-9]|25[0-5]?)\.([01]?[0-9][0-9]?|2[0-4][0-9]|25[0-5]?)\.([01]?[0-9][0-9]?|2[0-4][0-9]|25[0-5]?)($|\s)'

def isIpv4Address(address):
    if address == None:
        return False

    regex = re.compile(ipv4Regex)
    searchResult = regex.search(address)

    if searchResult != None:
        return True

    return False

def extractIpv4AddressesFrom(text):
    if text == None:
        return None

    regex = re.compile(ipv4Regex, re.MULTILINE)
    addresses = regex.finditer(str(text))
    results = []

    for current in addresses:
        results.append(current.group())

    return results


# todo: complete this regex
netmaskRegex = None
