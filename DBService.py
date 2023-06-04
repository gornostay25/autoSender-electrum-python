import mysql.connector


class DBService:
    def __init__(self, host, user, password, database):
        self.connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.connection.cursor()

    def getAddresses(self):
        select_query = "SELECT 'yyyy'"
        self.cursor.execute(select_query)

        adrresses = self.cursor.fetchall()
        return adrresses
