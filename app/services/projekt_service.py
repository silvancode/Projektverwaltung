from app.models.projekt import Projekt


def create_projekt(projekttitel, beschreibung, bewilligungsdatum, prioritaet, status,
                   startdatum_geplant, enddatum_geplant, projektleiter_id, vorgehensmodell, fortschritt):
    projekt = Projekt(projekttitel, beschreibung, bewilligungsdatum, prioritaet, status,
                      startdatum_geplant, enddatum_geplant, projektleiter_id, vorgehensmodell, fortschritt)
    projekt.save()


def get_alle_projekte():
    return Projekt.get_all()
