from app.services.projekt_service import create_projekt, get_alle_projekte


def handle_create_projekt():
    referenz = input("Projekt-Referenz: ")
    titel = input("Projekttitel: ")
    beschreibung = input("Beschreibung: ")
    startdatum = input("Startdatum (YYYY-MM-DD): ")
    enddatum = input("Enddatum (YYYY-MM-DD): ")
    projektleiter = input("Projektleiter: ")

    create_projekt(referenz, titel, beschreibung, startdatum, enddatum, projektleiter)


def handle_list_projekte():
    projekte = get_alle_projekte()
    for projekt in projekte:
        print(f"{projekt['referenz']} - {projekt['titel']}: {projekt['beschreibung']}")
