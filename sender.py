from flask import Flask
from plugins import AnimePlugin
from plugins import DotaPlugin
from flask_cors import CORS




app = Flask(__name__)
CORS(app)
anime_plugin = AnimePlugin(app)
dota_plugin = DotaPlugin(app)

if __name__ == "__main__":
    app.run(port=3333)