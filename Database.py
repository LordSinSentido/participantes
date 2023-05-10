import sqlite3


class Database:
    def __init__(self, database):
        self.database = database

    def connect(self):
        if self.database:
            try:
                connection = sqlite3.connect(self.database)
            except Exception as e:
                return Exception(e)

            return connection
        else:
            return None

    def getUsers(self):
        try:
            database = self.connect()
            cursor = database.cursor()
            result = cursor.execute(
                "SELECT * FROM users ORDER BY first_name DESC")
            database.commit()
        except Exception as e:
            if database:
                database.close()
            print(e)
            result = None
        finally:
            return result

    def postUser(self, data):
        try:
            database = self.connect()
            cursor = database.cursor()
            result = cursor.execute(
                "INSERT INTO users VALUES(NULL, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", data)
            database.commit()
        except Exception as e:
            if database:
                database.close()

            print(e)
        finally:
            pass
