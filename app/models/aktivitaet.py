from config.database import create_connection


class Aktivitaet:
    def __init__(self, phasen_id, verantwortliche_person_id, startdatum, enddatum, fortschritt):
        self.phasen_id = phasen_id
        self.verantwortliche_person_id = verantwortliche_person_id
        self.startdatum = startdatum
        self.enddatum = enddatum
        self.fortschritt = fortschritt

    def save(self):
        connection = create_connection()
        cursor = connection.cursor()
        query = """
        INSERT INTO AKTIVITAET (Phasen_ID, VerantwortlichePerson_ID, Startdatum_geplant, Enddatum_geplant, Aktivitaetsfortschritt)
        VALUES (%s, %s, %s, %s, %s)
        """
        data = (self.phasen_id, self.verantwortliche_person_id, self.startdatum, self.enddatum, self.fortschritt)
        cursor.execute(query, data)
        connection.commit()
        cursor.close()
        connection.close()

    @staticmethod
    def get_all():
        connection = create_connection()
        if connection:
            cursor = connection.cursor(dictionary=True)
            cursor.execute("SELECT * FROM aktivitaet")
            result = cursor.fetchall()
            cursor.close()
            connection.close()
            return result


class ExterneKosten:
    def __init__(self, aktivitaet_id, kostenart, budgetkosten, effektivekosten):
        self.aktivitaet_id = aktivitaet_id
        self.kostenart = kostenart
        self.budgetkosten = budgetkosten
        self.effektivekosten = effektivekosten

    def save(self):
        connection = create_connection()
        cursor = connection.cursor()
        query = """
        INSERT INTO EXTERNEKOSTEN (Aktivitaet_ID, Kostenart, Budgetkosten, EffektiveKosten)
        VALUES (%s, %s, %s, %s)
        """
        data = (self.aktivitaet_id, self.kostenart, self.budgetkosten, self.effektivekosten)
        cursor.execute(query, data)
        connection.commit()
        cursor.close()
        connection.close()

    @staticmethod
    def get_all():
        connection = create_connection()
        if connection:
            cursor = connection.cursor(dictionary=True)
            cursor.execute("SELECT * FROM externekosten")
            result = cursor.fetchall()
            cursor.close()
            connection.close()
            return result
