from flask import Blueprint, render_template, request, redirect, url_for
from app.models.projekt import Projekt

projekt_blueprint = Blueprint("projekt", __name__, template_folder="../templates/projekt")


@projekt_blueprint.route("/", methods=["GET"])
def list_projekte():
    projekte = Projekt.get_all()
    return render_template("projekt/projekt_list.html", projekte=projekte)


@projekt_blueprint.route("/new", methods=["GET", "POST"])
def create_projekt():
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

        projekt = Projekt(projekttitel, beschreibung, bewilligungsdatum, prioritaet, status,
                          startdatum_geplant, enddatum_geplant, projektleiter_id, vorgehensmodell, fortschritt)
        projekt.save()

        return redirect(url_for("projekt.list_projekte"))
    return render_template("projekt/projekt_form.html")


# Einzelnes Projekt anzeigen
@projekt_blueprint.route("/<int:projekt_id>", methods=["GET"])
def view_projekt(projekt_id):
    projekt = Projekt.get_by_id(projekt_id)
    if projekt:
        return render_template("projekt/projekt_view.html", projekt=projekt)
    return redirect(url_for("projekt.list_projekte"))


# Projekt bearbeiten
@projekt_blueprint.route("/<int:projekt_id>/edit", methods=["GET", "POST"])
def edit_projekt(projekt_id):
    projekt = Projekt.get_by_id(projekt_id)
    if request.method == "POST":
        projekt.projekttitel = request.form["projekttitel"]
        projekt.beschreibung = request.form["beschreibung"]
        projekt.bewilligungsdatum = request.form["bewilligungsdatum"]
        projekt.prioritaet = request.form["prioritaet"]
        projekt.status = request.form["status"]
        projekt.startdatum_geplant = request.form["startdatum_geplant"]
        projekt.enddatum_geplant = request.form["enddatum_geplant"]
        projekt.projektleiter_id = int(request.form["projektleiter_id"])
        projekt.vorgehensmodell = request.form["vorgehensmodell"]
        projekt.fortschritt = float(request.form["fortschritt"])

        projekt.update()
        return redirect(url_for("projekt.list_projekte"))

    return render_template("projekt/projekt_form.html", projekt=projekt)


# Projekt löschen
@projekt_blueprint.route("/projekte/<int:projekt_id>/delete", methods=["GET", "POST"])
def delete_projekt(projekt_id):
    Projekt.delete(projekt_id)
    return redirect(url_for("projekt.list_projekte"))
