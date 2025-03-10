from flask import Blueprint, render_template, request, redirect, url_for, flash
import os
from werkzeug.utils import secure_filename
from config.config import UPLOAD_FOLDER, allowed_file
from app.models.aktivitaet import Aktivitaet
from app.models.mitarbeiter import Mitarbeiter
from app.models.projektphase import Projektphase

aktivitaet_blueprint = Blueprint("aktivitaet", __name__, template_folder="../templates/aktivitaet")


@aktivitaet_blueprint.route("/", methods=["GET"])
def list_aktivitaeten():
    """
    Liste aller Aktivitäten anzeigen.
    """
    aktivitaeten = Aktivitaet.get_all()
    return render_template("aktivitaet/aktivitaet_list.html", aktivitaeten=aktivitaeten)


@aktivitaet_blueprint.route("/new", methods=["GET", "POST"])
@aktivitaet_blueprint.route("/<int:aktivitaet_id>/edit", methods=["GET", "POST"])
def upsert_aktivitaet(aktivitaet_id=None):
    """
    Neue Aktivität erstellen oder bestehende Aktivität bearbeiten.
    """
    aktivitaet = Aktivitaet.get_by_id(aktivitaet_id) if aktivitaet_id else None
    dokumentenpfad = aktivitaet.aktivitaetsdokumente if aktivitaet else None

    # Für Dropdown-Felder, z.B. verantwortliche Mitarbeiter, Projektphasen
    mitarbeiter = Mitarbeiter.get_all()
    phasen = Projektphase.get_all()

    if request.method == "POST":
        name = request.form["name"]
        beschreibung = request.form["beschreibung"]
        startdatum = request.form["startdatum"]
        enddatum = request.form["enddatum"]
        verantwortlicher_id = request.form["verantwortlicher_id"]
        budget = request.form["budget"]
        effektive_kosten = request.form["effektive_kosten"]
        pensum = request.form["pensum"]
        projektphase_id = request.form["projektphase_id"]

        # Datei-Upload prüfen
        if "aktivitaetsdokument" in request.files:
            file = request.files["aktivitaetsdokument"]
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                filepath = os.path.join(UPLOAD_FOLDER, filename)
                file.save(filepath)
                dokumentenpfad = "uploads/" + filename  # Nur den relativen Pfad speichern

        if aktivitaet:
            # Bearbeiten einer vorhandenen Aktivität
            aktivitaet.name = name
            aktivitaet.beschreibung = beschreibung
            aktivitaet.startdatum = startdatum
            aktivitaet.enddatum = enddatum
            aktivitaet.verantwortlicher_id = verantwortlicher_id
            aktivitaet.budget = budget
            aktivitaet.effektive_kosten = effektive_kosten
            aktivitaet.pensum = pensum
            aktivitaet.projektphase_id = projektphase_id
            aktivitaet.aktivitaetsdokumente = dokumentenpfad

            aktivitaet.update()
        else:
            # Neue Aktivität erstellen
            neue_aktivitaet = Aktivitaet(
                name=name,
                beschreibung=beschreibung,
                startdatum=startdatum,
                enddatum=enddatum,
                verantwortlicher_id=verantwortlicher_id,
                budget=budget,
                effektive_kosten=effektive_kosten,
                pensum=pensum,
                projektphase_id=projektphase_id,
                aktivitaetsdokumente=dokumentenpfad
            )
            neue_aktivitaet.save()

        flash("Aktivität erfolgreich gespeichert.", "success")
        return redirect(url_for("aktivitaet.list_aktivitaeten"))

    # GET: Formular anzeigen
    return render_template("aktivitaet/aktivitaet_form.html",
                           aktivitaet=aktivitaet,
                           mitarbeiter=mitarbeiter,
                           phasen=phasen)


@aktivitaet_blueprint.route("/<int:aktivitaet_id>", methods=["GET"])
def view_aktivitaet(aktivitaet_id):
    """
    Detailansicht einer Aktivität.
    """
    aktivitaet = Aktivitaet.get_by_id(aktivitaet_id)
    if aktivitaet:
        return render_template("aktivitaet/aktivitaet_view.html", aktivitaet=aktivitaet)
    return redirect(url_for("aktivitaet.list_aktivitaeten"))


@aktivitaet_blueprint.route("/<int:aktivitaet_id>/delete", methods=["GET", "POST"])
def delete_aktivitaet(aktivitaet_id):
    """
    Eine Aktivität löschen.
    """
    Aktivitaet.delete(aktivitaet_id)
    return redirect(url_for("aktivitaet.list_aktivitaeten"))
