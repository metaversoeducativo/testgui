from flask import Flask, render_template
import yaml
import os

# export FLASK_ENV=development 
os.environ['FLASK_ENV'] = 'development'
app = Flask(__name__)

def load_config():
    with open("configuracion.yaml", "r") as file:
        return yaml.safe_load(file)

@app.route("/")
def index():
    config = load_config()
    return render_template("index.html", site_title=config["titulo_sitio"])

if __name__ == "__main__":
        app.run(host='0.0.0.0', debug=True)
