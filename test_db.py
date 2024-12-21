from config.database import create_connection


def test_connection():
    connection = create_connection()
    if connection:
        print("Verbindung erfolgreich!")
    else:
        print("Verbindung fehlgeschlagen.")


if __name__ == "__main__":
    test_connection()
