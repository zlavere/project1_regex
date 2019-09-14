import re

# todo: complete this regex
ipv4Regex = r'^\b([01]?[0-9][0-9]?|2[0-4][0-9]|25[0-5]?)\.([01]?[0-9][0-9]?|2[0-4][0-9]|25[0-5]?)\.([01]?[0-9][0-9]?|2[0-4][0-9]|25[0-5]?)\.([01]?[0-9][0-9]?|2[0-4][0-9]|25[0-5]?)\b$'

def isIpv4Address(address):
    if address == None:
        return False

    regex = re.compile(ipv4Regex)
    searchResult = regex.search(address)

    if searchResult != None:
        return True

    return False

# todo: complete this regex
netmaskRegex = None
