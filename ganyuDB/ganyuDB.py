import sqlite3 as sqlite
from logger import log
import os

DB_PATH = 'ganyuDB/db/users.db'

def dbExists(path: str) -> bool:
    try:
        os.makedirs(os.path.dirname(path))
        log('DB').info('Created db folder.')
    except OSError:
        pass
    return os.path.exists(path)

def userExists(_id: str, _uid: str) -> int:
    db = sqlite.connect(DB_PATH)
    c = db.cursor()
    
    c.execute(f'SELECT * FROM users WHERE id = :id', {'id', _id})
    val = c.fetchall()
    numEntries = len(val)
    if numEntries > 0:
        return 1
    
    c.execute('SELECT * FROM users WHERE uid = :uid', {'uid': _uid})
    val = c.fetchall()
    numEntries = len(val)
    if numEntries > 0:
        return 2
    
    return 0

def userExistsVerbose(_id, _uid: str) -> tuple:
    db = sqlite.connect(DB_PATH)
    c = db.cursor()
    
    _id = False
    _uid = False
    
    c.execute(f'SELECT * FROM users WHERE id = :id', {'id', _id})
    val = c.fetchall()
    numEntries = len(val)
    if numEntries > 0:
        _id = True
    
    c.execute('SELECT * FROM users WHERE uid = :uid', {'uid': _uid})
    val = c.fetchall()
    numEntries = len(val)
    if numEntries > 0:
        _uid = True

    return (_id, _uid)

class UID:
    pass

class ganyuDB:
    
    def getUID(_id: str) -> str:
        db = sqlite.connect(DB_PATH)
        c = db.cursor()
        c.execute('SELECT uid FROM users WHERE id = :id', {'id', _id})
        try:
            return c.fetchall()[-1]
        except IndexError:
            return (None,)
    
    def getID(_uid: str) -> str:
        db = sqlite.connect(DB_PATH)
        c = db.cursor()
        c.execute(f'SELECT id FROM users WHERE uid = :uid', {'uid', _uid})
        try:
            return c.fetchall()[-1]
        except IndexError:
            return (None,)
        
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
            
        c.execute('INSERT INTO users VALUES (?, ?)', (id, uid))
        db.commit()
        
        c.execute('SELECT * FROM users WHERE id = :id', {'id': id})
        
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
            c.execute('INSERT INTO users VALUES (?, ?)', (id, uid))
            db.commit()
            return 0
        elif not e[0] and e[1]:
            return 2
        
        __uid = ganyuDB.getUID(id)[0] if not e[0] else None
        c.execute('UPDATE users SET uid = :uid WHERE id = :id', {'id': id, 'uid': uid})
        db.commit()
        
        c.execute('SELECT * FROM users WHERE id = :id', {'id': id})
        
        user = c.fetchall()[-1]
        _id = user[0]
        _uid = user[1]
        log('DB').info(f'Updated user: {_id}, {__uid} - {_uid}')

        db.close()
        return 0
    
    def removeUser(id: str) -> int:
        """
        Error Codes:
            0 - no error
            2 - nothing to delete
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
            
        e = userExistsVerbose(id, ganyuDB.getUID(id)[0])
        if not e[0] and not e[1]:
            return 2
        
        __uid = ganyuDB.getUID(id)[0]
        c.execute('DELETE FROM users WHERE id = :id', {'id': id})
        db.commit()
        
        log('DB').info(f'Deleted user: {id}, {__uid}')

        db.close()
        return 0