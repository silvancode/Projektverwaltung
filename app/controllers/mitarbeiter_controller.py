from flask import Blueprint, render_template, request, redirect, url_for
from app.models.mitarbeiter import Mitarbeiter

mitarbeiter_blueprint = Blueprint("mitarbeiter", __name__, template_folder="../templates/mitarbeiter")


@mitarbeiter_blueprint.route("/", methods=["GET"])
def list_mitarbeiter():
    mitarbeiter = Mitarbeiter.get_all()
    return render_template("mitarbeiter/mitarbeiter_list.html", mitarbeiter=mitarbeiter)


@mitarbeiter_blueprint.route("/new", methods=["GET", "POST"])
@mitarbeiter_blueprint.route("/<int:mitarbeiter_id>/edit", methods=["GET", "POST"])
def upsert_mitarbeiter(mitarbeiter_id=None):
    mitarbeiter = Mitarbeiter.get_by_id(mitarbeiter_id) if mitarbeiter_id else None

    if request.method == "POST":
        name = request.form["name"]
        vorname = request.form["vorname"]
        abteilung = request.form["abteilung"]
        arbeitspensum = float(request.form["arbeitspensum"])
        moegliche_funktionen = request.form["moegliche_funktionen"]

        if mitarbeiter:  # Bearbeiten
            mitarbeiter.name = name
            mitarbeiter.vorname = vorname
            mitarbeiter.abteilung = abteilung
            mitarbeiter.arbeitspensum = arbeitspensum
            mitarbeiter.moegliche_funktionen = moegliche_funktionen

            mitarbeiter.update()
        else:  # Erstellen
            neuer_mitarbeiter = Mitarbeiter(name, vorname, abteilung, arbeitspensum, moegliche_funktionen)
            neuer_mitarbeiter.save()

        return redirect(url_for("mitarbeiter.list_mitarbeiter"))

    return render_template("mitarbeiter/mitarbeiter_form.html", mitarbeiter=mitarbeiter)


# Einzelner Mitarbeiter anzeigen
@mitarbeiter_blueprint.route("/<int:mitarbeiter_id>", methods=["GET"])
def view_mitarbeiter(mitarbeiter_id):
    mitarbeiter = Mitarbeiter.get_by_id(mitarbeiter_id)
    if mitarbeiter:
        return render_template("mitarbeiter/mitarbeiter_view.html", mitarbeiter=mitarbeiter)
    return redirect(url_for("mitarbeiter.list_mitarbeiter"))


# Projekt löschen
@mitarbeiter_blueprint.route("/<int:mitarbeiter_id>/delete", methods=["GET", "POST"])
def delete_mitarbeiter(mitarbeiter_id):
    Mitarbeiter.delete(mitarbeiter_id)
    return redirect(url_for("mitarbeiter.list_mitarbeiter"))
