-- =======================================
-- Init-Skript für MySQL
-- =======================================

-- ---------------------------------------
-- Datenbank erstellen / verwenden
-- ---------------------------------------
CREATE DATABASE IF NOT EXISTS projektverwaltung_db;
USE projektverwaltung_db;

-- ---------------------------------------
-- Alle Tabellen droppen (falls schon vorhanden)
-- ---------------------------------------
SET FOREIGN_KEY_CHECKS=0;
DROP TABLE IF EXISTS AKTIVITAET;
DROP TABLE IF EXISTS PROJEKTPHASE;
DROP TABLE IF EXISTS PROJEKT;
DROP TABLE IF EXISTS MITARBEITER;
SET FOREIGN_KEY_CHECKS=1;

-- ---------------------------------------
-- Tabelle: MITARBEITER
-- ---------------------------------------
CREATE TABLE MITARBEITER (
    Personalnummer        INT NOT NULL AUTO_INCREMENT,
    Name                 VARCHAR(100) NOT NULL,
    Vorname              VARCHAR(100) NOT NULL,
    Abteilung            VARCHAR(100),
    Arbeitspensum        DECIMAL(5,2),
    MoeglicheFunktionen  TEXT,
    PRIMARY KEY (Personalnummer)
) ENGINE=InnoDB;

-- ---------------------------------------
-- Tabelle: PROJEKT
-- ---------------------------------------
CREATE TABLE PROJEKT (
    Projektreferenz       INT NOT NULL AUTO_INCREMENT,
    Projekttitel          VARCHAR(200) NOT NULL,
    Projektbeschreibung   TEXT,
    Bewilligungsdatum     DATE,
    Prioritaet            VARCHAR(50),
    Status                VARCHAR(50),
    Startdatum_geplant    DATE,
    Enddatum_geplant      DATE,
    Startdatum_effektiv   DATE,
    Enddatum_effektiv     DATE,
    Projektleiter_ID      INT,
    Vorgehensmodell       VARCHAR(100),
    Projektfortschritt    DECIMAL(5,2),
    LinkProjektdokumente  TEXT,
    PRIMARY KEY (Projektreferenz),
    CONSTRAINT fk_projekt_leiter
      FOREIGN KEY (Projektleiter_ID)
      REFERENCES MITARBEITER(Personalnummer)
      ON DELETE SET NULL
      ON UPDATE CASCADE
) ENGINE=InnoDB;

-- ---------------------------------------
-- Tabelle: PROJEKTPHASE
-- ---------------------------------------
CREATE TABLE PROJEKTPHASE (
    Phasen_ID            INT NOT NULL AUTO_INCREMENT,
    Projekt_ID           INT NOT NULL,
    Phasenname           VARCHAR(100) NOT NULL,
    Startdatum_geplant   DATE,
    Enddatum_geplant     DATE,
    Startdatum_effektiv  DATE,
    Enddatum_effektiv    DATE,
    Reviewdatum_geplant  DATE,
    Reviewdatum_effektiv DATE,
    Freigabedatum        DATE,
    Freigabevisum        VARCHAR(100),
    Phasenstatus         VARCHAR(50),
    Phasenfortschritt    DECIMAL(5,2),
    Phasendokumente      TEXT,
    PRIMARY KEY (Phasen_ID),
    CONSTRAINT fk_phasen_projekt
      FOREIGN KEY (Projekt_ID)
      REFERENCES PROJEKT(Projektreferenz)
      ON DELETE CASCADE
      ON UPDATE CASCADE
) ENGINE=InnoDB;

-- ---------------------------------------
-- Tabelle: AKTIVITAET
-- ---------------------------------------
CREATE TABLE AKTIVITAET (
    AktivitaetID         INT NOT NULL AUTO_INCREMENT,
    Name                 VARCHAR(100) NOT NULL,
    Beschreibung         TEXT,
    Startdatum           DATE,
    Enddatum             DATE,
    Verantwortlicher_ID  INT,
    Budget               DECIMAL(10,2),
    EffektiveKosten      DECIMAL(10,2),
    Pensum               INT,
    Projektphase_ID      INT,
    Aktivitaetsdokumente TEXT,
    PRIMARY KEY (AktivitaetID),
    CONSTRAINT fk_aktivitaet_verantwortlicher
      FOREIGN KEY (Verantwortlicher_ID)
      REFERENCES MITARBEITER(Personalnummer)
      ON DELETE SET NULL
      ON UPDATE CASCADE,
    CONSTRAINT fk_aktivitaet_projektphase
      FOREIGN KEY (Projektphase_ID)
      REFERENCES PROJEKTPHASE(Phasen_ID)
      ON DELETE CASCADE
      ON UPDATE CASCADE
) ENGINE=InnoDB;

COMMIT;
