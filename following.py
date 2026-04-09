import json

def cargar_following(archivo_following):
    following = []

    with open(archivo_following, "r", encoding="utf-8") as archivo_json:
        following_data = json.load(archivo_json)
        list = following_data["relationships_following"]
        for user in list:
            username = user["title"]
            following.append(username)

    return following