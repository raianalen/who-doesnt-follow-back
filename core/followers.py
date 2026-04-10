import json

def cargar_followers(archivos_followers):
    followers = []

    for archivo in archivos_followers:

        # 👇 detectar tipo
        if isinstance(archivo, str):
            with open(archivo, "r", encoding="utf-8") as f:
                data = json.load(f)
        else:
            archivo.seek(0)
            data = json.load(archivo)

        for follower in data:
            if follower["string_list_data"]:
                username = follower["string_list_data"][0]["value"]
                followers.append(username)

    return followers