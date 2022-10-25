import sqlite3 as sqlite
from logger import log
import genshin
import os

DB_PATH = 'ganyuDB/db/users.db'

def dbExists(path: str) -> bool:
    try:
        os.makedirs(os.path.dirname(path))
        log('DB').info('Created db folder.')
    except OSError:
        pass
    return os.path.exists(path)

def userExists(id: str, uid: str) -> int:
    db = sqlite.connect(DB_PATH)
    c = db.cursor()
    
    c.execute(f'SELECT * FROM users WHERE id = {id}')
    val = c.fetchall()
    numEntries = len(val)
    if numEntries > 0:
        return 1
    
    c.execute(f'SELECT * FROM users WHERE uid = {uid}')
    val = c.fetchall()
    numEntries = len(val)
    if numEntries > 0:
        return 2
    
    return 0

def userExistsVerbose(id, uid: str) -> tuple:
    db = sqlite.connect(DB_PATH)
    c = db.cursor()
    
    _id = False
    _uid = False
    
    c.execute(f'SELECT * FROM users WHERE id = {id}')
    val = c.fetchall()
    numEntries = len(val)
    if numEntries > 0:
        _id = True
    
    c.execute(f'SELECT * FROM users WHERE uid = {uid}')
    val = c.fetchall()
    numEntries = len(val)
    if numEntries > 0:
        _uid = True

    return (_id, _uid)

class UID:
    pass

class ganyuDB:
    
    def getUID(id: str) -> str:
        db = sqlite.connect(DB_PATH)
        c = db.cursor()
        c.execute(f'SELECT uid FROM users WHERE id = {id}')
        return c.fetchall()[-1]
    
    def getID(uid: str) -> str:
        db = sqlite.connect(DB_PATH)
        c = db.cursor()
        c.execute(f'SELECT id FROM users WHERE uid = {uid}')
        return c.fetchall()[-1]
        
    def createUser(id: str, uid: str) -> int:
        """
        Error Codes:
            0 - no error
            1 - id registered
            2 - uid registered
        """
        exists = dbExists(DB_PATH)
        open(DB_PATH, 'wb').close() if not exists else None
        db = sqlite.connect(DB_PATH)
        c = db.cursor()
        if not exists:
            c.execute('CREATE TABLE users (id text, uid text)')
            db.commit()
            
        e = userExists(id, uid)
        if e > 0:
            return e
            
        c.execute(f'INSERT INTO users VALUES ({id}, {uid})')
        db.commit()
        
        c.execute(f'SELECT * FROM users WHERE id = {id}')
        
        user = c.fetchall()[-1]
        _id = user[0]
        _uid = user[1]
        log('DB').info(f'Created user: {_id}, {_uid}')

        db.close()
        return 0
    
    def updateUser(id: str, uid: str) -> int:
        """
        Error Codes:
            0 - no error
            2 - uid registered
            3 - db error
        """
        exists = dbExists(DB_PATH)
        open(DB_PATH, 'wb').close() if not exists else None
        db = sqlite.connect(DB_PATH)
        c = db.cursor()
        if not exists:
            c.execute('CREATE TABLE users (id text, uid text)')
            db.commit()
            log('DB').error(f'Database error.')
            return 3
            
        e = userExistsVerbose(id, uid)
        if e[0] and e[1]:
            return 2
        elif not e[0] and not e[1]:
            c.execute(f'INSERT INTO users VALUES ({id}, {uid})')
            db.commit()
            return 0
        
        __uid = ganyuDB.getUID(id)[0]
        c.execute(f'UPDATE users SET uid = {uid} WHERE id = {id}')
        db.commit()
        
        c.execute(f'SELECT * FROM users WHERE id = {id}')
        
        user = c.fetchall()[-1]
        _id = user[0]
        _uid = user[1]
        log('DB').info(f'Updated user: {_id}, {__uid} - {_uid}')

        db.close()
        return 0