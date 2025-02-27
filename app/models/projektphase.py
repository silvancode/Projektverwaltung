from config.database import create_connection


class Projektphase:
    def __init__(self, projekt_id, phasenname, startdatum_geplant, enddatum_geplant,
                 startdatum_effektiv=None, enddatum_effektiv=None,
                 reviewdatum_geplant=None, reviewdatum_effektiv=None,
                 freigabedatum=None, freigabevisum=None,
                 phasenstatus=None, phasenfortschritt=0,
                 phasendokumente=None, phasen_id=None):
        self.phasen_id = phasen_id
        self.projekt_id = projekt_id
        self.phasenname = phasenname
        self.startdatum_geplant = startdatum_geplant
        self.enddatum_geplant = enddatum_geplant
        self.startdatum_effektiv = startdatum_effektiv
        self.enddatum_effektiv = enddatum_effektiv
        self.reviewdatum_geplant = reviewdatum_geplant
        self.reviewdatum_effektiv = reviewdatum_effektiv
        self.freigabedatum = freigabedatum
        self.freigabevisum = freigabevisum
        self.phasenstatus = phasenstatus
        self.phasenfortschritt = phasenfortschritt
        self.phasendokumente = phasendokumente

    def save(self):
        connection = create_connection()
        cursor = connection.cursor()
        query = """
        INSERT INTO PROJEKTPHASE (Projekt_ID, Phasenname, Startdatum_geplant, Enddatum_geplant, Startdatum_effektiv,
                                  Enddatum_effektiv, Reviewdatum_geplant, Reviewdatum_effektiv,
                                  Freigabedatum, Freigabevisum, Phasenstatus, Phasenfortschritt, Phasendokumente)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        data = (self.projekt_id, self.phasenname, self.startdatum_geplant, self.enddatum_geplant,
                self.startdatum_effektiv, self.enddatum_effektiv,
                self.reviewdatum_geplant, self.reviewdatum_effektiv,
                self.freigabedatum, self.freigabevisum,
                self.phasenstatus, self.phasenfortschritt, self.phasendokumente)
        cursor.execute(query, data)
        connection.commit()
        cursor.close()
        connection.close()

    @staticmethod
    def get_all():
        connection = create_connection()
        cursor = connection.cursor(dictionary=True)
        query = "SELECT * FROM PROJEKTPHASE"
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()
        connection.close()

        return [Projektphase(
            projekt_id=row["Projekt_ID"],
            phasenname=row["Phasenname"],
            phasen_id=row["Phasen_ID"],
            startdatum_geplant=row["Startdatum_geplant"],
            enddatum_geplant=row["Enddatum_geplant"],
            startdatum_effektiv=row["Startdatum_effektiv"],
            enddatum_effektiv=row["Enddatum_effektiv"],
            reviewdatum_geplant=row["Reviewdatum_geplant"],
            reviewdatum_effektiv=row["Reviewdatum_effektiv"],
            freigabedatum=row["Freigabedatum"],
            freigabevisum=row["Freigabevisum"],
            phasenstatus=row["Phasenstatus"],
            phasenfortschritt=row["Phasenfortschritt"],
            phasendokumente=row["Phasendokumente"]
        ) for row in result]

    @staticmethod
    def get_by_id(phasen_id):
        connection = create_connection()
        cursor = connection.cursor(dictionary=True)
        query = "SELECT * FROM PROJEKTPHASE WHERE Phasen_ID = %s"
        cursor.execute(query, (phasen_id,))
        result = cursor.fetchone()
        cursor.close()
        connection.close()

        if result:
            return Projektphase(
                projekt_id=result["Projekt_ID"],
                phasenname=result["Phasenname"],
                phasen_id=result["Phasen_ID"],
                startdatum_geplant=result["Startdatum_geplant"],
                enddatum_geplant=result["Enddatum_geplant"],
                startdatum_effektiv=result["Startdatum_effektiv"],
                enddatum_effektiv=result["Enddatum_effektiv"],
                reviewdatum_geplant=result["Reviewdatum_geplant"],
                reviewdatum_effektiv=result["Reviewdatum_effektiv"],
                freigabedatum=result["Freigabedatum"],
                freigabevisum=result["Freigabevisum"],
                phasenstatus=result["Phasenstatus"],
                phasenfortschritt=result["Phasenfortschritt"],
                phasendokumente=result["Phasendokumente"]
            )
        return None

    def update(self):
        connection = create_connection()
        cursor = connection.cursor()
        query = """
        UPDATE PROJEKTPHASE
        SET Projekt_ID = %s, Phasenname = %s, Startdatum_geplant = %s, Enddatum_geplant = %s, Startdatum_effektiv = %s,
            Enddatum_effektiv = %s, Reviewdatum_geplant = %s, Reviewdatum_effektiv = %s,
            Freigabedatum = %s, Freigabevisum = %s, Phasenstatus = %s, Phasenfortschritt = %s,
            Phasendokumente = %s
        WHERE Phasen_ID = %s
        """
        data = (self.projekt_id, self.phasenname, self.startdatum_geplant, self.enddatum_geplant, self.startdatum_effektiv,
                self.enddatum_effektiv, self.reviewdatum_geplant, self.reviewdatum_effektiv,
                self.freigabedatum, self.freigabevisum, self.phasenstatus,
                self.phasenfortschritt, self.phasendokumente, self.phasen_id)
        cursor.execute(query, data)
        connection.commit()
        cursor.close()
        connection.close()

    @staticmethod
    def delete(phasen_id):
        connection = create_connection()
        cursor = connection.cursor()
        query = "DELETE FROM PROJEKTPHASE WHERE Phasen_ID = %s"
        cursor.execute(query, (phasen_id,))
        connection.commit()
        cursor.close()
        connection.close()
