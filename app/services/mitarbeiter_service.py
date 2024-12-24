from app.models.mitarbeiter import Mitarbeiter


class MitarbeiterService:
    @staticmethod
    def get_all_mitarbeiter():
        return Mitarbeiter.get_all()

    @staticmethod
    def create_mitarbeiter(name, vorname, abteilung, arbeitspensum, moegliche_funktionen):
        mitarbeiter = Mitarbeiter(name, vorname, abteilung, arbeitspensum, moegliche_funktionen)
        mitarbeiter.save()
