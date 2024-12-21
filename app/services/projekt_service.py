from app.models.projekt import Projekt


def create_projekt(referenz, titel, beschreibung, startdatum, enddatum, projektleiter):
    projekt = Projekt(referenz, titel, beschreibung, startdatum, enddatum, projektleiter)
    projekt.save()


def get_alle_projekte():
    return Projekt.get_all()
