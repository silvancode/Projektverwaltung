from app.controllers.projekt_controller import handle_create_projekt, handle_list_projekte


def main():
    while True:
        print("\nProjektverwaltung")
        print("1. Neues Projekt erstellen")
        print("2. Alle Projekte anzeigen")
        print("3. Beenden")

        choice = input("Wähle eine Option: ")

        if choice == '1':
            handle_create_projekt()
        elif choice == '2':
            handle_list_projekte()
        elif choice == '3':
            break
        else:
            print("Ungültige Eingabe.")


if __name__ == "__main__":
    main()
