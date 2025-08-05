from plugins.abc_plugin import BasePluginPresence
from utils.get_hero import get_hero_name_by_code
from flask import request

DOTA_GAME_STATES = {
    "DOTA_GAMERULES_STATE_HERO_SELECTION": "Выбор героя",
    "DOTA_GAMERULES_STATE_STRATEGY_TIME": "Стадия планировки",
    "DOTA_GAMERULES_STATE_PRE_GAME": "До начала",
    "DOTA_GAMERULES_STATE_GAME_IN_PROGRESS": "Игра началась",
    "DOTA_GAMERULES_STATE_TEAM_SHOWCASE": "Показ команд",
    "DOTA_GAMERULES_STATE_POST_GAME": "Экран окончания"
}

class DotaPlugin(BasePluginPresence):
    def register_routes(self):
        @self.app.route('/dota', methods=['POST'])
        def dota_update():
            data = request.json
            game_state_raw = data.get("map", {}).get("game_state")
            phase = DOTA_GAME_STATES.get(game_state_raw, "В главном меню")
            hero_data = data.get("hero", None)
            if hero_data:
                hero_id = hero_data.get("name")
                hero = "Герой:" + get_hero_name_by_code(hero_id)
            else:
                hero = "AFK"
            payload = {
                "source": "dota",
                "content": {
                    "details": f"Состояние: {phase}",
                    "state": hero,
                    "large_image": "dota",
                    "large_text": f"{hero} - {phase}",
                }
            }
            return self.send_to_server(payload)