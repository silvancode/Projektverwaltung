from config.database import create_connection


class Meilenstein:
    def __init__(self, projekt_id, bezeichnung, geplantes_datum, status):
        self.projekt_id = projekt_id
        self.bezeichnung = bezeichnung
        self.geplantes_datum = geplantes_datum
        self.status = status

    def save(self):
        connection = create_connection()
        cursor = connection.cursor()
        query = """
        INSERT INTO MEILENSTEIN (Projekt_ID, Bezeichnung, GeplantesDatum, Status)
        VALUES (%s, %s, %s, %s)
        """
        data = (self.projekt_id, self.bezeichnung, self.geplantes_datum, self.status)
        cursor.execute(query, data)
        connection.commit()
        cursor.close()
        connection.close()

    @staticmethod
    def get_all():
        connection = create_connection()
        if connection:
            cursor = connection.cursor(dictionary=True)
            cursor.execute("SELECT * FROM meilenstein")
            result = cursor.fetchall()
            cursor.close()
            connection.close()
            return result
