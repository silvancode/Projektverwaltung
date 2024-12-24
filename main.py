from flask import Flask, render_template
from app.controllers.mitarbeiter_controller import mitarbeiter_blueprint
from app.controllers.projekt_controller import projekt_blueprint
# from app.controllers.projektphase_controller import projektphase_blueprint
# from app.controllers.aktivitaet_controller import aktivitaet_blueprint
# from app.controllers.meilenstein_controller import meilenstein_blueprint

app = Flask(__name__, template_folder='app/templates')

# Registrierung der Blueprints
app.register_blueprint(mitarbeiter_blueprint, url_prefix="/mitarbeiter")
app.register_blueprint(projekt_blueprint, url_prefix="/projekte")
# app.register_blueprint(projektphase_blueprint, url_prefix="/projektphasen")
# app.register_blueprint(aktivitaet_blueprint, url_prefix="/aktivitaeten")
# app.register_blueprint(meilenstein_blueprint, url_prefix="/meilensteine")


@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
