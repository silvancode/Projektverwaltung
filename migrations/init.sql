CREATE DATABASE IF NOT EXISTS projektverwaltung_db;

USE projektverwaltung_db;

CREATE TABLE IF NOT EXISTS projekte (
    id INT AUTO_INCREMENT PRIMARY KEY,
    referenz VARCHAR(50) NOT NULL,
    titel VARCHAR(100) NOT NULL,
    beschreibung TEXT,
    startdatum DATE,
    enddatum DATE,
    projektleiter VARCHAR(100)
);
