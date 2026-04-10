import json

def cargar_following(archivo_following):

    if isinstance(archivo_following, str):
        with open(archivo_following, "r", encoding="utf-8") as f:
            data = json.load(f)
    else:
        archivo_following.seek(0)
        data = json.load(archivo_following)

    following = []

    for user in data["relationships_following"]:
        username = user["title"]
        following.append(username)

    return following