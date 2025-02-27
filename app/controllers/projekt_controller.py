from flask import Blueprint, render_template, request, redirect, url_for
from app.models.projekt import Projekt
from app.models.mitarbeiter import Mitarbeiter

projekt_blueprint = Blueprint("projekt", __name__, template_folder="../templates/projekt")


@projekt_blueprint.route("/", methods=["GET"])
def list_projekte():
    projekte = Projekt.get_all()
    return render_template("projekt/projekt_list.html", projekte=projekte)


@projekt_blueprint.route("/new", methods=["GET", "POST"])
@projekt_blueprint.route("/<int:projekt_id>/edit", methods=["GET", "POST"])
def upsert_projekt(projekt_id=None):
    projekt = Projekt.get_by_id(projekt_id) if projekt_id else None
    mitarbeiter = Mitarbeiter.get_all() # Alle Mitarbeiter abrufen

    if request.method == "POST":
        projekttitel = request.form["projekttitel"]
        beschreibung = request.form["beschreibung"]
        bewilligungsdatum = request.form["bewilligungsdatum"]
        prioritaet = request.form["prioritaet"]
        status = request.form["status"]
        startdatum_geplant = request.form["startdatum_geplant"]
        enddatum_geplant = request.form["enddatum_geplant"]
        projektleiter_id = int(request.form["projektleiter_id"])
        vorgehensmodell = request.form["vorgehensmodell"]
        fortschritt = float(request.form["fortschritt"])

        if projekt:  # Bearbeiten
            projekt.projekttitel = projekttitel
            projekt.beschreibung = beschreibung
            projekt.bewilligungsdatum = bewilligungsdatum
            projekt.prioritaet = prioritaet
            projekt.status = status
            projekt.startdatum_geplant = startdatum_geplant
            projekt.enddatum_geplant = enddatum_geplant
            projekt.projektleiter_id = projektleiter_id
            projekt.vorgehensmodell = vorgehensmodell
            projekt.fortschritt = fortschritt

            projekt.update()
        else:  # Erstellen
            neues_projekt = Projekt(projekttitel, beschreibung, bewilligungsdatum, prioritaet,
                                    status, startdatum_geplant, enddatum_geplant, projektleiter_id,
                                    vorgehensmodell, fortschritt)
            neues_projekt.save()

        return redirect(url_for("projekt.list_projekte"))

    return render_template("projekt/projekt_form.html", projekt=projekt, mitarbeiter=mitarbeiter)


# Einzelnes Projekt anzeigen
@projekt_blueprint.route("/<int:projekt_id>", methods=["GET"])
def view_projekt(projekt_id):
    projekt = Projekt.get_by_id(projekt_id)
    if projekt:
        return render_template("projekt/projekt_view.html", projekt=projekt)
    return redirect(url_for("projekt.list_projekte"))


# Projekt löschen
@projekt_blueprint.route("/projekte/<int:projekt_id>/delete", methods=["GET", "POST"])
def delete_projekt(projekt_id):
    Projekt.delete(projekt_id)
    return redirect(url_for("projekt.list_projekte"))
