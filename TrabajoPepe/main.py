from tkinter import Tk, Label, Entry, Button, messagebox
from qr_generator import QRGenerator
from qr_scanner import QRScanner

class MainApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión de QR")
        self.root.geometry("400x400")

        # Widgets para los datos del estudiante
        Label(self.root, text="Matrícula", font=("Arial", 12)).pack(pady=5)
        self.matricula_entry = Entry(self.root, font=("Arial", 12))
        self.matricula_entry.pack(pady=5)

        Label(self.root, text="Nombre", font=("Arial", 12)).pack(pady=5)
        self.nombre_entry = Entry(self.root, font=("Arial", 12))
        self.nombre_entry.pack(pady=5)

        Label(self.root, text="Carrera", font=("Arial", 12)).pack(pady=5)
        self.carrera_entry = Entry(self.root, font=("Arial", 12))
        self.carrera_entry.pack(pady=5)

        Label(self.root, text="Carro", font=("Arial", 12)).pack(pady=5)
        self.carro_entry = Entry(self.root, font=("Arial", 12))
        self.carro_entry.pack(pady=5)

        Label(self.root, text="Ruta para guardar el QR", font=("Arial", 12)).pack(pady=10)
        self.file_path_entry = Entry(self.root, font=("Arial", 12))
        self.file_path_entry.pack(pady=5)

        Button(self.root, text="Generar QR", font=("Arial", 12), command=self.generate_qr).pack(pady=10)
        Button(self.root, text="Escanear QR", font=("Arial", 12), command=self.scan_qr).pack(pady=10)

    def generate_qr(self):
        """Genera un QR usando los datos proporcionados."""
        data = {
            "matricula": self.matricula_entry.get(),
            "nombre": self.nombre_entry.get(),
            "carrera": self.carrera_entry.get(),
            "carro": self.carro_entry.get(),
        }
        file_path = self.file_path_entry.get()

        if not all(data.values()) or not file_path:
            messagebox.showwarning("Campos Vacíos", "Por favor, llena todos los campos.")
            return

        QRGenerator.generate_qr(data, file_path)
        messagebox.showinfo("Éxito", f"QR generado y guardado en {file_path}")

    def scan_qr(self):
        """Escanea un QR usando la cámara."""
        qr_data = QRScanner.scan_qr_from_camera()
        if qr_data:
            messagebox.showinfo("Datos del QR", f"Contenido: {qr_data}")
        else:
            messagebox.showinfo("Sin Datos", "No se detectó ningún QR.")

if __name__ == "__main__":
    root = Tk()
    app = MainApp(root)
    root.mainloop()
