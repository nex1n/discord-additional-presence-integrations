from flask import Flask, request
from flask_cors import CORS, cross_origin
import threading
import time
from utils.presence_manager import PresenceManager
import requests

app = Flask(__name__)
CORS(app)

presence_manager = PresenceManager()

@app.route('/activity', methods=['POST'])
def update_activity():
    data = request.json
    source = data.get("source")
    presence_manager.update_presence(source, data.get("content", {}))
    print(f"SERVER[{source.upper()}] Data received: {data}")
    return {"status": "activity updated"}


@app.route('/api/activity_end', methods=['POST', 'OPTIONS'])
@cross_origin()
def activity_end():
    if request.method == 'OPTIONS':
        return '', 200
    data = request.form
    print(f"Activity end received: {data}")
    activity_type = data.get('type')
    presence_manager.remove_presence(activity_type)
    return '', 204


if __name__ == '__main__':
    app.run(port=2222)
