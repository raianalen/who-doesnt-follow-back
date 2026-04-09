import json


def cargar_followers(archivos_followers):
    followers = []

    for archivo in archivos_followers:
        with open(archivo, "r", encoding="utf-8") as archivo_json:
            followers_data = json.load(archivo_json)

            for follower in followers_data:
                if follower["string_list_data"]:
                    username = follower["string_list_data"][0]["value"]
                    followers.append(username)
    return followers