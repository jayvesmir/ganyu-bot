from logger import log
import genshin

def UIDValidity(uid: str) -> str:
    uidLength = len(uid)
    if uidLength != 9:
        return False
    if uid[0] != '9' and uid[0] != '8' and uid[0] != '7' and uid[0] != '6':
        return False
    return True

def UIDRegion(uid: str) -> str:
    uidLength = len(uid)
    if uidLength != 9:
        return 'None'
    if uid[0] == '9':
        return 'SAR'
    elif uid[0] == '8':
        return 'Asia'
    elif uid[0] == '7':
        return 'Europe'
    elif uid[0] == '6':
        return 'North America'
    return True

def validateUID(uid: str) -> list:
    """
    Returns a list representing the validity of the UID.
    [0] - validity (bool) If the UID is valid.
    [1] - region (0-3) Where the UID is registered.
    [2] - exists (bool) If the account exists.
    [3] - account creation (8-digit number)
    """
    r = [False, 'r', True, '00000000']
    r[0] = UIDValidity(uid)
    r[1] = UIDRegion(uid)
    log('UID').info(r)
    return r