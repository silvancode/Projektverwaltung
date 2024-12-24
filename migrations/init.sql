-- =======================================================
-- Beispiel-Init-Skript für MySQL basierend auf dem ERM
-- =======================================================

CREATE DATABASE IF NOT EXISTS projektverwaltung_db;
USE projektverwaltung_db;

-- ---------------------------------------
-- Alle Tabellen droppen (falls schon vorhanden)
-- ---------------------------------------
SET FOREIGN_KEY_CHECKS=0;
DROP TABLE IF EXISTS MEILENSTEIN;
DROP TABLE IF EXISTS PERSONELLERESSOURCEN;
DROP TABLE IF EXISTS EXTERNEKOSTEN;
DROP TABLE IF EXISTS AKTIVITAET;
DROP TABLE IF EXISTS PROJEKTPHASE;
DROP TABLE IF EXISTS PROJEKT;
DROP TABLE IF EXISTS MITARBEITER;
SET FOREIGN_KEY_CHECKS=1;

-- ---------------------------------------
-- Tabelle: MITARBEITER
-- ---------------------------------------
CREATE TABLE MITARBEITER (
    Personalnummer INT NOT NULL AUTO_INCREMENT,
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
    PhasenID               INT NOT NULL AUTO_INCREMENT,
    Projekt_ID             INT NOT NULL,
    Startdatum_geplant     DATE,
    Enddatum_geplant       DATE,
    Startdatum_effektiv    DATE,
    Enddatum_effektiv      DATE,
    Reviewdatum_geplant    DATE,
    Reviewdatum_effektiv   DATE,
    Freigabedatum          DATE,
    Freigabevisum          VARCHAR(100),
    Phasenstatus           VARCHAR(50),
    Phasenfortschritt      DECIMAL(5,2),
    LinkPhasendokumente    TEXT,
    PRIMARY KEY (PhasenID),
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
    AktivitaetsID            INT NOT NULL AUTO_INCREMENT,
    Phasen_ID                INT NOT NULL,
    VerantwortlichePerson_ID INT,
    Startdatum_geplant       DATE,
    Enddatum_geplant         DATE,
    Startdatum_effektiv      DATE,
    Enddatum_effektiv        DATE,
    Aktivitaetsfortschritt   DECIMAL(5,2),
    LinkAktivitaetsdokumente TEXT,
    PRIMARY KEY (AktivitaetsID),
    CONSTRAINT fk_aktivitaet_phase
      FOREIGN KEY (Phasen_ID) 
      REFERENCES PROJEKTPHASE(PhasenID)
      ON DELETE CASCADE
      ON UPDATE CASCADE,
    CONSTRAINT fk_aktivitaet_mitarbeiter
      FOREIGN KEY (VerantwortlichePerson_ID)
      REFERENCES MITARBEITER(Personalnummer)
      ON DELETE SET NULL
      ON UPDATE CASCADE
) ENGINE=InnoDB;

-- ---------------------------------------
-- Tabelle: EXTERNEKOSTEN
-- ---------------------------------------
CREATE TABLE EXTERNEKOSTEN (
    ExterneKostenID INT NOT NULL AUTO_INCREMENT,
    Aktivitaet_ID   INT NOT NULL,
    Kostenart       VARCHAR(100),
    Budgetkosten    DECIMAL(10,2),
    EffektiveKosten DECIMAL(10,2),
    Abweichung      TEXT,
    PRIMARY KEY (ExterneKostenID),
    CONSTRAINT fk_exkost_aktivitaet
      FOREIGN KEY (Aktivitaet_ID)
      REFERENCES AKTIVITAET(AktivitaetsID)
      ON DELETE CASCADE
      ON UPDATE CASCADE
) ENGINE=InnoDB;

-- ---------------------------------------
-- Tabelle: PERSONELLERESSOURCEN
-- ---------------------------------------
CREATE TABLE PERSONELLERESSOURCEN (
    RessourcenID    INT NOT NULL AUTO_INCREMENT,
    Aktivitaet_ID   INT NOT NULL,
    Mitarbeiter_ID  INT NOT NULL,
    Funktion        VARCHAR(100),
    BudgetierteZeit DECIMAL(10,2),
    EffektiveZeit   DECIMAL(10,2),
    Abweichung      TEXT,
    PRIMARY KEY (RessourcenID),
    CONSTRAINT fk_ressource_aktivitaet
      FOREIGN KEY (Aktivitaet_ID)
      REFERENCES AKTIVITAET(AktivitaetsID)
      ON DELETE CASCADE
      ON UPDATE CASCADE,
    CONSTRAINT fk_ressource_mitarbeiter
      FOREIGN KEY (Mitarbeiter_ID)
      REFERENCES MITARBEITER(Personalnummer)
      ON DELETE CASCADE
      ON UPDATE CASCADE
) ENGINE=InnoDB;

-- ---------------------------------------
-- Tabelle: MEILENSTEIN
-- ---------------------------------------
CREATE TABLE MEILENSTEIN (
    MeilensteinID  INT NOT NULL AUTO_INCREMENT,
    Projekt_ID     INT NOT NULL,
    Bezeichnung    VARCHAR(100),
    GeplantesDatum DATE,
    ErreichtesDatum DATE,
    Status         VARCHAR(50),
    PRIMARY KEY (MeilensteinID),
    CONSTRAINT fk_meilenstein_projekt
      FOREIGN KEY (Projekt_ID)
      REFERENCES PROJEKT(Projektreferenz)
      ON DELETE CASCADE
      ON UPDATE CASCADE
) ENGINE=InnoDB;

-- ---------------------------------------
-- Optional: Ende/Commit
-- ---------------------------------------
COMMIT;
