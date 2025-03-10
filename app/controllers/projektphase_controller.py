from flask import Blueprint, render_template, request, redirect, url_for, flash
import os
from werkzeug.utils import secure_filename
from config.config import UPLOAD_FOLDER, allowed_file
from app.models.projektphase import Projektphase
from app.models.projekt import Projekt  # Import Projekt-Modell

projektphase_blueprint = Blueprint("projektphase", __name__, template_folder="../templates/projektphase")


@projektphase_blueprint.route("/", methods=["GET"])
def list_phasen():
    phasen = Projektphase.get_all()
    return render_template("projektphase/projektphase_list.html", phasen=phasen)


@projektphase_blueprint.route("/new", methods=["GET", "POST"])
@projektphase_blueprint.route("/<int:phasen_id>/edit", methods=["GET", "POST"])
def upsert_phase(phasen_id=None):
    phase = Projektphase.get_by_id(phasen_id) if phasen_id else None
    dokumentenpfad = phase.phasendokumente if phase else None

    projekte = Projekt.get_all()  # Alle Projekte für das Dropdown abrufen

    if request.method == "POST":
        projekt_id = request.form["projekt_id"]
        phasenname = request.form["phasenname"]
        startdatum_geplant = request.form["startdatum_geplant"]
        enddatum_geplant = request.form["enddatum_geplant"]
        phasenstatus = request.form["phasenstatus"]
        phasenfortschritt = request.form["phasenfortschritt"]

        # Datei-Upload prüfen
        if "phasendokument" in request.files:
            file = request.files["phasendokument"]
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                filepath = os.path.join(UPLOAD_FOLDER, filename)
                file.save(filepath)
                dokumentenpfad = "uploads/" + filename

        if phase:
            # Bearbeiten einer vorhandenen Phase
            phase.projekt_id = projekt_id
            phase.phasenname = phasenname
            phase.startdatum_geplant = startdatum_geplant
            phase.enddatum_geplant = enddatum_geplant
            phase.phasenstatus = phasenstatus
            phase.phasenfortschritt = phasenfortschritt
            phase.phasendokumente = dokumentenpfad
            phase.update()
        else:
            # Neue Projektphase erstellen
            neue_phase = Projektphase(
                projekt_id=projekt_id,
                phasenname=phasenname,
                startdatum_geplant=startdatum_geplant,
                enddatum_geplant=enddatum_geplant,
                phasenstatus=phasenstatus,
                phasenfortschritt=phasenfortschritt,
                phasendokumente=dokumentenpfad
            )
            neue_phase.save()

        flash("Projektphase erfolgreich gespeichert.", "success")
        return redirect(url_for("projektphase.list_phasen"))

    # Projekte an das Template übergeben
    return render_template("projektphase/projektphase_form.html", phase=phase, projekte=projekte)

@projektphase_blueprint.route("/<int:phasen_id>", methods=["GET"])
def view_phase(phasen_id):
    phase = Projektphase.get_by_id(phasen_id)
    if phase:
        return render_template("projektphase/projektphase_view.html", phase=phase)
    return redirect(url_for("projektphase.list_phasen"))

@projektphase_blueprint.route("/<int:phasen_id>/delete", methods=["GET", "POST"])
def delete_phase(phasen_id):
    Projektphase.delete(phasen_id)
    return redirect(url_for("projektphase.list_phasen"))