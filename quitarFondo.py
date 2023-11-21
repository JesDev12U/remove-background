from rembg import remove
import PIL.Image
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox

def no_cerrar():
    pass

def abrir_archivo():
    entrada.set("")
    filepath = filedialog.askopenfilename(filetypes=(("Archivos PNG", "*.png"),))
    entrada.set(filepath)

def abrir_carpeta():
    salida.set("")
    directory_path = filedialog.askdirectory()
    salida.set(directory_path)

def quitar_fondo():
    nom_input = ""
    for ch in entrada.get():
        nom_input += ch
        if ch == '/' or ch == '\\':
            nom_input = ""
    caracteres = ".png"
    for ch in range(len(caracteres)):
        nom_input = nom_input.replace(caracteres[ch], "")

    nom_output_path = nom_input + "_sin_fondo" + ".png"
    output_completo = salida.get() + "/" + nom_output_path
    print(entrada.get())
    print(output_completo)
    try:
        image_input = PIL.Image.open(entrada.get())
        output = remove(image_input)
        output.save(output_completo)
        messagebox.showinfo("Imagen modificada con éxito", "La imagen sin fondo se ha guardado en " + salida.get())
        entrada.set("")
        salida.set("")
    except Exception as e:
        messagebox.showerror("Error", "No se ha podido realizar la operación, verifique que sus entradas sean correctas")
        messagebox.showerror("Error", e)
        entrada.set("")
        salida.set("")

ventana = Tk()
ventana.geometry("370x300")
ventana.title("Remover fondos de PNG")
ventana.resizable(0, 0)
input_path_lb = Label(ventana, text="Selecciona el archivo", )
input_path_lb.config(
    font=("Arial", 20)
)
input_path_lb.pack()

entrada = StringVar()
salida = StringVar()

input_path = Entry(ventana, textvariable=entrada)
input_path.config(
    font=("Arial", 15),
    width=30,
)
input_path.pack()
input_path_button = Button(ventana, text="Seleccionar", command=abrir_archivo)
input_path_button.config(
    font=("Arial", 15)
)
input_path_button.pack()
output_path_lb = Label(ventana, text="Selecciona la carpeta destino")
output_path_lb.config(
    font=("Arial", 20),
)
output_path_lb.pack()
output_path = Entry(ventana, textvariable=salida)
output_path.config(
    font=("Arial", 15),
    width=30
)
output_path.pack()
output_path_button = Button(ventana, text="Seleccionar", command=abrir_carpeta)
output_path_button.config(
    font=("Arial", 15)
)
output_path_button.pack()
Label(ventana).pack()
remove_bg_button = Button(ventana, text="Quitar fondo", command=quitar_fondo)
remove_bg_button.config(
    font=("Arial", 15)
)
remove_bg_button.pack()
ventana.mainloop()
"""
input_path = "C:/Users/jesus/desktop/Foto.png"
output_path = "C:/Users/jesus/desktop/Foto_sin_fondo.png"
image_input = Image.open(input_path)
output = remove(image_input)
output.save(output_path)
"""