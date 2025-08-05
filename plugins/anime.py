from flask import request
from flask_cors import cross_origin
from plugins.abc_plugin import BasePluginPresence

def format_time(seconds):
    minutes = int(seconds) // 60
    secs = int(seconds) % 60
    return f"{minutes}:{secs:02d}"

class AnimePlugin(BasePluginPresence):
    def register_routes(self):
        @self.app.route('/anime', methods=['POST', 'OPTIONS'])
        @cross_origin(origin='*')
        def anime_update():
            data = request.json
            current = format_time(data.get('currentTime', 0))
            total = format_time(data.get('duration', 0))
            payload = {
                "source": "anime",
                "content":{
                    "details": data.get("title"),
                    "state": f"{current}/{total}",
                    "large_image": "anime",
                    "large_text": data.get("title"),
                }
            }
            return self.send_to_server(payload)