from config.database import create_connection

class Aktivitaet:
    def __init__(self, name, beschreibung, startdatum, enddatum, verantwortlicher_id,
                 budget, effektive_kosten, pensum, projektphase_id, aktivitaet_id=None):
        self.aktivitaet_id = aktivitaet_id
        self.name = name
        self.beschreibung = beschreibung
        self.startdatum = startdatum
        self.enddatum = enddatum
        self.verantwortlicher_id = verantwortlicher_id
        self.budget = budget
        self.effektive_kosten = effektive_kosten
        self.pensum = pensum
        self.projektphase_id = projektphase_id

    def save(self):
        """
        Neue Aktivität in der Datenbank speichern.
        """
        connection = create_connection()
        cursor = connection.cursor()
        query = """
        INSERT INTO AKTIVITAET 
        (Name, Beschreibung, Startdatum, Enddatum, Verantwortlicher_ID, Budget, EffektiveKosten, Pensum, Projektphase_ID)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        data = (self.name, self.beschreibung, self.startdatum, self.enddatum,
                self.verantwortlicher_id, self.budget, self.effektive_kosten,
                self.pensum, self.projektphase_id)
        cursor.execute(query, data)
        connection.commit()
        cursor.close()
        connection.close()

    @staticmethod
    def get_all():
        """
        Alle Aktivitäten aus der Datenbank abrufen.
        """
        connection = create_connection()
        cursor = connection.cursor(dictionary=True)
        query = """
        SELECT *
        FROM AKTIVITAET
        """
        cursor.execute(query)
        rows = cursor.fetchall()
        cursor.close()
        connection.close()

        aktivitaeten = []
        for row in rows:
            aktivitaeten.append(Aktivitaet(
                aktivitaet_id=row["AktivitaetID"],
                name=row["Name"],
                beschreibung=row["Beschreibung"],
                startdatum=row["Startdatum"],
                enddatum=row["Enddatum"],
                verantwortlicher_id=row["Verantwortlicher_ID"],
                budget=row["Budget"],
                effektive_kosten=row["EffektiveKosten"],
                pensum=row["Pensum"],
                projektphase_id=row["Projektphase_ID"]
            ))
        return aktivitaeten

    @staticmethod
    def get_by_id(aktivitaet_id):
        """
        Eine bestimmte Aktivität anhand ihrer ID abrufen.
        """
        connection = create_connection()
        cursor = connection.cursor(dictionary=True)
        query = """
        SELECT *
        FROM AKTIVITAET
        WHERE AktivitaetID = %s
        """
        cursor.execute(query, (aktivitaet_id,))
        row = cursor.fetchone()
        cursor.close()
        connection.close()

        if row:
            return Aktivitaet(
                aktivitaet_id=row["AktivitaetID"],
                name=row["Name"],
                beschreibung=row["Beschreibung"],
                startdatum=row["Startdatum"],
                enddatum=row["Enddatum"],
                verantwortlicher_id=row["Verantwortlicher_ID"],
                budget=row["Budget"],
                effektive_kosten=row["EffektiveKosten"],
                pensum=row["Pensum"],
                projektphase_id=row["Projektphase_ID"]
            )
        return None

    def update(self):
        """
        Bestehende Aktivität in der Datenbank aktualisieren.
        """
        connection = create_connection()
        cursor = connection.cursor()
        query = """
        UPDATE AKTIVITAET
        SET Name = %s, Beschreibung = %s, Startdatum = %s, Enddatum = %s,
            Verantwortlicher_ID = %s, Budget = %s, EffektiveKosten = %s,
            Pensum = %s, Projektphase_ID = %s
        WHERE AktivitaetID = %s
        """
        data = (self.name, self.beschreibung, self.startdatum, self.enddatum,
                self.verantwortlicher_id, self.budget, self.effektive_kosten,
                self.pensum, self.projektphase_id, self.aktivitaet_id)
        cursor.execute(query, data)
        connection.commit()
        cursor.close()
        connection.close()

    @staticmethod
    def delete(aktivitaet_id):
        """
        Eine Aktivität anhand ihrer ID löschen.
        """
        connection = create_connection()
        cursor = connection.cursor()
        query = """
        DELETE FROM AKTIVITAET
        WHERE AktivitaetID = %s
        """
        cursor.execute(query, (aktivitaet_id,))
        connection.commit()
        cursor.close()
        connection.close()
