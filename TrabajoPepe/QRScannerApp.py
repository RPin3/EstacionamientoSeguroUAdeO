import json
from tkinter import Tk, Label, Button
from PIL import ImageTk
from qr_scanner import QRScanner

class QRScannerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Escáner de QR con Visualización")
        self.root.geometry("500x500")
        
        self.label_data = Label(root, text="Datos del QR", font=("Arial", 14))
        self.label_data.pack(pady=10)

        self.text_data = Label(root, text="", font=("Arial", 12), wraplength=400, justify="left")
        self.text_data.pack(pady=10)

        self.image_label = Label(root)
        self.image_label.pack(pady=10)

        self.scan_button = Button(root, text="Escanear QR", font=("Arial", 12), command=self.scan_qr)
        self.scan_button.pack(pady=20)

    def scan_qr(self):
        """Escanea un código QR y muestra los datos e imagen en la interfaz."""
        scanner = QRScanner()
        data = scanner.scan_qr_from_camera()

        if data:
            self.text_data.config(text=json.dumps({k: v for k, v in data.items() if k != "reconstructed_image"}, indent=2))

            if "reconstructed_image" in data:
                img = data["reconstructed_image"]
                img.thumbnail((300, 300))
                photo = ImageTk.PhotoImage(img)
                self.image_label.config(image=photo)
                self.image_label.image = photo
        else:
            self.text_data.config(text="No se detectó ningún QR.")
            self.image_label.config(image="")

if __name__ == "__main__":
    root = Tk()
    app = QRScannerApp(root)
    root.mainloop()
