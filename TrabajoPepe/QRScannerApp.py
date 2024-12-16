import json
import cv2
from pyzbar.pyzbar import decode
from tkinter import Tk, Label, Button, filedialog, messagebox, Frame
from PIL import Image, ImageTk

class QRScannerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Escáner de QR con Visualización")
        self.root.geometry("600x700")
        self.root.config(bg="#F3E5D8")

        # Encabezado
        header = Frame(root, bg="#8B0000", height=70)
        header.pack(fill="x")
        title = Label(header, text="Escáner de Códigos QR", font=("Arial", 18, "bold"), fg="white", bg="#8B0000")
        title.pack(pady=15)

        # Contenido principal
        content_frame = Frame(root, bg="#F3E5D8")
        content_frame.pack(expand=True, fill="both")

        self.label_data = Label(content_frame, text="Datos del QR", font=("Arial", 14, "bold"), bg="#F3E5D8", fg="#8B0000")
        self.label_data.pack(pady=10)

        self.text_data = Label(content_frame, text="", font=("Arial", 12), wraplength=500, justify="left", bg="#F3E5D8", fg="#4A4A4A")
        self.text_data.pack(pady=10)

        self.image_label = Label(content_frame, bg="#F3E5D8")
        self.image_label.pack(pady=10)

        self.scan_button = Button(content_frame, text="Escanear QR con Cámara", font=("Arial", 12), bg="#8B0000", fg="white", command=self.scan_qr_camera)
        self.scan_button.pack(pady=10)

        self.load_button = Button(content_frame, text="Cargar QR desde Archivo", font=("Arial", 12), bg="#8B0000", fg="white", command=self.load_qr_file)
        self.load_button.pack(pady=10)

    def scan_qr_camera(self):
        """Escanea un código QR usando la cámara y muestra los datos."""
        cap = cv2.VideoCapture(0)
        if not cap.isOpened():
            messagebox.showerror("Error", "No se pudo acceder a la cámara.")
            return

        messagebox.showinfo("Instrucciones", "Presiona 'q' para salir del escaneo.")
        while True:
            ret, frame = cap.read()
            if not ret:
                break

            decoded_objects = decode(frame)
            for obj in decoded_objects:
                data = obj.data.decode("utf-8")
                self.display_qr_data(data)
                cap.release()
                cv2.destroyAllWindows()
                return

            cv2.imshow("Escaneando QR - Presiona 'q' para salir", frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()

    def load_qr_file(self):
        """Carga un código QR desde un archivo y extrae los datos."""
        file_path = filedialog.askopenfilename(
            title="Seleccionar Imagen de QR",
            filetypes=[("Archivos de Imagen", "*.png;*.jpg;*.jpeg;*.bmp")]
        )

        if not file_path:
            messagebox.showinfo("Cancelado", "No se seleccionó ningún archivo.")
            return

        try:
            image = Image.open(file_path)
            qr_data = decode(image)

            if qr_data:
                # Extrae los datos del QR y procesa la imagen contenida
                self.display_qr_data(qr_data[0].data.decode("utf-8"))
            else:
                messagebox.showerror("Error", "No se detectó ningún código QR en la imagen seleccionada.")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo leer el archivo QR: {e}")

    def display_qr_data(self, data):
        """Muestra los datos del QR en la interfaz y carga la imagen si está especificada en los datos."""
        try:
            data_dict = json.loads(data)  # Intenta cargar el contenido como JSON
            display_text = "\n".join([f"{key}: {value}" for key, value in data_dict.items() if key != "imagen"])
            self.text_data.config(text=display_text)

            if "imagen" in data_dict:  # Si hay una imagen especificada en los datos
                image_path = data_dict["imagen"]
                try:
                    image = Image.open(image_path)  # Abre la imagen desde la ruta
                    image.thumbnail((600, 600))  # Ajusta el tamaño de la imagen
                    photo = ImageTk.PhotoImage(image)

                    self.image_label.config(image=photo)
                    self.image_label.image = photo
                except Exception as e:
                    messagebox.showerror("Error", f"No se pudo cargar la imagen de la ruta: {image_path}\n{e}")
            else:
                self.image_label.config(image="")
                messagebox.showinfo("Sin Imagen", "El QR no contiene una ruta a una imagen.")
        except json.JSONDecodeError:
            self.text_data.config(text=data)
            self.image_label.config(image="")
            messagebox.showinfo("Datos Sin Formato", "El QR no contiene datos en formato JSON.")

if __name__ == "__main__":
    root = Tk()
    app = QRScannerApp(root)
    root.mainloop()
