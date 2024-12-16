import json
from tkinter import Tk, Label, Entry, Button, filedialog, messagebox, Frame
import qrcode

class QRGenerator:
    @staticmethod
    def generate_qr_with_image(data, file_path):
        """
        Genera un código QR con los datos proporcionados.
        """
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(data)  # Agrega los datos al QR
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")

        # Guardar la imagen del QR
        img.save(file_path)

class QRGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Generador de QR")
        self.root.geometry("500x600")
        self.root.config(bg="#F3E5D8")  # Color de fondo beige

        # Encabezado
        header = Frame(root, bg="#8B0000", height=70)
        header.pack(fill="x")
        title = Label(header, text="Generador de Códigos QR", font=("Arial", 18, "bold"), fg="white", bg="#8B0000")
        title.pack(pady=15)

        # Contenido principal
        content_frame = Frame(root, bg="#F3E5D8")
        content_frame.pack(expand=True, fill="both")

        Label(content_frame, text="Matrícula:", font=("Arial", 12), bg="#F3E5D8", fg="#8B0000").pack(pady=5)
        self.entry_matricula = Entry(content_frame, font=("Arial", 12))
        self.entry_matricula.pack(pady=5, fill="x")

        Label(content_frame, text="Nombre:", font=("Arial", 12), bg="#F3E5D8", fg="#8B0000").pack(pady=5)
        self.entry_nombre = Entry(content_frame, font=("Arial", 12))
        self.entry_nombre.pack(pady=5, fill="x")

        Label(content_frame, text="Carrera:", font=("Arial", 12), bg="#F3E5D8", fg="#8B0000").pack(pady=5)
        self.entry_carrera = Entry(content_frame, font=("Arial", 12))
        self.entry_carrera.pack(pady=5, fill="x")

        Label(content_frame, text="Carro:", font=("Arial", 12), bg="#F3E5D8", fg="#8B0000").pack(pady=5)
        self.entry_carro = Entry(content_frame, font=("Arial", 12))
        self.entry_carro.pack(pady=5, fill="x")

        # Botón para seleccionar imagen opcional
        self.image_path = None
        self.select_image_button = Button(content_frame, text="Seleccionar Imagen (Opcional)", font=("Arial", 12), bg="#8B0000", fg="white", command=self.select_image)
        self.select_image_button.pack(pady=10)

        # Botón para generar QR
        self.generate_button = Button(content_frame, text="Generar QR", font=("Arial", 14), bg="#8B0000", fg="white", command=self.generate_qr)
        self.generate_button.pack(pady=20)

    def select_image(self):
        """Abre un diálogo para seleccionar una imagen."""
        self.image_path = filedialog.askopenfilename(
            title="Seleccionar Imagen",
            filetypes=[("Archivos de Imagen", "*.png;*.jpg;*.jpeg;*.bmp")]
        )
        if self.image_path:
            messagebox.showinfo("Imagen Seleccionada", f"Se seleccionó la imagen: {self.image_path}")

    def generate_qr(self):
        """Genera un código QR basado en los datos ingresados."""
        data = {
            "matricula": self.entry_matricula.get().strip(),
            "nombre": self.entry_nombre.get().strip(),
            "carrera": self.entry_carrera.get().strip(),
            "carro": self.entry_carro.get().strip(),
        }

        # Validar que los campos requeridos estén llenos
        if not all(data.values()):
            messagebox.showerror("Error", "Todos los campos deben estar llenos.")
            return

        # Agregar la ruta de la imagen si existe
        if self.image_path:
            data["imagen"] = self.image_path  # Agregar la ruta al JSON

        # Seleccionar ruta para guardar el QR
        file_path = filedialog.asksaveasfilename(
            title="Guardar QR",
            defaultextension=".png",
            filetypes=[("Imagen PNG", "*.png")]
        )

        if not file_path:
            messagebox.showinfo("Cancelado", "No se seleccionó una ubicación para guardar el QR.")
            return

        try:
            # Convertir el diccionario a una cadena JSON
            json_data = json.dumps(data)

            # Generar el QR usando la clase QRGenerator
            QRGenerator.generate_qr_with_image(json_data, file_path)  # Pasa el JSON como cadena
            messagebox.showinfo("Éxito", f"Código QR generado exitosamente en: {file_path}")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo generar el QR: {e}")

if __name__ == "__main__":
    root = Tk()
    app = QRGeneratorApp(root)
    root.mainloop()
