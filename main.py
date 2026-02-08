from rembg import remove
import PIL.Image
from tkinter import *
from tkinter import ttk
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

    remove_bg_button.config(state="disabled")
    progress_bar.grid()
    progress_bar.start()
    ventana.update_idletasks() # Force GUI update to show progress bar

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
    finally:
        progress_bar.stop()
        progress_bar.grid_remove()
        remove_bg_button.config(state="enabled")

ventana = Tk()
ventana.title("Remover fondos de PNG")
ventana.resizable(False, False)

main_frame = ttk.Frame(ventana, padding="20 20 20 20")
main_frame.grid(row=0, column=0, sticky=(N, W, E, S))
ventana.columnconfigure(0, weight=1)
ventana.rowconfigure(0, weight=1)

input_path_lb = ttk.Label(main_frame, text="Selecciona el archivo")
input_path_lb.grid(row=0, column=0, columnspan=2, pady=5)

entrada = StringVar()
salida = StringVar()

input_path = ttk.Entry(main_frame, textvariable=entrada, width=40)
input_path.grid(row=1, column=0, pady=5, padx=5, sticky=(W, E))
input_path_button = ttk.Button(main_frame, text="Seleccionar", command=abrir_archivo)
input_path_button.grid(row=1, column=1, pady=5, padx=5)
output_path_lb = ttk.Label(main_frame, text="Selecciona la carpeta destino")
output_path_lb.grid(row=2, column=0, columnspan=2, pady=5)
output_path = ttk.Entry(main_frame, textvariable=salida, width=40)
output_path.grid(row=3, column=0, pady=5, padx=5, sticky=(W, E))
output_path_button = ttk.Button(main_frame, text="Seleccionar", command=abrir_carpeta)
output_path_button.grid(row=3, column=1, pady=5, padx=5)
remove_bg_button = ttk.Button(main_frame, text="Quitar fondo", command=quitar_fondo)
remove_bg_button.grid(row=4, column=0, columnspan=2, pady=10)

progress_bar = ttk.Progressbar(main_frame, orient="horizontal", length=300, mode="indeterminate")
progress_bar.grid(row=5, column=0, columnspan=2, pady=5)
progress_bar.grid_remove() # Hide it initially
ventana.eval('tk::PlaceWindow . center')
ventana.mainloop()
"""
input_path = "C:/Users/jesus/desktop/Foto.png"
output_path = "C:/Users/jesus/desktop/Foto_sin_fondo.png"
image_input = Image.open(input_path)
output = remove(image_input)
output.save(output_path)
"""