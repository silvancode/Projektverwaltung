from config.database import create_connection


class Projekt:
    def __init__(self, projekttitel, beschreibung, bewilligungsdatum, prioritaet, status,
                 startdatum_geplant, enddatum_geplant, projektleiter_id, vorgehensmodell,
                 fortschritt, projektleiter_name=None, projektleiter_vorname=None, projekt_id=None):
        self.projekt_id = projekt_id
        self.projekttitel = projekttitel
        self.beschreibung = beschreibung
        self.bewilligungsdatum = bewilligungsdatum
        self.prioritaet = prioritaet
        self.status = status
        self.startdatum_geplant = startdatum_geplant
        self.enddatum_geplant = enddatum_geplant
        self.projektleiter_id = projektleiter_id
        self.projektleiter_name = projektleiter_name
        self.projektleiter_vorname = projektleiter_vorname
        self.vorgehensmodell = vorgehensmodell
        self.fortschritt = fortschritt

    def save(self):
        connection = create_connection()
        cursor = connection.cursor()
        query = """
        INSERT INTO PROJEKT (Projekttitel, Projektbeschreibung, Bewilligungsdatum, Prioritaet, Status,
                             Startdatum_geplant, Enddatum_geplant, Projektleiter_ID, Vorgehensmodell, Projektfortschritt)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        data = (self.projekttitel, self.beschreibung, self.bewilligungsdatum, self.prioritaet, self.status,
                self.startdatum_geplant, self.enddatum_geplant, self.projektleiter_id, self.vorgehensmodell, self.fortschritt)
        cursor.execute(query, data)
        connection.commit()
        cursor.close()
        connection.close()

    @staticmethod
    def get_all():
        connection = create_connection()
        cursor = connection.cursor(dictionary=True)
        query = """
                SELECT p.*, m.Name AS projektleiter_name, m.Vorname AS projektleiter_vorname
                FROM PROJEKT p
                LEFT JOIN MITARBEITER m ON p.Projektleiter_ID = m.Personalnummer
                """
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()
        connection.close()

        return [Projekt(
            projekt_id=row["Projektreferenz"],
            projekttitel=row["Projekttitel"],
            beschreibung=row["Projektbeschreibung"],
            bewilligungsdatum=row["Bewilligungsdatum"],
            prioritaet=row["Prioritaet"],
            status=row["Status"],
            startdatum_geplant=row["Startdatum_geplant"],
            enddatum_geplant=row["Enddatum_geplant"],
            projektleiter_id=row["Projektleiter_ID"],
            projektleiter_name=row["projektleiter_name"],
            projektleiter_vorname=row["projektleiter_vorname"],
            vorgehensmodell=row["Vorgehensmodell"],
            fortschritt=row["Projektfortschritt"]
        ) for row in result]

    @staticmethod
    def get_by_id(projekt_id):
        connection = create_connection()
        cursor = connection.cursor(dictionary=True)
        query = """
                SELECT p.*, m.Name AS projektleiter_name, m.Vorname AS projektleiter_vorname
                FROM PROJEKT p
                LEFT JOIN MITARBEITER m ON p.Projektleiter_ID = m.Personalnummer
                WHERE Projektreferenz = %s
                """
        cursor.execute(query, (projekt_id,))
        result = cursor.fetchone()
        cursor.close()
        connection.close()
        if result:
            return Projekt(
                projekt_id=result["Projektreferenz"],
                projekttitel=result["Projekttitel"],
                beschreibung=result["Projektbeschreibung"],
                bewilligungsdatum=result["Bewilligungsdatum"],
                prioritaet=result["Prioritaet"],
                status=result["Status"],
                startdatum_geplant=result["Startdatum_geplant"],
                enddatum_geplant=result["Enddatum_geplant"],
                projektleiter_id=result["Projektleiter_ID"],
                projektleiter_name=result["projektleiter_name"],
                projektleiter_vorname=result["projektleiter_vorname"],
                vorgehensmodell=result["Vorgehensmodell"],
                fortschritt=result["Projektfortschritt"]
            )
        return None

    def update(self):
        connection = create_connection()
        cursor = connection.cursor()
        query = """
        UPDATE PROJEKT
        SET Projekttitel = %s, Projektbeschreibung = %s, Bewilligungsdatum = %s, Prioritaet = %s, Status = %s,
            Startdatum_geplant = %s, Enddatum_geplant = %s, Projektleiter_ID = %s, Vorgehensmodell = %s,
            Projektfortschritt = %s
        WHERE Projektreferenz = %s
        """
        data = (self.projekttitel, self.beschreibung, self.bewilligungsdatum, self.prioritaet, self.status,
                self.startdatum_geplant, self.enddatum_geplant, self.projektleiter_id, self.vorgehensmodell,
                self.fortschritt, self.projekt_id)
        cursor.execute(query, data)
        connection.commit()
        cursor.close()
        connection.close()

    @staticmethod
    def delete(projekt_id):
        connection = create_connection()
        cursor = connection.cursor()
        cursor.execute("DELETE FROM PROJEKT WHERE Projektreferenz = %s", (projekt_id,))
        connection.commit()
        cursor.close()
        connection.close()
