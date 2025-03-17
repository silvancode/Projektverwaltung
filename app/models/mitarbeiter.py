from config.database import create_connection


class Mitarbeiter:
    def __init__(self, name, vorname, abteilung, arbeitspensum, moegliche_funktionen, personalnummer=None):
        self.personalnummer = personalnummer
        self.name = name
        self.vorname = vorname
        self.abteilung = abteilung
        self.arbeitspensum = arbeitspensum
        self.moegliche_funktionen = moegliche_funktionen

    def save(self):
        connection = create_connection()
        cursor = connection.cursor()
        query = """
        INSERT INTO MITARBEITER (Name, Vorname, Abteilung, Arbeitspensum, MoeglicheFunktionen)
        VALUES (%s, %s, %s, %s, %s)
        """
        data = (self.name, self.vorname, self.abteilung, self.arbeitspensum, self.moegliche_funktionen)
        cursor.execute(query, data)
        connection.commit()
        cursor.close()
        connection.close()

    @staticmethod
    def get_all():
        connection = create_connection()
        if connection:
            cursor = connection.cursor(dictionary=True)
            cursor.execute("SELECT * FROM mitarbeiter")
            result = cursor.fetchall()
            cursor.close()
            connection.close()
            return result

    @staticmethod
    def get_by_id(mitarbeiter_id):
        connection = create_connection()
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM mitarbeiter WHERE Personalnummer = %s", (mitarbeiter_id,))
        result = cursor.fetchone()
        cursor.close()
        connection.close()
        if result:
            return Mitarbeiter(
                name=result["Name"],
                vorname=result["Vorname"],
                abteilung=result["Abteilung"],
                arbeitspensum=result["Arbeitspensum"],
                moegliche_funktionen=result["MoeglicheFunktionen"],
                personalnummer=result["Personalnummer"]
            )
        return None

    def update(self):
        connection = create_connection()
        cursor = connection.cursor()
        query = """
        UPDATE mitarbeiter
        SET Name = %s, Vorname = %s, Abteilung = %s, Arbeitspensum = %s, MoeglicheFunktionen = %s
        WHERE Personalnummer = %s
        """
        data = (self.name, self.vorname, self.abteilung, self.arbeitspensum, self.moegliche_funktionen, self.personalnummer)
        cursor.execute(query, data)
        connection.commit()
        cursor.close()
        connection.close()

    @staticmethod
    def delete(mitarbeiter_id):
        connection = create_connection()
        cursor = connection.cursor()
        cursor.execute("DELETE FROM mitarbeiter WHERE Personalnummer = %s", (mitarbeiter_id,))
        connection.commit()
        cursor.close()
        connection.close()
