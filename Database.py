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
                "SELECT * FROM users WHERE (first_name LIKE ? OR first_last_name LIKE ? OR second_last_name LIKE ?) ORDER BY first_name DESC", data)
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

    def deleteUser(self, item):
        try:
            database = self.connect()
            cursor = database.cursor()
            result = cursor.execute(
                "DELETE FROM users WHERE id = ?", item)
            database.commit()
            return True
        except Exception as e:
            if database:
                database.close()
            print(e)
            return False
