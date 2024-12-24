from config.database import create_connection


class Projektphase:
    def __init__(self, projekt_id, startdatum_geplant, enddatum_geplant, status, fortschritt):
        self.projekt_id = projekt_id
        self.startdatum_geplant = startdatum_geplant
        self.enddatum_geplant = enddatum_geplant
        self.status = status
        self.fortschritt = fortschritt

    def save(self):
        connection = create_connection()
        cursor = connection.cursor()
        query = """
        INSERT INTO PROJEKTPHASE (Projekt_ID, Startdatum_geplant, Enddatum_geplant, Phasenstatus, Phasenfortschritt)
        VALUES (%s, %s, %s, %s, %s)
        """
        data = (self.projekt_id, self.startdatum_geplant, self.enddatum_geplant, self.status, self.fortschritt)
        cursor.execute(query, data)
        connection.commit()
        cursor.close()
        connection.close()

    @staticmethod
    def get_all():
        connection = create_connection()
        if connection:
            cursor = connection.cursor(dictionary=True)
            cursor.execute("SELECT * FROM projektphase")
            result = cursor.fetchall()
            cursor.close()
            connection.close()
            return result
