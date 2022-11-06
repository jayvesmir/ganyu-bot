import os
import sqlite3 as sqlite

from logger import log

DB_PATH = 'ganyuDB/db/users.db'

class ganyuDB:
    def __init__(self, userDB: sqlite.Connection):
        self.userDB = userDB

    @staticmethod
    def dbExists(path: str) -> bool:
        try:
            os.makedirs(os.path.dirname(path))
            log('DB').info('Created db folder.')
        except OSError:
            pass
        return os.path.exists(path)

    def getUID(self, _id: str) -> str:
        c = self.userDB.cursor()
        c.execute('SELECT uid FROM users WHERE id = :id', {"id": _id})
        try:
            return c.fetchall()[-1]
        except IndexError:
            return (None,)

    def getID(self, _uid: str) -> str:
        c = self.userDB.cursor()
        c.execute('SELECT id FROM users WHERE uid = :uid', {"uid": _uid})
        try:
            return c.fetchall()[-1]
        except IndexError:
            return (None,)

    def userExists(self, _id: str, _uid: str) -> int:
        c = self.userDB.cursor()

        c.execute('SELECT * FROM users WHERE id = :id', {"id": _id})
        val = c.fetchall()
        numEntries = len(val)
        if numEntries > 0:
            return 1

        c.execute('SELECT * FROM users WHERE uid = :uid', {"uid": _uid})
        val = c.fetchall()
        numEntries = len(val)
        if numEntries > 0:
            return 2

        return 0

    def userExistsVerbose(self, _id: str, _uid: str) -> tuple:
        c = self.userDB.cursor()

        id = False
        uid = False

        c.execute('SELECT * FROM users WHERE id = :id', {"id": _id})
        val = c.fetchall()
        numEntries = len(val)
        if numEntries > 0:
            id = True

        c.execute('SELECT * FROM users WHERE uid = :uid', {"uid": _uid})
        val = c.fetchall()
        numEntries = len(val)
        if numEntries > 0:
            uid = True

        return (id, uid)

    def createUser(self, _id: str, _uid: str) -> int:
        """
        Error Codes:
            0 - no error
            1 - id registered
            2 - uid registered
        """
        c = self.userDB.cursor()

        e = self.userExists(_id, _uid)
        if e > 0:
            return e

        c.execute('INSERT INTO users VALUES (?, ?)', (_id, _uid))
        self.userDB.commit()

        c.execute('SELECT * FROM users WHERE id = :id', {"id": _id})

        user = c.fetchall()[-1]
        _id = user[0]
        _uid = user[1]
        log('DB').info(f'Created user: {_id}, {_uid}')

        return 0

    def updateUser(self, _id: str, _uid: str) -> int:
        """
        Error Codes:
            0 - no error
            2 - uid registered
            3 - db error
        """
        c = self.userDB.cursor()

        e = self.userExistsVerbose(_id, _uid)
        if e[0] and e[1]:
            return 2
        elif not e[0] and not e[1]:
            c.execute('INSERT INTO users VALUES (?, ?)', (_id, _uid))
            self.userDB.commit()
            return 0
        elif not e[0] and e[1]:
            return 2

        __uid = self.getUID(_id)[0] if not e[0] else None
        self.removeUser(_id)
        c.execute('INSERT INTO users VALUES (?, ?)', (_id, _uid))
        self.userDB.commit()

        c.execute('SELECT * FROM users WHERE id = :id', {"id": _id})

        user = c.fetchall()[-1]
        _id = user[0]
        _uid = user[1]
        log('DB').info(f'Updated user: {_id}, {__uid} - {_uid}')

        return 0

    def removeUser(self, _id: str) -> int:
        """
        Error Codes:
            0 - no error
            2 - nothing to delete
            3 - db error
        """
        c = self.userDB.cursor()

        e = self.userExistsVerbose(_id, self.getUID(_id)[0])
        if not e[0] and not e[1]:
            return 2

        __uid = self.getUID(_id)[0]
        c.execute('DELETE FROM users WHERE id = :id', {"id": _id})
        self.userDB.commit()

        log('DB').info(f'Deleted user: {_id}, {__uid}')

        return 0
