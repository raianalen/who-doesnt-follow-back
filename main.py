from followers import cargar_followers
from following import cargar_following
import tkinter as tk
from tkinter import filedialog
import datetime

archivos_followers = []
archivo_following = ""
not_follow_back = []

#root y estilo de botones
root = tk.Tk()
root.title("Who Doesn't Follow Back by Raian Alen")

# lo centro porque me da TOC
ancho = 450
alto = 500

pantalla_ancho = root.winfo_screenwidth()
pantalla_alto = root.winfo_screenheight()

x = int((pantalla_ancho / 2) - (ancho / 2))
y = int((pantalla_alto / 2) - (alto / 2))

root.geometry(f"{ancho}x{alto}+{x}+{y}")

root.configure(bg="#1e1e1e")
root.iconbitmap("icono.ico")

btn_style = {
    "font": ("Arial", 11),
    "bg": "#2d2d2d",
    "fg": "white",
    "activebackground": "#3c3c3c",
    "width": 20,
    "bd": 0,
    "pady": 5
}

def seleccionar_followers():    #funcion para seleccionar los seguidores
    global archivos_followers

    archivos_followers = filedialog.askopenfilenames(
        title="Seleccionar archivos de Followers",
        filetypes=[("Archivos JSON", "*.json")]
    )

    cantidad = len(archivos_followers)      # acá hago que si es 1 archivo lo diga en singular o varios en plural

    if cantidad == 1:
        texto = "Follower cargado: 1 archivo"
    else:
        texto = f"Followers cargados: {cantidad} archivos"

    resultado_label.config(text=texto)

def seleccionar_following():        #funcion para seleccionar los siguiendo
    global archivo_following

    archivo_following = filedialog.askopenfilename(
        title="Seleccionar archivo de Following",
        filetypes=[("Archivo JSON", "*.json")]
    )

    if archivo_following:
        resultado_label.config(
            text="Following cargado: 1 archivo"
        )



def analizar():

    if not archivos_followers or not archivo_following:
        resultado_label.config(text="⚠️ Faltan archivos")
        return

    followers = cargar_followers(archivos_followers)
    following = cargar_following(archivo_following)

    global not_follow_back
    not_follow_back = set(following) - set(followers)

    resultado_label.config(
        text=f"No te siguen: {len(not_follow_back)}\n⚠️ Puede incluir cuentas eliminadas"
    )

    lista_texto.delete("1.0", tk.END)  # limpia antes

    for user in sorted(not_follow_back):
        lista_texto.insert(tk.END, user + "\n")

def exportar_txt():
    if not not_follow_back:
        resultado_label.config(text="⚠️ No hay datos para exportar")
        return

    fecha = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M")
    nombre_sugerido = f"not_follow_back_{fecha}.txt"

    ruta_guardado = filedialog.asksaveasfilename(
        title="Guardar archivo",
        initialfile=nombre_sugerido,
        defaultextension=".txt",
        filetypes=[("Archivo de texto", "*.txt")],
    )

    if not ruta_guardado:
        return

    with open(ruta_guardado, "w", encoding="utf-8") as f:
        for user in sorted(not_follow_back):
            f.write(user + "\n")

    resultado_label.config(text="Archivo exportado ✔")

#botones y caja

tk.Button(root, text="Cargar Followers", command=seleccionar_followers, **btn_style).pack(pady=5)
tk.Button(root, text="Cargar Following", command=seleccionar_following, **btn_style).pack(pady=5)
tk.Button(root, text="Analizar", command=analizar, **btn_style).pack(pady=10)
tk.Button(root, text="Exportar lista", command=exportar_txt, **btn_style).pack(pady=5)
resultado_label = tk.Label(
    root,
    text="Esperando acción...",
    font=("Arial", 11),
    bg="#1e1e1e",
    fg="white",
    justify="center"
)
resultado_label.pack(pady=10)
# scroll con lista
frame_lista = tk.Frame(root)
frame_lista.pack(pady=10)

scrollbar = tk.Scrollbar(frame_lista)

lista_texto = tk.Text(
    frame_lista,
    height=15,
    width=50,
    yscrollcommand=scrollbar.set,
    bg="#1e1e1e",
    fg="white",
    insertbackground="white"
)

scrollbar.config(command=lista_texto.yview)

scrollbar.pack(side="right", fill="y")
lista_texto.pack(side="left")


root.mainloop()