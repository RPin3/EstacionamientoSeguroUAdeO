import qrcode
import base64
import json
from PIL import Image

class QRGenerator:
    @staticmethod
    def generate_qr_with_image(data: dict, file_path: str, image_path: str = None):
        try:
            if not file_path.lower().endswith(".png"):
                file_path += ".png"

            formatted_data = {
                "matricula": data.get("matricula"),
                "nombre": data.get("nombre"),
                "carrera": data.get("carrera"),
                "carro": data.get("carro"),
            }

            if image_path:
                with open(image_path, "rb") as img_file:
                    image_base64 = base64.b64encode(img_file.read()).decode("utf-8")
                    formatted_data["image"] = image_base64

            qr = qrcode.QRCode(
                version=None,  # Ajusta automáticamente el tamaño del QR
                error_correction=qrcode.constants.ERROR_CORRECT_H,
                box_size=10,
                border=4,
            )
            qr.add_data(json.dumps(formatted_data))
            qr.make(fit=True)

            qr_image = qr.make_image(fill_color="black", back_color="white")
            qr_image.save(file_path)

            print(f"QR generado y guardado como: {file_path}")
        except Exception as e:
            print(f"Error al generar el QR: {e}")
