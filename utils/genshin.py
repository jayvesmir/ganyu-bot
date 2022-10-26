from logger import log

def UIDValidity(uid: str) -> str:
    uidLength = len(uid)
    if uidLength > 9 or uidLength < 9:
        return '0'
    if not uid[0] == '8' or not uid[0] == '7' or not uid[0] == '6':
        return '0'
    return '1'

def validateUID(uid: str) -> str:
    """
    Returns a string representing the UID.
    v - validity (0/1) If the UID is valid.
    r - region (0-3) Where the UID is registered.
    e - exists (0/1) If the account exists.
    """
    r = 'vre'
    r[0] = UIDValidity(uid)
    log('UID').info(r)