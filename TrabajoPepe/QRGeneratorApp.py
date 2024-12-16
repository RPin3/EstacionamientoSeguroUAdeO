import json
import base64
from tkinter import Tk, Label, Entry, Button, filedialog, messagebox
from qr_generator import QRGenerator

class QRGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Generador de QR")
        self.root.geometry("500x400")

        # Etiquetas y campos para datos
        Label(root, text="Matrícula:", font=("Arial", 12)).pack(pady=5)
        self.entry_matricula = Entry(root, font=("Arial", 12))
        self.entry_matricula.pack(pady=5, fill="x")

        Label(root, text="Nombre:", font=("Arial", 12)).pack(pady=5)
        self.entry_nombre = Entry(root, font=("Arial", 12))
        self.entry_nombre.pack(pady=5, fill="x")

        Label(root, text="Carrera:", font=("Arial", 12)).pack(pady=5)
        self.entry_carrera = Entry(root, font=("Arial", 12))
        self.entry_carrera.pack(pady=5, fill="x")

        Label(root, text="Carro:", font=("Arial", 12)).pack(pady=5)
        self.entry_carro = Entry(root, font=("Arial", 12))
        self.entry_carro.pack(pady=5, fill="x")

        # Botón para seleccionar imagen opcional
        self.image_path = None
        self.select_image_button = Button(root, text="Seleccionar Imagen (Opcional)", font=("Arial", 12), command=self.select_image)
        self.select_image_button.pack(pady=10)

        # Botón para generar QR
        self.generate_button = Button(root, text="Generar QR", font=("Arial", 14), command=self.generate_qr)
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
            # Generar el QR usando la clase QRGenerator
            QRGenerator.generate_qr_with_image(data, file_path, self.image_path)
            messagebox.showinfo("Éxito", f"Código QR generado exitosamente en: {file_path}")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo generar el QR: {e}")

if __name__ == "__main__":
    root = Tk()
    app = QRGeneratorApp(root)
    root.mainloop()
