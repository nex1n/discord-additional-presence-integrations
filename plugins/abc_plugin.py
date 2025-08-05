from flask import Flask, request
import requests
from abc import ABC, abstractmethod



class BasePluginPresence(ABC):
    def __init__(self, app):
        self.target_url = "http://localhost:2222/activity"
        self.app = app
        self.register_routes()

    @abstractmethod
    def register_routes(self):
        """Регистрирует маршруты Flask. Реализуется в наследниках."""
        pass

    def send_to_server(self, payload: dict) -> dict:
        try:
            requests.post(self.target_url, json=payload)
            return {"status": "data forwarded"}
        except Exception as e:
            return {"status": "error", "message": str(e)}, 500