from flask import Flask, render_template, request
from core.followers import cargar_followers
from core.following import cargar_following

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/analizar", methods=["POST"])
def analizar():
    archivos_followers = request.files.getlist("followers")
    archivo_following = request.files.get("following")

    if not archivos_followers or not archivo_following:
        return render_template("index.html", error="Please upload both files.")

    followers = cargar_followers(archivos_followers)
    following = cargar_following(archivo_following)

    not_follow_back = set(following) - set(followers)

    return render_template("index.html", resultados=sorted(not_follow_back))

if __name__ == "__main__":
    app.run(debug=True)