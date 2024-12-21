from config.database import create_connection


class Projekt:
    def __init__(self, referenz, titel, beschreibung, startdatum, enddatum, projektleiter):
        self.referenz = referenz
        self.titel = titel
        self.beschreibung = beschreibung
        self.startdatum = startdatum
        self.enddatum = enddatum
        self.projektleiter = projektleiter

    def save(self):
        connection = create_connection()
        if connection:
            cursor = connection.cursor()
            query = """
            INSERT INTO projekte (referenz, titel, beschreibung, startdatum, enddatum, projektleiter)
            VALUES (%s, %s, %s, %s, %s, %s)
            """
            data = (self.referenz, self.titel, self.beschreibung, self.startdatum, self.enddatum, self.projektleiter)
            cursor.execute(query, data)
            connection.commit()
            cursor.close()
            connection.close()
            print("Projekt erfolgreich gespeichert.")

    @staticmethod
    def get_all():
        connection = create_connection()
        if connection:
            cursor = connection.cursor(dictionary=True)
            cursor.execute("SELECT * FROM projekte")
            result = cursor.fetchall()
            cursor.close()
            connection.close()
            return result
