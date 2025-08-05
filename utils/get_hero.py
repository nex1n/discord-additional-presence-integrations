import json

def get_hero_name_by_code(hero_code: str) -> str:
    with open("heroes.json", encoding="utf-8") as f:
        heroes = json.load(f)
    for hero in heroes:
        if hero.get("name") == hero_code:
            return hero.get("localized_name")
    return "Неизвестный"