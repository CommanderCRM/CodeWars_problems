def is_valid_IP(strng):
    octets = strng.split('.')
    if len(octets) != 4:
        return False
    for octet in octets:
        if not octet.isdigit():
            return False
        if len(octet) > 1 and octet[0] == '0':
            return False
        if int(octet) < 0 or int(octet) > 255:
            return False
    return True
