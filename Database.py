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

    def searchUsers(self, data):
        try:
            database = self.connect()
            cursor = database.cursor()
            result = cursor.execute(
                f"SELECT * FROM users WHERE (first_name LIKE \"{data}\" OR first_last_name LIKE \"{data}\" OR second_last_name LIKE \"{data}\") ORDER BY first_name DESC")
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
            return True
        except Exception as e:
            if database:
                database.close()
            print(e)
            return False

    def patchUser(self, data):
        try:
            database = self.connect()
            cursor = database.cursor()
            result = cursor.execute(
                "UPDATE users SET first_name = ?, first_last_name = ?, second_last_name = ?, age = ?, gender = ?, school = ?, address = ?, curp = ?, category = ?, fee = ? WHERE id = ?", data)
            database.commit()
            return True
        except Exception as e:
            if database:
                database.close()
            print(e)
            return False

    def deleteUser(self, identifier):
        try:
            database = self.connect()
            cursor = database.cursor()
            result = cursor.execute(
                f"DELETE FROM users WHERE id = \"{identifier}\"")
            database.commit()
            return True
        except Exception as e:
            if database:
                database.close()
            print(e)
            return False
