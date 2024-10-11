import tkinter as tk
from tkinter import messagebox
import openai
import requests
from io import BytesIO
from PIL import Image, ImageTk
import credenciales

# Configura tu clave de API de OpenAI
openai.api_key = credenciales.API_KEY()

def generar_imagen():
    # Obtén el texto de entrada
    prompt = entrada.get()
    if not prompt:
        messagebox.showwarning("Entrada Vacía", "Por favor, introduzca un texto para generar una imagen.")
        return
    
    try:
        # Llama a la API de OpenAI para generar una imagen
        response = openai.Image.create(
            prompt=prompt,
            n=1,
            size="512x512"
        )
        image_url = response['data'][0]['url']
        
        # Descarga la imagen
        response = requests.get(image_url)
        img_data = response.content
        img = Image.open(BytesIO(img_data))
        
        # Muestra la imagen en la interfaz de Tkinter
        img_tk = ImageTk.PhotoImage(img)
        panel.config(image=img_tk)
        panel.image = img_tk
    
    except Exception as e:
        messagebox.showerror("Error", f"Ha ocurrido un error al generar la imagen: {str(e)}")

# Configura la ventana principal
root = tk.Tk()
root.title("Generador de Imágenes con DALL-E 3")

# Crea la entrada de texto
entrada = tk.Entry(root, width=50)
entrada.pack(pady=10)

# Crea el botón para generar la imagen
boton_generar = tk.Button(root, text="Generar Imagen", command=generar_imagen)
boton_generar.pack(pady=10)

# Crea un panel para mostrar la imagen generada
panel = tk.Label(root)
panel.pack(pady=10)

# Ejecuta la aplicación de Tkinter
root.mainloop()