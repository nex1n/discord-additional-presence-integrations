import os
import time
from pypresence import Presence
import config

class PresenceManager:
    def __init__(self):
        self.start_times = {}
        self.clients = {}
        self.connected = {}

        for key, app_id in config.PRESENCE_APPS.items():
            try:
                client = Presence(app_id)
                client.connect()
                self.clients[key] = client
                self.connected[key] = True
            except Exception as e:
                print(f"[PresenceManager] Failed to connect {key}: {e}")
                self.connected[key] = False

    def update_presence(self, key, data):
        now = int(time.time())
        if key not in self.start_times:
            self.start_times[key] = now  # сохраняем время начала
        try:
            self.clients[key].update(
                **data,
                start=self.start_times[key]
            )
        except Exception as e:
            print(f"[Presence Error][{key}] {e}")


    def remove_presence(self, key):
        print(f"[PresenceManager] Removing presence for {key}")
        if not self.connected.get(key):
            print(f"[PresenceManager] {key} not connected")
            return
        try:
            self.clients[key].clear()
            if key in self.start_times:
                del self.start_times[key]
        except Exception as e:
            print(f"[Presence Clear Error][{key}] {e}")