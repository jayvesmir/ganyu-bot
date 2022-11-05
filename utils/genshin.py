from enkapy import Enka, UIDNotFounded
from logger import log

def UIDValidity(uid: str) -> str:
    if len(uid) != 9:
        return False
    if uid[0] != '9' and uid[0] != '8' and uid[0] != '7' and uid[0] != '6' and uid[0] != '5' and uid[0] != '2' and uid[0] != '1':
        return False
    if 100000000 > int(uid) > 999999999:
        return False
    return True

def UIDRegion(uid: str) -> str:
    if len(uid) != 9:
        return 'None'
    if uid[0] == '9':
        return 'SAR'
    elif uid[0] == '8':
        return 'Asia'
    elif uid[0] == '7':
        return 'Europe'
    elif uid[0] == '6':
        return 'North America'
    elif uid[0] == '5':
        return '世界树 (Mainland China - Irminsul)'
    elif uid[0] == '1' or uid[0] == '2':
        return '天空岛 (Mainland China - Celestia)'
    return True

async def UIDExists(uid: int) -> bool:
    if not UIDValidity(str(uid)):
        return False
    try:
        client = Enka()
        await client.fetch_user(uid)
    except UIDNotFounded:
        return False
    return True

def UIDCreationRank(uid: str) -> str:
    raw = uid[-8:]
    i = 0
    for d in raw:
        if d == '0':
            i += 1
    raw = raw[-(8-i):]
    raw = format(int(raw), ',')
        
    if raw[-1:] == '1':
        raw += 'st'
    elif raw[-1:] == '2':
        raw += 'nd'
    elif raw[-1:] == '3':
        raw += 'rd'
    else:
        raw += 'th'
    return raw

async def validateUID(uid: str) -> list:
    """
    Returns a list representing the validity of the UID.
    [0] - validity (bool) If the UID is valid.
    [1] - region (0-3) Where the UID is registered.
    [2] - exists (bool) If the account exists.
    [3] - account creation rank (8-digit number signifying when the account was created.)
    """
    r = [False, 'r', True, '00000000']
    r[0] = UIDValidity(uid)
    r[1] = UIDRegion(uid)
    r[2] = await UIDExists(int(uid))
    r[3] = UIDCreationRank(uid)
    log('UID').info(r)
    return r