import qrcode

class QRGenerator:
    @staticmethod
    def generate_qr(data: dict, file_path: str):
        """
        Genera un código QR con los datos proporcionados y lo guarda en un archivo .png.
        
        Args:
            data (dict): Información del estudiante (matrícula, nombre, carrera, carro).
            file_path (str): Ruta del archivo para guardar el QR (debe terminar en .png).
        """
        try:
            # Asegúrate de que el archivo tenga extensión .png
            if not file_path.lower().endswith(".png"):
                file_path += ".png"

            # Formatea los datos en un string legible para el QR
            formatted_data = (
                f"Matrícula: {data['matricula']}\n"
                f"Nombre: {data['nombre']}\n"
                f"Carrera: {data['carrera']}\n"
                f"Carro: {data['carro']}"
            )

            # Configuración y generación del QR
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4,
            )
            qr.add_data(formatted_data)
            qr.make(fit=True)

            # Generar la imagen
            img = qr.make_image(fill_color="black", back_color="white")
            img.save(file_path)  # Guardar como .png

            print(f"QR generado y guardado como: {file_path}")
        except Exception as e:
            print(f"Error al generar el QR: {e}")
